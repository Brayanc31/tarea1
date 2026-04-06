# Generated from gramatica.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#prog.
    def visitProg(self, ctx:gramaticaParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#TermAlt.
    def visitTermAlt(self, ctx:gramaticaParser.TermAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#AddSub.
    def visitAddSub(self, ctx:gramaticaParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#MulDiv.
    def visitMulDiv(self, ctx:gramaticaParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#FactorAlt.
    def visitFactorAlt(self, ctx:gramaticaParser.FactorAltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Number.
    def visitNumber(self, ctx:gramaticaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Identifier.
    def visitIdentifier(self, ctx:gramaticaParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#Parens.
    def visitParens(self, ctx:gramaticaParser.ParensContext):
        return self.visitChildren(ctx)



del gramaticaParser