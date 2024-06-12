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
        4,1,26,120,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,4,0,26,8,0,11,0,
        12,0,27,1,1,1,1,1,1,3,1,33,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,45,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,69,8,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,
        7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,
        9,1,9,1,9,4,9,109,8,9,11,9,12,9,110,1,9,1,9,1,10,1,10,1,10,1,10,
        1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,0,0,124,0,25,1,0,0,
        0,2,32,1,0,0,0,4,34,1,0,0,0,6,46,1,0,0,0,8,68,1,0,0,0,10,70,1,0,
        0,0,12,77,1,0,0,0,14,88,1,0,0,0,16,93,1,0,0,0,18,100,1,0,0,0,20,
        114,1,0,0,0,22,26,3,2,1,0,23,26,3,18,9,0,24,26,3,20,10,0,25,22,1,
        0,0,0,25,23,1,0,0,0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,
        28,1,0,0,0,28,1,1,0,0,0,29,33,3,4,2,0,30,33,3,6,3,0,31,33,3,16,8,
        0,32,29,1,0,0,0,32,30,1,0,0,0,32,31,1,0,0,0,33,3,1,0,0,0,34,35,5,
        21,0,0,35,44,5,1,0,0,36,37,5,2,0,0,37,38,5,3,0,0,38,39,5,23,0,0,
        39,45,5,4,0,0,40,41,5,5,0,0,41,42,5,3,0,0,42,43,5,23,0,0,43,45,5,
        4,0,0,44,36,1,0,0,0,44,40,1,0,0,0,45,5,1,0,0,0,46,47,5,21,0,0,47,
        48,5,6,0,0,48,49,3,8,4,0,49,7,1,0,0,0,50,69,5,7,0,0,51,69,5,8,0,
        0,52,69,3,10,5,0,53,69,3,12,6,0,54,69,3,14,7,0,55,56,5,9,0,0,56,
        57,5,3,0,0,57,58,5,22,0,0,58,69,5,4,0,0,59,60,5,10,0,0,60,61,5,3,
        0,0,61,62,5,22,0,0,62,69,5,4,0,0,63,64,5,11,0,0,64,65,5,3,0,0,65,
        66,5,22,0,0,66,69,5,4,0,0,67,69,5,12,0,0,68,50,1,0,0,0,68,51,1,0,
        0,0,68,52,1,0,0,0,68,53,1,0,0,0,68,54,1,0,0,0,68,55,1,0,0,0,68,59,
        1,0,0,0,68,63,1,0,0,0,68,67,1,0,0,0,69,9,1,0,0,0,70,71,5,13,0,0,
        71,72,5,3,0,0,72,73,5,22,0,0,73,74,5,14,0,0,74,75,5,22,0,0,75,76,
        5,4,0,0,76,11,1,0,0,0,77,78,5,15,0,0,78,79,5,3,0,0,79,80,5,22,0,
        0,80,81,5,14,0,0,81,82,5,22,0,0,82,83,5,14,0,0,83,84,5,22,0,0,84,
        85,5,14,0,0,85,86,5,22,0,0,86,87,5,4,0,0,87,13,1,0,0,0,88,89,5,16,
        0,0,89,90,5,3,0,0,90,91,5,22,0,0,91,92,5,4,0,0,92,15,1,0,0,0,93,
        94,5,21,0,0,94,95,5,6,0,0,95,96,5,17,0,0,96,97,5,3,0,0,97,98,5,23,
        0,0,98,99,5,4,0,0,99,17,1,0,0,0,100,101,5,18,0,0,101,102,5,21,0,
        0,102,103,5,3,0,0,103,104,5,21,0,0,104,105,5,4,0,0,105,108,5,19,
        0,0,106,109,3,6,3,0,107,109,3,16,8,0,108,106,1,0,0,0,108,107,1,0,
        0,0,109,110,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,112,1,0,
        0,0,112,113,5,20,0,0,113,19,1,0,0,0,114,115,5,21,0,0,115,116,5,3,
        0,0,116,117,5,23,0,0,117,118,5,4,0,0,118,21,1,0,0,0,7,25,27,32,44,
        68,108,110
    ]

