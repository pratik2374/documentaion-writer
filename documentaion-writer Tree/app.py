from tree_sitter import Parser
from tree_sitter_languages import get_language
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage
import os

# Initialize Tree-Sitter for Python
PY_LANGUAGE = get_language("python")
parser = Parser()
parser.set_language(PY_LANGUAGE)

def parse_python_code(code):
    """Parses Python code using Tree-Sitter and extracts function names & parameters."""
    tree = parser.parse(code.encode("utf-8"))
    root = tree.root_node

    functions = []

    def traverse(node):
        if node.type == "function_definition":
            func_name = node.child_by_field_name("name").text.decode("utf-8")
            parameters = [child.text.decode("utf-8") for child in node.children if child.type == "parameters"]
            functions.append({"name": func_name, "parameters": parameters})
        for child in node.children:
            traverse(child)

    traverse(root)
    return functions

def generate_documentation(functions):
    """Uses Groq AI to generate documentation for extracted functions."""
    api_key = "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"
    if not api_key:
        raise ValueError("GROQ_API_KEY is missing. Set it as an environment variable.")

    model = ChatGroq(model_name="gemma2-9b-it", api_key=api_key)
    
    documentation = {}
    for func in functions:
        prompt = f"""
        Write a detailed docstring for the Python function '{func['name']}' with parameters {func['parameters']}.
        Explain its purpose, expected inputs, outputs, and an example if possible.
        """
        response = model.invoke([HumanMessage(content=prompt)])
        documentation[func['name']] = response.content

    return documentation

# Read the Python file content
file_path = "example.py"  # Update with the correct path
with open(file_path, "r", encoding="utf-8") as f:
    sample_code = f.read()

# Run the parser
parsed_functions = parse_python_code(sample_code)
documentation = generate_documentation(parsed_functions)

# Convert to Markdown format
markdown_content = "\n".join(f"## {func_name}\n{doc}\n" for func_name, doc in documentation.items())

# Save to an output file
output_file = "outputs.md"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Documentation saved to {output_file}")
