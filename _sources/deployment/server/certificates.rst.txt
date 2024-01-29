..    include:: <isonum.txt>
.. _Certificates:

############################################
Certificates & Reverse Proxy
############################################

Run the :file:`init.sh` script, to generate the required :file:`.env` file based on the user input for the primary domain.
The :file:`init.sh` script will also create the :file:`docker-compose.yml` file in the local directory and write the nginx configuration to :file:`/srv/docker/nginx/nginx.conf`.
The script will prompt the user, whether certificates should be obtained using certbot or if self-signed certificates are to be used.
Depending on the response, the certbot container will be commented out from the created :file:`docker-compose.yml` file.

If creating the .env file manually, it should contain the following variables:

.. code-block:: bash

    NGINX_DOMAIN_LIST="example.org app.example.org grafana.example.org eln.example.org auth.example.org api.example.org teleport.example.org"
    NGINX_PRIMARY_DOMAIN=example.org
    NGINX_PROXY_PASS="http://example.org"
    LETSENCRYPT_EMAIL=""
    LETSENCRYPT_STAGING="0"
    APP_PUBLIC_DOMAIN="app.example.org"
    ELN_PUBLIC_DOMAIN="eln.example.org"
    AUTH_PUBLIC_DOMAIN="auth.example.org"
    GRAFANA_PUBLIC_DOMAIN="grafana.example.org"
    API_PUBLIC_DOMAIN="api.example.org"
    TELEPORT_PUBLIC_DOMAIN="teleport.example.org"

.. warning::

    The ``LETSENCRYPT_STAGING`` setting only works for valid URLs (so *example.org* will not work).
    For local deployment using self-signed certificates this can remain at it's recommended value of "0".
    When moving to production and testing there, consider changing this to "1" to avoid the imposed rate limits.

***********
Certbot
***********

If certbot based certificates are to be obtained, the :file:`init.sh` will automatically call the :file:`certbot.sh` script, which in turn starts up both the certbot and nginx docker containers.
The certificates are stored in :file:`/srv/docker/certbot/conf/live/$\\{NGINX_PRIMARY_DOMAIN\\}` (which are actually just soft links).

.. warning::
    
    If running on arm-server make sure to select the correct docker image for certbot (``image: certbot/certbot:arm64v8-latest``), this should already be considered by the init script but if you're seeing some "exec format" issues this is likely the cause.

**********************
Self-signed
**********************

This approach aims to reproduce the certbot directory and file structure so transitioning from testing to production setup is streamlined.

Similar to the certbot based setup, the :file:`init.sh` will generate the :file:`.env` file.
However, the :file:`certbot.sh` script is not called and the nginx container needs to be manually started after performing all steps below to generate a custom CA, adding it to clients

Creation of private key and root certificate
============================================


Make a folder to hold the certificates and **make sure this folder, its subdirectories, and the files contained in it are in your gitignore file to exclude them from going public**.
However, you should backup the certificate files.

.. code-block:: console

    $ mdkir certs
    $ cd certs


Generate a private key and set a passphrase during the procedure:

.. code-block:: console

    $ openssl genrsa -des3 -out exampleCA.key 2048


Now generate the root certificate:

.. code-block:: console

    $ openssl req -x509 -new -nodes -key exampleCA.key -sha256 -days 1825 -out exampleCA.pem


Adding the Root Certificate to Linux (all clients)
========================================================================================

If it is not already installed, install the *ca-certificates* package with 

.. code-block:: console

    $ sudo apt-get install -y ca-certificates


Copy the `exampleCA.pem` file to the `/usr/local/share/ca-certificates` directory as a `exampleCA.crt` file. 

.. code-block:: console

    $ sudo cp ./exampleCA.pem /usr/local/share/ca-certificates/exampleCA.crt


Finally, update the certificate store. 

.. code-block:: console
    
    $ sudo update-ca-certificates


