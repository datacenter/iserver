# Node Protocol - ARP

## All view

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view all

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

Protocol ARP - Instance [#1]
----------------------------

+----------------------+-------------+--------+---------+
| Node                 | Admin State | Health | Faults  |
+----------------------+-------------+--------+---------+
| pod-1/bl2205-eu-spdc | enabled     | 100    | 0 0 0 0 | 
+----------------------+-------------+--------+---------+

Protocol ARP - Domain [#12]
---------------------------

+----------------------+-------------------------+--------+---------+-----------+
| Node                 | VRF                     | Health | Faults  | Adjacency |
+----------------------+-------------------------+--------+---------+-----------+
| pod-1/bl2205-eu-spdc | black-hole              | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | common:Infra_privIP_VRF | 100    | 0 0 0 0 | 1         | 
| pod-1/bl2205-eu-spdc | common:Infra_VRF        | 100    | 0 0 0 0 | 1         | 
| pod-1/bl2205-eu-spdc | Ericsson_PACO:PDN       | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | management              | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | mgmt:EU-SPDC-ERSPAN-VRF | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | mgmt:inb                | 100    | 0 0 0 0 | 1         | 
| pod-1/bl2205-eu-spdc | nidemo:streamz-vrf      | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | overlay-1               | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | SPN_IntraLab:SPN_VRF1   | 100    | 0 0 0 0 | 0         | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | 100    | 0 0 0 0 | 5         | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | 100    | 0 0 0 0 | 5         | 
+----------------------+-------------------------+--------+---------+-----------+

Protocol ARP - Adjacency [#13]
------------------------------

+----------------------+-------------------------+-------------------+----------------+------------+------------+---------------+-------------------------------+
| Node                 | VRF                     | MAC               | IP             | State      | Interface  | Phy Interface | Timestamp                     |
+----------------------+-------------------------+-------------------+----------------+------------+------------+---------------+-------------------------------+
| pod-1/bl2205-eu-spdc | common:Infra_privIP_VRF | 00:A3:8E:EB:B3:3F | 192.168.254.74 | normal     | eth1/25.17 | eth1/25       | 2023-08-02T14:28:36.062+02:00 | 
| pod-1/bl2205-eu-spdc | common:Infra_VRF        | 00:A3:8E:EB:B3:3F | 192.168.254.9  | normal     | eth1/25.18 | eth1/25       | 2023-08-02T14:28:37.342+02:00 | 
| pod-1/bl2205-eu-spdc | mgmt:inb                | 00:A3:8E:EB:B3:3F | 192.168.254.25 | normal     | eth1/25.19 | eth1/25       | 2023-08-02T14:28:36.112+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.1   | incomplete | vlan1      |               | 2023-08-02T14:34:17.954+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.2   | incomplete | vlan1      |               | 2023-08-02T14:34:17.955+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.3   | incomplete | vlan1      |               | 2023-08-02T14:34:17.956+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.4   | incomplete | vlan1      |               | 2023-08-02T14:34:17.957+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:ACC_VRF       | unspecified       | 192.168.23.5   | incomplete | vlan1      |               | 2023-08-02T14:34:17.959+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.1   | incomplete | vlan20     |               | 2023-08-02T14:34:17.948+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.2   | incomplete | vlan20     |               | 2023-08-02T14:34:17.949+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.3   | incomplete | vlan20     |               | 2023-08-02T14:34:17.950+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.4   | incomplete | vlan20     |               | 2023-08-02T14:34:17.951+02:00 | 
| pod-1/bl2205-eu-spdc | vEPC_demo:INT_VRF       | unspecified       | 192.168.24.5   | incomplete | vlan20     |               | 2023-08-02T14:34:17.953+02:00 | 
+----------------------+-------------------------+-------------------+----------------+------------+------------+---------------+-------------------------------+

Protocol ARP - Interface Adjacency Summary [#5]
-----------------------------------------------

+----------------------+------------+-----------+
| Node                 | Interface  | Adjacency |
+----------------------+------------+-----------+
| pod-1/bl2205-eu-spdc | eth1/25.17 | 1         | 
| pod-1/bl2205-eu-spdc | eth1/25.18 | 1         | 
| pod-1/bl2205-eu-spdc | eth1/25.19 | 1         | 
| pod-1/bl2205-eu-spdc | vlan1      | 5         | 
| pod-1/bl2205-eu-spdc | vlan20     | 5         | 
+----------------------+------------+-----------+

Protocol ARP - Faults [#0]
--------------------------
None

Protocol ARP - Fault Records last 10y [#0]
------------------------------------------
None

Protocol ARP - Event Logs last 10y [#2]
---------------------------------------

+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
| Node                 | Sev  | Code     | Cause              | Created Time                  | Description                       | Affected                              |
+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
| pod-1/bl2205-eu-spdc | Info | E4208089 | admin-state-change | 2023-06-12T09:51:01.479+02:00 | ARP instance is administratively  | topology/pod-1/node-2205/sys/arp/inst | 
|                      |      |          |                    |                               | Enabled                           |                                       | 
+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
| pod-1/bl2205-eu-spdc | Info | E4208089 | admin-state-change | 2023-06-18T09:37:07.519+02:00 | ARP instance is administratively  | topology/pod-1/node-2205/sys/arp/inst | 
|                      |      |          |                    |                               | Enabled                           |                                       | 
+----------------------+------+----------+--------------------+-------------------------------+-----------------------------------+---------------------------------------+
```

Developer

```
# iserver get aci proto arp
    --apic apic21
    --node bl2205-eu-spdc
    --when any
    --view all

{
    "duration": 2599,
    "apic": {
        "read": true,
        "success": 8,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 7,
        "connect_time": 383,
        "disconnect_time": 0,
        "mo_time": 2020,
        "total_time": 2403
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

True	383	-	connect apic21o.emea-sp.cisco.com:443
True	292	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	272	1	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query query-target=children&rsp-subtree-include=health,fault-count
True	318	12	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query rsp-subtree=children&rsp-subtree-include=health,fault-count
True	267	13	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/arpDom query query-target=subtree&target-subtree-class=arpAdjEp
True	283	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=faults,no-scoped,subtree
True	316	0	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=fault-records,no-scoped,subtree&order-by=faultRecord.created|desc&page=0&page-size=1000
True	272	2	apic21o.emea-sp.cisco.com:443 mo topology/pod-1/node-2205/sys/arp query rsp-subtree-include=event-logs,no-scoped,subtree&order-by=eventRecord.created|desc&page=0&page-size=1000
```

[[Back]](./ProtocolArp.md)