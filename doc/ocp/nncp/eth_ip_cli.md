## Interface Ethernet 

[[Back]](./README.md)

Intent | CLI | Task | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Configure IP address | See below | [Link](./eth_ip_json.md) | [Link](./eth_ip_nncp.md) | [Link](./eth_ip_outcome.md)

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
Value:

IPv4 (none, dhcp, cidrv4): 10.66.66.66/24

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
        address:
        - ip: 10.66.66.66
          prefix-length: 24
        dhcp: false
        enabled: true
      name: eno1
      state: up
      type: ethernet


Continue [Y/N]? y

Create NNCP
-----------
- policy
Waiting for [1]: policy
NNCP deleted
```

[[Back]](./README.md)