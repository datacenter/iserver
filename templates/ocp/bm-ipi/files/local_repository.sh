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

mkdir -p /opt/registry/auth
exit_on_error $?

mkdir -p /opt/registry/certs
exit_on_error $?

mkdir -p /opt/registry/data
exit_on_error $?

OCP_RELEASE=${OCP_RELEASE}
LOCAL_REGISTRY='${HOSTNAME}:5000'
LOCAL_REPOSITORY='ocp4/openshift4'
PRODUCT_REPO='openshift-release-dev'
LOCAL_SECRET_JSON=/root/pull-secret.txt
RELEASE_NAME="ocp-release"
ARCHITECTURE=x86_64
REMOVABLE_MEDIA_PATH=/opt/registry/data

oc adm release mirror -a ${LOCAL_SECRET_JSON} --from=quay.io/${PRODUCT_REPO}/${RELEASE_NAME}:${OCP_RELEASE}-${ARCHITECTURE} --to=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY} --to-release-image=${LOCAL_REGISTRY}/${LOCAL_REPOSITORY}:${OCP_RELEASE}-${ARCHITECTURE}

exit 0