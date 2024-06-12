from antlr4 import *
from ImageManipulationLexer import ImageManipulationLexer
from ImageManipulationParser import ImageManipulationParser
from ImageManipulationListener import ImageManipulationListener
from PIL import Image
import rotate
from colors import adjust_saturation, adjust_brightness, adjust_contrast
import os
import sys

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
        if image_id in self.images:
            image = self.images[image_id]
            action_type = ctx.actionType().getText()
            factor_ctx = ctx.actionType().NUMBER()
            factor = float(factor_ctx.getText()) if factor_ctx else None

            if 'saturation' in action_type:
                self.images[image_id] = adjust_saturation(image, factor)
            elif 'brightness' in action_type:
                self.images[image_id] = adjust_brightness(image, factor)
            elif 'contrast' in action_type:
                self.images[image_id] = adjust_contrast(image, factor)
            elif action_type == 'flipX':
                self.images[image_id] = rotate.flipX(image)
            elif action_type == 'flipY':
                self.images[image_id] = rotate.flipY(image)
        elif image_id in self.folders:
            self.apply_action_to_folder(image_id, ctx.actionType().getText())

    def apply_action_to_folder(self, folder_id, action_type):
        image_paths = self.folders[folder_id]
        for image_path in image_paths:
            image = Image.open(image_path)
            if action_type == 'flipX':
                image = rotate.flipX(image)
            elif action_type == 'flipY':
                image = rotate.flipY(image)
            elif 'resize' in action_type:
                width, height = map(int, action_type[action_type.find('(')+1:action_type.find(')')].split(','))
                image = image.resize((width, height))
            elif 'crop' in action_type:
                left, top, right, bottom = map(int, action_type[action_type.find('(')+1:action_type.find(')')].split(','))
                image = image.crop((left, top, right, bottom))
            elif 'rotate' in action_type:
                angle = float(action_type[action_type.find('(')+1:action_type.find(')')])
                image = image.rotate(angle, expand=True)
            elif 'saturation' in action_type:
                factor = float(action_type[action_type.find('(')+1:action_type.find(')')])
                image = adjust_saturation(image, factor)
            elif 'brightness' in action_type:
                factor = float(action_type[action_type.find('(')+1:action_type.find(')')])
                image = adjust_brightness(image, factor)
            elif 'contrast' in action_type:
                factor = float(action_type[action_type.find('(')+1:action_type.find(')')])
                image = adjust_contrast(image, factor)
            image.save(image_path)

    def exitResizeCommand(self, ctx):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()
        width = int(ctx.NUMBER(0).getText())
        height = int(ctx.NUMBER(1).getText())
        if image_id in self.images:
            self.images[image_id] = self.images[image_id].resize((width, height))
        elif image_id in self.folders:
            self.apply_resize_to_folder(image_id, width, height)

    def apply_resize_to_folder(self, folder_id, width, height):
        image_paths = self.folders[folder_id]
        for image_path in image_paths:
            image = Image.open(image_path)
            image = image.resize((width, height))
            image.save(image_path)

    def exitCropCommand(self, ctx):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()
        left = int(ctx.NUMBER(0).getText())
        top = int(ctx.NUMBER(1).getText())
        right = int(ctx.NUMBER(2).getText())
        bottom = int(ctx.NUMBER(3).getText())
        if image_id in self.images:
            self.images[image_id] = self.images[image_id].crop((left, top, right, bottom))
        elif image_id in self.folders:
            self.apply_crop_to_folder(image_id, left, top, right, bottom)

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
            for idx, image_path in image_paths:
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
        print("Usage: python Main.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    print(f"Running DSL commands from {file_path}...")
    run_commands_from_file(file_path)
    print("Completed.")
