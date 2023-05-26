# OpenShift Virtualization - Fedora Test Results

## Persistent Volume

```
# oc get pv -n default pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM              STORAGECLASS   REASON   AGE
pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea   30Gi       RWO            Delete           Bound    default/fedora06   thin                    116s


# oc get pv -n default pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea -o yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    kubernetes.io/createdby: vsphere-volume-dynamic-provisioner
    pv.kubernetes.io/bound-by-controller: "yes"
    pv.kubernetes.io/provisioned-by: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-16T17:10:33Z"
  finalizers:
  - kubernetes.io/pv-protection
  name: pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea
  resourceVersion: "23906053"
  uid: 30231535-8104-450e-87be-6b1a6faff895
spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 30Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: fedora06
    namespace: default
    resourceVersion: "23906047"
    uid: fbf28358-7dae-4741-aaf8-6aa4c48d7dea
  persistentVolumeReclaimPolicy: Delete
  storageClassName: thin
  volumeMode: Filesystem
  vsphereVolume:
    fsType: ext4
    volumePath: '[EU-SPDC-k8s-Datastore-WNAS] kubevols/kubevirt-nn4bm-dynamic-pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea.vmdk'
status:
  phase: Bound
```
