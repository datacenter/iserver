# Local Volume Discovery

## Get

```
# iserver get k8s locvd --cluster bm1
Cluster: bm1 (type: ocp)

+-------------------------+-----------------------+-----------+-------------+
| Namespace               | Name                  | Available | Phase       |
+-------------------------+-----------------------+-----------+-------------+
| openshift-local-storage | auto-discover-devices | ✓         | Discovering |
+-------------------------+-----------------------+-----------+-------------+

Filter: --
View:   state (def)
```

## Delete

```
# iserver delete k8s locvd
Cluster: bm1 (type: ocp)

+-------------------------+-----------------------+-----------+-------------+
| Namespace               | Name                  | Available | Phase       |
+-------------------------+-----------------------+-----------+-------------+
| openshift-local-storage | auto-discover-devices | ✓         | Discovering |
+-------------------------+-----------------------+-----------+-------------+
Continue [Y/N]?y

Delete local volume discovery
-----------------------------
- openshift-local-storage/auto-discover-devices
        REST API successful
        Wait for no local volume discovery [timeout:360]...
```

```
# iserver delete k8s locvd --cluster bm1
Cluster: bm1 (type: ocp)
[ERROR] Local Volume Discovery cannot be deleted when Local Volume Set exists
```

[[Back]](./README.md)