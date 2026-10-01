# Tetragon Operator - Create via Task

## HowTo

```
[
    {
        "tetragon": {
            "operator": {
                "image": "image-name-as-provided-by-isovalent"
            },
            "crd": {
                "filename": [
                    "policy/policy.yaml"
                ]
            },
            "wipe": {}
        }
    }
]
```

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm
```

Notes:
- [operator](./create_operator.md), [crd](./create_crd.md) trigger workflow execution with optional input parameters
- [wipe](./delete_wipe.md) is ignored in create task

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Tetragon - Create Operator
===============================================

OpenShift Cluster: bm1

Create Namespace
----------------
- name: tetragon

~~~
apiVersion: v1
kind: Namespace
metadata:
  labels:
    openshift.io/user-monitoring: 'true'
  name: tetragon
~~~
Namespace [tetragon] created
Wait for namespace [timeout:60]...

Check labels
- openshift.io/user-monitoring:true found

Create CatalogSource
--------------------
- namespace: tetragon
- name: tetragon-catalog

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: CatalogSource
metadata:
  name: tetragon-catalog
  namespace: tetragon
spec:
  ...
~~~
CatalogSource [tetragon/tetragon-catalog] created
- wait for CatalogSource tetragon/tetragon-catalog [timeout:60s]

Wait for tetragon package...
Tetragon package found

Create OperatorGroup
--------------------
- namespace: tetragon
- name: tetragon

~~~
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: tetragon
  namespace: tetragon
spec:
  upgradeStrategy: Default
~~~
OperatorGroup [tetragon/tetragon] created
- wait for OperatorGroup tetragon/tetragon [timeout:60s]

Create Subscription
-------------------
Subscription: tetragon/tetragon-operator
Source: tetragon/tetragon-catalog/tetragon-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...
Resolving channel name...
Channel: v1.18
- CSV [tetragon-operator.v1.18.2]
- CSV Display name [Tetragon Operator]
- CVS Version [1.18.2]
- CSV Provider [{'name': 'Isovalent', 'url': 'https://isovalent.com'}]
- CSV Maturity [alpha]

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/tetragon-operator.tetragon: ''
  name: tetragon-operator
  namespace: tetragon
spec:
  channel: v1.18
  installPlanApproval: Automatic
  name: tetragon-operator
  source: tetragon-catalog
  sourceNamespace: tetragon
~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-jk5j4
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment tetragon/tetragon-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for daemonset tetragon/tetragon ready (optional: False, timeout: 600s)...
Subscription tetragon ready

Completed tasks
- Namespace created
- Operator Group created
- Tetragon Operator installed

OpenShift Workflow - Tetragon - Create Policy
=============================================

OpenShift Cluster: bm1
File: policy/policy.yaml

Create TracingPolicy
--------------------
- name: upper-layers

~~~
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: upper-layers
spec:
  parser:
    burstExitGen:
      enable: true
      interval: 1000
    dns:
      enable: true
    http:
      enable: true
      http2: true
      selectors:
      - matchPorts:
        - 8080
        - 80
    icmp:
      enable: true
    interface:
      enable: true
      packet: true
    tcp:
      enable: true
      histogram:
        enable: true
        max: 50000
        min: 0
      statsInterval: 20
    udp:
      cgroup: true
      enable: true
      statsInterval: 20
~~~
TracingPolicy [upper-layers] created
- wait for TracingPolicy upper-layers [timeout:60s]

Completed tasks
- CRDs applied

+----+---------+----------+-----------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow        | Changes | Success | Duration [s] |
+----+---------+----------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | create operator | 4       | V       | 65           | 
| 2  | ocp:bm1 | tetragon | create crd      | 1       | V       | 1            | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)