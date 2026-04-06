# Tarea 1 - Generador de AST

## Descripción
Programa que dada una gramática y una cadena, genera el Árbol de Sintaxis Abstracta (AST) usando ANTLR y Python.

## Requisitos
- Python 3.8+
- Graphviz (para generar la imagen del árbol)

## Instalación
```bash
pip install antlr4-python3-runtime graphviz
```

## Uso
1. Crear un archivo `entrada.txt` con una expresión, por ejemplo:
   ```
   2 + 3 * 4
   ```
2. Ejecutar:
   ```bash
   python arbolAST.py entrada.txt
   ```
3. Resultados:
   - Se muestra el AST en consola
   - Se genera la imagen `entrada_ast.png` con el árbol visual

## Archivos incluidos
| Archivo | Descripción |
|---------|-------------|
| `arbolAST.py` | Script principal |
| `gramatica.g4` | Gramática en formato ANTLR |
| `gramaticaLexer.py` | Lexer generado |
| `gramaticaParser.py` | Parser generado |
| `gramaticaVisitor.py` | Visitor generado |
| `entrada.txt` | Ejemplo de entrada |
| `requirements.txt` | Dependencias |

## Gramática
Reconoce expresiones con:
- Operadores: `+`, `-`, `*`, `/`
- Números enteros
- Identificadores (letras)
- Paréntesis

Respeta **precedencia** (`*` y `/` antes que `+` y `-`) y **asociatividad izquierda**.

## Nota
Los archivos `gramatica*Lexer/Parser/Visitor/Listener.py` fueron generados con ANTLR e incluidos para que el programa funcione sin necesidad de instalar Java.
```

