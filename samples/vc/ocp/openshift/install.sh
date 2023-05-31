#!/bin/bash

HTTP_PROXY_ENABLED=${HTTP_PROXY_ENABLED}
if [ $HTTP_PROXY_ENABLED = "True" ]; then
    export HTTP_PROXY=${HTTP_PROXY}
    export HTTPS_PROXY=${HTTPS_PROXY}
    export NO_PROXY=localhost,${INTERFACE_0_IP},.${OCP_BASE_DOMAIN},${VCENTER_NAME},${VCENTER_IP},${VCENTER_CLUSTER_HOST_IPS},${OCP_API_VIP},${OCP_INGRESS_VIP},${OCP_NODES_IPS}
fi

cd /root
rm -rf install
mkdir -p install
cp /root/config.yaml /root/install/install-config.yaml
cd /root/
./openshift-install create cluster --log-level debug --dir install
