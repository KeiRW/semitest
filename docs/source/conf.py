r"""
Sphinx configuration
"""
import os, sys
import inspect
import sphinx_autodoc_typehints

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

    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx_autodoc_typehints',
    'sphinx_copybutton',
    'nbsphinx'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}

intersphinx_mapping = dict(
    python=('https://docs.python.org/3/', None),
    numpy=('https://numpy.org/doc/stable/', None),
    scipy=('https://docs.scipy.org/doc/scipy/reference/', None),
    pandas=('https://pandas.pydata.org/pandas-docs/stable/', None),
    sklearn=('https://scikit-learn.org/stable/', None),
    matplotlib=('https://matplotlib.org/stable/', None),
    seaborn=('https://seaborn.pydata.org/', None),
    networkx=('https://networkx.org/documentation/stable/', None),
    anndata=('https://anndata.readthedocs.io/en/stable/', None),
    scanpy=('https://scanpy.readthedocs.io/en/stable/', None),
    torch=('https://pytorch.org/docs/stable/', None),
    ignite=('https://pytorch.org/ignite/', None),
    plotly=('https://plotly.com/python-api-reference/', None)
)

qualname_overrides = {
    'anndata._core.anndata.AnnData': 'anndata.AnnData',
    'matplotlib.axes._axes.Axes': 'matplotlib.axes.Axes',
    'networkx.classes.graph.Graph': 'networkx.Graph',
    'networkx.classes.digraph.DiGraph': 'networkx.DiGraph',
    'networkx.classes.multigraph.MultiGraph': 'networkx.MultiGraph',
    'networkx.classes.multidigraph.MultiDiGraph': 'networkx.MultiDiGraph',
    'numpy.random.mtrand.RandomState': 'numpy.random.RandomState',
    'pandas.core.frame.DataFrame': 'pandas.DataFrame',
    'scipy.sparse.base.spmatrix': 'scipy.sparse.spmatrix',
    'seaborn.axisgrid.JointGrid': 'seaborn.JointGrid',
    'torch.device': 'torch.torch.device',
    'torch.nn.modules.module.Module': 'torch.nn.Module'
}

fa_orig = sphinx_autodoc_typehints.format_annotation
def format_annotation(annotation, config, fully_qualified=True):  # pylint: disable=unused-argument
    r"""
    Adapted from https://github.com/agronholm/sphinx-autodoc-typehints/issues/38#issuecomment-448517805
    """
    if inspect.isclass(annotation):
        full_name = f'{annotation.__module__}.{annotation.__qualname__}'
        override = qualname_overrides.get(full_name)
        if override is not None:
            return f':py:class:`~{override}`'
    return fa_orig(annotation)
sphinx_autodoc_typehints.format_annotation = format_annotation


intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output
#html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
