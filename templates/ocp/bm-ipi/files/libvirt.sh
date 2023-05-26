#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

usermod --append --groups libvirt kni
exit_on_error $?

systemctl enable libvirtd --now
exit_on_error $?

is_default=`virsh pool-list | grep default | wc -l`
if [ $is_default -eq 0 ]; then
    virsh pool-define-as --name default --type dir --target /var/lib/libvirt/images
    exit_on_error $?

    virsh pool-start default
    exit_on_error $?

    virsh pool-autostart default
    exit_on_error $?
else
    echo virsh pool default already defined
    virsh pool-info default
fi

exit 0