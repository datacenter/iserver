## Inteface Bond 

Intent | CLI | JSON | NNCP CRD | Outcome
--- | --- | --- | --- | ---
Add bond | See below | [Link](./bond_add_json.md) | [Link](./bond_add_nncp.md) | [Link](./bond_add_outcome.md)

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
Value:

Mode
----
- active-backup
- balance-xor
- 802.3ad
Value: active-backup

Bond members (comma separated): eno1,eno2

IPv4 (none, dhcp, cidrv4): 10.66.66.66/24

Miimon option: 140

Select target node
------------------
- ocp-bm1
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
- ocp-bm1

Check nns data
--------------
- ocp-bm1 bond interface not found: bond666
- ocp-bm1 ethernet interface found: eno1
- ocp-bm1 ethernet interface found: eno2

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
      link-aggregation:
        mode: active-backup
        options:
          miimon: '140'
        port:
        - eno1
        - eno2
      name: bond666
      state: up
      type: bond


Continue [Y/N]? y

Create NNCP
-----------
- policy
Waiting for [1]: policy
NNCP deleted
```

[[Back]](./README.md)