# Intersight Hardware Discovery - Unset

## Workflow

- get annotation for the nodes of the selected cluster
- if iaccount parameter is set, delete the annotations for the configured Intersight account
- otherwise delete all 'intersight hardware discovery' annotations

## Requirements

None

## Expected outcome

No node annotation for intersight hardware

## Example

```
# iserver delete ocp imm --cluster bm1

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