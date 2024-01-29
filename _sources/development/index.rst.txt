..    include:: <isonum.txt>
.. Development:

######################
Development
######################

.. toctree::
   :maxdepth: 2
   :caption: Server setup:
   :hidden:

   documentation
   debugging
   server/index
   controller/index
   devices/index


*************
Prerequisits
*************

The ${BIOTERM_ROOT_DIRECTORY} contains an additional :file:`requirements_dev.txt` file for developers.
Use

.. code-block:: console

    $ pip install -r requirements_dev.txt

after having your virtual environment activated, to install the additional packages required for developing.
Then, run

.. code-block:: console

    $ pre-commit install  # installs .git/hooks/pre-commit
    $ pre-commit install --hook-type pre-push  # installs .git/hooks/pre-push

to set up the git hook scripts stored in :file:`.pre-commit-config.yaml` in the :file:`.git/hooks` directory.



***********
Settings
***********

When deploying on a local machine, certain settings need to be adopted to ease the development.
This especially concerns the server backend and frontend, which are dockerized for production deployment and
The nginx configuration needs to be adopted as well, to point to either the docker container's host adress or the local machine's localhost.

In addition, on a local machine self-signed certificates are used and TLS verification needs to be disabled.

.. warning::

    Don't forget to turn TLS verification back on when deploying for production, as this might get by unnoticed.

Backend
=============

In the :file:`docker-compose.yml` file, uncomment the ports directive for the *timescaledb* service:

.. code-block:: yaml

    ...
        timescaledb:
            ...
            ports:
            - 5432:5432
    ...

Also, disable the *biotermserverapi* service completely by commenting out the whole service and its directives.

Then, change the environment variable **POSTGRES_SERVER** from *timescaledb:5432* to *localhost:5432*.

Set the environment variable **USE_TLS** to *False*.

.. warning::

    FastAPI requires Python 3.9 !

Then, set up a virtual environment and install the required packages located in :file:`bioterm/server/backend/requirements.txt`:

.. code-block:: console

    $ python3.9 -m venv .venv
    $ source .venv/bin/activate
    $ pip install -r requirements.txt

run

.. code-block:: console

    $ sudo docker compose up -d

in :file:`bioterm/server/backend` to start the PostgreSQL service.

To run the server use the following command in the bioterm root directory:

.. code-block:: console

    $ uvicorn bioterm.server.backend.app.main:app --reload --host 0.0.0.0 --port 8001



Frontend
=============

For information regarding frontend development, please refer to :doc:`server/webui`.

NGINX
=============

For local development, change the API section configuration as follows:

.. code-block:: bash

    ### API SECTION

    server {

        ...

        location / {
            # set $api_upstream http://biotermserverapi:8001;
            # proxy_pass $api_upstream;
            proxy_pass http://host.docker.internal:8001;

            ...

        }
    }

Change the APP section as follows:

.. code-block:: bash

    ### APP SECTION

    server {

        ...

        location / {
            # set $app_upstream http://bioterm-webui:8081;
            # proxy_pass $app_upstream;
            proxy_pass http://host.docker.internal:8081/;

            ...

        }
    }

authentik
=============

**********************
Commmitlint
**********************

- ``feat``: new feature
- ``fix``: bug fix
- ``docs``: changes to the documentation
- ``style``: formatting, missing semi colons, etc; no production code change
- ``refactor``: refactoring production code, eg. renaming a variable, moving stuff around
- ``test``: adding missing tests, refactoring tests; no production code change
- ``chore``: TBD

**********************
Coding Style
**********************

Please check :doc:`documentation` for details.
