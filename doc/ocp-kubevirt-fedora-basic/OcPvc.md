# OpenShift Virtualization - Fedora Test Results

## Persistent Volume Claim

```
# oc get pvc -n default fedora02
NAME       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
fedora02   Bound    pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784   30Gi       RWO            thin           3m21s


# oc get pvc -n default fedora02 -o yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    cdi.kubevirt.io/storage.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE2Nzg5ODY2OTAsImlhdCI6MTY3ODk4NjM5MCwiaXNzIjoiY2RpLWFwaXNlcnZlciIsIm5hbWUiOiJmZWRvcmEtcmVnaXN0cnkiLCJuYW1lc3BhY2UiOiJkZWZhdWx0IiwibmJmIjoxNjc4OTg2MzkwLCJvcGVydGF0aW9uIjoiQ2xvbmUiLCJwYXJhbXMiOnsidGFyZ2V0TmFtZSI6ImZlZG9yYTAyIiwidGFyZ2V0TmFtZXNwYWNlIjoiZGVmYXVsdCJ9LCJyZXNvdXJjZSI6eyJncm91cCI6IiIsInJlc291cmNlIjoicGVyc2lzdGVudHZvbHVtZWNsYWltcyIsInZlcnNpb24iOiJ2MSJ9fQ.SR2lkZZ3piBno8PZ2yGw_TJn3eDf1ZLXKM8YnW1eSf2THqegDCdHgWhiwEWnvzHdFcy7OsDlSwmePzXruoXyWgCY_sdjviEUkBBBR8cBV84_4W59uhx09Mt5TZq55GORu8ZW2Ll1sAKYcVNhdaWH6dnGL68qtfujZrMV5-zsbn1yYJdamo981nti8FGOth9bJeO4_0QZ76wi8xpXKOqODECtJAwF84yvg7EJcOkNvSdQU2xJ3pz6uJNACDNnniKNb9WqaKQ9tV7tEvJMsszt5mBWGMCQDu-SxHKZC3LbxIdFNtzwYGhVzrHVSYoufzaq8_FwG1c__n0-1Z77W9QePQ
    cdi.kubevirt.io/storage.condition.running: "false"
    cdi.kubevirt.io/storage.condition.running.message: Clone Complete
    cdi.kubevirt.io/storage.condition.running.reason: Completed
    cdi.kubevirt.io/storage.condition.source.running: "true"
    cdi.kubevirt.io/storage.condition.source.running.message: Clone Complete
    cdi.kubevirt.io/storage.condition.source.running.reason: Completed
    cdi.kubevirt.io/storage.extended.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE5OTQzNDY0MDUsImlhdCI6MTY3ODk4NjQwNSwiaXNzIjoiY2RpLWRlcGxveW1lbnQiLCJuYW1lIjoiZmVkb3JhLXJlZ2lzdHJ5IiwibmFtZXNwYWNlIjoiZGVmYXVsdCIsIm5iZiI6MTY3ODk4NjQwNSwib3BlcnRhdGlvbiI6IkNsb25lIiwicGFyYW1zIjp7InRhcmdldE5hbWUiOiJmZWRvcmEwMiIsInRhcmdldE5hbWVzcGFjZSI6ImRlZmF1bHQiLCJ1aWQiOiI5ODVhMDQzNC1iNGVhLTRkMDgtYWIxYS04NTcxMWM5ZmQ3ODQifSwicmVzb3VyY2UiOnsiZ3JvdXAiOiIiLCJyZXNvdXJjZSI6InBlcnNpc3RlbnR2b2x1bWVjbGFpbXMiLCJ2ZXJzaW9uIjoidjEifX0.cuBjgULPOZ-XHCLD9bDT_p22zfE8hsuFoSS8FunN8gy1WRuEN5EeDSf8LfMxl4fGrbIbp1HCITH-FVxdoUZNrQVwGJMWcC0TJJq9eeOP8ky3suwhGxlEUA9n4W8cWCum2qGnfBH3veoAaj0eVu56pRRBZP9Avy_ChCJ-I6aJBO8st9MkGMdxLzJpihlI3cOIfwwTay2HkHgwwiq5Su07AQWgUdHAVLUWE9beTFALxc2WnstXAu2tRGcUelLftKdxz0Wsu2iZc7zOY0pYlUTMVBr8KyPh4GfKwAzyOr30ZpleNaR2dvbC8ItX3dKcp6GwO6mUVFwgiMiAqD1YTN25Cg
    cdi.kubevirt.io/storage.pod.phase: Succeeded
    cdi.kubevirt.io/storage.pod.ready: "false"
    cdi.kubevirt.io/storage.pod.restarts: "0"
    cdi.kubevirt.io/storage.preallocation.requested: "false"
    cdi.kubevirt.io/storage.sourceClonePodName: 985a0434-b4ea-4d08-ab1a-85711c9fd784-source-pod
    cdi.kubevirt.io/storage.uploadPodName: cdi-upload-fedora02
    cdi.kubevirt.io/uploadClientName: default/fedora-registry-default/fedora02
    k8s.io/CloneOf: "true"
    k8s.io/CloneRequest: default/fedora-registry
    pv.kubernetes.io/bind-completed: "yes"
    pv.kubernetes.io/bound-by-controller: "yes"
    volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
    volume.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-16T17:06:45Z"
  finalizers:
  - kubernetes.io/pvc-protection
  labels:
    alerts.k8s.io/KubePersistentVolumeFillingUp: disabled
    app: containerized-data-importer
    app.kubernetes.io/component: storage
    app.kubernetes.io/managed-by: cdi-controller
    app.kubernetes.io/part-of: hyperconverged-cluster
    app.kubernetes.io/version: 4.11.3
  name: fedora02
  namespace: default
  ownerReferences:
  - apiVersion: cdi.kubevirt.io/v1beta1
    blockOwnerDeletion: true
    controller: true
    kind: DataVolume
    name: fedora02
    uid: e34991e0-443b-4270-9fdd-f074c4f16b78
  resourceVersion: "23904196"
  uid: 985a0434-b4ea-4d08-ab1a-85711c9fd784
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 30Gi
  storageClassName: thin
  volumeMode: Filesystem
  volumeName: pvc-985a0434-b4ea-4d08-ab1a-85711c9fd784
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 30Gi
  phase: Bound
```
