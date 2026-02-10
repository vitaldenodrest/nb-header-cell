# nb-header-cell
Inserting a cell at the beginning of Jupyter notebooks.


## Usage
```yaml
- uses: vitaldenodrest/nb-header-cell@v1
  with:
    # Cell source content. Note that this is a markdown cell
    # Required.
    cell_source:

    # Target files pattern
    # Optional. Default is '*.ipynb'
    file_pattern:
```