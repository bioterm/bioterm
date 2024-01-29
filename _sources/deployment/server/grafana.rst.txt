..    include:: <isonum.txt>
.. _Grafana Setup:

*************
Grafana Setup
*************

Perform the steps described below in the :file:`/bioterm/bioterm/server/grafana/` directory.

Run the :file:`init.sh` script.
After completion, extract the authentik client ID and client secret for the grafana provider and manually insert them in the created :file:`.env` file.

.. .. code-block:: console

..     $ sudo apt-get install -y pwgen # this should already be installed (see authentik documentation)
..     $ echo "GF_SECURITY_ADMIN_PASSWORD: $(pwgen -s 40 1)" > .env

.. Append the following lines to the :file:`.env` file (see :doc:`authentik` on information regarding the client id and client secret):

.. .. code-block:: bash

..     GF_SERVER_DOMAIN: "${GRAFANA_PUBLIC_DOMAIN}"
..     GF_SERVER_ROOT_URL: "https://${GRAFANA_PUBLIC_DOMAIN}"
..     GF_AUTH_GENERIC_OAUTH_AUTH_URL: "https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o/authorize/"
..     GF_AUTH_GENERIC_OAUTH_TOKEN_URL: "https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o/token/"
..     GF_AUTH_GENERIC_OAUTH_API_URL: "https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o/userinfo/"
..     GF_AUTH_SIGNOUT_REDIRECT_URL: "https://${AUTHENTIK_PUBLIC_DOMAIN}/if/session-end/grafana/"
..     GF_AUTH_GENERIC_OAUTH_CLIENT_ID: "" # insert authentik client ID obtained from provider settings
..     GF_AUTH_GENERIC_OAUTH_CLIENT_SECRET: "" # insert authentik client secret obtained from provider settings

Optionally, add the following lines for SMTP setup to the :file:`.env` file:

.. code-block:: bash

    GF_SMTP_ENABLED: true
    GF_SMTP_HOST: 
    GF_SMTP_USER:
    GF_SMTP_PASSWORD:
    GF_SMTP_FROM_ADDRESS:

Manually create the bind mount on the host and change the owner to user '472':

.. code-block:: console

    $ sudo mkdir -p /srv/docker/grafana
    $ sudo chown 472 /srv/docker/grafana

Then run 

.. code-block:: console

    $ sudo docker compose up -d

to start the container.

By default, the local login (user: ``admin``, pw: *see generated password in .env*) can not login because the :file:`docker-compose.yml` sets ``GF_AUTH_OAUTH_AUTO_LOGIN: "true"``.

.. Working with custom CA
.. -----------------------

.. Grafana running with docker requires a custom CA file (PEM) (see :doc:`certificates`) to be placed in :file:`/etc/ssl/certs/`, otherwise an error will be thrown when using oauth.

.. note::

  Continue here, after finishing the setup of the backend and frontend.

Data Sources
============

PostgreSQL
----------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Name
     - ``PostgreSQL``
   * - Default
     - **Enabled**
   * - Host
     - ``timescaledb:5432``
   * - Database
     - ``mydatabase``
   * - User
     - ``$POSTGRES_USER``
   * - Password
     - ``$POSTGRES_PASSWORD``
   * - TLS/SSL Mode
     - **disable**
   * - Version
     - **12**
   * - TimescaleDB
     - **Enabled**
   * - Min time interval
     - ``1s``

Loki
----

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Name
     - ``Loki``
   * - Default
     - **Disabled**
   * - Host
     - ``http://loki:3100``


Prometheus
----------

.. list-table::
   :widths: 50 50
   :header-rows: 1

   * - Name
     - ``Prometheus``
   * - Default
     - **Disabled**
   * - Host
     - ``http://prometheus:9090``