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

subscription-manager unregister

status=`subscription-manager status | grep "Overall Status" | awk '{ print $3 }'`
if [ $status = "Unknown" ]; then
    echo RHEL unregistered
else
    echo RHEL still registered
    exit 1
fi

exit 0