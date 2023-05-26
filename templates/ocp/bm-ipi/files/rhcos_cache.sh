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

if [ -d /opt/rhcos_image_cache ]; then
    echo "RHCOS image cache already created"
    exit 0
fi

# Create a directory to store the bootstraposimage
mkdir -p /opt/rhcos_image_cache
exit_on_error $?

# Set the appropriate SELinux context for the newly created directory
semanage fcontext -a -t httpd_sys_content_t "/opt/rhcos_image_cache(/.*)?"
restorecon -Rv /opt/rhcos_image_cache/
exit_on_error $?

# Get the URI for the RHCOS image that the installation program will deploy on the bootstrap VM
#
# Example
# https://rhcos.mirror.openshift.com/art/storage/releases/rhcos-4.11/411.86.202208112011-0/x86_64/rhcos-411.86.202208112011-0-qemu.x86_64.qcow2.gz
#
export RHCOS_QEMU_URI=$(/usr/local/bin/openshift-baremetal-install coreos print-stream-json | jq -r --arg ARCH "$(arch)" '.architectures[$ARCH].artifacts.qemu.formats["qcow2.gz"].disk.location')
exit_on_error $?
echo $RHCOS_QEMU_URI

# Get the name of the image that the installation program will deploy on the bootstrap VM
#
# Example:
# rhcos-411.86.202208112011-0-qemu.x86_64.qcow2.gz
export RHCOS_QEMU_NAME=${RHCOS_QEMU_URI##*/}
exit_on_error $?
echo $RHCOS_QEMU_NAME

# Get the SHA hash for the RHCOS image that will be deployed on the bootstrap VM
#
# Example:
# fc24ad2060fc2ac0e15ce44b69436925aaecca4f4de2249524089d6823d9d17e
export RHCOS_QEMU_UNCOMPRESSED_SHA256=$(/usr/local/bin/openshift-baremetal-install coreos print-stream-json | jq -r --arg ARCH "$(arch)" '.architectures[$ARCH].artifacts.qemu.formats["qcow2.gz"].disk["uncompressed-sha256"]')
exit_on_error $?
echo $RHCOS_QEMU_UNCOMPRESSED_SHA256

# Download the image and place it in the /opt/rhcos_image_cache directory
curl -L ${RHCOS_QEMU_URI} -o /opt/rhcos_image_cache/${RHCOS_QEMU_NAME}
exit_on_error $?

# Confirm SELinux type is of httpd_sys_content_t for the new file
#
# Example
# unconfined_u:object_r:usr_t:s0 rhcos-411.86.202208112011-0-qemu.x86_64.qcow2.gz
ls -Z /opt/rhcos_image_cache
exit_on_error $?

# Create the pod
podman run -d --name rhcos_image_cache -v /opt/rhcos_image_cache:/var/www/html -p 8080:8080/tcp quay.io/centos7/httpd-24-centos7:latest
exit_on_error $?
podman images
podman ps

export BOOTSTRAP_OS_IMAGE="http://${INTERFACE_0_IP}:8080/${RHCOS_QEMU_NAME}?sha256=${RHCOS_QEMU_UNCOMPRESSED_SHA256}"

echo Bootstrap OS Image is ${BOOTSTRAP_OS_IMAGE}
echo ${BOOTSTRAP_OS_IMAGE} > /root/bootstrap_os_image

exit 0