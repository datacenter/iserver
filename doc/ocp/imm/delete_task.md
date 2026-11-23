# Intersight Hardware Discovery - Unset via Task

## Input

```
[
  {
    "imm": {
      "iaccount": "my-iaccount"
    }
  }
]
```

Notes:
- [imm](./delete.md) triggers workflow execution with optional input parameter

## Requirements

None

## Configurable options

```
# iserver delete ocp task 
  --cluster TEXT   Cluster Name
  --filename TEXT  Tasks filename
  --validate       Validate only
  --break          Break on error
  --no-confirm     Confirmation mode
```

## Expected outcome

No node annotation for intersight hardware

## Example

```
# iserver delete ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm


OpenShift Workflow - Delete Tasks
=================================

Validate Input
--------------
Completed


OpenShift Workflow - Intersight Hardware - Unconfigure
======================================================

OpenShift Cluster: bm1
Node [bm1-1]
- delete annotation: intersight-hash
- delete annotation: server-imc
- delete annotation: server-model
- delete annotation: server-name
- delete annotation: server-serial
Node [bm1-2]
- delete annotation: intersight-hash
- delete annotation: server-imc
- delete annotation: server-model
- delete annotation: server-name
- delete annotation: server-serial
Node [bm1-3]
- delete annotation: intersight-hash
- delete annotation: server-imc
- delete annotation: server-model
- delete annotation: server-name
- delete annotation: server-serial
```

[[Back]](./README.md)