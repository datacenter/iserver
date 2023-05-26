# OpenShift Virtualization - Fedora Test Results

## Persistent Volume

```
# oc get pv -n default pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM              STORAGECLASS   REASON   AGE
pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784   30Gi       RWO            Delete           Bound    default/fedora02   thin                    3m


# oc get pv -n default pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784 -o yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
    pv.kubernetes.io/bound-by-controller: "yes"
    pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-16T17:07:06Z"
  finalizers:
  - kubernetes.io/pv-protection
  name: pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784
  resourceVersion: "23899720"
  uid: 73ca8d2b-49b9-4f57-965f-152de661f1d7
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 30Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: fedora02
    namespace: default
    resourceVersion: "23899638"
    uid: 985a0434-b4ea-4d08-ab1a-85711c9fd784
  persistentVolumeReclaimPolicy: Delete
  storageClassName: thin
  volumeMode: Filesystem
  vsphereVolume:
    fsType: ext4
    volumePath: '[EU-SPDC-k8s-Datastore-WNAS] kubevols/kubevirt-nn4bm-dynamic-pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784.vmdk'
status:
  phase: Bound
```
