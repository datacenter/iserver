# Node Feature Discovery Operator - Create Instance

[[Back]](./README.md) [[Next]](./create_all.md) [[Prev]](./create_operator.md)

## HowTo

```
# iserver set ocp nfd --cluster bm1 --mode instance --no-confirm

# iserver set ocp nfd --mode instance
  --cluster TEXT     Cluster Name
  --filename TEXT    NodeFeatureDiscovery CRD
  --no-confirm       Confirmation mode
```

## Workflow

- create NodeFeatureDiscovery based on package default or user-provided file
- wait for node annotations

## Requirements

NFD operator must be [created](./create_operator.md)

## Expected outcome

![InstanceCreate](../images/nfd/instance_create.png)

## Example

```
# iserver set ocp nfd --cluster bm1 --mode instance --no-confirm

OpenShift Workflow - Node Feature Discovery Operator - Create Instance
======================================================================

OpenShift Cluster: bm1

Operator
- subscription          : openshift-nfd/nfd
- package               : openshift-marketplace/redhat-operators/nfd
- channel               : stable
- install plan          : openshift-nfd/install-2pqw9
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
| 1  | ocp:bm1 | nfd   | create instance | 1       | ✓       | 21           | 
+----+---------+-------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md) [[Next]](./create_all.md) [[Prev]](./create_operator.md)