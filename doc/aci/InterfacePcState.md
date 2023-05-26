# Node Interface - Port Channel (PC)

## Filter by port channel state

```
# iserver get aci intf pc --apic apic11 --node any --state down

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

+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| Node                | Id   | Name                 | Admin | Switching | State | Reason                    | Oper Mode | VPC Domain | Active Links |
+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
| pod-1/cl201-eu-spdc | po12 | pod1a-NVBench_PolGrp | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po13 | pod4a-MX_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po24 | pod1a-MX_PolGrp      | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
| pod-1/cl202-eu-spdc | po25 | pod1a-NVBench_PolGrp | up    | enabled   | down  | port-channel-members-down | active    | 100        | 0            | 
+---------------------+------+----------------------+-------+-----------+-------+---------------------------+-----------+------------+--------------+
```

[[Back]](./InterfacePc.md)