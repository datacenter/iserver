# CLI Web Terminal - Delete Operator

## Workflow

- delete dev workspace templates
- delete web terminal and dev workspace operators subscription
- delete deployment and service (that is not cleaned up automatically)
- wait until resources (deployments, replica sets, pods) are gone

## Requirements

None

## Configurable options

```
# iserver delete ocp cli-web --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp cli-web --cluster bm1

OpenShift Workflow - Web Terminal Operator - Delete Operator
============================================================

OpenShift Cluster: bm1

Delete workspace templates
--------------------------
- openshift-operators/web-terminal-tooling
- wait for no workspace template

Delete Subscription
-------------------
- subscription: openshift-operators/devworkspace-operator-fast-redhat-operators-openshift-marketplace
- already deleted

Delete Subscription
-------------------
- subscription: openshift-operators/devworkspace-operator
- checking cluster service version...
- csv found and will be deleted: openshift-operators/devworkspace-operator.v0.38.0
- wait for no subscription
- check cluster service version: openshift-operators/devworkspace-operator.v0.38.0
- wait for no csv

Delete Subscription
-------------------
- subscription: openshift-operators/web-terminal
- checking cluster service version...
- csv found and will be deleted: openshift-operators/web-terminal.v1.13.0
- wait for no subscription
- check cluster service version: openshift-operators/web-terminal.v1.13.0
- wait for no csv

Delete Deployment
-----------------
- namespace: openshift-operators
- name: devworkspace-webhook-server
- replica set: devworkspace-webhook-server-d77dbc9b9
- pod: devworkspace-webhook-server-d77dbc9b9-wmjj2
- pod: devworkspace-webhook-server-d77dbc9b9-zqlmc
- wait for no deployment
- wait for no pod: devworkspace-webhook-server-d77dbc9b9-wmjj2
- wait for no pod: devworkspace-webhook-server-d77dbc9b9-zqlmc
Wait for deployments deleted (optional: False)...
- openshift-operators/web-terminal-controller
- openshift-operators/devworkspace-controller-manager
- openshift-operators/devworkspace-webhook-server
Wait for pods deleted...

Delete Service
--------------
- namespace: openshift-operators
- name: devworkspace-webhookserver
- wait for no service

Completed tasks
- Dev workspace templates deleted
- Subscription and csv deleted
- Resource cleaned
```

[[Back]](./README.md)