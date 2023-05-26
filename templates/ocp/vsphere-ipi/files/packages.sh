#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

HTTP_PROXY_ENABLED=${HTTP_PROXY_ENABLED}
if [ $HTTP_PROXY_ENABLED = "True" ]; then
    export http_proxy=${HTTP_PROXY}
    export https_proxy=${HTTPS_PROXY}
fi

yum update -y
exit_on_error $?

yum install -y unzip
exit_on_error $?

yum install -y dos2unix
exit_on_error $?

yum install -y net-tools
exit_on_error $?

MANAGED_DHCP_ENABLED=${MANAGED_DHCP_ENABLED}
if [ $MANAGED_DHCP_ENABLED = "True" ]; then
    yum install -y dhcp-server
    exit_on_error $?
fi

MANAGED_DNS_ENABLED=${MANAGED_DNS_ENABLED}
if [ $MANAGED_DNS_ENABLED = "True" ]; then
    yum install -y bind bind-utils
    exit_on_error $?
fi

yum install -y tcpdump
exit_on_error $?

yum install -y helm
exit_on_error $?

yum install -y wget
exit_on_error $?

yum install -y qemu-img
exit_on_error $?

yum install -y genisoimage
exit_on_error $?

yum install -y net-snmp
exit_on_error $?

yum install -y net-snmp-utils
exit_on_error $?

exit 0