class ImageManipulationParser ( Parser ):

    grammarFileName = "ImageManipulation.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'open'", "'('", "')'", "'openFolder'", 
                     "'.'", "'flipX'", "'flipY'", "'saturation'", "'brightness'", 
                     "'contrast'", "'polynomial'", "'resize'", "','", "'crop'", 
                     "'rotate'", "'save'", "'def'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "ID", "NUMBER", "STRING", "LINE_COMMENT", 
                      "BLOCK_COMMENT", "WS" ]

    RULE_prog = 0
    RULE_command = 1
    RULE_assignment = 2
    RULE_action = 3
    RULE_actionType = 4
    RULE_resizeCommand = 5
    RULE_cropCommand = 6
    RULE_rotateCommand = 7
    RULE_saveCommand = 8
    RULE_funcDef = 9
    RULE_funcCall = 10

    ruleNames =  [ "prog", "command", "assignment", "action", "actionType", 
                   "resizeCommand", "cropCommand", "rotateCommand", "saveCommand", 
                   "funcDef", "funcCall" ]

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
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    ID=21
    NUMBER=22
    STRING=23
    LINE_COMMENT=24
    BLOCK_COMMENT=25
    WS=26

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


        def funcDef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ImageManipulationParser.FuncDefContext)
            else:
                return self.getTypedRuleContext(ImageManipulationParser.FuncDefContext,i)


        def funcCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ImageManipulationParser.FuncCallContext)
            else:
                return self.getTypedRuleContext(ImageManipulationParser.FuncCallContext,i)


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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 25
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 22
                    self.command()
                    pass

                elif la_ == 2:
                    self.state = 23
                    self.funcDef()
                    pass

                elif la_ == 3:
                    self.state = 24
                    self.funcCall()
                    pass


                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==18 or _la==21):
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
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.action()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
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
            self.state = 34
            self.match(ImageManipulationParser.ID)
            self.state = 35
            self.match(ImageManipulationParser.T__0)
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 36
                self.match(ImageManipulationParser.T__1)
                self.state = 37
                self.match(ImageManipulationParser.T__2)
                self.state = 38
                self.match(ImageManipulationParser.STRING)
                self.state = 39
                self.match(ImageManipulationParser.T__3)
                pass
            elif token in [5]:
                self.state = 40
                self.match(ImageManipulationParser.T__4)
                self.state = 41
                self.match(ImageManipulationParser.T__2)
                self.state = 42
                self.match(ImageManipulationParser.STRING)
                self.state = 43
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
            self.state = 46
            self.match(ImageManipulationParser.ID)
            self.state = 47
            self.match(ImageManipulationParser.T__5)
            self.state = 48
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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(ImageManipulationParser.T__6)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.match(ImageManipulationParser.T__7)
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.resizeCommand()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.cropCommand()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.rotateCommand()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.match(ImageManipulationParser.T__8)
                self.state = 56
                self.match(ImageManipulationParser.T__2)
                self.state = 57
                self.match(ImageManipulationParser.NUMBER)
                self.state = 58
                self.match(ImageManipulationParser.T__3)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 7)
                self.state = 59
                self.match(ImageManipulationParser.T__9)
                self.state = 60
                self.match(ImageManipulationParser.T__2)
                self.state = 61
                self.match(ImageManipulationParser.NUMBER)
                self.state = 62
                self.match(ImageManipulationParser.T__3)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.match(ImageManipulationParser.T__10)
                self.state = 64
                self.match(ImageManipulationParser.T__2)
                self.state = 65
                self.match(ImageManipulationParser.NUMBER)
                self.state = 66
                self.match(ImageManipulationParser.T__3)
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 9)
                self.state = 67
                self.match(ImageManipulationParser.T__11)
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
            self.state = 70
            self.match(ImageManipulationParser.T__12)
            self.state = 71
            self.match(ImageManipulationParser.T__2)
            self.state = 72
            self.match(ImageManipulationParser.NUMBER)
            self.state = 73
            self.match(ImageManipulationParser.T__13)
            self.state = 74
            self.match(ImageManipulationParser.NUMBER)
            self.state = 75
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
            self.state = 77
            self.match(ImageManipulationParser.T__14)
            self.state = 78
            self.match(ImageManipulationParser.T__2)
            self.state = 79
            self.match(ImageManipulationParser.NUMBER)
            self.state = 80
            self.match(ImageManipulationParser.T__13)
            self.state = 81
            self.match(ImageManipulationParser.NUMBER)
            self.state = 82
            self.match(ImageManipulationParser.T__13)
            self.state = 83
            self.match(ImageManipulationParser.NUMBER)
            self.state = 84
            self.match(ImageManipulationParser.T__13)
            self.state = 85
            self.match(ImageManipulationParser.NUMBER)
            self.state = 86
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
            self.state = 88
            self.match(ImageManipulationParser.T__15)
            self.state = 89
            self.match(ImageManipulationParser.T__2)
            self.state = 90
            self.match(ImageManipulationParser.NUMBER)
            self.state = 91
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
            self.state = 93
            self.match(ImageManipulationParser.ID)
            self.state = 94
            self.match(ImageManipulationParser.T__5)
            self.state = 95
            self.match(ImageManipulationParser.T__16)
            self.state = 96
            self.match(ImageManipulationParser.T__2)
            self.state = 97
            self.match(ImageManipulationParser.STRING)
            self.state = 98
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ImageManipulationParser.ID)
            else:
                return self.getToken(ImageManipulationParser.ID, i)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ImageManipulationParser.ActionContext)
            else:
                return self.getTypedRuleContext(ImageManipulationParser.ActionContext,i)


        def saveCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ImageManipulationParser.SaveCommandContext)
            else:
                return self.getTypedRuleContext(ImageManipulationParser.SaveCommandContext,i)


        def getRuleIndex(self):
            return ImageManipulationParser.RULE_funcDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncDef" ):
                listener.enterFuncDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncDef" ):
                listener.exitFuncDef(self)




    def funcDef(self):

        localctx = ImageManipulationParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_funcDef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(ImageManipulationParser.T__17)
            self.state = 101
            self.match(ImageManipulationParser.ID)
            self.state = 102
            self.match(ImageManipulationParser.T__2)
            self.state = 103
            self.match(ImageManipulationParser.ID)
            self.state = 104
            self.match(ImageManipulationParser.T__3)
            self.state = 105
            self.match(ImageManipulationParser.T__18)
            self.state = 108 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                if la_ == 1:
                    self.state = 106
                    self.action()
                    pass

                elif la_ == 2:
                    self.state = 107
                    self.saveCommand()
                    pass


                self.state = 110 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==21):
                    break

            self.state = 112
            self.match(ImageManipulationParser.T__19)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ImageManipulationParser.ID, 0)

        def STRING(self):
            return self.getToken(ImageManipulationParser.STRING, 0)

        def getRuleIndex(self):
            return ImageManipulationParser.RULE_funcCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCall" ):
                listener.enterFuncCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCall" ):
                listener.exitFuncCall(self)




    def funcCall(self):

        localctx = ImageManipulationParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ImageManipulationParser.ID)
            self.state = 115
            self.match(ImageManipulationParser.T__2)
            self.state = 116
            self.match(ImageManipulationParser.STRING)
            self.state = 117
            self.match(ImageManipulationParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





