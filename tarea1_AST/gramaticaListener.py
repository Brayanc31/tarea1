# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#prog.
    def enterProg(self, ctx:gramaticaParser.ProgContext):
        pass

    # Exit a parse tree produced by gramaticaParser#prog.
    def exitProg(self, ctx:gramaticaParser.ProgContext):
        pass


    # Enter a parse tree produced by gramaticaParser#TermAlt.
    def enterTermAlt(self, ctx:gramaticaParser.TermAltContext):
        pass

    # Exit a parse tree produced by gramaticaParser#TermAlt.
    def exitTermAlt(self, ctx:gramaticaParser.TermAltContext):
        pass


    # Enter a parse tree produced by gramaticaParser#AddSub.
    def enterAddSub(self, ctx:gramaticaParser.AddSubContext):
        pass

    # Exit a parse tree produced by gramaticaParser#AddSub.
    def exitAddSub(self, ctx:gramaticaParser.AddSubContext):
        pass


    # Enter a parse tree produced by gramaticaParser#MulDiv.
    def enterMulDiv(self, ctx:gramaticaParser.MulDivContext):
        pass

    # Exit a parse tree produced by gramaticaParser#MulDiv.
    def exitMulDiv(self, ctx:gramaticaParser.MulDivContext):
        pass


    # Enter a parse tree produced by gramaticaParser#FactorAlt.
    def enterFactorAlt(self, ctx:gramaticaParser.FactorAltContext):
        pass

    # Exit a parse tree produced by gramaticaParser#FactorAlt.
    def exitFactorAlt(self, ctx:gramaticaParser.FactorAltContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Number.
    def enterNumber(self, ctx:gramaticaParser.NumberContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Number.
    def exitNumber(self, ctx:gramaticaParser.NumberContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Identifier.
    def enterIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Identifier.
    def exitIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        pass


    # Enter a parse tree produced by gramaticaParser#Parens.
    def enterParens(self, ctx:gramaticaParser.ParensContext):
        pass

    # Exit a parse tree produced by gramaticaParser#Parens.
    def exitParens(self, ctx:gramaticaParser.ParensContext):
        pass



del gramaticaParser