# Node Protocol - CDP

## Show CDP interface counters for all nodes

```
# iserver get aci proto cdp --apic apic11 --node any --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors                    | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/bl205-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 62220   | 62210       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 62213   | 62220       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 62214   | 62211       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 62219   | 62221       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 62228   | 62234       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 62228   | 62226       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 62229   | 62226       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 62228   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 61670   | 61655       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 61661   | 61664       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 61655   | 61647       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 61670   | 61667       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 61671   | 61671       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 61670   | 61666       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 61671   | 61664       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 61671   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 62227   | 58912       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 61869   | 61860       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 62213   | 62206       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 62216   | 62207       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 62167   | 62108       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 62227   | 62227       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 62228   | 62223       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 61310   | 61296       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 61654   | 61642       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 61657   | 61643       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 61607   | 61544       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn22-eu-spdc                | 61668   | 61662       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 61668   | 61659       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 62235   | 62232       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 62225   | 62230       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 62226   | 62219       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 62234   | 62236       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 61677   | 61668       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 61676   | 61674       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 61676   | 61662       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 61676   | 61672       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s101-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 62230   | 62233       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s102-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 46522   | 46519       | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node any --view intf

{
    "duration": 8501,
    "apic": {
        "read": true,
        "success": 26,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 25,
        "connect_time": 387,
        "disconnect_time": 0,
        "mo_time": 7601,
        "total_time": 7988
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
    }
}

Log: apic
----------

True	387	-	connect apic11o.emea-sp.cisco.com
True	310	11	apic11o.emea-sp.cisco.com class fabricNode
True	280	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst
True	278	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-205/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	303	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	356	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst
True	308	8	apic11o.emea-sp.cisco.com mo topology/pod-1/node-206/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	299	29	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	289	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst
True	289	17	apic11o.emea-sp.cisco.com mo topology/pod-1/node-201/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	353	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	296	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst
True	297	15	apic11o.emea-sp.cisco.com mo topology/pod-1/node-202/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	328	100	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	341	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst
True	288	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-301/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	303	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	303	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst
True	294	4	apic11o.emea-sp.cisco.com mo topology/pod-1/node-302/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	329	43	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	307	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst
True	281	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-101/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	295	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
True	287	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst
True	299	1	apic11o.emea-sp.cisco.com mo topology/pod-1/node-102/sys/cdp/inst query query-target=subtree&target-subtree-class=cdpAdjEp
True	288	17	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)