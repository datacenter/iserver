# Apply CRDs from YAML file

## Workflow

Read files
- read files defined in --filename parameters (multiple allowed)
- if filename is file name, file must have YAML content
- if filename is directory name, then all candidate files within the directory are checke for YAML content to be selected
- subdirectories are not checked recursively

For every candidate file
- ask for user's confirmation unless --no-confirm
- upload the file to cluster's management host
- run 'oc apply -f' command with optional namespace parameter
- break on command failure

## Configurable options

```
# iserver set ocp file
  --cluster TEXT    Cluster Name
  --namespace TEXT  Namespace name
  --filename TEXT   YAML crds filename
  --no-confirm      Confirmation mode
```

## Requirements

YAML files provided by the user in --filename parameter are
- uploaded to aka management node of the cluster
- each file is applied using 'oc' command

As such it is required to one-time prepare [management server](../ManagementServer.md) for such workflow.

## Example

```
# iserver set ocp file --cluster bm1 --namespace default --filename C:\tmp\to-apply\

OpenShift Workflow - Apply CRDs from file
=========================================

OpenShift Cluster: bm1

Checking filename [.\tasks\cli\crd.yaml]...

File: .\tasks\cli\crd.yaml
~~~
apiVersion: v1
kind: Service
metadata:
  name: test-apply
spec:
  ports:
    - port: 22
      protocol: TCP
  selector:
    kubevirt.io/domain: aaa
  type: NodePort
~~~

Upload yaml file to /tmp/9bc3bc2fb1fc.yaml...
oc apply -f /tmp/9bc3bc2fb1fc.yaml

~~~
service/test-apply created
~~~

+----+---------+-------+-------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow    | Changes | Success | Duration [s] |
+----+---------+-------+-------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | create file | 0       | V       | 6            | 
+----+---------+-------+-------------+---------+---------+--------------+
```

[[Back]](../Operations.md)