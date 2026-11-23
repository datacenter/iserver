## Inteface Bond 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete bond | See below | [Link](./bond_del_json.md) | [Link](./bond_del_nncp.md) | [Link](./bond_del_outcome.md)

```
# iserver create k8s nncp 
Cluster: bm1 (type: ocp)

Policy name (def: policy):

Select interface type
---------------------
- bond
- eth
- lb
- vlan
Value: bond

Interface name: bond666

State
-----
- up [default]
- absent
Value: absent

Select target node
------------------
- ocp-bm1
- __workers__
- __all__ [default]
Value:

Delete policy once applied
--------------------------
- true
- false [default]
Value: true

Get nns data
------------
- ocp-bm1

Check nns data
--------------
- ocp-bm1 bond interface found: bond666

Generated CRDs
--------------

apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - name: bond666
      state: absent
      type: bond


Continue [Y/N]? y

Create NNCP
-----------
- policy
Waiting for [1]: policy
NNCP deleted
```

[[Back]](./README.md)