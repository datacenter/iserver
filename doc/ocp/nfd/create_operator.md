# Node Feature Discovery Operator - Create Operator

## Workflow

- create openshift-nfd namespace
- create operator group
- create subscription with user controlled channel or defaultChannelName
- wait for node annotations

## Requirements

None

## Expected outcome

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

OpenShift Workflow - Node Feature Discover Operator - Create Operator
=====================================================================

OpenShift Cluster: bm1
Operator not found: nfd

Create Namespace
----------------
- name: openshift-nfd

~~~
apiVersion: v1
kind: Namespace
metadata:
  name: openshift-nfd

~~~
Namespace [openshift-nfd] created
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
- CSV [nfd.4.21.0-202603230446]
- CSV Display name [Node Feature Discovery Operator]
- CVS Version [4.21.0-202603230446]
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
Install plan: install-s5x2w
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment openshift-nfd/nfd-controller-manager ready (optional: False, allow zero replicas: False, timout: 600s)...
Subscription nfd ready


Operator
--------
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-s5x2w
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202603230446
- latest_csv            : ✓


Create NodeFeatureDiscovery
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
    configData: |-
      #    - name: "more.kernel.features"
      #      matchOn:
      #      - loadedKMod: ["example_kmod3"]
      #    - name: "more.features.by.nodename"
      #      value: customValue
      #      matchOn:
      #      - nodename: ["special-.*-node-.*"]
  operand:
    imagePullPolicy: IfNotPresent
    servicePort: 12000
  workerConfig:
    configData: |-
      core:
      #  labelWhiteList:
      #  noPublish: false
        sleepInterval: 60s
      #  sources: [all]
      #  klog:
      #    addDirHeader: false
      #    alsologtostderr: false
      #    logBacktraceAt:
      #    logtostderr: true
      #    skipHeaders: false
      #    stderrthreshold: 2
      #    v: 0
      #    vmodule:
      ##   NOTE: the following options are not dynamically run-time
      ##          configurable and require a nfd-worker restart to take effect
      ##          after being changed
      #    logDir:
      #    logFile:
      #    logFileMaxSize: 1800
      #    skipLogHeaders: false
      sources:
      #  cpu:
      #    cpuid:
      ##     NOTE: whitelist has priority over blacklist
      #      attributeBlacklist:
      #        - "BMI1"
      #        - "BMI2"
      #        - "CLMUL"
      #        - "CMOV"
      #        - "CX16"
      #        - "ERMS"
      #        - "F16C"
      #        - "HTT"
      #        - "LZCNT"
      #        - "MMX"
      #        - "MMXEXT"
      #        - "NX"
      #        - "POPCNT"
      #        - "RDRAND"
      #        - "RDSEED"
      #        - "RDTSCP"
      #        - "SGX"
      #        - "SSE"
      #        - "SSE2"
      #        - "SSE3"
      #        - "SSE4.1"
      #        - "SSE4.2"
      #        - "SSSE3"
      #      attributeWhitelist:
      #  kernel:
      #    kconfigFile: "/path/to/kconfig"
      #    configOpts:
      #      - "NO_HZ"
      #      - "X86"
      #      - "DMI"
        pci:
          deviceClassWhitelist:
            - "0200"
            - "03"
            - "12"
          deviceLabelFields:
      #      - "class"
            - "vendor"
      #      - "device"
      #      - "subsystem_vendor"
      #      - "subsystem_device"
      #  usb:
      #    deviceClassWhitelist:
      #      - "0e"
      #      - "ef"
      #      - "fe"
      #      - "ff"
      #    deviceLabelFields:
      #      - "class"
      #      - "vendor"
      #      - "device"
      #  custom:
      #    - name: "my.kernel.feature"
      #      matchOn:
      #        - loadedKMod: ["example_kmod1", "example_kmod2"]
      #    - name: "my.pci.feature"
      #      matchOn:
      #        - pciId:
      #            class: ["0200"]
      #            vendor: ["15b3"]
      #            device: ["1014", "1017"]
      #        - pciId :
      #            vendor: ["8086"]
      #            device: ["1000", "1100"]
      #    - name: "my.usb.feature"
      #      matchOn:
      #        - usbId:
      #          class: ["ff"]
      #          vendor: ["03e7"]
      #          device: ["2485"]
      #        - usbId:
      #          class: ["fe"]
      #          vendor: ["1a6e"]
      #          device: ["089a"]
      #    - name: "my.combined.feature"
      #      matchOn:
      #        - pciId:
      #            vendor: ["15b3"]
      #            device: ["1014", "1017"]
      #          loadedKMod : ["vendor_kmod1", "vendor_kmod2"]

~~~
NodeFeatureDiscovery [openshift-nfd/nfd-instance] created
- wait for NodeFeatureDiscovery openshift-nfd/nfd-instance [timeout:60s]
Wait for deployment openshift-nfd/nfd-controller-manager ready (optional: False, allow zero replicas: False, timout: 600s)...
Wait for deployment openshift-nfd/nfd-master ready (optional: False, allow zero replicas: False, timout: 600s)...
Wait for daemonset ready (optional: False, timout: 600s)...
Subscription nfd ready
Wait for annotations on all worker nodes
Node [bm1-1] annotations found
Node [bm1-2] annotations found
Node [bm1-3] annotations found

Completed tasks
- Namespace created
- Operator Group created
- NFD Operator installed and configured
- NFD annotations found on the nodes
```

[[Back]](./README.md)