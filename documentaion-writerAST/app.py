import ast
from tree_sitter import Language, Parser
from langchain_groq import ChatGroq
#from tree_sitter_languages import get_language
from langchain_core.messages import HumanMessage
import textwrap

import ast
from tree_sitter import Language, Parser

def parse_python_code(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read())

    functions = []
    classes = []
    imports = []
    
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_name = node.name
            args = [arg.arg for arg in node.args.args]
            docstring = ast.get_docstring(node)
            functions.append({"name": func_name, "args": args, "docstring": docstring})
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Import):
            imports.extend([name.name for name in node.names])
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)
    
    return {"functions": functions, "classes": classes, "imports": imports}

def generate_documentation(parsed_data):
    llm = ChatGroq(model_name="gemma2-9b-it", api_key="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")
    documentation = {}
    
    for func in parsed_data["functions"]:
        prompt = f"""
        Generate a detailed documentation for the following function:
        
        **Function Name:** `{func['name']}`
        **Arguments:** `{', '.join(func['args'])}`
        **Existing Docstring:**
        ```python
        {func['docstring'] or 'None'}
        ```
        
        Provide a meaningful docstring with usage examples in proper markdown format with proper spacing and new line
        """
        response = llm.invoke([HumanMessage(content=prompt)])
        formatted_response = f"""```python\n{response.content.strip()}\n```"""
        documentation[func["name"]] = formatted_response
    
    return documentation





file_path = "example.py"  # Replace with an actual Python script path
parsed_data = parse_python_code(file_path)
documentation = generate_documentation(parsed_data)

# Convert documentation to markdown format
markdown_content = "\n".join(f"## {func_name}\n{doc}\n" for func_name, doc in documentation.items())

# Save the markdown content to output.md
with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(documentation)



# from tree_sitter_languages import get_language

# PY_LANGUAGE = get_language("python")  # Corrected method
# parser = Parser()
# parser.set_language(PY_LANGUAGE)

# def parse_with_tree_sitter(code):
#     tree = parser.parse(code.encode("utf-8"))
#     return tree.root_node.sexp()

# # Example usage
# tree_output = parse_with_tree_sitter("def hello(name): return 'Hello ' + name")
# print(tree_output)
