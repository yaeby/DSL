import sys
import os
import cv2  # Import cv2
import numpy as np
from antlr4 import *
from PIL import Image
from ImageManipulationLexer import ImageManipulationLexer
from ImageManipulationParser import ImageManipulationParser
from ImageManipulationListener import ImageManipulationListener
from Image import edge_detection
from Coordinates import pixels_coordinates, adjacent_pixels as get_adjacent_pixels, get_upper_edge_pixels, sort_pixels_by_adjacency, get_all_edges
from Functions import rotate_points, functions

# Add the directory containing your modules to the Python path
module_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'From-Image-to-Functions'))
if module_path not in sys.path:
    sys.path.append(module_path)

class ImageManipulationCommandListener(ImageManipulationListener):
    def __init__(self):
        self.images = {}
        self.folders = {}
        self.functions = {}
        self.folder_images = {}
        print("Initialized ImageManipulationCommandListener")

    def exitAssignment(self, ctx):
        assignment_type = ctx.getChild(2).getText()
        id = ctx.ID().getText()
        path = ctx.STRING().getText().strip('"')
        
        if assignment_type == 'open':
            try:
                self.images[id] = Image.open(path)
                print(f"Opened image: {path}")
            except IOError as e:
                print(f"Error opening image {path}: {e}")
        elif assignment_type == 'openFolder':
            try:
                self.folders[id] = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('.png', '.jpg', '.jpeg'))]
                self.folder_images[id] = {img_path: Image.open(img_path) for img_path in self.folders[id]}
                print(f"Opened folder: {path}")
            except IOError as e:
                print(f"Error opening folder {path}: {e}")

    def exitAction(self, ctx):
        id = ctx.ID().getText()
        if id in self.images:
            image = self.images[id]
            self.images[id] = self.process_image(image, ctx)
            print(f"Processed action for image: {id}")
        elif id in self.folders:
            for image_path, image in self.folder_images[id].items():
                self.folder_images[id][image_path] = self.process_image(image, ctx)
                print(f"Processed action for image in folder: {image_path}")

    def process_image(self, image, ctx):
        action_type = ctx.actionType().getText()
        if 'saturation' in action_type or 'brightness' in action_type or 'contrast' in action_type:
            factor = float(ctx.actionType().NUMBER().getText())
            if 'saturation' in action_type:
                return adjust_saturation(image, factor)
            elif 'brightness' in action_type:
                return adjust_brightness(image, factor)
            elif 'contrast' in action_type:
                return adjust_contrast(image, factor)
        elif action_type == 'flipX':
            return rotate.flipX(image)
        elif action_type == 'flipY':
            return rotate.flipY(image)
        elif 'resize' in action_type:
            width = int(ctx.actionType().NUMBER(0).getText())
            height = int(ctx.actionType().NUMBER(1).getText())
            return image.resize((width, height))
        elif 'crop' in action_type:
            left = int(ctx.actionType().NUMBER(0).getText())
            top = int(ctx.actionType().NUMBER(1).getText())
            right = int(ctx.actionType().NUMBER(2).getText())
            bottom = int(ctx.actionType().NUMBER(3).getText())
            return image.crop((left, top, right, bottom))
        elif 'rotate' in action_type:
            angle = float(ctx.actionType().NUMBER().getText())
            return image.rotate(angle, expand=True)
        elif action_type == 'polynomial':
            return self.apply_polynomial_transformation(image)
        return image

    def apply_polynomial_transformation(self, image):
        img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        edge_detection(img)
        pixel_coords = pixels_coordinates('final.png')
        adj_pixels = get_adjacent_pixels(pixel_coords)

        result = []
        for edge in adj_pixels:
            upper_pixels = get_upper_edge_pixels(edge)
            sorted_pixels = sort_pixels_by_adjacency(upper_pixels)
            edges = get_all_edges(sorted_pixels)
            result.append(edges)

        flattened_result = [edge for edges_group in result for edge in edges_group]
        points = rotate_points(flattened_result, 180)
        functions(points)

        polynomial_image = Image.open('polynomial.jpg')
        return polynomial_image

    def exitSaveCommand(self, ctx):
        id = ctx.ID().getText()
        save_path = ctx.STRING().getText().strip('"')
        if id in self.images:
            image = self.images[id]
            if image and save_path:
                try:
                    image.save(save_path)
                    print(f"Saved image: {save_path}")
                except IOError as e:
                    print(f"Error saving image to {save_path}: {e}")
        elif id in self.folders:
            if save_path:
                os.makedirs(save_path, exist_ok=True)
                for image_path, image in self.folder_images[id].items():
                    base_name = os.path.basename(image_path)
                    new_image_path = os.path.join(save_path, base_name)
                    image.save(new_image_path)
                    print(f"Saved image: {new_image_path}")

    def exitFuncDef(self, ctx):
        func_name = ctx.ID(0).getText()
        param_name = ctx.ID(1).getText()
        actions = ctx.action() + ctx.saveCommand()
        self.functions[func_name] = (param_name, actions)
        print(f"Defined function: {func_name}")
        
    def exitFuncCall(self, ctx):
        func_name = ctx.ID().getText()
        image_path = ctx.STRING().getText().strip('"')
        if func_name in self.functions:
            param_name, actions = self.functions[func_name]
            if os.path.isdir(image_path):
                temp_folder_id = "temp_folder"
                self.folders[temp_folder_id] = [os.path.join(image_path, f) for f in os.listdir(image_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
                self.folder_images[temp_folder_id] = {img_path: Image.open(img_path) for img_path in self.folders[temp_folder_id]}
                for action in actions:
                    if isinstance(action, ImageManipulationParser.ActionContext):
                        action_ctx = action
                        action_ctx.children[0].symbol.text = temp_folder_id
                        self.exitAction(action_ctx)
                    elif isinstance(action, ImageManipulationParser.SaveCommandContext):
                        save_ctx = action
                        save_ctx.children[0].symbol.text = temp_folder_id
                        self.exitSaveCommand(save_ctx)
            else:
                temp_image_id = "temp_image"
                self.images[temp_image_id] = Image.open(image_path)
                for action in actions:
                    if isinstance(action, ImageManipulationParser.ActionContext):
                        action_ctx = action
                        action_ctx.children[0].symbol.text = temp_image_id
                        self.exitAction(action_ctx)
                    elif isinstance(action, ImageManipulationParser.SaveCommandContext):
                        save_ctx = action
                        save_ctx.children[0].symbol.text = temp_image_id
                        self.exitSaveCommand(save_ctx)

                if param_name and param_name in self.images:
                    image = self.images[param_name]
                    for action in actions:
                        if isinstance(action, ImageManipulationParser.ActionContext):
                            image = self.process_image(image, action)

                    if image:
                        save_path = f"{func_name}.jpg"
                        try:
                            image.save(save_path)
                            print(f"Generated image saved as: {save_path}")
                        except IOError as e:
                            print(f"Error saving generated image to {save_path}: {e}")

def run_commands_from_file(file_path):
    with open(file_path, 'r') as file:
        commands = file.read()

    input_stream = InputStream(commands)
    lexer = ImageManipulationLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ImageManipulationParser(stream)
    tree = parser.prog()

    listener = ImageManipulationCommandListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

if __name__ == "__main__":
    print("Running DSL commands...")
    run_commands_from_file('/home/liviu/DSL/function.txt')
    print("Completed.")
