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

status=`subscription-manager status | grep "Overall Status" | awk '{ print $3 }'`
if [ $status = "Unknown" ]; then
    echo RHEL registration required
    subscription-manager register --username=${RHEL_USERNAME} --password=${RHEL_PASSWORD} --auto-attach
    exit_on_error $?
    echo RHEL registered

    subscription-manager repos --enable=rhel-8-for-x86_64-appstream-rpms --enable=rhel-8-for-x86_64-baseos-rpms
    exit_on_error $?
    echo RHEL repos enabled
else
    echo RHEL already registered
    subscription-manager status
fi

exit 0