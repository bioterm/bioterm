..    include:: <isonum.txt>
.. _elabftw Setup:

######################
elabftw Setup
######################

The :file:`init.sh` script takes care of setting up the :file:`.env` file and starting the docker containers.
Once all containers have been started, run

.. code-block:: console

    $ sudo docker exec -it elabftw bin/console db:install

to initialize the database.
Afterwards, follow the provided URL in the terminal to register the administrator account.
Choose `Default Team` as the Team.

Continue with setting up the email in the SYSADMIN panel.

**********************
eLabFTW Configuration
**********************

In the webUI, navigate to the :menuselection:`SYSADMIN` panel and start configuring eLabFTW

SERVER
=======

.. list-table::
   :widths: 25 75
   :header-rows: 0

   * - Enable local account creation
     - *No*
   * - Admins can create local accounts
     - *No*
   * - Show local login form
     - *No*

If needed, the local login form can still be display by appending `?letmein` to the login URL.
Alternatively, in case you messed up by disabling the local login feature and can't access the sysadmin account, the local login feature can be enabled my modifying the SQL database in the mysql (default name) container.

.. code-block:: bash

    sudo elabctl mysql

.. code-block:: sql

    SELECT * FROM config WHERE conf_name='local_login';
    UPDATE config SET conf_value=1 WHERE conf_name='local_login';



SAML
=======

Service provider (this instance of eLabFTW)
--------------------------------------------

.. list-table:: General settings
   :widths: 25 75
   :header-rows: 0

   * - Toggle SAML login
     - *Enabled*
   * - Strict mode
     - *Yes*
   * - Debug mode
     - *No*

.. list-table:: Service provider
   :widths: 5 95
   :header-rows: 0

   * - Base URL
     - ``https://${ELN_PUBLIC_DOMAIN}``
   * - EntityId
     - ``https://${ELN_PUBLIC_DOMAIN}``
   * - Assertion Consumer Service binding (only POST supported)
     - *POST*
   * - Single Logout Service binding (only Redirect supported)
     - *Redirect*
   * - NameIDFormat. Default is "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
     - ``urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress``
   * - x509 Certificate in PEM format
     - *leave empty*
   * - x509 Certificate private key
     - *leave empty*
   * - Rollover x509 Certificate in PEM format (only published in metadata, not used)
     - *leave empty*


.. list-table:: Teams settings
   :widths: 5 95
   :header-rows: 0

   * - Fallback to internal id if existing user cannot be matched with email
     -
   * - If user is matched with internal id, update the email sent by IDP?
     -
   * - Synchronize the local teams with the teams sent by IDP
     -
   * - Create team sent by IDP if it doesn't exist already
     - *Yes*
   * - If no team attribute is found, to which team user is assigned?
     - *Throw error*
   * - If the user doesn't exist yet, what to do?
     - *Create the user on the fly*


.. list-table:: Security settings
   :widths: 5 95
   :header-rows: 0

   * - Encrypt the nameID of the samlp:logoutRequest sent by this SP (nameIdEncrypted)
     - No
   * - Sign the samlp:AuthnRequest messages sent (authnRequestsSigned)
     - No
   * - Sign the samlp:logoutRequest messages sent (logoutRequestSigned)
     - No
   * - Sign the samlp:logoutResponse messages sent (logoutresponsesigned)
     - No
   * - Sign the metadata (signMetadata)
     - No
   * - Require the samlp:Response to be signed (wantMessagesSigned)
     - No
   * - Require the saml:Assertion to be encrypted (wantAssertionsEncrypted)
     - No
   * - Require the saml:Assertion to be signed (wantAssertionsSigned)
     - No
   * - Require the NameID element on the SAMLResponse received (wantNameId)
     - Yes
   * - Require the NameID element received to be encrypted (wantNameIdEncrypted)
     - No
   * - Validate all received xmls (strict mode must be activated) (wantXMLValidation)
     - Yes
   * - SAMLResponse with an empty value as its Destination will not be rejected for this fact. (relaxDestinationValidation)
     - No
   * - ADFS compatibility on signature verification (lowercaseUrlEncoding)
     - No
   * - Allow attribute elements with name duplicated
     - No


Add new Identity Provider
--------------------------------------------

.. list-table::
   :widths: 5 95
   :header-rows: 0

   * - Friendly name
     - ``bioterm``
   * - EntityId
     - ``https://${AUTH_PUBLIC_DOMAIN}``
   * - Single Sign-On URL
     - ``https://${AUTH_PUBLIC_DOMAIN}/application/saml/eln/sso/binding/redirect/``
   * - Single Sign-On binding (only Redirect is supported)
     - *Redirect*
   * - Single Log Out URL
     - ``https://${AUTH_PUBLIC_DOMAIN}/application/saml/eln/slo/binding/redirect/``
   * - Single Log Out binding (only Redirect is supported)
     - *Redirect*
   * - x509cert
     - *Download the authentik self-signed certificate and insert it here* (see :doc:`authentik`)
   * - x509cert (additional for rollover)
     - *Download the authentik self-signed certificate and insert it here* (see :doc:`authentik`)
   * - What attribute to look for the email
     - ``http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress``

   * - What attribute to look for the firstname
     - *leave empty*
   * - What attribute to look for the lastname
     - ``http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name``
   * - What attribute to look for the team name (optional)
     - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name
   * - What attribute to look for the internal id (optional)
     - http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name
   * - Enabled
     - *Yes*
