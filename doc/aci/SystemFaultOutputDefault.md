# System Fault

## Default output

```
# iserver get aci system fault --apic apic21 --view summary

Apic: apic21 (mode:online, cache:off)

System Faults Summary [#31]
---------------------------

+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| Severity | Domain    | Type           | Code    | Count | Cause                            | Explanation                                                                                                                       |
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| critical | access    | communications | F0532   | 16    | interface-physical-down          | This fault occurs when a port is down and is in use for epg                                                                       | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | operational    | F0103   | 1     | port-down                        | This fault occurs when a physical interface on a controller is in the link-down state.                                            | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | external  | config         | F4222   | 1     | rum-ack-not-received             | F4222                                                                                                                             | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | communications | F1547   | 6     | packets-dropped                  | This fault occurs when a significant number of excess packets are detected by a configured and enabled Atomic Counter             | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | communications | F1545   | 4     | packets-dropped                  | This fault occurs when a significant number of packet drops are detected by a configured and enabled Atomic Counter               | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | communications | F1549   | 8     | packets-dropped                  | This fault occurs when a significant number of packet drops are detected by a configured and enabled Atomic Counter               | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | communications | F1551   | 8     | packets-dropped                  | This fault occurs when a significant number of excess packets are detected by a configured and enabled Atomic Counter             | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | operational    | F0111   | 3     | operational-issues               | This fault occurs when operational issues are detected on a LooseNode (Unmanaged switch)                                          | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | external  | operational    | F0132   | 1     | operational-issues               | This fault is raised when Remote or External disruptive operations on VMM Controller are detected.                                | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | external  | operational    | F2840   | 12    | remote-oper-issues               | This fault is raised when ACI controller failed to update the properties of a VMware hypervisor.                                  | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | config         | F610395 | 3     | fsm-failed                       | F610395                                                                                                                           | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | external  | operational    | F1313   | 3     | operational-issues               | This fault is raised when remote or external disruptive operations are performed on Host Physical NIC from within the Controller. | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | framework | operational    | F2547   | 1     | nodeid-not-in-pod                | This fault occurs when node-id to pod-id mapping is wrong.                                                                        | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | communications | F1296   | 6     | interface-vpc-down               | This fault occurs when vpc interface goes down while peer interface is also down.                                                 | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | access    | communications | F0475   | 2     | interface-tunnel-down            | This fault occurs when destination becomes unreachable.                                                                           | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | access    | config         | F0600   | 2     | interface-pcmbr-down             | This fault occurs when port has been suspended.                                                                                   | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | infra     | config         | F609423 | 1     | fsm-failed                       | None set.                                                                                                                         | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| major    | external  | communications | F3208   | 1     | connect-failed                   | This fault is raised when the APIC is unable to connect to the External Device. Recovery is in process.                           | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| minor    | tenant    | config         | F1298   | 2     | configuration-failed             | : This fault occurs when deliverying EPg policies to a node has failed                                                            | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| minor    | access    | communications | F0603   | 4     | interface-pcmbr-down             | This fault occurs when port becomes operationally individual.                                                                     | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| minor    | tenant    | config         | F0467   | 17    | configuration-failed             | This fault occurs when an End Point Group is incompletely or incorrectly configured.                                              | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| minor    | infra     | operational    | F1700   | 4     | protocol-ntp-sync-failed         | This fault occurs when a ntp configuration on a controller has problems                                                           | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| minor    | infra     | config         | F1295   | 2     | configuration-failed             | This fault is raised when a Date and Time Policy (datetime:Pol) fails to apply due to configuration issues.                       | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| minor    | infra     | config         | F0849   | 2     | configuration-failed             | This fault occurs when a infra selector (port selector, card selector, node selector etc.) is incorrectly configured.             | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | external  | config         | F3057   | 1     | network-settings-not-configured  | This fault is raised when APIC Controller product is not registered with Cisco Smart Software Manager (CSSM).                     | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | infra     | config         | F0882   | 1     | resolution-failed                | The object refers to an object that was not found.                                                                                | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | infra     | config         | F1665   | 1     | resolution-failed                | The object refers to an object that was not found.                                                                                | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | external  | operational    | F0299   | 56    | protocol-bgp-adjacency-down      | This fault occurs when the peer state is not established                                                                          | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | infra     | operational    | F3927   | 2     | protocol-ntp-duplicate-ip        | F3927                                                                                                                             | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | infra     | operational    | F112128 | 4     | threshold-crossed                | This fault is caused by 'ingress drop packets rate' statistical property crossing threshold level.                                | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
| warning  | infra     | operational    | F1699   | 2     | protocol-ntp-provisioning-failed | This fault occurs when a ntp configuration on a switch has problems                                                               | 
+----------+-----------+----------------+---------+-------+----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
```

Developer

```
# iserver get aci system fault --apic apic21 --view summary

{
    "duration": 1583,
    "apic": {
        "read": true,
        "success": 2,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 454,
        "disconnect_time": 0,
        "mo_time": 793,
        "total_time": 1247
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

True	454	-	connect apic21o.emea-sp.cisco.com:443
True	793	164	apic21o.emea-sp.cisco.com:443 class faultInst
```

[[Back]](./SystemFault.md)