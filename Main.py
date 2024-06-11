from antlr4 import *
from ImageManipulationLexer import ImageManipulationLexer
from ImageManipulationParser import ImageManipulationParser
from ImageManipulationListener import ImageManipulationListener
from PIL import Image
import rotate
from colors import adjust_saturation, adjust_brightness, adjust_contrast

class ImageManipulationCommandListener(ImageManipulationListener):
    def __init__(self):
        self.images = {}

    def exitAssignment(self, ctx):
        image_id = ctx.ID().getText()
        file_path = ctx.STRING().getText().strip('"')
        self.images[image_id] = Image.open(file_path)

    def exitAction(self, ctx):
        image_id = ctx.ID().getText()
        image = self.images.get(image_id)
        if image is not None:
            action_type = ctx.actionType().getText()

            # Check for image adjustments that require a factor
            if 'saturation' in action_type or 'brightness' in action_type or 'contrast' in action_type:
                # Correctly extract the factor directly from the actionType's context
                factor_ctx = ctx.actionType().NUMBER()  # Directly accessing the NUMBER token
                factor = float(factor_ctx.getText())  # Convert the factor to float
                if 'saturation' in action_type:
                    self.images[image_id] = adjust_saturation(image, factor)
                elif 'brightness' in action_type:
                    self.images[image_id] = adjust_brightness(image, factor)
                elif 'contrast' in action_type:
                    self.images[image_id] = adjust_contrast(image, factor)
            
            # Handle rotation actions
            elif action_type == 'flipX':
                self.images[image_id] = rotate.flipX(image)
            elif action_type == 'flipY':
                self.images[image_id] = rotate.flipY(image)

    def exitResizeCommand(self, ctx):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()
        width = int(ctx.NUMBER(0).getText())
        height = int(ctx.NUMBER(1).getText())
        self.images[image_id] = self.images[image_id].resize((width, height))

    def exitCropCommand(self, ctx):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()
        left = int(ctx.NUMBER(0).getText())
        top = int(ctx.NUMBER(1).getText())
        right = int(ctx.NUMBER(2).getText())
        bottom = int(ctx.NUMBER(3).getText())
        image = self.images.get(image_id)
        if image:
            self.images[image_id] = self.images[image_id].crop((left, top, right, bottom))

    def exitRotateCommand(self, ctx):
        action_context = ctx.parentCtx.parentCtx
        image_id = action_context.ID().getText()
        angle = float(ctx.NUMBER().getText())
        image = self.images.get(image_id)
        if image:
            self.images[image_id] = image.rotate(angle, expand=True)

    def exitSaveCommand(self, ctx):
        image_id = ctx.ID().getText()
        file_path = ctx.STRING().getText().strip('"')
        self.images[image_id].save(file_path)

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
    run_commands_from_file('/home/liviu/DSL/commands.txt')
    print("Completed.")
