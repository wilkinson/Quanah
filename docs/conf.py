#-  Sphinx build configuration file

#-  conf.py ~~
#
#   This file was originally generated by `sphinx-quickstart`, but it wasn't
#   especially readable (because I'm a picky jerkface). It's important to note
#   the following:
#
#   -   This file is execfile()d with the current directory set to its
#       containing dir.
#
#   -   Note that not all possible configuration values are present in this
#       file.
#
#   -   All configuration values have a default; values that were commented out
#       served to show the default, and I removed most of them.
#
#                                                       ~~ (c) SRW, 09 Jul 2014
#                                                   ~~ last updated 24 Nov 2014

import os, urllib

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.

extensions = []

# Add any paths that contain templates here, relative to this directory.

templates_path = ['_templates']

# The suffix of source filenames.

source_suffix = '.rst'

# The master toctree document.

master_doc = 'index'

# General information about the project.

project = u'Quanah'
copyright = u'2014, Sean Wilkinson'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.

version = '0.3'

# The full version, including alpha/beta/rc tags.

release = '0.3.0'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.

exclude_patterns = ['_build']

# The name of the Pygments (syntax highlighting) style to use.

pygments_style = 'sphinx'


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'default'

# Here, we will download a favicon from QM's homepage dynamically during the
# build itself to avoid adding the image to the project repository. We need
# only set the name of the image file to be found within the static path, and
# it should be a 16x16 or 32x32 pixel Windows icon file (.ico).

try:
  os.stat('_static')
except:
  os.mkdir('_static')

try:
  urllib.urlretrieve('https://qmachine.github.io/quanah/favicon.ico', \
    os.path.join('_static', 'favicon.ico'))
  html_favicon = 'favicon.ico'
except:
  pass

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path = ['_static']

# Add directories that contain files not directly related to the documentation,
# such as "robots.txt" or ".htaccess" here.

#html_extra_path = ['_extra']

# Output file base name for HTML help builder.

htmlhelp_basename = 'Quanahdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'Quanah.tex', u'Quanah Documentation',
   u'Sean Wilkinson', 'manual'),
]

# If true, show page references after internal links.

latex_show_pagerefs = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).

man_pages = [
  ('index', 'quanah', u'Quanah Documentation', [u'Sean Wilkinson'], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)

texinfo_documents = [
  ('index', 'Quanah', u'Quanah Documentation', u'Sean Wilkinson', 'Quanah',
    'A framework for distributing and scheduling computations',
    'Miscellaneous'),
]


#-  vim:set syntax=python:
