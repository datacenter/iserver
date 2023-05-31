#!/bin/bash

HTTP_PROXY_ENABLED=${HTTP_PROXY_ENABLED}
if [ $HTTP_PROXY_ENABLED = "True" ]; then
    export HTTP_PROXY=${HTTP_PROXY}
    export HTTPS_PROXY=${HTTPS_PROXY}
    export NO_PROXY=${VCENTER_NAME},${VCENTER_IP},${VCENTER_CLUSTER_HOST_IPS}
fi

cd /root/
rm -rf certs
mkdir -p certs
curl --insecure https://${VCENTER_NAME}/certs/download.zip --output certs/download.zip
cd certs
unzip -o download.zip
cp certs/lin/* /etc/pki/ca-trust/source/anchors
update-ca-trust extract
cd /root/
rm -rf certs
