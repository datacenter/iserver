#!/bin/bash
node_name=$1
oc debug node/$node_name -- chroot /host shutdown -h 1
exit $?