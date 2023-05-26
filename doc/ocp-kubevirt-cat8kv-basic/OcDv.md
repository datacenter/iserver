# OpenShift Virtualization - Cat8000v Test Results

## Data Volume

```
# oc get dvs -n default cat8kv-01
NAME        PHASE       PROGRESS   RESTARTS   AGE
cat8kv-01   Succeeded   100.0%                6m34s


# oc get dvs -n default cat8kv-01 -o yaml
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/cloneType: network
    cdi.kubevirt.io/storage.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE2Nzk5OTI5MjQsImlhdCI6MTY3OTk5MjYyNCwiaXNzIjoiY2RpLWFwaXNlcnZlciIsIm5hbWUiOiJjYXQ4a3YtZHYiLCJuYW1lc3BhY2UiOiJkZWZhdWx0IiwibmJmIjoxNjc5OTkyNjI0LCJvcGVydGF0aW9uIjoiQ2xvbmUiLCJwYXJhbXMiOnsidGFyZ2V0TmFtZSI6ImNhdDhrdi0wMSIsInRhcmdldE5hbWVzcGFjZSI6ImRlZmF1bHQifSwicmVzb3VyY2UiOnsiZ3JvdXAiOiIiLCJyZXNvdXJjZSI6InBlcnNpc3RlbnR2b2x1bWVjbGFpbXMiLCJ2ZXJzaW9uIjoidjEifX0.f4OopL_vMKvqEcouvWqEDXkWtVjIz4gmZcAKW7areG1gRrVa7W0lTixVRRNqdPudAzAJ-vjqyRZg0A4P39xkY3bxQSqp-9XoJ4TyUAM-yzoV0gUc2lXOf5jbpUG6lc8VKMHcO1k-oc-wcd5UQPK1n0p0oddIgvU5ufyo2LG5aZfQaZQfBAtpzQbMdMCAqg2AL2eVLc0XW7hyeJBHjMkwNiGkSc4i7Tfv5n440Me8Kp_1_o1TFWiic7IHZM0HX6SPhoKDmi23jlqLfYurvJ8OLWHYWSeA-kqbu1RMxuILTU9TuhS_1A1c1Y4tsJbHRs3aiiLhNcejdEEz33bOEyNLnA
  creationTimestamp: "2023-03-28T08:37:04Z"
  generation: 82
  labels:
    kubevirt.io/created-by: 13cc4023-acd7-4696-9f6a-662703655788
  name: cat8kv-01
  namespace: default
  ownerReferences:
  - apiVersion: kubevirt.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: VirtualMachine
    name: cat8kv-01
    uid: 13cc4023-acd7-4696-9f6a-662703655788
  resourceVersion: "50308417"
  uid: da36defa-9ad9-4d54-b561-cf9b28a5a534
spec:
  pvc:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 16Gi
    storageClassName: thick
    volumeMode: Block
  source:
    pvc:
      name: cat8kv-dv
      namespace: default
status:
  claimName: cat8kv-01
  conditions:
  - lastHeartbeatTime: "2023-03-28T08:37:05Z"
    lastTransitionTime: "2023-03-28T08:37:05Z"
    message: PVC cat8kv-01 Bound
    reason: Bound
    status: "True"
    type: Bound
  - lastHeartbeatTime: "2023-03-28T08:38:30Z"
    lastTransitionTime: "2023-03-28T08:38:30Z"
    status: "True"
    type: Ready
  - lastHeartbeatTime: "2023-03-28T08:38:28Z"
    lastTransitionTime: "2023-03-28T08:38:28Z"
    message: Clone Complete
    reason: Completed
    status: "False"
    type: Running
  phase: Succeeded
  progress: 100.0%
```
