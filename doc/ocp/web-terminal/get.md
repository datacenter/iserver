# CLI Web Terminal - Get Information

## Workflow

Check and show information about web terminal operator and terminals.

## Example

```
# iserver get ocp terminal --cluster bm1

OpenShift Workflow - Web Terminal Operator - Get Information
============================================================

OpenShift Cluster: bm1

Collecting state...


State
-----
- package   : openshift-marketplace/redhat-operators/web-terminal
- csv       : web-terminal.v1.16.0
- resources : V


+----+--------------------+-------+
| ID | Dev Workspace      | Ready |
+----+--------------------+-------+
| 1  | openshift-terminal | V     | 
|    | terminal-eed2wz    |       | 
+----+--------------------+-------+
```

[[Back]](./README.md)