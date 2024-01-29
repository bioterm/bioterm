..    include:: <isonum.txt>
.. _Debugging:

######################
Debugging
######################

List all docker container names and their IPs:

.. code-block:: console

    $ sudo docker ps -q | xargs -n 1 sudo docker inspect --format '{{ .Name }} {{range .NetworkSettings.Networks}} {{.IPAddress}}{{end}}' | sed 's#^/##';


List exposed ports of docker containers:

.. code-block:: console

    $ sudo docker container ls --format "table {{.ID}}\t{{.Names}}\t{{.Ports}}" -a