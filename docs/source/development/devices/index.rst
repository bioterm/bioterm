..    include:: <isonum.txt>

######################
Devices Development
######################

If you want to add your device as a process controlled and supervised by *systemd*, you need to place a unit configuration file in :file:`/etc/systemd/system/`.
These files have to end in ".service".
A template is located in :file:`${BIOTERM_ROOT_DIRECTORY}/bioterm/devices/template.service`, which needs to be modified, renamed, and then placed in :file:`/etc/systemd/system/`.
