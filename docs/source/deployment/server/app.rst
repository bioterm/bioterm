..    include:: <isonum.txt>
.. App:

######################
App
######################

Required entries in :file:`${BIOTERM_ROOT_DIRECTORY}/bioterm/server/frontend/webui/.env`:

.. code-block:: bash

    API_URL="https://${API_PUBLIC_DOMAIN}"
    BASE_URL="https://${APP_PUBLIC_DOMAIN}"
    AUTH0_DOMAIN="https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o"
    AUTHENTIK_METADATA_URL="https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o/bioterm/.well-known/openid-configuration"
    AUTHENTIK_CLIENT_ID="" # insert authentik client ID obtained from backend provider settings
    AUTHENTIK_REDIRECT_URI="https://${APP_PUBLIC_DOMAIN}/callback.html"
    AUTHENTIK_POST_LOGOUT_REDIRECT_URI="https://${APP_PUBLIC_DOMAIN}"
    AUTHENTIK_AUTHORIZE_URI="https://${AUTHENTIK_PUBLIC_DOMAIN}/application/o/authorize/"
    ELN_DOMAIN="${ELN_PUBLIC_DOMAIN}"
    GRAFANA_DOMAIN="${GRAFANA_PUBLIC_DOMAIN}"


.. warning::

    The :file:`.env` file is required for the following docker build process!

Navigate to :file:`${BIOTERM_ROOT_DIRECTORY}/bioterm/server/frontend`, build the docker image, and then run it using the docker-compose file:

.. code-block:: console

    $ sudo docker buildx build -t bioterm/server/frontend .
    $ sudo docker compose up -d
