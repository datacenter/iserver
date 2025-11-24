# Intersight Hardware Discovery - Set via Task

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
- [imm](./set.md) triggers workflow execution with optional input parameter

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

Every cluster node CRD with extra annotation for
- management ip
- Intersight server identity

## Example

```
# iserver set ocp task --cluster bm1 --filename C:\tmp\task.json --no-confirm

OpenShift Workflow - Create Tasks
=================================

Validate Input
--------------
Completed

OpenShift Workflow - Intersight Hardware - Discovery
====================================================

OpenShift Cluster: bm1
NMState ready

Cluster node physical interfaces

+-------+------------+-------+------+-------------------+
| Node  | Interface  | State | MTU  | MAC               |
+-------+------------+-------+------+-------------------+
| bm1-1 | eno1       | ✗     | 1500 | AA:AA:AA:AA:AA:10 | 
+-------+------------+-------+------+-------------------+
| bm1-1 | eno2       | ✗     | 1500 | AA:AA:AA:AA:AA:11 | 
+-------+------------+-------+------+-------------------+
| bm1-2 | eno1       | ✗     | 1500 | AA:AA:AA:AA:AA:20 | 
+-------+------------+-------+------+-------------------+
| bm1-2 | eno2       | ✗     | 1500 | AA:AA:AA:AA:AA:21 | 
+-------+------------+-------+------+-------------------+
| bm1-3 | eno1       | ✗     | 1500 | AA:AA:AA:AA:AA:30 | 
+-------+------------+-------+------+-------------------+
| bm1-3 | eno2       | ✗     | 1500 | AA:AA:AA:AA:AA:31 | 
+-------+------------+-------+------+-------------------+

Collect Intersight servers information
--------------------------------------
Select servers...
Collect server api objects [666]...
Selected servers: 666

Derive Node to Server Mapping
-----------------------------
Node [bm1-1]
- Moid: aaaa1
- Name: comp1
- Model: UCSC-C220-M7SX
- Serial: AAAA1
- CIMC IP: 10.10.10.10
Node [bm1-2]
- Moid: aaaa2
- Name: comp2
- Model: UCSC-C220-M7SX
- Serial: AAAA2
- CIMC IP: 10.10.10.11
Node [bm1-3]
- Moid: aaaa3
- Name: comp3
- Model: UCSC-C220-M7SX
- Serial: AAAA3
- CIMC IP: 10.10.10.12

Set Kubernetes Annotation
-------------------------
- node [bm1-1] annotation key [intersight-hash] value [aaaa1]
- node [bm1-1] annotation key [server-imc] value [10.10.10.10]
- node [bm1-1] annotation key [server-name] value [comp1]
- node [bm1-1] annotation key [server-serial] value [AAAA1]
- node [bm1-1] annotation key [server-model] value [UCSC-C220-M7SX]
- node [bm1-2] annotation key [intersight-hash] value [aaaa2]
- node [bm1-2] annotation key [server-imc] value [10.10.10.11]
- node [bm1-2] annotation key [server-name] value [comp2]
- node [bm1-2] annotation key [server-serial] value [AAAA2]
- node [bm1-2] annotation key [server-model] value [UCSC-C220-M7SX]
- node [bm1-3] annotation key [intersight-hash] value [aaaa3]
- node [bm1-3] annotation key [server-imc] value [10.10.10.12]
- node [bm1-3] annotation key [server-name] value [comp3]
- node [bm1-3] annotation key [server-serial] value [AAAA3]
- node [bm1-3] annotation key [server-model] value [UCSC-C220-M7SX]
- node [bm1-3] annotation key [server-model] value [UCSC-C220-M7SX]
```

[[Back]](./README.md)