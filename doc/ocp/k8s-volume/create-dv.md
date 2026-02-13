# Data Volume - Create

Data Volume is OpenShift Virtualization extension used to automate the creation of a PVC and the importation of virtual machine images from sources like HTTP.

## Workflow

Create data volume based on user-defined parameters
- data volume ready for manual file upload
- data volume populated with local/remote file using virtctl upload
- data volume populated based on http source

Check the examples below for data volume create options vs. used-defined parameters

## Requirements

Container virtualization (cnv) operator [installed](../cnv/README.md)

## Configurable options

```
# iserver create k8s dv
  --cluster TEXT    Cluster Name
  --namespace TEXT  Namespace
  --name TEXT       Name
  --sc TEXT         Storage class
  --source TEXT     Source filename
  --secret TEXT     Secret reference
  --size TEXT       Target PVC size
  --no-confirm      Confirmation mode
```

Notes:
- storage class (sc) can be undefined if (a) there is default one (b) there is only one storage class
- source format example
  - "http://10.1.1.1/image.qcow"
  - "/tmp/image.qcow"
  - "mylinux@/tmp/image.qcow"

where mylinux is pre-configured Linux connector that defines IP/FQDN and authentication to remote *nix server.

## Example (upload ready)

```
# iserver create k8s dv --namespace default --name test --size 1G --no-confirm

OpenShift Workflow - Data Volume - Create
=========================================

OpenShift Cluster: bm1

Create Data Volume ready for upload
-----------------------------------
- namespace: default
- name: test
- access mode: ReadWriteOnce
- storage class: lvms-vg1
- size [1G]

~~~
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/storage.bind.immediate.requested: 'true'
  name: test
  namespace: default
spec:
  pvc:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1G
    storageClassName: lvms-vg1
  source:
    upload: {}

~~~

Data volume created

Wait for data volume...
Wait for data volume upload ready state...

+----+-------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+------+
| ID | Data Volume | Bound | Ready | Phase       | Progress | Size | Usage                                                            | Age  |
+----+-------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+------+
| 1  | default     | X     | X     | UploadReady | N/A      | 1G   | [pvc] test                                                       | 1h0m |
|    | test        |       |       |             |          |      | [pvc] default/prime-8c406f5a-b8be-4927-9918-660abafd5529         |      |
|    |             |       |       |             |          |      | [pod] cdi-upload-prime-8c406f5a-b8be-4927-9918-660abafd5529      |      |
|    |             |       |       |             |          |      | [pvc] default/prime-8c406f5a-b8be-4927-9918-660abafd5529-scratch |      |
+----+-------------+-------+-------+-------------+----------+------+------------------------------------------------------------------+------+
```

## Example (http)

Note:
- if parameter --secret is defined, it is used as spec:source:http:sourceRef for http authentication

```
# iserver create k8s dv --namespace default --name test --size 1G --source http://10.10.10.10:8080/cirros-0.5.1-x86_64-disk.img --no-confirm

OpenShift Workflow - Data Volume - Create
=========================================

OpenShift Cluster: bm1

Create Data Volume ready for upload
-----------------------------------
- namespace: default
- name: test
- access mode: ReadWriteOnce
- storage class: lvms-vg1
- size [1G]
- source: http://10.10.10.10:8080/cirros-0.5.1-x86_64-disk.img

~~~
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/storage.bind.immediate.requested: 'true'
  name: test
  namespace: default
spec:
  pvc:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1G
    storageClassName: lvms-vg1
  source:
    http:
      url: http://10.10.10.10:8080/cirros-0.5.1-x86_64-disk.img

~~~

Data volume created

Wait for data volume...
Wait for data volume upload ready state...

+----+-------------+-------+-------+------------------+----------+------+-----------------------------------------------------------+------+
| ID | Data Volume | Bound | Ready | Phase            | Progress | Size | Usage                                                     | Age  |
+----+-------------+-------+-------+------------------+----------+------+-----------------------------------------------------------+------+
| 1  | default     | X     | X     | ImportInProgress | N/A      | 1G   | [pvc] test                                                | 1h0m | 
|    | test        |       |       |                  |          |      | [pvc] default/prime-7acc50d3-1dc4-4103-8f96-153c494fd639  |      | 
|    |             |       |       |                  |          |      | [pod] importer-prime-7acc50d3-1dc4-4103-8f96-153c494fd639 |      | 
+----+-------------+-------+-------+------------------+----------+------+-----------------------------------------------------------+------+

+----+-------------+-------+-------+-----------+----------+------+------------+------+
| ID | Data Volume | Bound | Ready | Phase     | Progress | Size | Usage      | Age  |
+----+-------------+-------+-------+-----------+----------+------+------------+------+
| 1  | default     | V     | V     | Succeeded | 100.0%   | 1G   | [pvc] test | 1h0m | 
|    | test        |       |       |           |          |      |            |      | 
+----+-------------+-------+-------+-----------+----------+------+------------+------+
```

