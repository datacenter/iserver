# CLI Web Terminal - Delete Operator

## Workflow

- delete dev workspaces
- delete dev workspace templates
- delete web terminal and dev workspace operators subscription
- delete deployment and service (that is not cleaned up automatically)
- wait until resources (deployments, replica sets, pods) are gone

## Requirements

None

## Configurable options

```
# iserver delete ocp terminal --mode operator
  --cluster TEXT                  Cluster Name
```

## Example

```
# iserver delete ocp terminal --cluster bm1

OpenShift Workflow - Web Terminal Operator - Delete Operator
============================================================

OpenShift Cluster: bm1

Delete workspace
----------------
- openshift-terminal/terminal-eed2wz
- wait for no workspace

Delete workspace templates
--------------------------
- openshift-operators/web-terminal-exec
- wait for no workspace template
- openshift-operators/web-terminal-tooling
- wait for no workspace template

Delete Subscription
-------------------
- subscription: openshift-operators/devworkspace-operator
- checking cluster service version...
- csv found and will be deleted: openshift-operators/devworkspace-operator.v0.40.1
- wait for no subscription
- check cluster service version: openshift-operators/devworkspace-operator.v0.40.1
- wait for no csv

Delete Subscription
-------------------
- subscription: openshift-operators/web-terminal
- checking cluster service version...
- csv found and will be deleted: openshift-operators/web-terminal.v1.16.0
- wait for no subscription
- check cluster service version: openshift-operators/web-terminal.v1.16.0
- wait for no csv

Delete Deployment
-----------------
- namespace: openshift-operators
- name: devworkspace-webhook-server
- replica set: devworkspace-webhook-server-79bdb5fd64
- pod: devworkspace-webhook-server-79bdb5fd64-76z6w
- pod: devworkspace-webhook-server-79bdb5fd64-dpkq6
- wait for no deployment
- wait for no replica set openshift-operators/devworkspace-webhook-server-79bdb5fd64
- wait for no pod: devworkspace-webhook-server-79bdb5fd64-76z6w
- wait for no pod: devworkspace-webhook-server-79bdb5fd64-dpkq6
- wait for no Deployment openshift-operators/web-terminal-controller [timeout:180s]
- wait for no Deployment openshift-operators/devworkspace-controller-manager [timeout:180s]
- wait for no Deployment openshift-operators/devworkspace-webhook-server [timeout:180s]
Wait for pods deleted...

Delete Service
--------------
- namespace: openshift-operators
- name: devworkspace-webhookserver
- wait for no service

Completed tasks
- Subscription deleted
- Operator Group deleted
- Namespace deleted

+----+---------+----------+-----------------+---------+---------+--------------+
| ID | Target  | Scope    | Workflow        | Changes | Success | Duration [s] |
+----+---------+----------+-----------------+---------+---------+--------------+
| 1  | ocp:bm1 | terminal | delete operator | 9       | V       | 12           | 
+----+---------+----------+-----------------+---------+---------+--------------+
```

[[Back]](./README.md)