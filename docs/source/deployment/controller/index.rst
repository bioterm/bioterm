..    include:: <isonum.txt>


######################
Controller
######################

To build the bioterm controller docker image run while in the bioterm root directory:

.. code-block:: console

    $ sudo docker buildx build -t bioterm/controller -f bioterm/controller/Dockerfile .
