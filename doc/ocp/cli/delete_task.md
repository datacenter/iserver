# CLI Tools - Delete via Task

## Input

```
[
  {
    "cli": {
      "butane": {},
      "cilium": {},
      "helm": {},
      "hubble": {},
      "tridentctl": {
        "version": "26.02.0"
      },
      "virtctl": {},
      "file": {
        "namespace": "default",
        "filename": [
            "C:\\tmp\\to-apply"
        ]
      }
    }
  }
]
```

Notes:
- [butane](./delete_butane.md), [cilium](./delete_cilium.md), [helm](./delete_helm.md), [hubble](./delete_hubble.md), [tridentctl](./delete_tridentctl.md) and [virtctl](./delete_virtctl.md) trigger workflow execution with optional input parameters
- [file](./unapply_file.md) unapplies crds from files

## Requirements

None

## Configurable options

```
# iserver set ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

CLI tool uninstalled

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - CLI - Delete butane
========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/butane
Ssh cmd: sudo rm -f /usr/local/bin/butane

Completed tasks
- butane deleted

OpenShift Workflow - CLI - Delete cilium
========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/cilium
Ssh cmd: sudo rm -f /usr/local/bin/cilium

Completed tasks
- cilium deleted

OpenShift Workflow - CLI - Delete helm
======================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/helm
Ssh cmd: sudo rm -f /usr/local/bin/helm

Completed tasks
- helm deleted

OpenShift Workflow - CLI - Delete hubble
========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/hubble
Ssh cmd: sudo rm -f /usr/local/bin/hubble

Completed tasks
- hubble deleted

OpenShift Workflow - CLI - Delete tridentctl
============================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/tridentctl
Ssh cmd: sudo rm -f /usr/local/bin/tridentctl

Completed tasks
- tridentctl deleted

OpenShift Workflow - CLI - Delete virtctl
=========================================

OpenShift Cluster: bm1
Delete file: /usr/local/bin/virtctl
Ssh cmd: sudo rm -f /usr/local/bin/virtctl

Completed tasks
- virtctl deleted

+----+---------+-------+-------------------+---------+---------+--------------+
| ID | Target  | Scope | Workflow          | Changes | Success | Duration [s] |
+----+---------+-------+-------------------+---------+---------+--------------+
| 1  | ocp:bm1 | cli   | delete butane     | 0       | V       | 2            | 
| 2  | ocp:bm1 | cli   | delete cilium     | 0       | V       | 3            | 
| 3  | ocp:bm1 | cli   | delete helm       | 0       | V       | 3            | 
| 4  | ocp:bm1 | cli   | delete hubble     | 0       | V       | 4            | 
| 5  | ocp:bm1 | cli   | delete tridentctl | 0       | V       | 3            | 
| 6  | ocp:bm1 | cli   | delete virtctl    | 0       | V       | 3            | 
+----+---------+-------+-------------------+---------+---------+--------------+
```

[[Back]](./README.md)