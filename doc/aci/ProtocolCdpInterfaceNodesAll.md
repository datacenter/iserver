# Node Protocol - CDP

## Show CDP interface counters for all nodes

```
# iserver get aci proto cdp --apic apic11 --node any --view intf

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
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors                    | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/bl205-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 2752    | 2753        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 2726    | 2720        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 2728    | 5438        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 2726    | 2721        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 2729    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 2755    | 2754        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 2726    | 2721        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 2726    | 2721        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 2729    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn22-eu-spdc                | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 2752    | 2753        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s101-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2753    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s102-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node any --view intf

{
    "duration": 12089,
    "apic": {
        "read": true,
        "success": 32,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 31,
        "connect_time": 454,
        "disconnect_time": 0,
        "mo_time": 10228,
        "total_time": 10682
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

True	454	-	connect apic11o.emea-sp.cisco.com
True	314	13	apic11o.emea-sp.cisco.com class fabricNode
True	302	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst
True	326	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	324	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst
True	310	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	328	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	301	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	346	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	407	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	366	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst
True	333	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	326	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	337	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst
True	302	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-209/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	323	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	315	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst
True	304	0	apic11o.emea-sp.cisco.com mo topology/pod-1/node-210/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	337	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	318	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	322	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	329	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	433	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	298	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	338	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	332	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst
True	338	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	339	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst
True	323	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	327	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)