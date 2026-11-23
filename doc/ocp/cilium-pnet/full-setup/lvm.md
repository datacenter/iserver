```
[
  {
    "lvm": {
      "wipe": {},
      "operator": {},
      "cluster": {
        "chunk": "64Ki"
      }
    }
  }
]
```

!! Make sure to change mode all to include wipe
```
iserver set ocp lvm --mode all --chunk 64Ki
```

```
apiVersion: lvm.topolvm.io/v1alpha1
kind: LVMCluster
metadata:
  name: lvmcluster
  namespace: openshift-storage
spec:
  storage:
    deviceClasses:
    - default: false
      fstype: xfs
      name: vg1
      thinPoolConfig:
        chunkSize: 64Ki
        chunkSizeCalculationPolicy: Static
        metadataSizeCalculationPolicy: Host
        name: thin-pool-1
        overprovisionRatio: 10
        sizePercent: 90
```

```
# iserver get ocp lvm

OpenShift Workflow - LVM - Get Information
==========================================

OpenShift Cluster: bm3

Collecting state...


Operator
--------
- package   : openshift-marketplace/redhat-operators/lvms-operator
- csv       : lvms-operator.v4.18.4
- resources : ✓



LVMCluster
----------
- Namespace : openshift-storage
- Name      : lvmcluster
- State     : Ready
- Ready     : ✓
- Resources : ✓
- VGs       : ✓



LVM Related Resources
---------------------
- storage class : 1
- pvc           : 0
- dv            : ---
- pv            : 0
- snapshot      : 0


View: state (def), res, lvm, all
```