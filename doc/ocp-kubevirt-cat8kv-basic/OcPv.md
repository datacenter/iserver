# OpenShift Virtualization - Cat8000v Test Results

## Persistent Volume

```
# oc get pv -n default pvc-c792205f-f1cf-4984-9616-78d61e0044b1
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM               STORAGECLASS   REASON   AGE
pvc-c792205f-f1cf-4984-9616-78d61e0044b1   16Gi       RWO            Delete           Bound    default/cat8kv-01   thick                   6m43s


# oc get pv -n default pvc-c792205f-f1cf-4984-9616-78d61e0044b1 -o yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
    pv.kubernetes.io/bound-by-controller: "yes"
    pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-28T08:37:05Z"
  finalizers:
  - kubernetes.io/pv-protection
  name: pvc-c792205f-f1cf-4984-9616-78d61e0044b1
  resourceVersion: "50305939"
  uid: 5fce5279-a892-411e-bb18-63e03245b116
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 16Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: cat8kv-01
    namespace: default
    resourceVersion: "50305930"
    uid: c792205f-f1cf-4984-9616-78d61e0044b1
  persistentVolumeReclaimPolicy: Delete
  storageClassName: thick
  volumeMode: Block
  vsphereVolume:
    volumePath: '[EU-SPDC-k8s-Datastore-WNAS] kubevols/kubevirt-nn4bm-dynamic-pvc-c792205f-f1cf-4984-9616-78d61e0044b1.vmdk'
status:
  phase: Bound


# oc get pv -n default pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                    STORAGECLASS   REASON   AGE
pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003   1Gi        RWO            Delete           Bound    default/cat8kv-01-day0   thin                    7m3s


# oc get pv -n default pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003 -o yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
    pv.kubernetes.io/bound-by-controller: "yes"
    pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-28T08:36:48Z"
  finalizers:
  - kubernetes.io/pv-protection
  name: pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003
  resourceVersion: "50305356"
  uid: 7f519b32-f4c8-483b-81be-bda76e9e1ae1
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 1Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: cat8kv-01-day0
    namespace: default
    resourceVersion: "50305338"
    uid: 0f2aefe8-7a56-406a-9c73-e087fdb21003
  persistentVolumeReclaimPolicy: Delete
  storageClassName: thin
  volumeMode: Block
  vsphereVolume:
    volumePath: '[EU-SPDC-k8s-Datastore-WNAS] kubevols/kubevirt-nn4bm-dynamic-pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003.vmdk'
status:
  phase: Bound
```
