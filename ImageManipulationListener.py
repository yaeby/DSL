# Generated from ImageManipulation.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ImageManipulationParser import ImageManipulationParser
else:
    from ImageManipulationParser import ImageManipulationParser

# This class defines a complete listener for a parse tree produced by ImageManipulationParser.
class ImageManipulationListener(ParseTreeListener):

    # Enter a parse tree produced by ImageManipulationParser#prog.
    def enterProg(self, ctx:ImageManipulationParser.ProgContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#prog.
    def exitProg(self, ctx:ImageManipulationParser.ProgContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#command.
    def enterCommand(self, ctx:ImageManipulationParser.CommandContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#command.
    def exitCommand(self, ctx:ImageManipulationParser.CommandContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#assignment.
    def enterAssignment(self, ctx:ImageManipulationParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#assignment.
    def exitAssignment(self, ctx:ImageManipulationParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#action.
    def enterAction(self, ctx:ImageManipulationParser.ActionContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#action.
    def exitAction(self, ctx:ImageManipulationParser.ActionContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#actionType.
    def enterActionType(self, ctx:ImageManipulationParser.ActionTypeContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#actionType.
    def exitActionType(self, ctx:ImageManipulationParser.ActionTypeContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#resizeCommand.
    def enterResizeCommand(self, ctx:ImageManipulationParser.ResizeCommandContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#resizeCommand.
    def exitResizeCommand(self, ctx:ImageManipulationParser.ResizeCommandContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#cropCommand.
    def enterCropCommand(self, ctx:ImageManipulationParser.CropCommandContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#cropCommand.
    def exitCropCommand(self, ctx:ImageManipulationParser.CropCommandContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#rotateCommand.
    def enterRotateCommand(self, ctx:ImageManipulationParser.RotateCommandContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#rotateCommand.
    def exitRotateCommand(self, ctx:ImageManipulationParser.RotateCommandContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#saveCommand.
    def enterSaveCommand(self, ctx:ImageManipulationParser.SaveCommandContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#saveCommand.
    def exitSaveCommand(self, ctx:ImageManipulationParser.SaveCommandContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#funcDef.
    def enterFuncDef(self, ctx:ImageManipulationParser.FuncDefContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#funcDef.
    def exitFuncDef(self, ctx:ImageManipulationParser.FuncDefContext):
        pass


    # Enter a parse tree produced by ImageManipulationParser#funcCall.
    def enterFuncCall(self, ctx:ImageManipulationParser.FuncCallContext):
        pass

    # Exit a parse tree produced by ImageManipulationParser#funcCall.
    def exitFuncCall(self, ctx:ImageManipulationParser.FuncCallContext):
        pass



del ImageManipulationParser