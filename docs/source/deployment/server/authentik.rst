..    include:: <isonum.txt>
.. _Authentik Setup:

######################
Authentik Setup
######################

Perform the steps described below in the :file:`/bioterm/bioterm/server/auth/` directory.

**********************
Preparation
**********************

First, you need to generate a password and a secret key using pwgen, and store both in an :file:`.env` file:

.. code-block:: console

    $ sudo apt-get install -y pwgen
    $ echo "PG_PASS=$(pwgen -s 40 1)" >> .env
    $ echo "AUTHENTIK_SECRET_KEY=$(pwgen -s 50 1)" >> .env

To configure email credentials, append this block to your .env file:

.. code-block:: bash

    # SMTP Host Emails are sent to
    AUTHENTIK_EMAIL__HOST=localhost
    AUTHENTIK_EMAIL__PORT=25
    # Optionally authenticate (don't add quotation marks to your password)
    AUTHENTIK_EMAIL__USERNAME=
    AUTHENTIK_EMAIL__PASSWORD=
    # Use StartTLS
    AUTHENTIK_EMAIL__USE_TLS=false
    # Use SSL
    AUTHENTIK_EMAIL__USE_SSL=false
    AUTHENTIK_EMAIL__TIMEOUT=10
    # Email address authentik will send from, should have a correct @domain
    AUTHENTIK_EMAIL__FROM=authentik@localhost

***********
Startup
***********

.. code-block:: console

    $ docker compose pull
    $ docker compose up -d

**********************
Create Admin Account
**********************

Navigate to ``${AUTH_PUBLIC_DOMAIN}/if/flow/initial-setup/`` (previously defined during the proxy setup, e.g., ``auth.example.org/if/flow/initial-setup/``).
Create an administrator account (the authenik default account *akadmin*), ideally using a dedicated email address so your personal email remains available for a user account.

Next, enable 2FA (especially when setting up a production deployment) by navigating to the account settings |rarr| MFA Devices and enroll the recommended **TOTP Authenticator Setup Stage** by scanning the displayed QRcode with your preferred authentication app on your mobile phone.

********************************************
Export authentik Self-signed Certificate
********************************************

Open the :menuselection:`Admin interface` and navigate to :menuselection:`System` |rarr| :menuselection:`Certificates`.
Download both the certificate and private key of the authentik Self-signed Certificate, and store them in a secure location.
These files are required to set up the SAML authentication.  

.. *********************************
.. Import Certificates
.. *********************************

.. Open the :menuselection:`Admin interface` and navigate to :menuselection:`Dashboards` |rarr| :menuselection:`System Tasks` and run the ``certificate_discovery`` task.
.. Check if any certificates have been imported.

.. .. todo::

..     This section might be obsolete, but we'll keep it in for now.

******************************************
Create Providers and Applications
******************************************

Open the :menuselection:`Admin interface` and navigate to :menuselection:`Applications` |rarr| :menuselection:`Providers` to create providers with the settings specified below. 
Applications are created and configured in :menuselection:`Applications` |rarr| :menuselection:`Applications`.

OAuth2
============

Grafana
--------------

Provider settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Name
     - ``grafana``
   * - Authorization flow
     - *default-provider-authorization-explicit-consent*
   * - Client type
     - *Confidential*
   * - Client ID
     - *auto generated*
   * - Client secret
     - *auto generated*
   * - Redirect URIs/Origins (RegEx)
     - ``https://${GRAFANA_PUBLIC_DOMAIN}/login/generic_oauth``

**Advanced protocol setting**

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Access code validity
     - ``minutes=1``
   * - Access Token validity
     - ``minutes=5``
   * - Refresh Token validity
     - ``days=30``
   * - Scopes
     - ``email, openid, profile``
   * - Subject mode
     - **Based on the User's hashed ID**
   * - Issuer mode
     - **Each provider has a different issuer, based on the application slug**


Application settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Name
     - ``grafana``
   * - Slug
     - ``grafana``
   * - Group
     - 
   * - Provider
     - ``grafana``
   * - Policy engine mode
     - *all*

Backend (API)
--------------

Provider settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Name
     - ``backend``
   * - Authorization flow
     - *default-provider-authorization-explicit-consent*
   * - Client type
     - *Public*
   * - Client ID
     - *auto generated*
   * - Redirect URIs/Origins (RegEx)
     - | ``https://${API_PUBLIC_DOMAIN}/docs/oauth2-redirect``
       | ``https://${APP_PUBLIC_DOMAIN}/callback.html``
   * - Signing Key
     - *authentik Self-signed Certificate*

**Advanced protocol setting**

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Access code validity
     - ``minutes=1``
   * - Access Token validity
     - ``minutes=5``
   * - Refresh Token validity
     - ``days=30``
   * - Scopes
     - ``email, openid, profile``
   * - Subject mode
     - **Based on the User's hashed ID**
   * - Issuer mode
     - **Each provider has a different issuer, based on the application slug**


Application settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Name
     - ``backend``
   * - Slug
     - ``backend``
   * - Group
     - 
   * - Provider
     - ``backend``
   * - Policy engine mode
     - *all*


SAML
============

ELN
--------------

Provider settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Name
     - ``eln``
   * - Authorization flow
     - *default-provider-authorization-explicit-consent*
   * - ACS URL
     - ``https://${ELN_PUBLIC_DOMAIN}/index.php?acs``
   * - Issuer
     - ``https://${AUTH_PUBLIC_DOMAIN}``
   * - Service Provider Binding
     - *Post*

**Advanced protocol setting**

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Signing Certificate
     - *authentik Self-signed Certificate*
   * - Verification Certificate
     - *---------*
   * - Property mappings
     - *select all*
   * - NameID Property Mapping
     - ``authentik default SAML Mapping: Email``
   * - Assertion valid not before
     - ``minutes=-5``
   * - Assertion valid not on or after
     - ``minutes=5``
   * - Session valid not on or after
     - ``minutes=30`` 
   * - Digest algorithm
     - *SHA256*
   * - Signature algorithm
     - *RSA-SHA256*


Application settings
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Name
     - ``eln``
   * - Slug
     - ``eln``
   * - Group
     - ``eln``
   * - Provider
     - ``eln``
   * - Policy engine mode
     - *ANY*


**UI settings**

.. list-table:: 
   :widths: 25 75
   :header-rows: 0

   * - Launch URL
     - ``https://${ELN_PUBLIC_DOMAIN}``



