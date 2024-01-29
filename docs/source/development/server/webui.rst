..    include:: <isonum.txt>
.. WEBUI:

######################
webUI
######################


To install nodejs, run the following commands:

.. code-block:: console

    $ curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - && sudo apt-get install -y nodejs


.. warning::

    We need node v18.16.1 and npm v9.5.1

Then install quasar cli:

.. code-block:: console

    $ npm i -g @quasar/cli
.. $ npm init quasar

Development server works by running in :file:`${BIOTERM_ROOT_DIRECTORY}/bioterm/server/frontend/web_ui`

.. code-block:: console

    $ quasar dev

When running ``$ quasar dev`` at this point, the webpage at ${APP_PUBLIC_DOMAIN} will not be running correctly and the console log will output websocket connection errors and webpack-dev-server errors.
Also, when opening ``localhost:8081`` the login button won't work, with the console indicating CORS policy violations.
There are three possible solutions, all of which need to be evaluated further before deciding on a way.

**Solution 1 (possibly the worst with regards to developing comfort)**

Disable the hot module reload (HMR) functionality of the quasar dev server by commenting in the lines below in :file:`quasar.config.js`:

.. code-block:: javascript

    ...
    devServer: {

      // the following lines can be enabled to deactivate the HMR when developing
      hot: false,
      liveReload: false,
      webSocketServer: false,

        ...
    },
    ...


**Solution 2 (slightly less worse)**

Add the following URIs to the *Redirect URIs/Origins (RegEx)* backend provider settings in authentik:

.. code-block:: none

    http://localhost:8081/callback.html

However, this will downgrade the protocol to http and bypass the nginx reverse proxy, so overall, it won't reflect the production setup as good.

**Solution 3 (currently preferred solution)**

Commenting out the lines below in :file:`quasar.config.js` (and leaving the lines from solution 2 commented in) allows specifying the URL to the web socket server when you're proxying the dev server and the client script does not know where to connect to:

.. code-block:: javascript

    ...
    devServer: {

      // the following lines can be enabled to deactivate the HMR when developing
      // hot: false,
      // liveReload: false,
      // webSocketServer: false,

      // to get protocol/hostname/port from browser use
      client: {
        webSocketURL: 'auto://0.0.0.0:0/ws'
      },
        ...
    },
    ...

This solution does not require additions to the *Redirect URIs/Origins (RegEx)* backend provider settings in authentik and won't bypass the nginx reverse proxy (so you can still navigate to ${APP_PUBLIC_DOMAIN}).


****
PWA
****

During development it is **not recommended** to run

.. code-block:: console

    $ quasar dev -m pwa
