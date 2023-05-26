#!/bin/bash

HTTP_PROXY_ENABLED=${HTTP_PROXY_ENABLED}

cd /root
mkdir -p calico
cd calico

if [ $HTTP_PROXY_ENABLED = "True" ]; then
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-apiserver.yaml -o 01-crd-apiserver.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-installation.yaml -o 01-crd-installation.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-imageset.yaml -o 01-crd-imageset.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-tigerastatus.yaml -o 01-crd-tigerastatus.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_bgpconfigurations.yaml -o crd.projectcalico.org_bgpconfigurations.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_bgppeers.yaml -o crd.projectcalico.org_bgppeers.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_blockaffinities.yaml -o crd.projectcalico.org_blockaffinities.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_clusterinformations.yaml -o crd.projectcalico.org_clusterinformations.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_felixconfigurations.yaml -o crd.projectcalico.org_felixconfigurations.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_globalnetworkpolicies.yaml -o crd.projectcalico.org_globalnetworkpolicies.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_globalnetworksets.yaml -o crd.projectcalico.org_globalnetworksets.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_hostendpoints.yaml -o crd.projectcalico.org_hostendpoints.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ipamblocks.yaml -o crd.projectcalico.org_ipamblocks.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ipamconfigs.yaml -o crd.projectcalico.org_ipamconfigs.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ipamhandles.yaml -o crd.projectcalico.org_ipamhandles.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ippools.yaml -o crd.projectcalico.org_ippools.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_kubecontrollersconfigurations.yaml -o crd.projectcalico.org_kubecontrollersconfigurations.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_networkpolicies.yaml -o crd.projectcalico.org_networkpolicies.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_networksets.yaml -o crd.projectcalico.org_networksets.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/00-namespace-tigera-operator.yaml -o 00-namespace-tigera-operator.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-rolebinding-tigera-operator.yaml -o 02-rolebinding-tigera-operator.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-role-tigera-operator.yaml -o 02-role-tigera-operator.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-serviceaccount-tigera-operator.yaml -o 02-serviceaccount-tigera-operator.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-configmap-calico-resources.yaml -o 02-configmap-calico-resources.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-tigera-operator.yaml -o 02-tigera-operator.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/01-cr-installation.yaml -o 01-cr-installation.yaml
    curl --proxy ${HTTP_PROXY} https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/01-cr-apiserver.yaml -o 01-cr-apiserver.yaml
else
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-apiserver.yaml -o 01-crd-apiserver.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-installation.yaml -o 01-crd-installation.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-imageset.yaml -o 01-crd-imageset.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/01-crd-tigerastatus.yaml -o 01-crd-tigerastatus.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_bgpconfigurations.yaml -o crd.projectcalico.org_bgpconfigurations.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_bgppeers.yaml -o crd.projectcalico.org_bgppeers.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_blockaffinities.yaml -o crd.projectcalico.org_blockaffinities.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_clusterinformations.yaml -o crd.projectcalico.org_clusterinformations.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_felixconfigurations.yaml -o crd.projectcalico.org_felixconfigurations.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_globalnetworkpolicies.yaml -o crd.projectcalico.org_globalnetworkpolicies.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_globalnetworksets.yaml -o crd.projectcalico.org_globalnetworksets.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_hostendpoints.yaml -o crd.projectcalico.org_hostendpoints.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ipamblocks.yaml -o crd.projectcalico.org_ipamblocks.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ipamconfigs.yaml -o crd.projectcalico.org_ipamconfigs.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ipamhandles.yaml -o crd.projectcalico.org_ipamhandles.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_ippools.yaml -o crd.projectcalico.org_ippools.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_kubecontrollersconfigurations.yaml -o crd.projectcalico.org_kubecontrollersconfigurations.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_networkpolicies.yaml -o crd.projectcalico.org_networkpolicies.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/crds/calico/kdd/crd.projectcalico.org_networksets.yaml -o crd.projectcalico.org_networksets.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/00-namespace-tigera-operator.yaml -o 00-namespace-tigera-operator.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-rolebinding-tigera-operator.yaml -o 02-rolebinding-tigera-operator.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-role-tigera-operator.yaml -o 02-role-tigera-operator.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-serviceaccount-tigera-operator.yaml -o 02-serviceaccount-tigera-operator.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-configmap-calico-resources.yaml -o 02-configmap-calico-resources.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/tigera-operator/02-tigera-operator.yaml -o 02-tigera-operator.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/01-cr-installation.yaml -o 01-cr-installation.yaml
    curl https://docs.projectcalico.org/archive/v${CALICO_VERSION}/manifests/ocp/01-cr-apiserver.yaml -o 01-cr-apiserver.yaml
fi

cd /root
cp calico/* install/manifests/
