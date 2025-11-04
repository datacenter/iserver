# Node Feature Discovery Operator - Create Operator

## Workflow

- create openshift-nfd namespace
- create operator group
- create subscription with user controlled channel or defaultChannelName
- wait for node annotations

## Requirements

None

## Expected Outcome

![OperatorCreate](../images/nfd/operator_create.png)

![InstanceCreate](../images/nfd/instance_create.png)

## Configurable options

```
# iserver set ocp nfd --mode operator
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --filename TEXT    NodeFeatureDiscovery CRD
  --no-confirm       Confirmation mode
```

## Example

```
# iserver set ocp nfd --mode operator --cluster bm1 --no-confirm
OpenShift Cluster: bm1


OpenShift Workflow - Node Feature Discover Operator - Create Operator
=====================================================================

Workflow Parameters
-------------------
{
    "cluster": "bm1",
    "channel": "__default__",
    "instance": null,
    "confirmation": false,
    "check-verbose": true,
    "namespace": "openshift-nfd",
    "name": "nfd",
    "operator-group-name": "nfd-operator-group",
    "delete-namespace": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:local]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


Create Namespace
----------------
- name: openshift-nfd

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nfd

~~~

Namespace created

Wait for namespace [timeout:60]...

Create Operator Group
---------------------
Operator group: openshift-nfd/nfd-operator-group

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: nfd-operator-group
  namespace: openshift-nfd
spec:
  targetNamespaces:
  - openshift-nfd
  upgradeStrategy: Default

~~~

Operator group created

Wait for operator group [timeout:60]...

Create Subscription
-------------------
Subscription: openshift-nfd/nfd
Source: openshift-marketplace/redhat-operators/nfd
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [nfd.4.18.0-202509240837]
- CSV Display name [Node Feature Discovery Operator]
- CVS Version [4.18.0-202509240837]
- CSV Provider [{'name': 'Red Hat', 'url': 'https://github.com/openshift/cluster-nfd-operator'}]
- CSV Maturity [stable]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: nfd
  namespace: openshift-nfd
spec:
  channel: stable
  installPlanApproval: Automatic
  name: nfd
  source: redhat-operators
  sourceNamespace: openshift-marketplace

~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-5l8kt
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-nfd/nfd-controller-manager

Create NFD Default Instance
---------------------------
- namespace: openshift-nfd
- name: nfd-instance

~~~
apiVersion: nfd.openshift.io/v1
kind: NodeFeatureDiscovery
metadata:
  name: nfd-instance
  namespace: openshift-nfd
spec:
  customConfig:
    configData: '#    - name: "more.kernel.features"

      #      matchOn:

      #      - loadedKMod: ["example_kmod3"]

      #    - name: "more.features.by.nodename"

      #      value: customValue

      #      matchOn:

      #      - nodename: ["special-.*-node-.*"]

      '
  operand:
    imagePullPolicy: IfNotPresent
    servicePort: 12000
  workerConfig:
    configData: "core:\n#  labelWhiteList:\n#  noPublish: false\n  sleepInterval:\
      \ 60s\n#  sources: [all]\n#  klog:\n#    addDirHeader: false\n#    alsologtostderr:\
      \ false\n#    logBacktraceAt:\n#    logtostderr: true\n#    skipHeaders: false\n\
      #    stderrthreshold: 2\n#    v: 0\n#    vmodule:\n##   NOTE: the following\
      \ options are not dynamically run-time \n##          configurable and require\
      \ a nfd-worker restart to take effect\n##          after being changed\n#  \
      \  logDir:\n#    logFile:\n#    logFileMaxSize: 1800\n#    skipLogHeaders: false\n\
      sources:\n#  cpu:\n#    cpuid:\n##     NOTE: whitelist has priority over blacklist\n\
      #      attributeBlacklist:\n#        - \"BMI1\"\n#        - \"BMI2\"\n#    \
      \    - \"CLMUL\"\n#        - \"CMOV\"\n#        - \"CX16\"\n#        - \"ERMS\"\
      \n#        - \"F16C\"\n#        - \"HTT\"\n#        - \"LZCNT\"\n#        -\
      \ \"MMX\"\n#        - \"MMXEXT\"\n#        - \"NX\"\n#        - \"POPCNT\"\n\
      #        - \"RDRAND\"\n#        - \"RDSEED\"\n#        - \"RDTSCP\"\n#     \
      \   - \"SGX\"\n#        - \"SSE\"\n#        - \"SSE2\"\n#        - \"SSE3\"\n\
      #        - \"SSE4.1\"\n#        - \"SSE4.2\"\n#        - \"SSSE3\"\n#      attributeWhitelist:\n\
      #  kernel:\n#    kconfigFile: \"/path/to/kconfig\"\n#    configOpts:\n#    \
      \  - \"NO_HZ\"\n#      - \"X86\"\n#      - \"DMI\"\n  pci:\n    deviceClassWhitelist:\n\
      \      - \"0200\"\n      - \"03\"\n      - \"12\"\n    deviceLabelFields:\n\
      #      - \"class\"\n      - \"vendor\"\n#      - \"device\"\n#      - \"subsystem_vendor\"\
      \n#      - \"subsystem_device\"\n#  usb:\n#    deviceClassWhitelist:\n#    \
      \  - \"0e\"\n#      - \"ef\"\n#      - \"fe\"\n#      - \"ff\"\n#    deviceLabelFields:\n\
      #      - \"class\"\n#      - \"vendor\"\n#      - \"device\"\n#  custom:\n#\
      \    - name: \"my.kernel.feature\"\n#      matchOn:\n#        - loadedKMod:\
      \ [\"example_kmod1\", \"example_kmod2\"]\n#    - name: \"my.pci.feature\"\n\
      #      matchOn:\n#        - pciId:\n#            class: [\"0200\"]\n#      \
      \      vendor: [\"15b3\"]\n#            device: [\"1014\", \"1017\"]\n#    \
      \    - pciId :\n#            vendor: [\"8086\"]\n#            device: [\"1000\"\
      , \"1100\"]\n#    - name: \"my.usb.feature\"\n#      matchOn:\n#        - usbId:\n\
      #          class: [\"ff\"]\n#          vendor: [\"03e7\"]\n#          device:\
      \ [\"2485\"]\n#        - usbId:\n#          class: [\"fe\"]\n#          vendor:\
      \ [\"1a6e\"]\n#          device: [\"089a\"]\n#    - name: \"my.combined.feature\"\
      \n#      matchOn:\n#        - pciId:\n#            vendor: [\"15b3\"]\n#   \
      \         device: [\"1014\", \"1017\"]\n#          loadedKMod : [\"vendor_kmod1\"\
      , \"vendor_kmod2\"]\n"

~~~

NFD instance created

Wait for nfd instance [timeout:60]...
Wait for nfd instance resources...
Wait for deployments ready (optional: True, allow zero replicas: False)...
- openshift-nfd/nfd-controller-manager
- openshift-nfd/nfd-master
Wait for deamon sets ready...
- openshift-nfd/nfd-worker
Wait for annotations on all worker nodes
Node [ocp-bm1] annotations found

Completed tasks
- Namespace created
- Operator Group created
- NFD Operator installed and configured
- NFD annotations found on the nodes
```

[[Back]](./README.md)