# Generated from ImageManipulation.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,21,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,3,1,27,
        8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,57,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,
        6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,0,0,9,
        0,2,4,6,8,10,12,14,16,0,0,89,0,19,1,0,0,0,2,26,1,0,0,0,4,28,1,0,
        0,0,6,35,1,0,0,0,8,56,1,0,0,0,10,58,1,0,0,0,12,65,1,0,0,0,14,76,
        1,0,0,0,16,81,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,
        21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,27,3,4,2,0,24,27,3,6,
        3,0,25,27,3,16,8,0,26,23,1,0,0,0,26,24,1,0,0,0,26,25,1,0,0,0,27,
        3,1,0,0,0,28,29,5,16,0,0,29,30,5,1,0,0,30,31,5,2,0,0,31,32,5,3,0,
        0,32,33,5,18,0,0,33,34,5,4,0,0,34,5,1,0,0,0,35,36,5,16,0,0,36,37,
        5,5,0,0,37,38,3,8,4,0,38,7,1,0,0,0,39,57,5,6,0,0,40,57,5,7,0,0,41,
        57,3,10,5,0,42,57,3,12,6,0,43,57,3,14,7,0,44,45,5,8,0,0,45,46,5,
        3,0,0,46,47,5,17,0,0,47,57,5,4,0,0,48,49,5,9,0,0,49,50,5,3,0,0,50,
        51,5,17,0,0,51,57,5,4,0,0,52,53,5,10,0,0,53,54,5,3,0,0,54,55,5,17,
        0,0,55,57,5,4,0,0,56,39,1,0,0,0,56,40,1,0,0,0,56,41,1,0,0,0,56,42,
        1,0,0,0,56,43,1,0,0,0,56,44,1,0,0,0,56,48,1,0,0,0,56,52,1,0,0,0,
        57,9,1,0,0,0,58,59,5,11,0,0,59,60,5,3,0,0,60,61,5,17,0,0,61,62,5,
        12,0,0,62,63,5,17,0,0,63,64,5,4,0,0,64,11,1,0,0,0,65,66,5,13,0,0,
        66,67,5,3,0,0,67,68,5,17,0,0,68,69,5,12,0,0,69,70,5,17,0,0,70,71,
        5,12,0,0,71,72,5,17,0,0,72,73,5,12,0,0,73,74,5,17,0,0,74,75,5,4,
        0,0,75,13,1,0,0,0,76,77,5,14,0,0,77,78,5,3,0,0,78,79,5,17,0,0,79,
        80,5,4,0,0,80,15,1,0,0,0,81,82,5,16,0,0,82,83,5,5,0,0,83,84,5,15,
        0,0,84,85,5,3,0,0,85,86,5,18,0,0,86,87,5,4,0,0,87,17,1,0,0,0,3,21,
        26,56
    ]

