# Node Feature Discovery Operator - Create All

[[Back]](./README.md) [[Next]](./create_task.md) [[Prev]](./create_instance.md)

## HowTo

```
# iserver set ocp nfd --cluster bm1 --mode all --no-confirm

# iserver set ocp nfd --mode all
  --cluster TEXT     Cluster Name
  --channel TEXT     Operator channel  [default: __default__]
  --filename TEXT    NodeFeatureDiscovery CRD
  --no-confirm       Confirmation mode
```

## Workflow

- create openshift-nfd namespace
- create operator group
- create subscription with user controlled channel or defaultChannelName
- create NodeFeatureDiscovery based on package default or user-provided file
- wait for node annotations

## Requirements

None

## Expected outcome

![OperatorCreate](../images/nfd/operator_create.png)

![OperatorCreate](../images/nfd/instance_create.png)

## Example

```
# iserver set ocp nfd --cluster bm1 --mode all --no-confirm

OpenShift Workflow - Node Feature Discovery Operator - Create Operator
======================================================================

OpenShift Cluster: bm1
Subscription not found nfd

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

Create OperatorGroup
--------------------
- namespace: openshift-nfd
- name: nfd-operator-group

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
OperatorGroup [openshift-nfd/nfd-operator-group] created
- wait for OperatorGroup openshift-nfd/nfd-operator-group [timeout:60s]

Create Subscription
-------------------
Subscription: openshift-nfd/nfd
Source: openshift-marketplace/redhat-operators/nfd
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: stable
- CSV [nfd.4.21.0-202604140347]
- CSV Display name [Node Feature Discovery Operator]
- CVS Version [4.21.0-202604140347]
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
Install plan: install-tfwcl
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment openshift-nfd/nfd-controller-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...
Subscription nfd ready

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-tfwcl
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202604140347
- latest_csv            : ✓


Completed tasks
- Namespace created
- Operator Group created
- Subscription created

OpenShift Workflow - Node Feature Discovery Operator - Create Instance
======================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-tfwcl
- install plan approved : ✓
- installed csv         : nfd.4.21.0-202604140347
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
Wait for deployment openshift-nfd/nfd-controller-manager ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for deployment openshift-nfd/nfd-master ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for daemonset openshift-nfd/nfd-worker ready (optional: False, timeout: 600s)...
Subscription nfd ready
Wait for annotations on all worker nodes
Node [bm1-1] annotations found
Node [bm1-2] annotations found
Node [bm1-3] annotations found

Completed tasks
- Node feature discovery instance created
- Note annotations found

+----+---------+-------+-----------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow        | Changes | Success | Duration [s] |
+----+---------+-------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | nfd   | create operator | 3       | ✓       | 27           | 
| 2  | ocp:bm1 | nfd   | create instance | 1       | ✓       | 19           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./create_task.md) [[Prev]](./create_instance.md)