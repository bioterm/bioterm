
######################
Server setup
######################

.. toctree::
   :maxdepth: 2
   :caption: Server setup:
   :hidden:

   certificates
   teleport
   authentik
   elabftw
   grafana
   api
   app

**********************
Startup order
**********************

#. Create a docker bridge network on the host machine

	.. code-block:: console

		$ sudo docker network create -d bridge bioterm-net

#. Start NGINX and Certbot Services (`bioterm/bioterm/server/proxy/`)

	see :doc:`certificates`

	.. todo::
      
		Check if server tokens must be off (line 28 in nginx.conf.template)

#. Setup Teleport (`bioterm/bioterm/server/teleport/`)

	see :doc:`teleport`

#. Start SSO & SAML Service (`bioterm/bioterm/server/auth/`)

	see :doc:`authentik`

#. Start ELN Service (`bioterm/bioterm/server/eln/`)

	see :doc:`elabftw`

#. Start Grafana Service (`bioterm/bioterm/server/grafana/`)

	see :doc:`grafana`

#. Build and start API Service (`bioterm/bioterm/server/backend/`)

	see :doc:`api`

#. Build and serve frontend (`bioterm/bioterm/server/frontend/`)

	see :doc:`app`

#. Finish Grafana Setup  (`bioterm/bioterm/server/grafana/`)

	see :doc:`grafana`


***********
Development
***********

When working on a local machine, certain settings and configuration files need to be modified.
Check :doc:`../../development/index` for more information.