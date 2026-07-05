# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'With Deepest Regret...'
copyright = '2026, Rod'
author = 'Rod'
release = '0.9.2'
version = '0.9.2'

extensions = [
    'sphinx.ext.autosectionlabel',
]

# Make autosectionlabel unique per document (needed since many sections
# share subsection titles across chapters, e.g. multiple "Overview" headers)
autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# Preserve rule-numbering order in the sidebar rather than alphabetising
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Numbered figure/table support for future use (maps, counter diagrams)
numfig = True

# Keep the build strict: warnings (e.g. malformed tables, bad refs) should
# be visible rather than silently swallowed.
suppress_warnings = []
