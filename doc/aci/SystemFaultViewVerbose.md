# System Fault

## Verbose view

```
# iserver get aci system fault --apic apic21 --severity critical --view verbose

Apic: apic21 (mode:online, cache:off)

System Faults Details [#16]
---------------------------

+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| Severity | Domain | Type           | Code  | Cause                   | Object                                   | Description                                                                    |
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2202/sys/phys-[eth1/ | Port is down, reason being sfpAbsent(connected), used by EPG on node 2202 of   | 
|          |        |                |       |                         | 33]/phys/fault-F0532                     | fabric ACI2-EU-SPDC with hostname cl2202-eu-spdc                               | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2202/sys/aggr-[po2]/ | Port is down, reason being noOperMembers(connected), used by EPG on node 2202  | 
|          |        |                |       |                         | aggrif/fault-F0532                       | of fabric ACI2-EU-SPDC with hostname cl2202-eu-spdc                            | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2201/sys/phys-[eth1/ | Port is down, reason being sfpAbsent(connected), used by EPG on node 2201 of   | 
|          |        |                |       |                         | 33]/phys/fault-F0532                     | fabric ACI2-EU-SPDC with hostname cl2201-eu-spdc                               | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2201/sys/aggr-[po1]/ | Port is down, reason being noOperMembers(connected), used by EPG on node 2201  | 
|          |        |                |       |                         | aggrif/fault-F0532                       | of fabric ACI2-EU-SPDC with hostname cl2201-eu-spdc                            | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2207/sys/phys-[eth1/ | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|          |        |                |       |                         | 22]/phys/fault-F0532                     | 2207 of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                       | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2207/sys/aggr-[po1]/ | Port is down, reason being noOperMembers(connected), used by EPG on node 2207  | 
|          |        |                |       |                         | aggrif/fault-F0532                       | of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                            | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2207/sys/phys-[eth1/ | Port is down, reason being suspended(no LACP PDUs)(connected), used by EPG on  | 
|          |        |                |       |                         | 2/1]/phys/fault-F0532                    | node 2207 of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                  | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2207/sys/aggr-[po2]/ | Port is down, reason being noOperMembers(connected), used by EPG on node 2207  | 
|          |        |                |       |                         | aggrif/fault-F0532                       | of fabric ACI2-EU-SPDC with hostname cl2207-eu-spdc                            | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2208/sys/phys-[eth1/ | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|          |        |                |       |                         | 22]/phys/fault-F0532                     | 2208 of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                       | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2208/sys/aggr-[po1]/ | Port is down, reason being noOperMembers(connected), used by EPG on node 2208  | 
|          |        |                |       |                         | aggrif/fault-F0532                       | of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                            | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2208/sys/phys-[eth1/ | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|          |        |                |       |                         | 6/3]/phys/fault-F0532                    | 2208 of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                       | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2208/sys/phys-[eth1/ | Port is down, reason being suspended(no LACP PDUs)(connected), used by EPG on  | 
|          |        |                |       |                         | 2/1]/phys/fault-F0532                    | node 2208 of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                  | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2208/sys/aggr-[po6]/ | Port is down, reason being noOperMembers(connected), used by EPG on node 2208  | 
|          |        |                |       |                         | aggrif/fault-F0532                       | of fabric ACI2-EU-SPDC with hostname cl2208-eu-spdc                            | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2702/sys/phys-[eth1/ | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|          |        |                |       |                         | 1]/phys/fault-F0532                      | 2702 of fabric ACI2-EU-SPDC with hostname rl2702-eu-spdc                       | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2702/sys/phys-[eth1/ | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|          |        |                |       |                         | 19]/phys/fault-F0532                     | 2702 of fabric ACI2-EU-SPDC with hostname rl2702-eu-spdc                       | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
| critical | access | communications | F0532 | interface-physical-down | topology/pod-1/node-2701/sys/phys-[eth1/ | Port is down, reason being linkNotConnected(connected), used by EPG on node    | 
|          |        |                |       |                         | 1]/phys/fault-F0532                      | 2701 of fabric ACI2-EU-SPDC with hostname rl2701-eu-spdc                       | 
+----------+--------+----------------+-------+-------------------------+------------------------------------------+--------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci system fault --apic apic21 --severity critical --view verbose

{
    "duration": 1828,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 430,
        "disconnect_time": 0,
        "mo_time": 848,
        "total_time": 1278
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

True	430	-	connect apic21o.emea-sp.cisco.com:443
True	848	163	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)