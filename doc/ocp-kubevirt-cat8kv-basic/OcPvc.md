# OpenShift Virtualization - Cat8000v Test Results

## Persistent Volume Claim

```
# oc get pvc -n default cat8kv-01
NAME        STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cat8kv-01   Bound    pvc-c792205f-f1cf-4984-9616-78d61e0044b1   16Gi       RWO            thick          6m38s


# oc get pvc -n default cat8kv-01 -o yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    cdi.kubevirt.io/storage.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE2Nzk5OTI5MjQsImlhdCI6MTY3OTk5MjYyNCwiaXNzIjoiY2RpLWFwaXNlcnZlciIsIm5hbWUiOiJjYXQ4a3YtZHYiLCJuYW1lc3BhY2UiOiJkZWZhdWx0IiwibmJmIjoxNjc5OTkyNjI0LCJvcGVydGF0aW9uIjoiQ2xvbmUiLCJwYXJhbXMiOnsidGFyZ2V0TmFtZSI6ImNhdDhrdi0wMSIsInRhcmdldE5hbWVzcGFjZSI6ImRlZmF1bHQifSwicmVzb3VyY2UiOnsiZ3JvdXAiOiIiLCJyZXNvdXJjZSI6InBlcnNpc3RlbnR2b2x1bWVjbGFpbXMiLCJ2ZXJzaW9uIjoidjEifX0.f4OopL_vMKvqEcouvWqEDXkWtVjIz4gmZcAKW7areG1gRrVa7W0lTixVRRNqdPudAzAJ-vjqyRZg0A4P39xkY3bxQSqp-9XoJ4TyUAM-yzoV0gUc2lXOf5jbpUG6lc8VKMHcO1k-oc-wcd5UQPK1n0p0oddIgvU5ufyo2LG5aZfQaZQfBAtpzQbMdMCAqg2AL2eVLc0XW7hyeJBHjMkwNiGkSc4i7Tfv5n440Me8Kp_1_o1TFWiic7IHZM0HX6SPhoKDmi23jlqLfYurvJ8OLWHYWSeA-kqbu1RMxuILTU9TuhS_1A1c1Y4tsJbHRs3aiiLhNcejdEEz33bOEyNLnA
    cdi.kubevirt.io/storage.condition.running: "false"
    cdi.kubevirt.io/storage.condition.running.message: Clone Complete
    cdi.kubevirt.io/storage.condition.running.reason: Completed
    cdi.kubevirt.io/storage.condition.source.running: "true"
    cdi.kubevirt.io/storage.condition.source.running.message: Clone Complete
    cdi.kubevirt.io/storage.condition.source.running.reason: Completed
    cdi.kubevirt.io/storage.extended.clone.token: eyJhbGciOiJQUzI1NiJ9.eyJleHAiOjE5OTUzNTI2MjQsImlhdCI6MTY3OTk5MjYyNCwiaXNzIjoiY2RpLWRlcGxveW1lbnQiLCJuYW1lIjoiY2F0OGt2LWR2IiwibmFtZXNwYWNlIjoiZGVmYXVsdCIsIm5iZiI6MTY3OTk5MjYyNCwib3BlcnRhdGlvbiI6IkNsb25lIiwicGFyYW1zIjp7InRhcmdldE5hbWUiOiJjYXQ4a3YtMDEiLCJ0YXJnZXROYW1lc3BhY2UiOiJkZWZhdWx0IiwidWlkIjoiYzc5MjIwNWYtZjFjZi00OTg0LTk2MTYtNzhkNjFlMDA0NGIxIn0sInJlc291cmNlIjp7Imdyb3VwIjoiIiwicmVzb3VyY2UiOiJwZXJzaXN0ZW50dm9sdW1lY2xhaW1zIiwidmVyc2lvbiI6InYxIn19.SgA_qM_WFdzEVJTU-goDWQVwHafrw14sLqBc4Yd9PZSj-3kImo1xf3s36_qPXpxuisrAdzGvtJ7USyAb87w98fH37-g5zjXJ_bcQH2HvQL3-twGSGxdycWjpwstA7z4N1MBuhXLROcTE57UG7Z7m7FnRIwsYEm3cpxH8XmlYM_ieu8KCzkosT7wCZHoYKpD0yHGiDWzHKwbIELQAH_5zUZgZQVnjVmDrZMgZRU-UYsn1AO8ddBPb3O8qiW2Xf4iBZ9hl251C1Lfs9nLwo62GuC3QGYPtV48x8d_o0ko6GDw2w-ynMfYFpmrgGRDf8nTo6TkUyWxQKXjlpg4vy69tWw
    cdi.kubevirt.io/storage.pod.phase: Succeeded
    cdi.kubevirt.io/storage.pod.ready: "false"
    cdi.kubevirt.io/storage.pod.restarts: "0"
    cdi.kubevirt.io/storage.preallocation.requested: "false"
    cdi.kubevirt.io/storage.sourceClonePodName: c792205f-f1cf-4984-9616-78d61e0044b1-source-pod
    cdi.kubevirt.io/storage.uploadPodName: cdi-upload-cat8kv-01
    cdi.kubevirt.io/uploadClientName: default/cat8kv-dv-default/cat8kv-01
    k8s.io/CloneOf: "true"
    k8s.io/CloneRequest: default/cat8kv-dv
    pv.kubernetes.io/bind-completed: "yes"
    pv.kubernetes.io/bound-by-controller: "yes"
    volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
    volume.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-28T08:37:04Z"
  finalizers:
  - kubernetes.io/pvc-protection
  labels:
    app: containerized-data-importer
    app.kubernetes.io/component: storage
    app.kubernetes.io/managed-by: cdi-controller
    app.kubernetes.io/part-of: hyperconverged-cluster
    app.kubernetes.io/version: 4.11.3
  name: cat8kv-01
  namespace: default
  ownerReferences:
  - apiVersion: cdi.kubevirt.io/v1beta1
    blockOwnerDeletion: true
    controller: true
    kind: DataVolume
    name: cat8kv-01
    uid: da36defa-9ad9-4d54-b561-cf9b28a5a534
  resourceVersion: "50308476"
  uid: c792205f-f1cf-4984-9616-78d61e0044b1
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 16Gi
  storageClassName: thick
  volumeMode: Block
  volumeName: pvc-c792205f-f1cf-4984-9616-78d61e0044b1
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 16Gi
  phase: Bound


# oc get pvc -n default cat8kv-01-day0
NAME             STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
cat8kv-01-day0   Bound    pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003   1Gi        RWO            thin           6m57s


# oc get pvc -n default cat8kv-01-day0 -o yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  annotations:
    cdi.kubevirt.io/storage.condition.bound: "true"
    cdi.kubevirt.io/storage.condition.bound.message: ""
    cdi.kubevirt.io/storage.condition.bound.reason: ""
    cdi.kubevirt.io/storage.condition.running: "false"
    cdi.kubevirt.io/storage.condition.running.message: Upload Complete
    cdi.kubevirt.io/storage.condition.running.reason: Completed
    cdi.kubevirt.io/storage.contentType: ""
    cdi.kubevirt.io/storage.pod.phase: Succeeded
    cdi.kubevirt.io/storage.pod.ready: "false"
    cdi.kubevirt.io/storage.pod.restarts: "0"
    cdi.kubevirt.io/storage.preallocation.requested: "false"
    cdi.kubevirt.io/storage.upload.target: ""
    cdi.kubevirt.io/storage.uploadPodName: cdi-upload-cat8kv-01-day0
    pv.kubernetes.io/bind-completed: "yes"
    pv.kubernetes.io/bound-by-controller: "yes"
    volume.beta.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
    volume.kubernetes.io/storage-provisioner: kubernetes.io/vsphere-volume
  creationTimestamp: "2023-03-28T08:36:48Z"
  finalizers:
  - kubernetes.io/pvc-protection
  labels:
    app: containerized-data-importer
    app.kubernetes.io/component: storage
    app.kubernetes.io/managed-by: cdi-controller
    app.kubernetes.io/part-of: hyperconverged-cluster
    app.kubernetes.io/version: 4.11.3
  name: cat8kv-01-day0
  namespace: default
  ownerReferences:
  - apiVersion: cdi.kubevirt.io/v1beta1
    blockOwnerDeletion: true
    controller: true
    kind: DataVolume
    name: cat8kv-01-day0
    uid: cf026c9b-ac9b-47df-b267-15af638f0b30
  resourceVersion: "50305862"
  uid: 0f2aefe8-7a56-406a-9c73-e087fdb21003
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 1Gi
  storageClassName: thin
  volumeMode: Block
  volumeName: pvc-0f2aefe8-7a56-406a-9c73-e087fdb21003
status:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 1Gi
  phase: Bound
```
