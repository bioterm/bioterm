..    include:: <isonum.txt>
.. Network:

########################
Network Settings
########################


************************
Docker
************************

By default, Docker uses 172.16.0.0/16 as the IP address range.
If this leads to conflict with the LAN configuration due to overlapping IP address ranges, the default Docker IP address range can be changed.
Changing the default Docker IP address range on an Ubuntu client requires modifying the Docker daemon configuration.
Here's a step-by-step guide to do that:

#. **Stop Docker Service**: Before making changes, stop the Docker service to prevent any conflicts. Use the command:

   .. code-block:: console

      $ sudo systemctl stop docker

#. **Edit Docker Daemon Configuration**: Open the Docker daemon configuration file in a text editor (create it if it doesn't exist).

   .. code-block:: console

      $ sudo nano /etc/docker/daemon.json

   Add or modify the `bip` (bridge IP) setting to change the default subnet. For example, to change it to `10.0.0.0/16`, the configuration should look like this:

   .. code-block:: json

      {
        "bip": "10.0.0.1/16"
      }

   Save the file and exit the editor.

#. **Reload Docker System Daemon**: To apply these changes, reload the system daemon and then restart the Docker service:

   .. code-block:: console

      $ sudo systemctl daemon-reload
      $ sudo systemctl start docker

#. **Verify the Changes**: Verify the changes by inspecting the Docker network:

   .. code-block:: console

      $ sudo docker network inspect bridge

   This should show the new IP range for the default bridge network.

#. **Note on Existing Containers**:
   This change will not affect the IP addresses of already running containers.
   To apply the new IP range, you will need to recreate these containers.

************************
Controller
************************

==================================
Uncomplicated Firewall (UFW)
==================================


It is recommended to enable the Uncomplicated Firewall (UFW) on the controller, especially when setting up the controller in a network managed by others.
This applies in particular if Redis is operated without access data or SSL, in which case UFW should be used to block all incoming connections (provided that no external device [driver] requires access to Redis).

The following command will display the current status of ufw.
If ```Status: inactive``` is returned when running ```ufw status```, it means the firewall is not yet enabled on the system.


.. code-block:: console

    $ sudo ufw status verbose

To enable ufw to block all incomming connections, run:

.. code-block:: console

    $ sudo ufw enable
    $ sudo ufw reload

To enable access to Redis from an external device with a specific IP address using UFW, use the following command:

.. code-block:: console

    $ sudo ufw allow from [SPECIFIC_IP] to any port 6379
