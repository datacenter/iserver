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

export VERSION=stable-${OCP_VERSION}
exit_on_error $?

export RELEASE_ARCH=x86_64
exit_on_error $?

export RELEASE_IMAGE=$(curl -s https://mirror.openshift.com/pub/openshift-v4/$RELEASE_ARCH/clients/ocp/$VERSION/release.txt | grep 'Pull From: quay.io' | awk -F ' ' '{print $3}')
exit_on_error $?

export cmd=openshift-baremetal-install
exit_on_error $?

export pullsecret_file=/root/pull-secret.txt
exit_on_error $?

export extract_dir=$(pwd)
exit_on_error $?

curl -s https://mirror.openshift.com/pub/openshift-v4/clients/ocp/${OCP_RELEASE}/openshift-client-linux.tar.gz | tar zxvf - oc
exit_on_error $?

cp oc /usr/local/bin
exit_on_error $?

oc adm release extract --registry-config "${pullsecret_file}" --command=$cmd --to "${extract_dir}" ${RELEASE_IMAGE}
exit_on_error $?

sudo cp openshift-baremetal-install /usr/local/bin
exit_on_error $?

exit 0