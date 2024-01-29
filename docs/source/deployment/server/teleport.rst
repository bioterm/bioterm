..    include:: <isonum.txt>
.. _Teleport Setup:

######################
Teleport Setup
######################

***********
Host
***********

Docker setup
============

Navigate to :file:`bioterm/bioterm/server/teleport/` and create a :file:`.env`-file with the content

.. code-block:: bash

    TELEPORT_PUBLIC_DOMAIN="${TELEPORT_PUBLIC_DOMAIN}"

Afterwards, run the init.sh script.
This will create a :file:`docker-compose.yml` file in the local directory and write the teleport configuration to :file:`/srv/docker/teleport/teleport.yaml`.
The :file:`docker-compose.yml` is tailored to the underlying operating system of the server.
The teleport docker container will be started automatically.

To create the first user, enter the Teleport container with

.. code-block:: bash

    sudo docker compose exec -it teleport bash

In the container shell, enter

.. code-block:: bash

    tctl users add teleport-admin --roles=editor,access,auditor --logins=root,ubuntu,ec2-user

to create a user name *teleport-admin* with the roles to access nodes, edit the teleport settings, and use the auditing feature.
The output of this command will provide a URL, to create the new user.

The users specified in the logins flag (e.g., *root*, *ubuntu* and *ec2-user*) must exist on the Linux host.
Otherwise, an authentication error will be thrown when establishing a connection.

The use of two-factor authentication is enforced.
A QRcode is provided during the user setup stage in the webUI to use with an authenticator app.

Adding host to server list
====================================

To add the host running the Teleport docker container to the list of accessible servers, teleport needs to be installed manually.
On the host device, as root user, run:

.. code-block:: bash

    wget -qO- https://deb.releases.teleport.dev/teleport-pubkey.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/teleport.gpg
    echo "deb https://deb.releases.teleport.dev/ stable main" > /etc/apt/sources.list.d/teleport.list
    apt update
    apt install teleport

In the webUI, navigate to :menuselection:`Servers` |rarr| :menuselection:`ADD SERVER` and select *Ubuntu* from the list.
Using the browser, navigate to the URL stated in the *Command* section of the guided resource setup.
From there, extract the **JOIN_TOKEN** and run the following command after replacing the nodename, auth_token, and auth_servers values:

.. code-block:: bash


    cat > /etc/teleport.yaml << 'EOL'
    teleport:
       nodename: ${NODE_NAME}
       auth_token: ${JOIN_TOKEN}
       auth_servers:
       - teleport.example.org:443
       log:
           output: stderr
           severity: INFO
    auth_service:
    enabled: no
    ssh_service:
    enabled: yes
    proxy_service:
    enabled: no
    EOL

Then, create a Teleport agent systemd service unit file if not already existing;

.. code-block:: bash

    cat > /lib/systemd/system/teleport.service << 'EOL'
    [Unit]
    Description=Teleport SSH Service
    After=network.target

    [Service]
    Type=simple
    Restart=on-failure
    EnvironmentFile=-/etc/default/teleport
    ExecStart=/usr/local/bin/teleport start --pid-file=/run/teleport.pid
    ExecReload=/bin/kill -HUP $MAINPID
    PIDFile=/run/teleport.pid
    LimitNOFILE=8192

    [Install]
    WantedBy=multi-user.target
    EOL

Finally, reload the systemd unit files and start and enable Teleport to run on boot:

.. code-block:: bash

    systemctl daemon-reload
    systemctl enable teleport
    systemctl start teleport

***********
Clients
***********

Using the webUI, navigate to :menuselection:`Resources` |rarr| :menuselection:`Servers` |rarr| :menuselection:`ADD SERVER`.
Select the appropriate distro (most likely Ubuntu) and run the stated *Command* on the client.

SSH access for existing client users
====================================

Using the webUI, navigate to :menuselection:`Management` |rarr| :menuselection:`Roles` and modify the *logins* section of the **access** role:

.. code-block:: yaml

    spec:
        ...
        allow:
            ...
            logins:
            - '{{internal.logins}}' # default logins for access role
            - ${CLIENT_USER} # local user account on client
