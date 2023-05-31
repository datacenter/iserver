#!/bin/bash

exit_on_error() {
    exit_code=$1
    if [ $exit_code -ne 0 ]; then
        exit $exit_code
    fi
}

HTTP_PROXY_ENABLED=${HTTP_PROXY_ENABLED}
if [ $HTTP_PROXY_ENABLED = "True" ]; then
    export HTTP_PROXY=${HTTP_PROXY}
    export HTTPS_PROXY=${HTTPS_PROXY}
fi

yum update -y

yum install -y net-tools

exit 0