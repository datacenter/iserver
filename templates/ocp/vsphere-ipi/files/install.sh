#!/bin/bash

HTTP_PROXY_ENABLED=${HTTP_PROXY_ENABLED}
if [ $HTTP_PROXY_ENABLED = "True" ]; then
    export HTTP_PROXY=${HTTP_PROXY}
    export HTTPS_PROXY=${HTTPS_PROXY}
    export NO_PROXY=localhost,${INTERFACE_0_IP},.${OCP_BASE_DOMAIN},${VCENTER_NAME},${VCENTER_IP},${VCENTER_CLUSTER_HOST_IPS},${OCP_API_VIP},${OCP_INGRESS_VIP},${OCP_NODES_IPS}
fi

cd /root

CNI="${CNI_TYPE}"
if [ $CNI = "Calico" ]; then
    mkdir -p install
    cp /root/config.yaml /root/install/install-config.yaml
    ./openshift-install create manifests --log-level debug --dir install
    ./calico_manifests.sh
    ./openshift-install create cluster --log-level debug --dir install

    if [ $? -eq 0 ]; then
        BGP_CONFIGURATION=/root/bgp_configuration.yaml
        if [ -f "$BGP_CONFIGURATION" ]; then
            export KUBECONFIG=/root/install/auth/kubeconfig
            calicoctl apply -f $BGP_CONFIGURATION
        fi
    fi
else
    mkdir -p install
    cp /root/config.yaml /root/install/install-config.yaml
    cd /root/
    ./openshift-install create cluster --log-level debug --dir install
fi

echo export KUBECONFIG=/root/install/auth/kubeconfig >> /root/.bashrc

if [ $HTTP_PROXY_ENABLED = "True" ]; then
    export HTTP_PROXY=${HTTP_PROXY} >> /root/.bashrc
    export HTTPS_PROXY=${HTTPS_PROXY} >> /root/.bashrc
    export NO_PROXY=localhost,${INTERFACE_0_IP},.${OCP_BASE_DOMAIN},${VCENTER_NAME},${VCENTER_IP},${VCENTER_CLUSTER_HOST_IPS},${OCP_API_VIP},${OCP_INGRESS_VIP},${OCP_NODES_IPS} >> /root/.bashrc
fi

exit 0