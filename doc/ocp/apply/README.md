# Apply CRDs from YAML file

## Workflow

Read files
- read files defined in --location parameters (multiple allowed)
- if location is file name, file must have YAML content
- if location is directory name, then all candidate files within the directory are checke for YAML content to be selected
- subdirectories are not checked recursively

For every candidate file
- ask for user's confirmation unless --no-confirm
- upload the file to cluster's management host
- run 'oc apply -f' command with optional namespace parameter
- break on command failure

## Configurable options

```
# iserver set ocp file
  --cluster TEXT   Cluster Name
  --namespace TEXT  Namespace name
  --location TEXT  YAML crds location
  --no-confirm     Confirmation mode
```

## Requirements

YAML files provided by the user in --location parameter are
- uploaded to aka management node of the cluster
- each file is applied using 'oc' command

As such it is required to one-time prepare [management server](../ManagementServer.md) for such workflow.

## Example

```
# iserver set ocp file --cluster bm1 --namespace default --location C:\tmp\to-apply\

OpenShift Workflow - Apply CRDs from file
=========================================

OpenShift Cluster: bm1

File: C:\tmp\to-apply\to-apply.yaml
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
Continue [Y/N]? y

Upload yaml file to /tmp/1e2353f50b5d.yaml...
oc apply -n default -f /tmp/1e2353f50b5d.yaml

~~~
service/test-apply created

~~~
```

## Task way

Task file

```
[
    {
        "cli": {
           "file": {
                "namespace": "default",
                "location": [
                    "C:\\tmp\\to-apply"
                ]
           }
        }
    }
]
```

Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task_apply.json --no-confirm
Cluster: bm1 (type: ocp)

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - CLI Tools Installation
===========================================

Workflow Parameters
-------------------
{
    "file": {
        "namespace": "default",
        "location": [
            "C:\\tmp\\to-apply"
        ],
        "cluster": "bm1",
        "confirmation": false,
        "verbose": false,
        "check-verbose": false
    },
    "cluster": "bm1",
    "exec": [],
    "check-verbose": true
}


OpenShift Cluster
-----------------
- cluster: bm1 [domain:milan]
- api [C:\Users\user\.itool\ocp-clusters\bm1\kubeconfig]: ok
- dns resolution: ok


OpenShift Workflow - Apply CRDs from file
=========================================

OpenShift Cluster: bm1

File: C:\tmp\to-apply\to-apply.yaml
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

Upload yaml file to /tmp/f6ecd407e586.yaml...
oc apply -n default -f /tmp/f6ecd407e586.yaml

~~~
service/test-apply created

~~~
```

[[Back]](../Operations.md)