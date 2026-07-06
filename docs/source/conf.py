# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = 'With Deepest Regret...'
copyright = '2026, Rod Peters'
author = 'Rod Peters'
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

# Field-manual reskin (olive/khaki/aged-paper) over the default RTD blue/white
html_css_files = ['custom.css']

# Numbered figure/table support for future use (maps, counter diagrams)
numfig = True

# Keep the build strict: warnings (e.g. malformed tables, bad refs) should
# be visible rather than silently swallowed.
suppress_warnings = []

# Adds a "Last updated on <date>" line to every page's footer (sphinx_rtd_theme
# renders this automatically once set). Reflects each build's checkout time on
# Read the Docs, not per-file git history -- same tradeoff as most RTD sites.
html_last_updated_fmt = '%d %B %Y'
