# Node Protocol - LLDP

## Filter by mac address

```
# iserver get aci proto lldp --apic apic11 --role leaf --mac 3cfdfece --view nei

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

LLDP Adjacency [#29]
--------------------

+---------------------+--------+---------+--------------+-----------+-----------------+-------------------+------+------+-----------------------------------------------+--------------+
| Node                | Health | Faults  | Interface ID | Hold Time | Neighbor Device | MAC               | Port | VLAN | Port Description                              | Capabilities |
+---------------------+--------+---------+--------------+-----------+-----------------+-------------------+------+------+-----------------------------------------------+--------------+
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/1       | 121       |                 | 3c:fd:fe:ce:13:a8 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/2       | 121       |                 | 3c:fd:fe:ce:13:a9 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/3       | 121       |                 | 3c:fd:fe:ce:13:aa |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/7       | 121       |                 | 3c:fd:fe:ce:16:40 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/8       | 121       |                 | 3c:fd:fe:ce:16:41 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/9       | 121       |                 | 3c:fd:fe:ce:16:42 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/10      | 121       |                 | 3c:fd:fe:ce:1a:60 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/11      | 121       |                 | 3c:fd:fe:ce:1a:61 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/12      | 121       |                 | 3c:fd:fe:ce:1a:62 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/23      | 121       |                 | 3c:fd:fe:ce:0e:40 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/64      | 121       |                 | 3c:fd:fe:ce:c4:28 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/65      | 121       |                 | 3c:fd:fe:ce:c4:29 |      |      |                                               |              | 
| pod-1/cl201-eu-spdc | 100    | 0 0 0 0 | eth1/66      | 121       |                 | 3c:fd:fe:ce:c4:2a |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/1       | 121       |                 | 3c:fd:fe:ce:16:48 |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/2       | 121       |                 | 3c:fd:fe:ce:16:49 |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/3       | 121       |                 | 3c:fd:fe:ce:16:4a |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/7       | 121       |                 | 3c:fd:fe:ce:13:b8 |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/8       | 121       |                 | 3c:fd:fe:ce:13:b9 |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/9       | 121       |                 | 3c:fd:fe:ce:13:ba |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/13      | 121       |                 | 3c:fd:fe:ce:0e:68 |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/14      | 121       |                 | 3c:fd:fe:ce:0e:69 |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/15      | 121       |                 | 3c:fd:fe:ce:0e:6a |      |      |                                               |              | 
| pod-1/cl202-eu-spdc | 100    | 0 0 0 0 | eth1/23      | 121       |                 | 3c:fd:fe:ce:11:b8 |      |      |                                               |              | 
| pod-1/rl301-eu-spdc | 100    | 0 0 0 0 | eth1/25/1    | 180       | esx2-eu-spdc    | 3c:fd:fe:ce:11:43 |      |      | port 19 on dvSwitch EU-SPDC-R3DC (cswitch)    | bridge       | 
| pod-1/rl301-eu-spdc | 100    | 0 0 0 0 | eth1/25/2    | 180       | esx3-eu-spdc    | 3c:fd:fe:ce:19:f3 |      |      | port 1 on dvSwitch EU-SPDC-R3DC (cswitch)     | bridge       | 
| pod-1/rl301-eu-spdc | 100    | 0 0 0 0 | eth1/25/3    | 180       | esx4-eu-spdc    | 3c:fd:fe:ce:1b:13 |      |      | port 512 on dvSwitch EU-SPDC-CDC-22 (cswitch) | bridge       | 
| pod-1/rl302-eu-spdc | 100    | 0 0 0 0 | eth1/25/1    | 180       | esx2-eu-spdc    | 3c:fd:fe:ce:11:42 |      |      | port 18 on dvSwitch EU-SPDC-R3DC (cswitch)    | bridge       | 
| pod-1/rl302-eu-spdc | 100    | 0 0 0 0 | eth1/25/2    | 180       | esx3-eu-spdc    | 3c:fd:fe:ce:19:f2 |      |      | port 0 on dvSwitch EU-SPDC-R3DC (cswitch)     | bridge       | 
| pod-1/rl302-eu-spdc | 100    | 0 0 0 0 | eth1/25/3    | 180       | esx4-eu-spdc    | 3c:fd:fe:ce:1b:12 |      |      | port 513 on dvSwitch EU-SPDC-CDC-22 (cswitch) | bridge       | 
+---------------------+--------+---------+--------------+-----------+-----------------+-------------------+------+------+-----------------------------------------------+--------------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --role leaf --mac 3cfdfece --view nei

{
    "duration": 3320,
    "apic": {
        "read": true,
        "success": 10,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 9,
        "connect_time": 419,
        "disconnect_time": 0,
        "mo_time": 2650,
        "total_time": 3069
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

True	419	-	connect apic11o.emea-sp.cisco.com:443
True	293	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	293	13	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-205/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	286	10	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-206/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	324	44	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-201/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	301	44	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-202/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	296	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-209/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	281	1	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-210/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	294	21	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-301/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
True	282	21	apic11o.emea-sp.cisco.com:443 mo topology/pod-1/node-302/sys/lldp/inst query query-target=subtree&target-subtree-class=lldpAdjEp&rsp-subtree-include=health,fault-count
```

[[Back]](./ProtocolLldp.md)