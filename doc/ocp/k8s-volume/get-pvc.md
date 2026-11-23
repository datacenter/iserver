# Persistent Volume Claim - Get

## Workflow

- get persistent volume claims
- in case of usage option, extra information is collected and augmented with pvc information
  - persistent volume
  - data volume
  - volume snapshot
  - pod
  - virtual machine instance
- selected view controls type of information presented on the output

## Requirements

None

## Configurable options

```
# iserver get k8s pvc 
  --cluster TEXT                  Kubernetes cluster name
  --namespace TEXT                Filter by namespace
  --name TEXT                     Filter by name
  -v, --view TEXT                 [state|metadata|usage|all]  [default: state]
```

## Example (state)

```
# iserver get k8s pvc --cluster bm1 --namespace default
Cluster: bm1 (type: ocp)

+----+-----------------------------+---------+------------------------------------------+-------+------+--------+---------------+-------+
| ID | PVC                         | Status  | PV                                       | Mode  | Size | Access | Storage Class | Age   |
+----+-----------------------------+---------+------------------------------------------+-------+------+--------+---------------+-------+
| 1  | default                     | Bound   | pvc-0940bbb7-d735-4930-bd66-f21c33bfc4d7 | Block | 30Gi | RWO    | lvms-vg1      | 16d   |
|    | fedora-apricot-chickadee-80 |         |                                          |       |      |        |               |       | 
+----+-----------------------------+---------+------------------------------------------+-------+------+--------+---------------+-------+
| 2  | default                     | Bound   | pvc-2b9645ed-4574-4fc1-8b1b-3c127fc12e16 | Block | 8Gi  | RWO    | lvms-vg1      | 1d    |
|    | mtv1-vm-61951-nrh7j         |         |                                          |       |      |        |               |       |
+----+-----------------------------+---------+------------------------------------------+-------+------+--------+---------------+-------+
| 3  | default                     | Pending | ---                                      | Block | 1Gi  | RWO    | lvms-vg1      | 1h44m |
|    | test                        |         |                                          |       |      |        |               |       |
+----+-----------------------------+---------+------------------------------------------+-------+------+--------+---------------+-------+
```

## Example (metadata)

