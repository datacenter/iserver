# OpenShift Virtualization - Fedora Test Results

## Persistent Volume Claim

```
# oc get pvc -n default fedora06
NAME       STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
fedora06   Bound    pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea   30Gi       RWO            thin           118s


# oc get pvc -n default fedora06 -o yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    cdi.kubevirt.io/storage.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE2Nzg5ODY5MzAsImlhdCI6MTY3ODk4NjYzMCwiaXNzIjoiY2RpLWFwaXNlcnZlciIsIm5hbWUiOiJmZWRvcmEtcmVnaXN0cnkiLCJuYW1lc3BhY2UiOiJkZWZhdWx0IiwibmJmIjoxNjc4OTg2NjMwLCJvcGVydGF0aW9uIjoiQ2xvbmUiLCJwYXJhbXMiOnsidGFyZ2V0TmFtZSI6ImZlZG9yYTA2IiwidGFyZ2V0TmFtZXNwYWNlIjoiZGVmYXVsdCJ9LCJyZXNvdXJjZSI6eyJncm91cCI6IiIsInJlc291cmNlIjoicGVyc2lzdGVudHZvbHVtZWNsYWltcyIsInZlcnNpb24iOiJ2MSJ9fQ.GCiWKbiNQP-COp8a8zMOIjhGIttFOHrLK6oWNbSEyxkkftqKG8mX1c2nHhCMV2OHIeZXvi0Bz1p4bYFdgqDk_c5g12aQZvyKApBXGtFtcY47oTMC9s2CUc_2bA4o3I0oFyYrEJkXvkTCVN197FG_rYElUxr1158nbUUxMyD_WYHZxF21uD4r7pzQ8qp0YZGdukZBVdAHIbd-PIzIIc87kDXsdiughUd4CyKbT2vKPeCsFnAy4IYes8lVDk0b3o8RSm3Yg2nSE4KkC8fd_Qf_OjlanhrYej909k1r_jBDv7JPUDqp2la7V5b48oJGBGh11TIvQORsfjD1O2wUEAP7RA
    cdi.kubevirt.io/storage.condition.running: "false"
    cdi.kubevirt.io/storage.condition.running.message: Clone Complete
    cdi.kubevirt.io/storage.condition.running.reason: Completed
    cdi.kubevirt.io/storage.condition.source.running: "true"
    cdi.kubevirt.io/storage.condition.source.running.message: Clone Complete
    cdi.kubevirt.io/storage.condition.source.running.reason: Completed
    cdi.kubevirt.io/storage.extended.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE5OTQzNDY2MzAsImlhdCI6MTY3ODk4NjYzMCwiaXNzIjoiY2RpLWRlcGxveW1lbnQiLCJuYW1lIjoiZmVkb3JhLXJlZ2lzdHJ5IiwibmFtZXNwYWNlIjoiZGVmYXVsdCIsIm5iZiI6MTY3ODk4NjYzMCwib3BlcnRhdGlvbiI6IkNsb25lIiwicGFyYW1zIjp7InRhcmdldE5hbWUiOiJmZWRvcmEwNiIsInRhcmdldE5hbWVzcGFjZSI6ImRlZmF1bHQiLCJ1aWQiOiJmYmYyODM1OC03ZGFlLTQ3NDEtYWFmOC02YWE0YzQ4ZDdkZWEifSwicmVzb3VyY2UiOnsiZ3JvdXAiOiIiLCJyZXNvdXJjZSI6InBlcnNpc3RlbnR2b2x1bWVjbGFpbXMiLCJ2ZXJzaW9uIjoidjEifX0.zcN6CwOcAqKKmbmQTg0_RadC8aB_JMQW-wVHooEt2lUneK9XkUyT5P2MfVbXLqx35Lgf5_y1zf-JWERRN93BsYLxT1oy0C_i47LRxwQg7XVXdlcaJ7MZJqT9U-w06fcL6_icJeQD8BRrJC8i8xB7ocopiqIGzomzxtFQrcmQ7GP7uNNb7hGG56Zc89yIrzR2ftXvDahtPnif7pQeCU_hzWUp41bV1HdMZo9MXGWAKc9MyEjYrvKJ7nsjFsrZaqT-M_GitVhK3WPv5Oq8FfKCnCrAEvb5IgIfuAcvidjXeeOHyowapYSWqHzgqVGDy-azsNeVi9qMJ7AuywHSlaK1vA
    cdi.kubevirt.io/storage.pod.phase: Succeeded
    cdi.kubevirt.io/storage.pod.ready: "false"
    cdi.kubevirt.io/storage.pod.restarts: "0"
    cdi.kubevirt.io/storage.preallocation.requested: "false"
    cdi.kubevirt.io/storage.sourceClonePodName: fbf28358-7dae-4741-aaf8-6aa4c48d7dea-source-pod
    cdi.kubevirt.io/storage.uploadPodName: cdi-upload-fedora06
    cdi.kubevirt.io/uploadClientName: default/fedora-registry-default/fedora06
    k8s.io/CloneOf: "true"
    k8s.io/CloneRequest: default/fedora-registry
    pv.kubernetes.io/bind-completed: "yes"
    pv.kubernetes.io/bound-by-controller: "yes"
    volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
    volume.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-16T17:10:30Z"
  finalizers:
  - kubernetes.io/pvc-protection
  labels:
    alerts.k8s.io/KubePersistentVolumeFillingUp: disabled
    app: containerized-data-importer
    app.kubernetes.io/component: storage
    app.kubernetes.io/managed-by: cdi-controller
    app.kubernetes.io/part-of: hyperconverged-cluster
    app.kubernetes.io/version: 4.11.3
  name: fedora06
  namespace: default
  ownerReferences:
  - apiVersion: cdi.kubevirt.io/v1beta1
    blockOwnerDeletion: true
    controller: true
    kind: DataVolume
    name: fedora06
    uid: b50e140b-59ea-4f9c-8f8d-1d0fbc90056d
  resourceVersion: "23907265"
  uid: fbf28358-7dae-4741-aaf8-6aa4c48d7dea
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 30Gi
  storageClassName: thin
  volumeMode: Filesystem
  volumeName: pvc-fbf28358-7dae-4741-aaf8-6aa4c48d7dea
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 30Gi
  phase: Bound
```
