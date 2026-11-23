# Overview

SR-IOV enables you to segment a compliant network device, recognized on the host node as a physical function (PF), into multiple virtual functions (VFs). The VF is used like any other network device. The SR-IOV device driver for the device determines how the VF is exposed in the container:
- netdevice driver: A regular kernel network device in the netns of the container
- vfio-pci driver: A character device mounted in the container

SR-IOV Network Operator is responsible for configuring the SR-IOV components in OpenShift cluster.
- initialize the SR-IOV NICs on nodes.
- provision SR-IOV device plugin on selected node.
- provision SR-IOV CNI plugin on selected nodes.
- manage configuration of SR-IOV device plugin.
- generate net-att-def CRs for SR-IOV CNI plugin.
- create node specific SriovNetworkNodeState custom resources

SR-IOV Network Operator installation in few steps:
- Goto Administrator - Operators - OperatorHub page on OCP Console UI
- Select 'SR-IOV Network Operator' provided by RedHat Inc
- Install operator
- Create SriovOperatorConfig CR

SR-IOV Network Operator adds the SriovNetworkNodePolicy CR. It is used to configure an SR-IOV network device on cluster worker node.

### iserver features

'iserver set ocp sriov' command used to install SR-IOV Network Operator and create SriovNetworkNodePolicy CRD.

```
# iserver set ocp sriov --help

Options:
  --cluster TEXT    Cluster Name
  --namespace TEXT  Operator namespace
  --name TEXT       Operator name
  --channel TEXT    Operator channel
  --policy TEXT     Policy filename
  --intel           Enable SR-IOV on all Intel NICs
  --vfio            Enable vfio vf
  --netdevice       Enable netdevice vf
  --help            Show this message and exit.
```

In case of simple run i.e. 'iserver set ocp sriov', operator is created and configured. However SriovNetworkNodePolicy CR is not created.

Use flags (intel, vfio, netdevice) flags for default policy definitions on all-Intel-nics or define policy parameters in json file.

Workflow in all-Intel-nics mode:
- install SR-IOV network operator
- wait for install plan completion
- create SR-IOV operator configuration
- wait for deployments and daemon sets
- check network interfaces on a single node
  - Important note: nic layout must be the same on all cluster nodes
- create policy definitions for all Intel NICs following --vfio and --netdevice flags
- SriovNetworkNodePolicy CRD generation and applying
- wait for node reboot
- wait for all SRIOV resources to be ready after reboot

### Task: install with default policy on all Intel NICs

Notes:
- flags (intel, vfio, netdevice) used to trigger automatic partitioning of SR-IOV VF resources on every intel nic detected on the node for vfio and netdevice
- check output below starting with 'SRIOV Policies' to understand the policy definition structure
- define custome json file with list of policies if you don't want default behavior and use --policy [filename] option

