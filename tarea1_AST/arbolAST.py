import sys
from antlr4 import *
from gramaticaLexer import gramaticaLexer
from gramaticaParser import gramaticaParser
from gramaticaVisitor import gramaticaVisitor
from graphviz import Digraph

# ----- Clases para el AST -----
class ASTNode:
    pass

class BinOp(ASTNode):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right

class Num(ASTNode):
    def __init__(self, value):
        self.value = value

class Id(ASTNode):
    def __init__(self, name):
        self.name = name

# ----- Visitor que construye el AST -----
class ASTBuilder(gramaticaVisitor):
    def visitProg(self, ctx):
        return self.visit(ctx.expr())

    def visitAddSub(self, ctx):
        return BinOp(ctx.getChild(1).getText(),
                     self.visit(ctx.expr()),
                     self.visit(ctx.term()))

    def visitTermAlt(self, ctx):
        return self.visit(ctx.term())

    def visitMulDiv(self, ctx):
        return BinOp(ctx.getChild(1).getText(),
                     self.visit(ctx.term()),
                     self.visit(ctx.factor()))

    def visitFactorAlt(self, ctx):
        return self.visit(ctx.factor())

    def visitNumber(self, ctx):
        return Num(int(ctx.NUMBER().getText()))

    def visitIdentifier(self, ctx):
        return Id(ctx.IDENT().getText())

    def visitParens(self, ctx):
        return self.visit(ctx.expr())

# ----- Dibujar el AST con Graphviz -----
def draw_ast(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph(format='png')
        graph.attr(rankdir='TB')
    node_id = str(id(node))
    if isinstance(node, BinOp):
        graph.node(node_id, node.op)
    elif isinstance(node, Num):
        graph.node(node_id, str(node.value))
    elif isinstance(node, Id):
        graph.node(node_id, node.name)
    if parent:
        graph.edge(parent, node_id)
    if isinstance(node, BinOp):
        draw_ast(node.left, graph, node_id)
        draw_ast(node.right, graph, node_id)
    return graph

# ----- Main -----
def main():
    if len(sys.argv) != 2:
        print("Uso: python arbolAST.py <archivo.txt>")
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        texto = f.read().strip()

    # Analizar
    input_stream = InputStream(texto)
    lexer = gramaticaLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = gramaticaParser(stream)
    tree = parser.prog()

    if parser.getNumberOfSyntaxErrors() > 0:
        print("Error: la cadena no pertenece a la gramática")
        sys.exit(1)

    # Construir AST y mostrar en consola
    builder = ASTBuilder()
    ast = builder.visit(tree)

    print("AST (notación LISP):", ast)  # lo muestra bonito porque __repr__ se hereda de object

    # Dibujar imagen
    try:
        graph = draw_ast(ast)
        output_file = sys.argv[1].replace('.txt', '_ast')
        graph.render(output_file, view=True, cleanup=True)
        print(f"\nImagen generada: {output_file}.png")
    except Exception as e:
        print(f"\nNo se pudo generar imagen: {e}")

if __name__ == '__main__':
    main()
