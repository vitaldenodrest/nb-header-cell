import os
import sys
import nbformat


def update_notebook():
    # Get bash arguments
    file_path = sys.argv[1]
    cell_source = sys.argv[2]

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            notebook = nbformat.read(f, as_version=4)

        # Check whether nb has cells
        if len(notebook['cells']) > 0 and notebook['cells'][0]['source'] == cell_source:
            print(f"Skipping {file_path}: Header already present.")
        else:
            header_cell = nbformat.v4.new_markdown_cell(source=cell_source)
            notebook['cells'].insert(0, header_cell)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                nbformat.write(notebook, f)
            print(f"Success: Header inserted in {file_path}.")
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    update_notebook()