..    include:: <isonum.txt>
.. BACKEND:

######################
backend
######################


********
Alembic
********

During development, run

.. code-block:: console

    $ alembic -c bioterm/server/backend/alembic.ini revision --autogenerate -m "Initial migration"

in the `${BIOTERM_ROOT_DIRECTORY}`.

Review the file created in :file:`./bioterm/server/backend/alembic/versions` and conduct manual changes.
Finally, run

.. code-block:: console

    $ alembic -c bioterm/server/backend/alembic.ini upgrade head

to apply the migrations
