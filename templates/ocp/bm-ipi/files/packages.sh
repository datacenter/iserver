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

dnf install -y libvirt
exit_on_error $?

dnf install -y qemu-kvm
exit_on_error $?

dnf install -y mkisofs
exit_on_error $?

dnf install -y python3-devel
exit_on_error $?

dnf install -y jq
exit_on_error $?

dnf install -y ipmitool
exit_on_error $?

# iocp tool

dnf install -y dos2unix
exit_on_error $?

# local registry

dnf install -y podman
exit_on_error $?

dnf install -y python3
exit_on_error $?

dnf install -y httpd
exit_on_error $?

dnf install -y httpd-tools
exit_on_error $?

exit 0