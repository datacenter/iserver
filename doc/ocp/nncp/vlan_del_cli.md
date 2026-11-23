## Inteface VLAN 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Delete VLAN | See below | [Link](./vlan_del_json.md) | [Link](./vlan_del_nncp.md) | [Link](./vlan_del_outcome.md)

```
# iserver create k8s nncp 
Cluster: my-cluster (type: ocp)

Policy name (def: policy):

Select interface type
---------------------
- bond
- eth
- lb
- vlan
Value: vlan

Interface name: eno1

VLAN ID: 666

State
-----
- up [default]
- absent
Value: absent

Select target node
------------------
- my-node
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
- my-node

Check nns data
--------------
- my-node base interface found: eno1
- my-node vlan interface found: eno1.666

Generated CRDs
--------------

apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - name: eno1.666
      state: absent
      type: vlan
      vlan:
        base-iface: eno1
        id: 666


Continue [Y/N]? y

Create NNCP
-----------
- policy
Waiting for [1]: policy
NNCP deleted
```

[[Back]](./README.md)