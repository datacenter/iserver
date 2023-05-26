# Node Protocol - BGP

## Show BGP state summary for all nodes

```
# iserver get aci proto bgp --apic apic11 --node any -o node

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

+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| Node                | Admin State | ASN   | VRF (Up/Count) | Neighbors (Up/Count) | AS Path Entries | Attribute Entries | Memory Status | SNMP Trap | Syslog Level |
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
| pod-1/bl205-eu-spdc | enabled     | 50000 | 27/27          | 25/26                | 27              | 336               | normal        | disable   | err          | 
| pod-1/bl206-eu-spdc | enabled     | 50000 | 26/26          | 25/26                | 27              | 336               | normal        | disable   | err          | 
| pod-1/cl201-eu-spdc | enabled     | 50000 | 30/30          | 9/33                 | 23              | 333               | normal        | disable   | err          | 
| pod-1/cl202-eu-spdc | enabled     | 50000 | 30/30          | 8/33                 | 23              | 334               | normal        | disable   | err          | 
| pod-1/rl301-eu-spdc | enabled     | 50000 | 18/18          | 7/7                  | 25              | 274               | normal        | disable   | err          | 
| pod-1/rl302-eu-spdc | enabled     | 50000 | 18/18          | 7/7                  | 25              | 276               | normal        | disable   | err          | 
| pod-1/s101-eu-spdc  | enabled     | 50000 | 3/3            | 8/8                  | 30              | 117               | normal        | disable   | err          | 
| pod-1/s102-eu-spdc  | enabled     | 50000 | 3/3            | 8/8                  | 30              | 117               | normal        | disable   | err          | 
+---------------------+-------------+-------+----------------+----------------------+-----------------+-------------------+---------------+-----------+--------------+
```

[[Back]](./ProtocolBgp.md)