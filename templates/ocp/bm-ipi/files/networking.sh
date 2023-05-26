#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

is_baremetal=`nmcli con show | grep baremetal | wc -l`
if [ $is_baremetal -eq 0 ]; then
    echo Networking configuration required
    nmcli con show
    ip a
else
    echo Networking configuration already completed
    nmcli con show
    ip a
    exit 0
fi

export PUB_CONN=${INTERFACE_0_NAME}

sudo nohup bash -c "
    nmcli con down \"$PUB_CONN\"
    nmcli con delete \"$PUB_CONN\"
    nmcli con down \"System $PUB_CONN\"
    nmcli con delete \"System $PUB_CONN\"
    nmcli connection add ifname baremetal type bridge con-name baremetal
    nmcli con add type bridge-slave ifname \"$PUB_CONN\" master baremetal
    nmcli con mod baremetal ipv4.addresses ${INTERFACE_0_IP}/${INTERFACE_0_PREFIX}
    nmcli con mod baremetal ipv4.gateway ${INTERFACE_0_GATEWAY}
    nmcli con mod baremetal ipv4.dns "${DNS_NAMESERVER}"
    nmcli con mod baremetal ipv4.method manual
"

nmcli con show

exit 0