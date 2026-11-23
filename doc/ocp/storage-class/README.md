# Storage Class

Command | Intent 
--- | --- 
iserver get k8s sc | get storage classes 
iserver set k8s sc default | set storage class as default 
iserver set k8s sc nondefault | unset storage class as default 

## Get

```
# iserver get k8s sc --cluster bm1
Cluster: bm1 (type: ocp)

+----+---------------+---------+-------------+----------------+----------------------+------------------------+-----+----+
| ID | Storage Class | Default | Provisioner | Reclaim Policy | Volume Binding Mode  | Allow Volume Expansion | PVC | PV |
+----+---------------+---------+-------------+----------------+----------------------+------------------------+-----+----+
| 1  | lvms-vg1      | V       | topolvm.io  | Delete         | WaitForFirstConsumer | True                   | 24  | 22 |
+----+---------------+---------+-------------+----------------+----------------------+------------------------+-----+----+
```

## Set as default

```
# iserver set k8s sc default --name lvms-vg1 --cluster bm1
Cluster: bm1 (type: ocp)

Set Default Storage Class
-------------------------
- name: lvms-vg1

~~~
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: 'true'
  name: lvms-vg1

~~~
- storage class set to default
```

## Unset as default

```
# iserver set k8s sc nondefault --name lvms-vg1 --cluster bm1
Cluster: bm1 (type: ocp)

Unset Default Storage Class
---------------------------
- name: lvms-vg1

~~~
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: 'false'
  name: lvms-vg1

~~~
- storage class default unset
```

[[Back]](../Operations.md)