You can test that the certificate has been installed by running the following command:

.. code-block:: console

    $ awk -v cmd='openssl x509 -noout -subject' '/BEGIN/{close(cmd)};{print | cmd}' < /etc/ssl/certs/ca-certificates.crt | grep 

and appending one of the information provided during the root certificate creation process as grep input.


Creating CA-Signed Certificates for Your Dev Sites
========================================================================================


Now we are a CA on all our devices and we can sign certificates for any new dev sites that need HTTPS. 
First, we create a private key for the dev site. 

.. Note that we name the private key using the domain name URL of the dev site. 
.. This is not required, but it makes it easier to manage if you have multiple sites:

.. .. code-block:: bash

..     openssl genrsa -out auth.example.org.key 2048
..     openssl genrsa -out app.example.org.key 2048
..     openssl genrsa -out grafana.example.org.key 2048

.. code-block:: console

    $ openssl genrsa -out privkey.pem 2048


Then we create a CSR:

.. .. code-block:: bash

..     openssl req -new -key auth.example.org.key -out auth.example.org.csr
..     openssl req -new -key app.example.org.key -out app.example.org.csr
..     openssl req -new -key grafana.example.org.key -out grafana.example.org.csr

.. code-block:: console

    $ openssl req -new -key privkey.pem -out example.org.csr


Now create a config file for each url to define the subject alternative name (SAN)

.. code-block:: console

    $ nano example.org.ext


with the following content

.. code-block:: bash

    authorityKeyIdentifier=keyid,issuer
    basicConstraints=CA:FALSE
    keyUsage = digitalSignature, nonRepudiation, keyEncipherment, dataEncipherment
    subjectAltName = @alt_names

    [alt_names]
    DNS.1 = app.example.org
    DNS.2 = api.example.org
    DNS.3 = auth.example.org
    DNS.4 = eln.example.org
    DNS.5 = grafana.example.org
    DNS.6 = teleport.example.org



Then run

.. code-block:: console

    $ openssl x509 -req -in example.org.csr -CA exampleCA.pem -CAkey exampleCA.key \
    -CAcreateserial -out cert.pem -days 825 -sha256 -extfile example.org.ext


Complete certbot like folder and file system
============================================

.. code-block:: console

    $ cat cert.pem exampleCA.pem > fullchain.pem
    $ sudo mkdir -p /srv/docker/certbot/conf/live/example.org/
    $ sudo cp cert.pem fullchain.pem privkey.pem /srv/docker/certbot/conf/live/example.org/

.. code-block:: console

    $ openssl dhparam -out ssl-dhparams.pem 2048
    $ sudo cp ssl-dhparams.pem /srv/docker/certbot/conf/
    

Remaining settings
============================================

DNS
----

Resolving the domain names for all services can either be done by adding them to the nameserver.
Alternatively, all domain lookups can be added to a machine's host file.
Locate the host file and add the following lines (replace 127.0.0.1 with the host running the services):

.. code-block:: console

    127.0.0.1		example.org
    127.0.0.1		app.example.org
    127.0.0.1		api.example.org
    127.0.0.1		auth.example.org
    127.0.0.1		grafana.example.org
    127.0.0.1		teleport.example.org
    127.0.0.1		eln.example.org

**Windows path:** ``c:\Windows\System32\Drivers\etc\hosts``

**Linux path:** ``/etc/hosts``


Firefox settings
----------------

#. Start Firefox

#. Go to Settings > Privacy & Security

#. Under Certificates, click "View Certificates..."

#. In the Certificate Manager, click the Authorities tab

#. Click the Import button to import the created ``exampleCA.pem``

You might be prompted to set the trust level upon importing the certificate. 
If not, you can do that manually via the 'Edit Trust' button.


Grafana
^^^^^^^^

.. todo::
    
    See Grafana for details on how to make sure Grafana is working with oauth2 when using self-signed certificates.

