import os
import nbformat


# Get env variables
env_vars = os.environ

# Open notebook
notebook = nbformat.read(env_vars['file'])

# Get current header cell
current_header_cell = notebook['cells'][0]

# Process header
if current_header_cell['source'] == env_vars['CELL_SOURCE']:
    status = 'Header cell already present.'
else:
    header_cell = nbformat.v4.new_markdown_cell(source=env_vars['CELL_SOURCE'])
    notebook['cells'].insert(0, header_cell)
    status = 'Header cell insterted.'

# Save notebook
nbformat.write(notebook, env_vars['file'])

# Write status as env var
os.environ['STATUS'] = status