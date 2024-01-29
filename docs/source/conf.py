# Configuration file for the Sphinx documentation builder.

import os
import sys

includedir = os.path.abspath(f"{os.path.dirname(__file__)}/../..")

print(f"{includedir}")
sys.path.insert(0, includedir)

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "bioterm"
copyright = "2023, Nils Stanislawski"
author = "Nils Stanislawski"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.coverage",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
    "sphinx.ext.todo",
    "sphinx_favicon",
]

templates_path = ["_templates"]
exclude_patterns = []

copybutton_exclude = ".linenos, .gp"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

favicons = [
    {"href": "bioterm_icon.svg"},  # => use `_static/icon.svg`
    {"href": "bioterm_icon_16x16.png"},
    {"href": "bioterm_icon_32x32.png"},
    {
        "rel": "apple-touch-icon",
        "href": "bioterm_icon_180x180.png",
    },
]

# Display todos by setting to True
todo_include_todos = True

# Change sorting order to mirror source, not alphabetically.
autodoc_member_order = "bysource"
