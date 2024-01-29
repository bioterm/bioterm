######################
Coding Style Guide
######################

*****************
reStructuredText
*****************

Content of ``.vscode/settings.json``: 

.. code-block:: json

    {
        "[python]": {
            "editor.defaultFormatter": "ms-python.black-formatter"
        },
        "python.formatting.provider": "none",
        "esbonio.sphinx.buildDir": "${workspaceFolder}/_build/html",
        "esbonio.sphinx.confDir": "${workspaceFolder}/docs/source",
        "esbonio.sphinx.srcDir": "${workspaceFolder}/docs/source"
    }


Headings
=========

In reST documents, follow the `Python Developer's Guide for documenting <https://devguide.python.org/documentation/markup/#sections>`_:

- \# with overline, for parts

- \* with overline, for chapters

- \= for sections

- \- for subsections

- \^ for subsubsections

- \" for paragraphs
