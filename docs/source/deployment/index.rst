..    include:: <isonum.txt>
.. Deployment:

##########
Deployment
##########

.. toctree::
   :maxdepth: 2
   :hidden:

   network
   server/index
   controller/index

************
Server setup
************


Prerequisits
============

Successfully tested with the following operating systems:

* Ubuntu 22.04 LTS amd64
* Ubuntu 22.04 LTS aarch64


Server installation
===================

Autoinstall
-----------

Install virt-manager:

.. code-block:: console

   $ sudo apt install virt-manager
   $ sudo usermod -aG libvirt $USER


.. code-block:: console

   $ sudo apt install genisoimage mtools

Download and copy Ubuntu-22.04.2-live-server-amd64.iso to :file:`/var/lib/libvirt/images/` (the default location for qemu)

.. todo::

   Check with other iso files for ubuntu server (arm64 etc.)

.. Open :file:`bioterm/deployment/autoinstall`

Run

.. code-block:: console

   $ make all-temp

Open virt-manager, select the image and check ''Customize configuration before install''.
Then, click :menuselection:`Add Hardware` |rarr| Storage |rarr| :menuselection:`Select or create custom storage` |rarr| :menuselection:`Manage` |rarr| `+`-Button (bottom left).
Set name to *testseed* and Target Path to */tmp/testseed* |rarr| Finish.
Select **test-seed-cd.iso** and confirm by clicking :menuselection:`Choose volume`.
Finish & :menuselection:`Begin Installation`.

.. # Cloud Init for Local Server install

.. ## Cloud init source for installer

.. Most practical for us: Use a USB stick or ISO image with our cloud init data

.. - Supported: vfat or iso9660
.. - Volume label must be `CIDATA`s

.. See: https://cloudinit.readthedocs.io/en/latest/reference/datasources/nocloud.html
