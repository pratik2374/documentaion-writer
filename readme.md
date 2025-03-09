# Document Writer: AST vs. Tree-Sitter

## Overview
This repository contains two different approaches for generating Python function documentation: **AST-based parsing** and **Tree-Sitter-based parsing**. Both implementations extract function details and use an LLM (Groq API) to generate documentation automatically.

---

## 1️⃣ AST-Based Document Writer

### Description
The **AST (Abstract Syntax Tree)** approach utilizes Python's built-in `ast` module to analyze a given Python script and extract relevant information about functions, classes, and imports. The extracted data is then processed and passed to an AI model to generate meaningful documentation.

### Features
- Uses Python's native `ast` module for parsing.
- Extracts functions, classes, and imports.
- Captures function names, arguments, and docstrings.
- Generates documentation in **Markdown format** (`output.md`).

### Workflow
1. Reads and parses a Python script using `ast.parse()`.
2. Extracts function definitions, arguments, and existing docstrings.
3. Sends extracted details to an AI model for docstring generation.
4. Saves the generated documentation into `output.md`.

### File Generated
- `output.md`: Contains the generated documentation in Markdown format.

---

## 2️⃣ Tree-Sitter-Based Document Writer

### Description
The **Tree-Sitter** approach uses a more advanced parsing technique, enabling precise function extraction even in cases where the AST parser might struggle (e.g., handling dynamically generated code or more complex syntax structures).

### Features
- Uses **Tree-Sitter**, a powerful incremental parsing tool.
- Extracts function names and their parameters efficiently.
- Generates structured documentation using Groq AI.
- Saves output in **Markdown format** (`outputs.md`).

### Workflow
1. Uses Tree-Sitter to parse a Python script and identify function nodes.
2. Extracts function names and parameters from the syntax tree.
3. Sends the extracted details to an AI model for generating docstrings.
4. Saves the generated documentation into `outputs.md`.

### File Generated
- `outputs.md`: Contains the generated documentation in Markdown format.

---

## 🔍 Comparison: AST vs. Tree-Sitter
| Feature            | AST-Based Approach  | Tree-Sitter-Based Approach  |
|--------------------|--------------------|----------------------------|
| Parsing Method    | Python `ast` module | Tree-Sitter Parser |
| Function Extraction | ✅ Extracts functions | ✅ Extracts functions |
| Class Extraction   | ✅ Yes | ❌ No |
| Import Extraction  | ✅ Yes | ❌ No |
| Handles Complex Syntax | ❌ Limited | ✅ More robust |
| Output File       | `output.md` | `outputs.md` |

### Summary
- **AST-Based Approach** is simpler, leveraging built-in Python modules but is limited in handling complex syntax.
- **Tree-Sitter-Based Approach** is more robust, efficiently handling complex structures but requires an external parser.

Both implementations generate structured documentation automatically, helping in code documentation and analysis. Choose based on your project needs!



---

## Setup & Usage

1. Clone this repository:

   ```sh
   git clone https://github.com/yourusername/document-writer.git
   cd document-writer
   ```

2. Install dependencies (for Tree-Sitter only):

   ```sh
   pip install tree-sitter tree-sitter-languages langchain-groq
   ```

3. Run the AST-based parser:

   ```sh
   python document_writer_ast.py
   ```

4. Run the Tree-Sitter-based parser:

   ```sh
   python document_writer_tree.py
   ```

5. Check the generated files:

   - `output.md` (from AST-based parser)
   - `outputs.md` (from Tree-Sitter-based parser)

---

## License

This project is open-source and available under the MIT License.

Author-Kush
