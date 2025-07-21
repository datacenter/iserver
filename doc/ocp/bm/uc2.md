# OpenShift Cluster with Cilium CNI

## Intent

Main automation goals
- deploy OpenShift Cluster on single UCS server with Cilium CNI
- prepare the cli tools and .bashrc on the cluster node for day2ops

Options
- [add extra servers](./uc2_multi_node.md) for multi-node OpenShift setup
- [check data center network](./uc2_fabric_check.md) for consistency with OpenShift cluster configuration intent
- [configure data center network](./uc2_fabric_configuration.md) to prepare for OpenShift cluster installation
- define [post-installation tasks](input_data_tasks.md) e.g.,
    - HTPasswd Identity Provider
    - extra ssh keys
    - operators installation and configuration
    - CSI setup

## RunIt

- prepare input directory files with your intent
- **iserver create ocp cluster bm --dir [dir-name] --mode install --fabric patch**
- wait for the fabric-and-cluster installation to be completed

## Workflow

- verify [input files](./uc2_input.md) incl. Cilium manifests consistency checks
- [check server](./uc2_server.md) for Redfish access and operations
- network fabric checks or configuration
- [cluster installation](./uc2_logs.md) using RedHat Console API and Redfish API
    - define cluster with Cilium CNI
    - upload manifests
    - download generated ISO
    - boot server from ISO
    - wait for server calling-home to RedHat's cloud
    - initiate cluster
- [post-installation tasks](./uc2_tasks.md)

## Result

OpenShift Cluster installed as requested
- OpenShift version 4.18.9
- Cilium CNI
- single node ready
- .bashrc configured with proxy settings
- kubeconfig uploaded to cluster node
- selected day2ops binaries uploaded to cluster node

```
$ oc version
Client Version: 4.18.0-202503201434.p0.geb9bc9b.assembly.stream-eb9bc9b
Kustomize Version: v5.4.2
Server Version: 4.18.9
Kubernetes Version: v1.31.7
```

```
$ oc get node
NAME  STATUS   ROLES                         AGE   VERSION
sno   Ready    control-plane,master,worker   18h   v1.31.7
```

```
$ oc get network cluster -o yaml
apiVersion: config.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  externalIP:
    policy: {}
  networkDiagnostics:
    mode: ""
    sourcePlacement: {}
    targetPlacement: {}
  networkType: Cilium
  serviceNetwork:
  - 172.30.0.0/16
status:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: Cilium
  serviceNetwork:
  - 172.30.0.0/16
```

SNO server prepared for oc/kubectl with kubeconfig

```
$ ls .kube/
config

$ oc get node
[ready to be used]
```

Selected binaries prepared

```
$ ls /usr/local/bin/
hubble
cilium
helm
virtctl
```

[Back](../BareMetalCluster.md)