# Tetragon - Create Operator

## Workflow

>[!NOTE]
>Check tetragon operator version at Isovalent registry directly or in the documentation

- create tetragon namespace 
- create catalog source with user-defined version
- create operator group
- create subscription 

## Requirements

None

## Configurable options

```
# iserver set ocp tetragon --mode operator
  --cluster TEXT            Cluster Name
  --channel TEXT            Operator channel  [default: __default__]
  --image TEXT              Tetragon Enterprise Operator image
  --no-confirm              Confirmation mode
```

## Expected outcome

![OperatorCreate](../images/tetragon/operator_create.png)

## Example

```
# iserver set ocp tetragon --cluster bm1 --mode operator --version 1.19.4 --no-confirm

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
Access token created
~~~
{
    "token_id": "aaa",
    "access_token": "bbb",
    "expires_in": 7776000,
    "scope": "applied-permissions/user",
    "token_type": "Bearer",
    "description": "iserver-test-token",
    "username": "userid"
}
~~~
CatalogSource secret data
~~~
{
    "auths": {
        "artifactory.devhub-cloud.cisco.com": {
            "username": "userid",
            "password": "bbb",
            "auth": "base64 endoced userid:bbb"
        }
    }
}
~~~

Create Secret
-------------
- namespace: tetragon
- name: isovalent-registry

~~~
apiVersion: v1
data:
  .dockerconfigjson: ...
kind: Secret
metadata:
  name: isovalent-registry
  namespace: tetragon
type: kubernetes.io/dockerconfigjson
~~~
Secret [tetragon/isovalent-registry] created
Wait for Secret tetragon/isovalent-registry [timeout:60s]

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
  image: artifactory.devhub-cloud.cisco.com/isovalent-iep-docker-local/tetragon-operator-index:v0.0.1
  secrets:
  - isovalent-registry
  sourceType: grpc
~~~
CatalogSource [tetragon/tetragon-catalog] created
Wait for CatalogSource tetragon/tetragon-catalog [timeout:60s]
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
Wait for OperatorGroup tetragon/tetragon [timeout:60s]

Create Subscription
-------------------
Subscription: tetragon/tetragon-operator
Source: tetragon/tetragon-catalog/tetragon-operator
Install plan approval: Automatic
Getting subscription and packege manifest information...

~~~
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  labels:
    operators.coreos.com/tetragon-operator.tetragon: ''
  name: tetragon-operator
  namespace: tetragon
spec:
  installPlanApproval: Automatic
  name: tetragon-operator
  source: tetragon-catalog
  sourceNamespace: tetragon
~~~

Subscription created

Wait for subscription install plan started [timeout:360]...
Install plan: install-vglpl
Wait for subscription install plan ready [timeout:600]...
Install plan succeeded
Wait for deployment tetragon/tetragon-operator ready (optional: False, allow zero replicas: False, timeout: 600s)...
Wait for daemonset tetragon/tetragon ready (optional: False, timeout: 600s)...
Subscription tetragon ready

Completed tasks
- Namespace created
- Operator Group created
- Tetragon Operator installed

+----+---------+----------+-----------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow        | Changes | Success | Duration [s] |
+----+---------+----------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | tetragon | create operator | 5       | ✓       | 76           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)