# Node Interface - Physical

## Fault view

```
# iserver get aci intf phy --apic apic21 --node any --view fault

Apic: apic21 (mode:online, cache:off)
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: cl2209-eu-spdc
- node: cl2210-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

Interface Phy - Faults [#14]
----------------------------

+----------------------+-----------+------+-------+-------------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| Node                 | Interface | Sev  | Code  | Cause                   | Created Time                  | Lifecycle | Description                                                                    |
+----------------------+-----------+------+-------+-------------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
| pod-1/rl2702-eu-spdc | eth1/1    | Crit | F0532 | interface-physical-down | 2023-06-18T09:14:55.503+02:00 | raised    | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|                      |           |      |       |                         |                               |           | 2702 of fabric ACI2-EU-SPDC with hostname rl2702-eu-spdc                       | 
| pod-1/rl2702-eu-spdc | eth1/19   | Crit | F0532 | interface-physical-down | 2023-06-18T09:14:55.572+02:00 | raised    | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|                      |           |      |       |                         |                               |           | 2702 of fabric ACI2-EU-SPDC with hostname rl2702-eu-spdc                       | 
| pod-1/cl2208-eu-spdc | eth1/2/1  | Crit | F0532 | interface-physical-down | 2023-06-18T09:16:15.767+02:00 | raised    | Port is down, reason being suspended(no LACP PDUs)(connected), used by EPG on  | 
|                      |           |      |       |                         |                               |           | node 2208 of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                  | 
| pod-1/cl2208-eu-spdc | eth1/6/3  | Crit | F0532 | interface-physical-down | 2023-06-18T09:16:15.836+02:00 | raised    | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|                      |           |      |       |                         |                               |           | 2208 of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                       | 
| pod-1/cl2208-eu-spdc | eth1/19   | Min  | F0603 | interface-pcmbr-down    | 2023-06-18T09:18:02.582+02:00 | raised    | Port is operationally individual.                                              | 
| pod-1/cl2208-eu-spdc | eth1/2/1  | Maj  | F0600 | interface-pcmbr-down    | 2023-06-18T09:18:06.110+02:00 | raised    | Port is suspended on node 2208 fabric hostname cl2208-eu-spdc.                 | 
| pod-1/cl2202-eu-spdc | eth1/33   | Crit | F0532 | interface-physical-down | 2023-06-18T09:18:20.725+02:00 | raised    | Port is down, reason being sfpAbsent(connected), used by EPG on node 2202 of   | 
|                      |           |      |       |                         |                               |           | fabric ACI2-EU-SPDC with hostname cl2202-eu-spdc                               | 
| pod-1/cl2202-eu-spdc | eth1/90   | Min  | F0603 | interface-pcmbr-down    | 2023-06-18T09:19:13.041+02:00 | raised    | Port is operationally individual.                                              | 
| pod-1/rl2701-eu-spdc | eth1/1    | Crit | F0532 | interface-physical-down | 2023-06-18T09:41:54.203+02:00 | raised    | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|                      |           |      |       |                         |                               |           | 2701 of fabric ACI2-EU-SPDC with hostname rl2701-eu-spdc                       | 
| pod-1/cl2207-eu-spdc | eth1/2/1  | Crit | F0532 | interface-physical-down | 2023-06-18T09:44:11.459+02:00 | raised    | Port is down, reason being suspended(no LACP PDUs)(connected), used by EPG on  | 
|                      |           |      |       |                         |                               |           | node 2207 of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                  | 
| pod-1/cl2201-eu-spdc | eth1/33   | Crit | F0532 | interface-physical-down | 2023-06-18T09:44:35.362+02:00 | raised    | Port is down, reason being sfpAbsent(connected), used by EPG on node 2201 of   | 
|                      |           |      |       |                         |                               |           | fabric ACI2-EU-SPDC with hostname cl2201-eu-spdc                               | 
| pod-1/cl2207-eu-spdc | eth1/19   | Min  | F0603 | interface-pcmbr-down    | 2023-06-18T09:45:09.539+02:00 | raised    | Port is operationally individual.                                              | 
| pod-1/cl2207-eu-spdc | eth1/2/1  | Maj  | F0600 | interface-pcmbr-down    | 2023-06-18T09:45:13.295+02:00 | raised    | Port is suspended on node 2207 fabric hostname cl2207-eu-spdc.                 | 
| pod-1/cl2201-eu-spdc | eth1/90   | Min  | F0603 | interface-pcmbr-down    | 2023-06-18T09:45:30.446+02:00 | raised    | Port is operationally individual.                                              | 
+----------------------+-----------+------+-------+-------------------------+-------------------------------+-----------+--------------------------------------------------------------------------------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy --apic apic21 --node any --view fault

{
    "duration": 32121,
    "apic": {
        "read": true,
        "success": 38,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 37,
        "connect_time": 425,
        "disconnect_time": 0,
        "mo_time": 28612,
        "total_time": 29037
    },
    "error": {
        "read": false,
        "lines": 0
    },
    "info": {
        "read": false,
        "lines": 0
    },
    "debug": {
        "read": false,
        "lines": 0
    },
    "cache_hits": 0
}

Log: apic
----------

True	425	-	connect apic21o.emea-sp.cisco.com:443
True	326	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	951	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	334	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	556	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	988	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	321	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/ethpmPhysIf
True	739	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2206/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1974	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	399	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/ethpmPhysIf
True	1186	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2201/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	2158	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	433	108	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/ethpmPhysIf
True	1079	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2202/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1279	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	340	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/ethpmPhysIf
True	842	3	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2207/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1180	60	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	398	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/ethpmPhysIf
True	690	4	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2208/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1053	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	343	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/ethpmPhysIf
True	420	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2209/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1219	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	370	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/ethpmPhysIf
True	449	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2210/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1628	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	354	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/ethpmPhysIf
True	822	1	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2701/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	1775	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	380	54	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/ethpmPhysIf
True	732	2	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2702/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	701	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	304	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/ethpmPhysIf
True	424	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2101/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
True	676	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	356	34	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/ethpmPhysIf
True	433	0	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2102/l1PhysIf query rsp-subtree-include=faults,no-scoped,subtree
```

[[Back]](./InterfacePhy.md)