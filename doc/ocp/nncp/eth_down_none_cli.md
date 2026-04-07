## Interface Ethernet 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Disable interface with no IP address | See below | [Link](./eth_down_none_json.md) | [Link](./eth_down_none_nncp.md) | [Link](./eth_down_none_outcome.md)

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
Value: eth

Interface name: eno1

State
-----
- up [default]
- down
Value: down

IPv4 (none, dhcp, cidrv4): none

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
- my-node ethernet interface found: eno1

Generated CRDs
--------------

apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - ipv4:
        enabled: false
      name: eno1
      state: down
      type: ethernet


Continue [Y/N]? y

Create NNCP
-----------
- policy
Waiting for [1]: policy
NNCP deleted
```

[[Back]](./README.md)