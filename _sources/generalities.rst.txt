..    include:: <isonum.txt>
.. General Specifications:

######################
General Specifications
######################

***********
Terminology
***********

**Server:**  runs various services to provide authentication, an electronic lab notebook, the backend for receiving data from controllers, and a web-based user interface for interacting with the backend.

**Controller:** runs software to control the connected devices and send the collected data to the server. Controller software can run on the same hardware as the server.

**Device:** a sensor or actuator (or a combination of both) connected to the controller.

******************
Folder Structure
******************

After cloning the repository, the folder structure should look a lot like this:

::

    ${BIOTERM_ROOT_DIRECTORY}
    ├── .git
    ├── bioterm
    │   ├── common
    │   ├── controller
    │   │   └── devices
    │   └── server
    ├── deployment
    ├── docs
    ├── README.md
    └── requirements.txt

***********
Variables
***********

.. list-table:: Variables
   :widths: 25 25 50
   :header-rows: 1

   * - Variable
     - Default
     - Description
   * - ${BIOTERM_ROOT_DIRECTORY}
     -
     - The top-level directory of the bioterm repository (the one containing the :file:`.git` folder)
   * - ${NGINX_DOMAIN_LIST}
     -
     -
   * - ${NGINX_PRIMARY_DOMAIN}
     -
     -
   * - ${NGINX_PROXY_PASS}
     -
     -
   * - ${LETSENCRYPT_EMAIL}
     -
     -
   * - ${LETSENCRYPT_STAGING}
     -
     -
   * - ${APP_PUBLIC_DOMAIN}
     -
     -
   * - ${ELN_PUBLIC_DOMAIN}
     -
     -
   * - ${AUTH_PUBLIC_DOMAIN}
     -
     -
   * - ${GRAFANA_PUBLIC_DOMAIN}
     -
     -
   * - ${API_PUBLIC_DOMAIN}
     -
     -
   * - ${TELEPORT_PUBLIC_DOMAIN}
     -
     -
