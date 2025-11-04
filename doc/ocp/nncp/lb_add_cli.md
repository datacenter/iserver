## Linux Bridge 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add linux bridge | See below | [Link](./lb_add_json.md) | [Link](./lb_add_nncp.md) | [Link](./lb_add_outcome.md)

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
Value: lb

Linux bridge name: br666

State
-----
- up [default]
- absent
Value:

Spanning Tree Protocol
----------------------
- true [default]
- false
Value: false

Upstream interface: enp216s0f0

IPv4 (none, dhcp, cidrv4): 10.66.66.66/24

Select target node
------------------
- my-node
- _workers_
- _all_ [default]
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
- my-node linux bridge interface not found: br666
- my-node upstream interface found: enp216s0f0

Generated CRDs
--------------

apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: policy
spec:
  desiredState:
    interfaces:
    - bridge:
        options:
          stp:
            enabled: false
        port:
        - name: enp216s0f0
      ipv4:
        address:
        - ip: 10.66.66.66
          prefix-length: 24
        dhcp: false
        enabled: true
      name: br666
      state: up
      type: linux-bridge


Continue [Y/N]? y

Create NNCP
-----------
- policy
Waiting for [1]: policy
Status: Available
NNCP deleted
```

[[Back]](./README.md)