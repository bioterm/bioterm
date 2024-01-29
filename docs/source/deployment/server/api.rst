..    include:: <isonum.txt>
.. _API:

######################
bioterm Backend Setup
######################


.. To rebuild images listed in docker-compose files run:

.. .. code-block:: console

..     $ sudo docker compose up -d --build

Create a :file:`.env` file in the :file:`bioterm/server/backend` directory with the following content:

.. code-block:: bash

    SECRET_KEY="" # use 'openssl rand -base64 32' to generate SECRET_KEY
    POSTGRES_USER=postgres
    POSTGRES_DB=bioterm
    POSTGRES_PASSWORD="" # insert value of POSTGRES_PASSWORD from ${BIOTERM_ROOT_DIRECTORY}/bioterm/server/backend/.env
    GF_SECURITY_ADMIN_PASSWORD="" # insert value of GF_SECURITY_ADMIN_PASSWORD from ${BIOTERM_ROOT_DIRECTORY}/bioterm/server/grafana/.env
    GF_SERVER_DOMAIN="${GRAFANA_PUBLIC_DOMAIN}"
    GF_SERVER_ROOT_URL="https://${GRAFANA_PUBLIC_DOMAIN}"
    AUTHENTIK_CLIENT_ID="" # insert authentik client ID obtained from backend provider settings
    AUTHENTIK_URL="https://${AUTHENTIK_PUBLIC_DOMAIN}"
    AUTHENTIK_ISSUER="https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o/bioterm/"

Then, append the public key of authentik's self-signed certificate.
Open the authentik page at ``${AUTH_PUBLIC_DOMAIN}`` and navigate to the :menuselection:`Admin interface`.
Go to System |rarr| Certificates and expand the **authentik Self-signed Certificate** card.
Export the certificate by clicking :menuselection:`Download Certificate` and store it in the :file:`bioterm/server/backend` directory.
Then cd into this directory and run the following bash command to append the public key as a single line string to the :file:`.env` file (with newline characters inserted):

.. code-block:: console

    $ printf 'AUTHENTIK_PUBLIC_KEY = "%s"\n' "$(openssl x509 -in 'authentik Self-signed Certificate_certificate.pem' -pubkey -noout | awk '{printf "%s\\n",$0}')" >> .env

.. warning::

    Certificates should not be checked into Git version control.
    The .gitignore settings ignore both .env and common certificate files.


To build the biotermserverapi docker image run while in the bioterm root directory:

.. code-block:: console

    $ sudo docker buildx build -t bioterm/server/backend -f bioterm/server/backend/Dockerfile .

After a successful build, change into the backend directory and start all containers using docker compose:

.. code-block:: console

    $ cd bioterm/server/backend
    $ sudo docker compose up -d

To initialize the database (or update it), run the following command:

.. code-block:: console

    $ sudo docker compose exec -it bioterm-dbworker /bin/bash

In the openend interactive shell of the bioterm-dbworker container run

.. code-block:: console

    $ alembic -c bioterm/server/backend/alembic.ini upgrade head

to initialize/update the database.


**********************
Working with swagger
**********************

The swagger documentation should now be accessible at `${API_PUBLIC_DOMAIN}/docs`.

Use the :menuselection:`Authorize` button in the top right corner to start the authentication process with authentik.
In the popup, the **client_id** should already be filled out while the **client_secret** remains blank.
Click on the popup's :menuselection:`Authorize` button, which will redirect you to authentik for logging it.
After a successful login, you will get redirected to the swagger documentation page and are able to try out the API's endpoint.

.. note::

    Some endpoints are only accessible with an API-key.


.. warning::

    Currently, the received token is not refreshed within swagger.
    You need to use the :menuselection:`Authorize` button in the top right corner to logout and login again.