```
# iserver get k8s pvc --cluster bm1 --namespace default -v metadata
Cluster: bm1 (type: ocp)

+----+-----------------------------+-----------------------------+-----------------------------------------------------------+--------------------------------------------------------------+      
| ID | PVC                         | Owner                       | Label                                                     | Annotation                                                   |      
+----+-----------------------------+-----------------------------+-----------------------------------------------------------+--------------------------------------------------------------+      
| 1  | default                     | DataVolume                  | app = containerized-data-importer                         | cdi.kubevirt.io/allowClaimAdoption = true                    | 
|    | fedora-apricot-chickadee-80 | fedora-apricot-chickadee-80 | app.kubernetes.io/component = storage                     | cdi.kubevirt.io/clonePhase = Succeeded                       |      
|    |                             |                             | app.kubernetes.io/managed-by = cdi-controller             | cdi.kubevirt.io/cloneType = copy                             |      
|    |                             |                             | app.kubernetes.io/part-of = hyperconverged-cluster        | cdi.kubevirt.io/createdForDataVolume =                       |      
|    |                             |                             | app.kubernetes.io/version = 4.18.23                       | 05eebc71-0629-4ff5-a215-a2a8143a8df3                         |      
|    |                             |                             | instancetype.kubevirt.io/default-instancetype = u1.medium | cdi.kubevirt.io/dataSourceNamespace =                        |      
|    |                             |                             | instancetype.kubevirt.io/default-preference = fedora      | openshift-virtualization-os-images                           |      
|    |                             |                             | kubevirt.io/created-by =                                  | cdi.kubevirt.io/storage.condition.running = false            |      
|    |                             |                             | 2bb10f72-5942-40fa-966f-b285a8e9f11e                      | cdi.kubevirt.io/storage.condition.running.message = Clone    |      
|    |                             |                             |                                                           | Complete                                                     |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.condition.running.reason =           |      
|    |                             |                             |                                                           | Completed                                                    | 
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.contentType = kubevirt               |         
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.pod.restarts = 0                     |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.populator.progress = 100.0%          |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.preallocation.requested = false      |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.usePopulator = true                  |      
|    |                             |                             |                                                           | k8s.io/CloneOf = true                                        |      
|    |                             |                             |                                                           | pv.kubernetes.io/bind-completed = yes                        |      
|    |                             |                             |                                                           | pv.kubernetes.io/bound-by-controller = yes                   |      
|    |                             |                             |                                                           | volume.beta.kubernetes.io/storage-provisioner = topolvm.io   |      
|    |                             |                             |                                                           | volume.kubernetes.io/selected-node = bm1-2                   |      
|    |                             |                             |                                                           | volume.kubernetes.io/storage-provisioner = topolvm.io        |      
+----+-----------------------------+-----------------------------+-----------------------------------------------------------+--------------------------------------------------------------+
| 2  | default                     | DataVolume                  | app = containerized-data-importer                         | cdi.kubevirt.io/createdForDataVolume =                       |      
|    | mtv1-vm-61951-nrh7j         | mtv1-vm-61951-nrh7j         | app.kubernetes.io/component = storage                     | 1727438b-ac91-4fd3-bcf5-9535baf5c944                         |      
|    |                             |                             | app.kubernetes.io/managed-by = cdi-controller             | cdi.kubevirt.io/storage.condition.running = false            |      
|    |                             |                             | app.kubernetes.io/part-of = hyperconverged-cluster        | cdi.kubevirt.io/storage.condition.running.message =          |      
|    |                             |                             | app.kubernetes.io/version = 4.18.23                       | cdi.kubevirt.io/storage.condition.running.reason =           |      
|    |                             |                             | migration = d5eea2bc-660a-4841-ac2a-c74898f0c6ea          | Completed                                                    |      
|    |                             |                             | plan = f4f003e2-2942-4a5e-ba2a-6255df4c7043               | cdi.kubevirt.io/storage.contentType = kubevirt               |      
|    |                             |                             | resource = vm-config                                      | cdi.kubevirt.io/storage.deleteAfterCompletion = false        |      
|    |                             |                             | vmID = vm-61951                                           | cdi.kubevirt.io/storage.pod.phase = Succeeded                |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.pod.restarts = 0                     |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.populator.progress = 100.0%          |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.preallocation.requested = false      |      
|    |                             |                             |                                                           | cdi.kubevirt.io/storage.usePopulator = true                  |      
|    |                             |                             |                                                           | forklift.konveyor.io/disk-index = 0                          |      
|    |                             |                             |                                                           | forklift.konveyor.io/disk-source = [My-NAS]                  |      
|    |                             |                             |                                                           | New Virtual Machine/New Virtual Machine.vmdk                 |      
|    |                             |                             |                                                           | migration = d5eea2bc-660a-4841-ac2a-c74898f0c6ea             |      
|    |                             |                             |                                                           | plan = f4f003e2-2942-4a5e-ba2a-6255df4c7043                  |      
|    |                             |                             |                                                           | pv.kubernetes.io/bind-completed = yes                        | 
|    |                             |                             |                                                           | pv.kubernetes.io/bound-by-controller = yes                   |      
|    |                             |                             |                                                           | resource = vm-config                                         |      
|    |                             |                             |                                                           | vmID = vm-61951                                              |      
|    |                             |                             |                                                           | volume.beta.kubernetes.io/storage-provisioner = topolvm.io   |      
|    |                             |                             |                                                           | volume.kubernetes.io/selected-node = bm1-3                   |      
|    |                             |                             |                                                           | volume.kubernetes.io/storage-provisioner = topolvm.io        |      
+----+-----------------------------+-----------------------------+-----------------------------------------------------------+--------------------------------------------------------------+
| 3  | default                     | ---                         | ---                                                       | ---                                                          |      
|    | test                        |                             |                                                           |                                                              |      
+----+-----------------------------+-----------------------------+-----------------------------------------------------------+--------------------------------------------------------------+ 
```

## Example (usage)

```
# iserver get k8s pvc --cluster bm1 --namespace default -v usage
Cluster: bm1 (type: ocp)

+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+-------+
| ID | PVC                         | Status  | Mode  | Size | Access | Storage Class | Usage                                                         | Age   |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+-------+
| 1  | default                     | Bound   | Block | 30Gi | RWO    | lvms-vg1      | [dv] fedora-apricot-chickadee-80                              | 16d   |
|    | fedora-apricot-chickadee-80 |         |       |      |        |               | [pod] default/virt-launcher-fedora-apricot-chickadee-80-ldstf |       | 
|    |                             |         |       |      |        |               | [vmi] default/fedora-apricot-chickadee-80                     |       |
|    |                             |         |       |      |        |               | [pv] pvc-0940bbb7-d735-4930-bd66-f21c33bfc4d7                 |       |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+-------+
| 2  | default                     | Bound   | Block | 8Gi  | RWO    | lvms-vg1      | [dv] mtv1-vm-61951-nrh7j                                      | 1d    |
|    | mtv1-vm-61951-nrh7j         |         |       |      |        |               | [pv] pvc-2b9645ed-4574-4fc1-8b1b-3c127fc12e16                 |       |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+-------+
| 3  | default                     | Pending | Block | 1Gi  | RWO    | lvms-vg1      | ---                                                           | 1h44m |
|    | test                        |         |       |      |        |               |                                                               |       |
+----+-----------------------------+---------+-------+------+--------+---------------+---------------------------------------------------------------+-------+
```

[[Back]](./README.md)