# Cilium Operator

## Overview

[Cilium Operator](https://docs.cilium.io/en/stable/internals/cilium_operator/) performs cluster-wide operations such as
- CRD registration
- IP Address management e.g. cluster-scope IPAM or LB IPAM
- KVStore operations
- Garbage collection

High availability with multiple operator replicas deployed on different cluster nodes. Leader election mechanims selects single actively working operator.

```
$ oc logs -n cilium cilium-operator-5dcc9dbf6f-7pnmc
    time=2026-02-04T17:58:21.499106024Z 
    level=info 
    msg="Leader re-election complete" 
    module=enterprise-operator.operator 
    newLeader=bm3-1-wfkzn2jk9c 
    operatorID=bm3-1-wfkzn2jk9c
```

```
$ oc -n cilium get lease cilium-operator-resource-lock
NAME                            HOLDER             AGE
cilium-operator-resource-lock   bm1-1-wfkzn2jk9c   104d
```

## Life Cycle Management Commands

Command | Intent | Details
--- | --- | ---
iserver get ocp cilium operator -v pod | get cilium operator pods incl. leader flag | [Link](./get_operator_pod.md)
iserver get ocp cilium operator -v config | get operator configuration from cilium config | [Link](./get_operator_config.md)
iserver get ocp cilium operator -v logs | get cilium operator leader logs | [Link](./get_operator_logs.md)
iserver set ocp cilium restart --mode operator | restart cilium operators | [Link](./restart.md)

[[Back]](../Operations.md)