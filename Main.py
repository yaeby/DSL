from antlr4 import *
from ImageManipulationLexer import ImageManipulationLexer
from ImageManipulationParser import ImageManipulationParser
from ImageManipulationListener import ImageManipulationListener
from PIL import Image
import rotate
from colors import adjust_saturation, adjust_brightness, adjust_contrast
import os
import cv2
import sys
from Image import edge_detection
from Coordinates import pixels_coordinates, adjacent_pixels, get_upper_edge_pixels, sort_pixels_by_adjacency, get_all_edges
from Functions import rotate_points, functions

class ImageManipulationCommandListener(ImageManipulationListener):
    def __init__(self):
        self.images = {}
        self.folders = {}

    def exitAssignment(self, ctx):
        image_id = ctx.ID().getText()
        file_path = ctx.STRING().getText().strip('"')
        if os.path.isdir(file_path):
            self.folders[image_id] = [os.path.join(file_path, f) for f in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, f))]
        else:
            self.images[image_id] = Image.open(file_path)

    def exitAction(self, ctx):
        image_id = ctx.ID().getText()
        action_type = ctx.actionType().getText()
        factor_ctx = ctx.actionType().NUMBER()
        factor = float(factor_ctx.getText()) if factor_ctx else None

        if image_id in self.images:
            self.images[image_id] = self.apply_action(self.images[image_id], action_type, factor)
        elif image_id in self.folders:
            self.apply_action_to_folder(image_id, action_type, factor)

    def apply_action(self, image, action_type, factor=None):
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
        elif action_type == 'polynomial':
            return self.apply_polynomial(image)
        return image

    def apply_action_to_folder(self, folder_id, action_type, factor=None):
        image_paths = self.folders[folder_id]
        for image_path in image_paths:
            image = Image.open(image_path)
            image = self.apply_action(image, action_type, factor)
            image.save(image_path)

    def apply_polynomial(self, image):
        image_path = "temp_image.png"
        image.save(image_path)
        
        img = cv2.imread(image_path)
        edge_detection(img)
        
        pixel_coords = pixels_coordinates('final.png')
        adj_pixels = adjacent_pixels(pixel_coords)

        result = []
        for edge in adj_pixels:
            upper_pixels = get_upper_edge_pixels(edge)
            sorted_pixels = sort_pixels_by_adjacency(upper_pixels)
            edges = get_all_edges(sorted_pixels)
            result.append(edges)

        flattened_result = [edge for edges_group in result for edge in edges_group]
        points = rotate_points(flattened_result, 180)
        functions(points)
        
        polynomial_image = Image.open('final.png')
        return polynomial_image

    def exitResizeCommand(self, ctx):
        self.apply_resize_or_crop(ctx, 'resize')

    def exitCropCommand(self, ctx):
        self.apply_resize_or_crop(ctx, 'crop')

    def apply_resize_or_crop(self, ctx, command_type):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()

        if command_type == 'resize':
            width = int(ctx.NUMBER(0).getText())
            height = int(ctx.NUMBER(1).getText())
            if image_id in self.images:
                self.images[image_id] = self.images[image_id].resize((width, height))
            elif image_id in self.folders:
                self.apply_resize_to_folder(image_id, width, height)
        elif command_type == 'crop':
            left = int(ctx.NUMBER(0).getText())
            top = int(ctx.NUMBER(1).getText())
            right = int(ctx.NUMBER(2).getText())
            bottom = int(ctx.NUMBER(3).getText())
            if image_id in self.images:
                self.images[image_id] = self.images[image_id].crop((left, top, right, bottom))
            elif image_id in self.folders:
                self.apply_crop_to_folder(image_id, left, top, right, bottom)

    def apply_resize_to_folder(self, folder_id, width, height):
        image_paths = self.folders[folder_id]
        for image_path in image_paths:
            image = Image.open(image_path)
            image = image.resize((width, height))
            image.save(image_path)

    def apply_crop_to_folder(self, folder_id, left, top, right, bottom):
        image_paths = self.folders[folder_id]
        for image_path in image_paths:
            image = Image.open(image_path)
            image = image.crop((left, top, right, bottom))
            image.save(image_path)

    def exitRotateCommand(self, ctx):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()
        angle = float(ctx.NUMBER().getText())
        if image_id in self.images:
            self.images[image_id] = self.images[image_id].rotate(angle, expand=True)
        elif image_id in self.folders:
            self.apply_rotate_to_folder(image_id, angle)

    def apply_rotate_to_folder(self, folder_id, angle):
        image_paths = self.folders[folder_id]
        for image_path in image_paths:
            image = Image.open(image_path)
            image = image.rotate(angle, expand=True)
            image.save(image_path)

    def exitSaveCommand(self, ctx):
        image_id = ctx.ID().getText()
        file_path = ctx.STRING().getText().strip('"')
        if image_id in self.images:
            self.images[image_id].save(file_path)
        elif image_id in self.folders:
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            image_paths = self.folders[image_id]
            for idx, image_path in enumerate(image_paths):
                image = Image.open(image_path)
                image.save(os.path.join(file_path, f'image_{idx}.jpg'))

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
    if len(sys.argv) != 2:
        print("Usage: python Main.py <filepath>")
    else:
        filepath = sys.argv[1]
        print("Running DSL commands...")
        run_commands_from_file(filepath)
        print("Completed.")