## Example (local file)

```
# iserver create k8s dv --namespace default --name test --size 1G --source C:\tmp\cirros-0.5.1-x86_64-disk.img --no-confirm


OpenShift Workflow - Data Volume - Create
=========================================

OpenShift Cluster: bm1

Create Data Volume ready for upload
-----------------------------------
- namespace: default
- name: test
- access mode: ReadWriteOnce
- storage class: lvms-vg1
- size [1G]
- ready for upload

~~~
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/storage.bind.immediate.requested: 'true'
  name: test
  namespace: default
spec:
  pvc:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1G
    storageClassName: lvms-vg1
  source:
    upload: {}

~~~
Continue [Y/N]? y

Data volume created

Wait for data volume...
Wait for data volume upload ready state...
scp file upload: C:\tmp\cirros-0.5.1-x86_64-disk.img => /tmp/c5f3f49c7f41
Run: virtctl -n default image-upload dv test --no-create --image-path=/tmp/c5f3f49c7f41 --insecure

+----+-------------+-------+-------+-----------+----------+------+------------+------+
| ID | Data Volume | Bound | Ready | Phase     | Progress | Size | Usage      | Age  |
+----+-------------+-------+-------+-----------+----------+------+------------+------+
| 1  | default     | V     | V     | Succeeded | N/A      | 1G   | [pvc] test | 1h0m |
|    | test        |       |       |           |          |      |            |      |
+----+-------------+-------+-------+-----------+----------+------+------------+------+
```

## Example (remote file)

```
# iserver create k8s dv --namespace default --name test --size 1G --source myserver@/home/user/image/cirros-0.5.1-x86_64-disk.img 

OpenShift Workflow - Data Volume - Create
=========================================

OpenShift Cluster: bm1
Download file: /home/user/image/cirros-0.5.1-x86_64-disk.img => /tmp/11e48396c180

Create Data Volume ready for upload
-----------------------------------
- namespace: default
- name: test
- access mode: ReadWriteOnce
- storage class: lvms-vg1
- size [1G]
- ready for upload

~~~
apiVersion: cdi.kubevirt.io/v1beta1
kind: DataVolume
metadata:
  annotations:
    cdi.kubevirt.io/storage.bind.immediate.requested: 'true'
  name: test
  namespace: default
spec:
  pvc:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 1G
    storageClassName: lvms-vg1
  source:
    upload: {}

~~~
Continue [Y/N]? y

Data volume created

Wait for data volume...
Wait for data volume upload ready state...
scp file upload: /tmp/11e48396c180 => /tmp/f0a9585f0cdd
Run: virtctl -n default image-upload dv test --no-create --image-path=/tmp/f0a9585f0cdd --insecure

+----+-------------+-------+-------+-----------+----------+------+------------+------+
| ID | Data Volume | Bound | Ready | Phase     | Progress | Size | Usage      | Age  |
+----+-------------+-------+-------+-----------+----------+------+------------+------+
| 1  | default     | V     | V     | Succeeded | N/A      | 1G   | [pvc] test | 1h0m |
|    | test        |       |       |           |          |      |            |      |
+----+-------------+-------+-------+-----------+----------+------+------------+------+
```

[[Back]](./README.md)