```
# iserver set ocp sriov --cluster my-cluster --intel --vfio --netdevice
kind: Subscription
apiVersion: operators.coreos.com/v1alpha1
metadata:
  name: sriov-network-operator
  namespace: openshift-sriov-network-operator
spec:
  channel: stable
  installPlanApproval: Automatic
  name: sriov-network-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
  startingCSV: sriov-network-operator.v4.18.0-202506230505

Subsciption create api successful
Wait for install plan...
Wait for install plan install-n8v25 finished...
Install plan succeeded
Wait for deployments ready...
- openshift-sriov-network-operator/sriov-network-operator

SR-IOV Operator Configuration

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovOperatorConfig
metadata:
  name: default
  namespace: openshift-sriov-network-operator
spec:
  enableInjector: true
  enableOperatorWebhook: true
  logLevel: 2

Wait for deployments ready...
- openshift-sriov-network-operator/sriov-network-operator
Wait for deamon sets ready...
- openshift-sriov-network-operator/network-resources-injector
- openshift-sriov-network-operator/operator-webhook
- openshift-sriov-network-operator/sriov-network-config-daemon

Collecting interface details...
- ip link show
- ethtool [eno5]
- ethtool [eno6]
- ethtool [eno7]
- ethtool [eno8]
- ethtool [ens1f0]
- ethtool [ens1f1]
- ethtool [enp216s0f0]
- ethtool [eno1]
- ethtool [enp216s0f1]
- ethtool [eno2]
- ethtool [ovs-system]
- ethtool [ovn-k8s-mp0]
- ethtool [br-int]
- ethtool [br-ex]
- lspci eno5 [0000:1d:00.0]
- lspci eno6 [0000:1d:00.1]
- lspci eno7 [0000:1d:00.2]
- lspci eno8 [0000:1d:00.3]
- lspci ens1f0 [0000:5e:00.0]
- lspci ens1f1 [0000:5e:00.1]
- lspci enp216s0f0 [0000:d8:00.0]
- lspci eno1 [0000:3b:00.0]
- lspci enp216s0f1 [0000:d8:00.1]
- lspci eno2 [0000:3b:00.1]

SRIOV Policies
--------------
[
    {
        "interface": "ens1f0",
        "type": "netdevice",
        "name": "ens1f0net",
        "resource": "ens1f0net",
        "vfs": "64",
        "range": "0-31"
    },
    {
        "interface": "ens1f1",
        "type": "netdevice",
        "name": "ens1f1net",
        "resource": "ens1f1net",
        "vfs": "64",
        "range": "0-31"
    },
    {
        "interface": "enp216s0f0",
        "type": "netdevice",
        "name": "enp216s0f0net",
        "resource": "enp216s0f0net",
        "vfs": "64",
        "range": "0-31"
    },
    {
        "interface": "enp216s0f1",
        "type": "netdevice",
        "name": "enp216s0f1net",
        "resource": "enp216s0f1net",
        "vfs": "64",
        "range": "0-31"
    },
    {
        "interface": "ens1f0",
        "type": "vfio-pci",
        "name": "ens1f0dpdk",
        "resource": "ens1f0dpdk",
        "vfs": "64",
        "range": "32-63"
    },
    {
        "interface": "ens1f1",
        "type": "vfio-pci",
        "name": "ens1f1dpdk",
        "resource": "ens1f1dpdk",
        "vfs": "64",
        "range": "32-63"
    },
    {
        "interface": "enp216s0f0",
        "type": "vfio-pci",
        "name": "enp216s0f0dpdk",
        "resource": "enp216s0f0dpdk",
        "vfs": "64",
        "range": "32-63"
    },
    {
        "interface": "enp216s0f1",
        "type": "vfio-pci",
        "name": "enp216s0f1dpdk",
        "resource": "enp216s0f1dpdk",
        "vfs": "64",
        "range": "32-63"
    }
]

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f0net
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f0#0-31
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f0net

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f1net
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f1#0-31
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f1net

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: enp216s0f0net
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: false
  nicSelector:
    pfNames:
    - enp216s0f0#0-31
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: enp216s0f0net

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: enp216s0f1net
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: false
  nicSelector:
    pfNames:
    - enp216s0f1#0-31
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: enp216s0f1net

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f0dpdk
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f0#32-63
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f0dpdk

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ens1f1dpdk
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - ens1f1#32-63
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: ens1f1dpdk

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: enp216s0f0dpdk
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - enp216s0f0#32-63
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: enp216s0f0dpdk

apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: enp216s0f1dpdk
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  isRdma: false
  nicSelector:
    pfNames:
    - enp216s0f1#32-63
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 64
  resourceName: enp216s0f1dpdk

Wait for node reload due to sriov network node policy created

Max wait time reached, all cluster nodes ready

Completed tasks
- SR-IOV Operator installed
- SR-IOV Node Network Policy defined
```

Example output for single physical interface

```
$ ip link show ens1f0
6: ens1f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
    link/ether aa:aa:aa:aa:aa:aa brd ff:ff:ff:ff:ff:ff
    vf 0     link/ether b2:08:2f:50:c2:eb brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 1     link/ether a2:04:8a:c6:11:d6 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 2     link/ether 92:3e:c8:4f:f8:0c brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 3     link/ether ea:b6:fc:e1:83:53 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 4     link/ether 6e:fc:2d:50:ba:97 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 5     link/ether e2:ef:a3:09:fe:17 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 6     link/ether ae:8e:70:81:fb:c3 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 7     link/ether 32:2a:b8:6e:42:c8 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 8     link/ether 46:37:30:84:c7:7f brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 9     link/ether 32:2c:c3:1a:f6:bf brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 10     link/ether f2:63:ab:70:bf:07 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 11     link/ether a6:22:5f:b8:91:f3 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 12     link/ether 42:b1:77:f5:99:23 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 13     link/ether ca:65:c4:b1:37:04 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 14     link/ether de:de:4d:d9:59:01 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 15     link/ether d6:98:97:17:b1:c5 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 16     link/ether ae:da:76:f6:98:48 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 17     link/ether de:ed:7e:53:fb:01 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 18     link/ether d6:1c:75:c7:60:9e brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 19     link/ether ea:53:b6:73:db:08 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 20     link/ether b2:d8:7b:da:79:84 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 21     link/ether 42:a1:7d:a4:b9:94 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 22     link/ether 42:1e:6e:2d:49:f1 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 23     link/ether 7e:02:51:aa:18:e6 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 24     link/ether 16:56:d5:9b:ea:ce brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 25     link/ether 02:4d:48:77:ce:84 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 26     link/ether 2e:e0:31:b7:85:df brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 27     link/ether b6:ab:ec:78:e0:ec brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 28     link/ether fe:d2:95:d6:66:1b brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 29     link/ether 0a:fd:0c:72:b6:0a brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 30     link/ether da:6d:58:ce:80:a1 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 31     link/ether a2:b0:26:aa:e1:90 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 32     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 33     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 34     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 35     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 36     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 37     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 38     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 39     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 40     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 41     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 42     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 43     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 44     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 45     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 46     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 47     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 48     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 49     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 50     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 51     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 52     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 53     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 54     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 55     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 56     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 57     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 58     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 59     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 60     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 61     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 62     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    vf 63     link/ether 00:00:00:00:00:00 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
    altname enp94s0f0
```

[[Back]](../Operations.md)