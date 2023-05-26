# Node Interface - MACsec

## Filter by port id

```
# iserver get aci intf macsec --apic apic11 --node bl205-eu-spdc --id eth1/28

Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| Node                | Interface | Admin State | Oper State | Reason     | Session State   | Peers | Cepher Suite | Confid Offset | Ker Server Prio | Replay Window |
+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
| pod-1/bl205-eu-spdc | eth1/28   | disabled    | down       | admin-down | not-initialized | 0     | 0            | 0             | 16              | 64            | 
+---------------------+-----------+-------------+------------+------------+-----------------+-------+--------------+---------------+-----------------+---------------+
```

[[Back]](./InterfaceMacSec.md)