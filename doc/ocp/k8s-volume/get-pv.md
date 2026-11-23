# Persistent Volume - Get

## Configurable options

```
# iserver get k8s pv
  --cluster TEXT                  Kubernetes cluster name
  --name TEXT                     Filter by name
  -v, --view TEXT                 [state|csi]  [default: state]
```

## Example (state)

```
# iserver get k8s pv --cluster bm1
Cluster: bm1 (type: ocp)

+----+------------------------------------------+--------+------------+----------+------+--------+-----------------------------------------------------------------+-------+
| ID | Persistent Volume                        | Status | Mode       | SC       | Size | Access | PVC                                                             | Age   |
+----+------------------------------------------+--------+------------+----------+------+--------+-----------------------------------------------------------------+-------+
| 1  | pvc-02a923e1-56d6-41c9-984d-026da4862e48 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/fedora-b37907f3bbf8          | 16d   |
| 2  | pvc-04117e45-3a45-44c5-a000-7ad3cf78661b | Bound  | Filesystem | lvms-vg1 | 30Gi | RWO    | openshift-image-registry/image-registry-storage                 | 21d   | 
| 3  | pvc-0940bbb7-d735-4930-bd66-f21c33bfc4d7 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | default/fedora-apricot-chickadee-80                             | 16d   |
| 4  | pvc-0c60ec2e-2c5d-4d5d-8fdf-8159d4b3eca2 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/centos-stream9-0e16ba1cf6c9  | 3h33m |
| 5  | pvc-2069b3e5-7836-4489-8946-c2897f01c9ff | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/centos-stream10-5db94eb365eb | 1d    |
| 6  | pvc-2197e80c-dc2e-4e96-82c1-13d4d893d563 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/centos-stream9-86bfc3da3797  | 6d    |
| 7  | pvc-2f4acc8a-472b-4ca0-bd01-0d17f2fbaa90 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/rhel10-c03936a065f2          | 16d   | 
| 8  | pvc-6a3b66f0-6d4a-4ba7-a88b-f7a961a5ddd3 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/centos-stream10-8adef4f5457b | 14d   | 
| 9  | pvc-a04c3eb7-89c8-46b6-8ec8-b6bd4b2af026 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/rhel9-ab4ec16077fe           | 16d   |
| 10 | pvc-a7e7ceb0-da6d-40e4-bc34-db64390cef22 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/centos-stream10-e1e46c96a306 | 7d    |
| 11 | pvc-a82e9ae9-c71e-4313-8c25-957e3f42ef0a | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/rhel8-004e24cfacec           | 16d   |
| 12 | pvc-d53e4396-855c-406e-a7bc-e77e4ddda467 | Bound  | Block      | lvms-vg1 | 30Gi | RWO    | openshift-virtualization-os-images/centos-stream9-4c67dd12e190  | 13d   | 
+----+------------------------------------------+--------+------------+----------+------+--------+-----------------------------------------------------------------+-------+
```

## Example (csi)

```
# iserver get k8s pv --cluster bm1 -v csi
Cluster: bm1 (type: ocp)

+----+------------------------------------------+--------+------+----------+------------+--------------------------------------+--------+-------+
| ID | Persistent Volume                        | Status | Size | SC       | CSI Driver | CSI Handle                           | Device | Age   |
+----+------------------------------------------+--------+------+----------+------------+--------------------------------------+--------+-------+
| 1  | pvc-02a923e1-56d6-41c9-984d-026da4862e48 | Bound  | 30Gi | lvms-vg1 | topolvm.io | f8051f6f-260e-4c01-8a9e-916259f95c3b | --     | 16d   |
| 2  | pvc-04117e45-3a45-44c5-a000-7ad3cf78661b | Bound  | 30Gi | lvms-vg1 | topolvm.io | 58e18cba-3702-4d0a-913e-800cc4cb8452 | --     | 21d   | 
| 3  | pvc-0940bbb7-d735-4930-bd66-f21c33bfc4d7 | Bound  | 30Gi | lvms-vg1 | topolvm.io | a3742b72-7423-4f60-8904-cd5e0b32c613 | --     | 16d   |
| 4  | pvc-0c60ec2e-2c5d-4d5d-8fdf-8159d4b3eca2 | Bound  | 30Gi | lvms-vg1 | topolvm.io | bcb750e6-89c4-420c-a472-dc22f18291a9 | --     | 3h33m |
| 5  | pvc-2069b3e5-7836-4489-8946-c2897f01c9ff | Bound  | 30Gi | lvms-vg1 | topolvm.io | 59a44961-f679-4ae3-992c-472b0a2f1466 | --     | 1d    |
| 6  | pvc-2197e80c-dc2e-4e96-82c1-13d4d893d563 | Bound  | 30Gi | lvms-vg1 | topolvm.io | bbb6ac8a-fe15-41e8-81b8-2cdb99a8b37f | --     | 6d    |
| 7  | pvc-2f4acc8a-472b-4ca0-bd01-0d17f2fbaa90 | Bound  | 30Gi | lvms-vg1 | topolvm.io | b4aba592-5dc8-497a-9298-51f871a50898 | --     | 16d   |
| 8  | pvc-6a3b66f0-6d4a-4ba7-a88b-f7a961a5ddd3 | Bound  | 30Gi | lvms-vg1 | topolvm.io | f20daaeb-0cfc-4817-8ec8-db968f5455d1 | --     | 14d   |
| 9  | pvc-a04c3eb7-89c8-46b6-8ec8-b6bd4b2af026 | Bound  | 30Gi | lvms-vg1 | topolvm.io | 42cf7d1e-bce1-4472-81b8-a9110ee5606e | --     | 16d   |
| 10 | pvc-a7e7ceb0-da6d-40e4-bc34-db64390cef22 | Bound  | 30Gi | lvms-vg1 | topolvm.io | e45ec7c3-795e-4f73-9f29-602a9a3e257e | --     | 7d    |
| 11 | pvc-a82e9ae9-c71e-4313-8c25-957e3f42ef0a | Bound  | 30Gi | lvms-vg1 | topolvm.io | d0ae3d2f-711e-47c2-9757-7342049d7f20 | --     | 16d   |
| 12 | pvc-d53e4396-855c-406e-a7bc-e77e4ddda467 | Bound  | 30Gi | lvms-vg1 | topolvm.io | 54a0dc51-42e1-4224-af3a-937041f6f310 | --     | 13d   |
+----+------------------------------------------+--------+------+----------+------------+--------------------------------------+--------+-------+
```

[[Back]](./README.md)