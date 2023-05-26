# OpenShift Virtualization - Fedora Test Results

## Data Volume

```
# oc get dvs -n default fedora06
NAME       PHASE       PROGRESS   RESTARTS   AGE
fedora06   Succeeded   100.0%                118s


# oc get dvs -n default fedora06 -o yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/cloneType: network
    cdi.kubevirt.io/storage.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE2Nzg5ODY5MzAsImlhdCI6MTY3ODk4NjYzMCwiaXNzIjoiY2RpLWFwaXNlcnZlciIsIm5hbWUiOiJmZWRvcmEtcmVnaXN0cnkiLCJuYW1lc3BhY2UiOiJkZWZhdWx0IiwibmJmIjoxNjc4OTg2NjMwLCJvcGVydGF0aW9uIjoiQ2xvbmUiLCJwYXJhbXMiOnsidGFyZ2V0TmFtZSI6ImZlZG9yYTA2IiwidGFyZ2V0TmFtZXNwYWNlIjoiZGVmYXVsdCJ9LCJyZXNvdXJjZSI6eyJncm91cCI6IiIsInJlc291cmNlIjoicGVyc2lzdGVudHZvbHVtZWNsYWltcyIsInZlcnNpb24iOiJ2MSJ9fQ.GCiWKbiNQP-COp8a8zMOIjhGIttFOHrLK6oWNbSEyxkkftqKG8mX1c2nHhCMV2OHIeZXvi0Bz1p4bYFdgqDk_c5g12aQZvyKApBXGtFtcY47oTMC9s2CUc_2bA4o3I0oFyYrEJkXvkTCVN197FG_rYElUxr1158nbUUxMyD_WYHZxF21uD4r7pzQ8qp0YZGdukZBVdAHIbd-PIzIIc87kDXsdiughUd4CyKbT2vKPeCsFnAy4IYes8lVDk0b3o8RSm3Yg2nSE4KkC8fd_Qf_OjlanhrYej909k1r_jBDv7JPUDqp2la7V5b48oJGBGh11TIvQORsfjD1O2wUEAP7RA
  creationTimestamp: "2023-03-16T17:10:30Z"
  generation: 48
  labels:
    kubevirt.io/created-by: 94e0304d-26d6-4868-942a-7e1043cc9c8d
  name: fedora06
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: fedora06
    uid: 94e0304d-26d6-4868-942a-7e1043cc9c8d
  resourceVersion: "23908005"
  uid: b50e140b-59ea-4f9c-8f8d-1d0fbc90056d
spec:
  pvc:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 30Gi
    volumeMode: Filesystem
  source:
    pvc:
      name: fedora-registry
      namespace: default
status:
  claimName: fedora06
  conditions:
  - lastHeartbeatTime: "2023-03-16T17:10:33Z"
    lastTransitionTime: "2023-03-16T17:10:33Z"
    message: PVC fedora06 Bound
    reason: Bound
    status: "True"
    type: Bound
  - lastHeartbeatTime: "2023-03-16T17:11:43Z"
    lastTransitionTime: "2023-03-16T17:11:43Z"
    status: "True"
    type: Ready
  - lastHeartbeatTime: "2023-03-16T17:11:11Z"
    lastTransitionTime: "2023-03-16T17:11:11Z"
    message: Clone Complete
    reason: Completed
    status: "False"
    type: Running
  phase: Succeeded
  progress: 100.0%
```
