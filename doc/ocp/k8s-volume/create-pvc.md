# Persistent Volume Claim - Create

## Workflow

- create pvc based on user-defined parameters
- if storage class name is not defined then it is the default one or the only one

## Requirements

None

## Configurable options

```
# iserver create k8s pvc 
  --cluster TEXT    Cluster name
  --namespace TEXT  Namespace
  --name TEXT       Name
  --mode [f|b|]     Fileystem or block mode
  --sc TEXT         Storage class
  --size TEXT       Requested size
  --limit TEXT      Requested limit
  --no-confirm      Confirmation mode
```

## Example

With parameters provided in interactive way

```
# iserver create k8s pvc --cluster bm1
Cluster: bm1 (type: ocp)

PVC Namespace: default
PVC Name: test
Volume mode (filesystem, block):
- f
- b
Value: b
Requests size (e.g. 1Gi): 1Gi
Limits size (e.g. 1Gi): 1Gi

Create Persistent Volume Claim
------------------------------
- namespace: default
- name: test
- volume mode: Block
- storage class: lvms-vg1
- requests [1Gi] limits [1Gi]

~~~
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test
  namespace: default
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    limits:
      storage: 1Gi
    requests:
      storage: 1Gi
  storageClassName: lvms-vg1
  volumeMode: Block

~~~
Continue [Y/N]? y

Persistent volume claim created

Wait for pvc...
Wait for pvc pending or bound...

+----+---------+---------+-------+------+--------+---------------+------+
| ID | PVC     | Status  | Mode  | Size | Access | Storage Class | Age  |
+----+---------+---------+-------+------+--------+---------------+------+
| 1  | default | Pending | Block | 1Gi  | RWO    | lvms-vg1      | 1h0m |
|    | test    |         |       |      |        |               |      |
+----+---------+---------+-------+------+--------+---------------+------+
```

With parameters provided in command options

```
# iserver create k8s pvc --cluster bm1 --namespace default --name test --mode b --sc lvms-vg1 --size 1Gi --limit 1Gi --no-confirm
Cluster: bm1 (type: ocp)

Create Persistent Volume Claim
------------------------------
- namespace: default
- name: test
- volume mode: Block
- storage class: lvms-vg1
- requests [1Gi] limits [1Gi]

~~~
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: test
  namespace: default
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    limits:
      storage: 1Gi
    requests:
      storage: 1Gi
  storageClassName: lvms-vg1
  volumeMode: Block

~~~

Persistent volume claim created

Wait for pvc...
Wait for pvc pending or bound...

+----+---------+---------+-------+------+--------+---------------+------+
| ID | PVC     | Status  | Mode  | Size | Access | Storage Class | Age  |
+----+---------+---------+-------+------+--------+---------------+------+
| 1  | default | Pending | Block | 1Gi  | RWO    | lvms-vg1      | 1h0m |
|    | test    |         |       |      |        |               |      |
+----+---------+---------+-------+------+--------+---------------+------+
```

[[Back]](./README.md)