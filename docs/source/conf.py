r"""
Sphinx configuration
"""
import os, sys

sys.path.insert(0, os.path.abspath('../..'))


#import scsemiprofiler
project = 'scSemiProfiler'
version = '1.0.0'
release = '1.0.0'
author = "Jingtao Wang"
copyright = "McGill Ding Lab, 2023"



extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
