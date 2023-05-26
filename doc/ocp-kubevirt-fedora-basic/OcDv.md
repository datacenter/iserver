# OpenShift Virtualization - Fedora Test Results

## Data Volume

```
# oc get dvs -n default fedora02
NAME       PHASE       PROGRESS   RESTARTS   AGE
fedora02   Succeeded   100.0%                3m35s


# oc get dvs -n default fedora02 -o yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/cloneType: network
    cdi.kubevirt.io/storage.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE2Nzg5ODY2OTAsImlhdCI6MTY3ODk4NjM5MCwiaXNzIjoiY2RpLWFwaXNlcnZlciIsIm5hbWUiOiJmZWRvcmEtcmVnaXN0cnkiLCJuYW1lc3BhY2UiOiJkZWZhdWx0IiwibmJmIjoxNjc4OTg2MzkwLCJvcGVydGF0aW9uIjoiQ2xvbmUiLCJwYXJhbXMiOnsidGFyZ2V0TmFtZSI6ImZlZG9yYTAyIiwidGFyZ2V0TmFtZXNwYWNlIjoiZGVmYXVsdCJ9LCJyZXNvdXJjZSI6eyJncm91cCI6IiIsInJlc291cmNlIjoicGVyc2lzdGVudHZvbHVtZWNsYWltcyIsInZlcnNpb24iOiJ2MSJ9fQ.SR2lkZZ3piBno8PZ2yGw_TJn3eDf1ZLXKM8YnW1eSf2THqegDCdHgWhiwEWnvzHdFcy7OsDlSwmePzXruoXyWgCY_sdjviEUkBBBR8cBV84_4W59uhx09Mt5TZq55GORu8ZW2Ll1sAKYcVNhdaWH6dnGL68qtfujZrMV5-zsbn1yYJdamo981nti8FGOth9bJeO4_0QZ76wi8xpXKOqODECtJAwF84yvg7EJcOkNvSdQU2xJ3pz6uJNACDNnniKNb9WqaKQ9tV7tEvJMsszt5mBWGMCQDu-SxHKZC3LbxIdFNtzwYGhVzrHVSYoufzaq8_FwG1c__n0-1Z77W9QePQ
  creationTimestamp: "2023-03-16T17:06:30Z"
  generation: 60
  labels:
    kubevirt.io/created-by: 4a95b3f6-bf78-4c4c-a361-415cfce605ca
  name: fedora02
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: fedora02
    uid: 4a95b3f6-bf78-4c4c-a361-415cfce605ca
  resourceVersion: "23904151"
  uid: e34991e0-443b-4270-9fdd-f074c4f16b78
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
  claimName: fedora02
  conditions:
  - lastHeartbeatTime: "2023-03-16T17:07:06Z"
    lastTransitionTime: "2023-03-16T17:07:06Z"
    message: PVC fedora02 Bound
    reason: Bound
    status: "True"
    type: Bound
  - lastHeartbeatTime: "2023-03-16T17:09:27Z"
    lastTransitionTime: "2023-03-16T17:09:27Z"
    status: "True"
    type: Ready
  - lastHeartbeatTime: "2023-03-16T17:09:25Z"
    lastTransitionTime: "2023-03-16T17:09:25Z"
    message: Clone Complete
    reason: Completed
    status: "False"
    type: Running
  phase: Succeeded
  progress: 100.0%
```
