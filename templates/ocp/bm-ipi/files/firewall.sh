#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

systemctl start firewalld
exit_on_error $?

firewall-cmd --zone=public --add-service=http --permanent
exit_on_error $?

# RHCOS image cache

firewall-cmd --add-port=8080/tcp --zone=public --permanent
exit_on_error $?

# Local registry

firewall-cmd --add-port=5000/tcp --zone=libvirt --permanent
exit_on_error $?

firewall-cmd --add-port=5000/tcp --zone=public   --permanent
exit_on_error $?

firewall-cmd --reload
exit_on_error $?

exit 0