class ImageManipulationParser ( Parser ):

    grammarFileName = "ImageManipulation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'open'", "'('", "')'", "'.'", 
                     "'flipX'", "'flipY'", "'saturation'", "'brightness'", 
                     "'contrast'", "'resize'", "','", "'crop'", "'rotate'", 
                     "'save'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUMBER", "STRING", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_assignment = 2
    RULE_action = 3
    RULE_actionType = 4
    RULE_resizeCommand = 5
    RULE_cropCommand = 6
    RULE_rotateCommand = 7
    RULE_saveCommand = 8

    ruleNames =  [ "prog", "command", "assignment", "action", "actionType", 
                   "resizeCommand", "cropCommand", "rotateCommand", "saveCommand" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    NUMBER=17
    STRING=18
    LINE_COMMENT=19
    BLOCK_COMMENT=20
    WS=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def command(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ImageManipulationParser.CommandContext)
            else:
                return self.getTypedRuleContext(ImageManipulationParser.CommandContext,i)


        def getRuleIndex(self):
            return ImageManipulationParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = ImageManipulationParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.command()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==16):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(ImageManipulationParser.AssignmentContext,0)


        def action(self):
            return self.getTypedRuleContext(ImageManipulationParser.ActionContext,0)


        def saveCommand(self):
            return self.getTypedRuleContext(ImageManipulationParser.SaveCommandContext,0)


        def getRuleIndex(self):
            return ImageManipulationParser.RULE_command

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommand" ):
                listener.enterCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommand" ):
                listener.exitCommand(self)




    def command(self):

        localctx = ImageManipulationParser.CommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_command)
        try:
            self.state = 26
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.action()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.saveCommand()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ImageManipulationParser.ID, 0)

        def STRING(self):
            return self.getToken(ImageManipulationParser.STRING, 0)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)




    def assignment(self):

        localctx = ImageManipulationParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(ImageManipulationParser.ID)
            self.state = 29
            self.match(ImageManipulationParser.T__0)
            self.state = 30
            self.match(ImageManipulationParser.T__1)
            self.state = 31
            self.match(ImageManipulationParser.T__2)
            self.state = 32
            self.match(ImageManipulationParser.STRING)
            self.state = 33
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ImageManipulationParser.ID, 0)

        def actionType(self):
            return self.getTypedRuleContext(ImageManipulationParser.ActionTypeContext,0)


        def getRuleIndex(self):
            return ImageManipulationParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = ImageManipulationParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_action)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ImageManipulationParser.ID)
            self.state = 36
            self.match(ImageManipulationParser.T__4)
            self.state = 37
            self.actionType()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def resizeCommand(self):
            return self.getTypedRuleContext(ImageManipulationParser.ResizeCommandContext,0)


        def cropCommand(self):
            return self.getTypedRuleContext(ImageManipulationParser.CropCommandContext,0)


        def rotateCommand(self):
            return self.getTypedRuleContext(ImageManipulationParser.RotateCommandContext,0)


        def NUMBER(self):
            return self.getToken(ImageManipulationParser.NUMBER, 0)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_actionType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionType" ):
                listener.enterActionType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionType" ):
                listener.exitActionType(self)




    def actionType(self):

        localctx = ImageManipulationParser.ActionTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_actionType)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(ImageManipulationParser.T__5)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(ImageManipulationParser.T__6)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 41
                self.resizeCommand()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 4)
                self.state = 42
                self.cropCommand()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 43
                self.rotateCommand()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 6)
                self.state = 44
                self.match(ImageManipulationParser.T__7)
                self.state = 45
                self.match(ImageManipulationParser.T__2)
                self.state = 46
                self.match(ImageManipulationParser.NUMBER)
                self.state = 47
                self.match(ImageManipulationParser.T__3)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 7)
                self.state = 48
                self.match(ImageManipulationParser.T__8)
                self.state = 49
                self.match(ImageManipulationParser.T__2)
                self.state = 50
                self.match(ImageManipulationParser.NUMBER)
                self.state = 51
                self.match(ImageManipulationParser.T__3)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 8)
                self.state = 52
                self.match(ImageManipulationParser.T__9)
                self.state = 53
                self.match(ImageManipulationParser.T__2)
                self.state = 54
                self.match(ImageManipulationParser.NUMBER)
                self.state = 55
                self.match(ImageManipulationParser.T__3)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ResizeCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ImageManipulationParser.NUMBER)
            else:
                return self.getToken(ImageManipulationParser.NUMBER, i)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_resizeCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterResizeCommand" ):
                listener.enterResizeCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitResizeCommand" ):
                listener.exitResizeCommand(self)




    def resizeCommand(self):

        localctx = ImageManipulationParser.ResizeCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_resizeCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(ImageManipulationParser.T__10)
            self.state = 59
            self.match(ImageManipulationParser.T__2)
            self.state = 60
            self.match(ImageManipulationParser.NUMBER)
            self.state = 61
            self.match(ImageManipulationParser.T__11)
            self.state = 62
            self.match(ImageManipulationParser.NUMBER)
            self.state = 63
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CropCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(ImageManipulationParser.NUMBER)
            else:
                return self.getToken(ImageManipulationParser.NUMBER, i)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_cropCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCropCommand" ):
                listener.enterCropCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCropCommand" ):
                listener.exitCropCommand(self)




    def cropCommand(self):

        localctx = ImageManipulationParser.CropCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cropCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.match(ImageManipulationParser.T__12)
            self.state = 66
            self.match(ImageManipulationParser.T__2)
            self.state = 67
            self.match(ImageManipulationParser.NUMBER)
            self.state = 68
            self.match(ImageManipulationParser.T__11)
            self.state = 69
            self.match(ImageManipulationParser.NUMBER)
            self.state = 70
            self.match(ImageManipulationParser.T__11)
            self.state = 71
            self.match(ImageManipulationParser.NUMBER)
            self.state = 72
            self.match(ImageManipulationParser.T__11)
            self.state = 73
            self.match(ImageManipulationParser.NUMBER)
            self.state = 74
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RotateCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ImageManipulationParser.NUMBER, 0)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_rotateCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRotateCommand" ):
                listener.enterRotateCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRotateCommand" ):
                listener.exitRotateCommand(self)




    def rotateCommand(self):

        localctx = ImageManipulationParser.RotateCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_rotateCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ImageManipulationParser.T__13)
            self.state = 77
            self.match(ImageManipulationParser.T__2)
            self.state = 78
            self.match(ImageManipulationParser.NUMBER)
            self.state = 79
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SaveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ImageManipulationParser.ID, 0)

        def STRING(self):
            return self.getToken(ImageManipulationParser.STRING, 0)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_saveCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSaveCommand" ):
                listener.enterSaveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSaveCommand" ):
                listener.exitSaveCommand(self)




    def saveCommand(self):

        localctx = ImageManipulationParser.SaveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_saveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(ImageManipulationParser.ID)
            self.state = 82
            self.match(ImageManipulationParser.T__4)
            self.state = 83
            self.match(ImageManipulationParser.T__14)
            self.state = 84
            self.match(ImageManipulationParser.T__2)
            self.state = 85
            self.match(ImageManipulationParser.STRING)
            self.state = 86
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





