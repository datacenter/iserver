# Node Interface - Physical

## Filter by QoS stats

Example: ports with data

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --qos data
    --view qos

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+-------+------+---------------+--------------+-----------+-------------+---------+--------------+-----------+-------------+---------+
| Node                 | Interface | Admin | Oper | Class         | Rx Admit [B] | Rx Admin  | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin  | Tx Drop [B] | Tx Drop |
+----------------------+-----------+-------+------+---------------+--------------+-----------+-------------+---------+--------------+-----------+-------------+---------+
| pod-1/bl2205-eu-spdc | eth1/1    | up    | up   | control-plane | 79236023     | 311220    | 0           | 0       | 96659796     | 311196    | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/2    | up    | up   | control-plane | 79234002     | 311211    | 0           | 0       | 96659796     | 311196    | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/11   | up    | up   | control-plane | 77993545     | 311223    | 0           | 0       | 96473072     | 311196    | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/12   | up    | up   | control-plane | 77988439     | 311209    | 0           | 0       | 96473200     | 311197    | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/19   | up    | up   | control-plane | 33707245     | 248750    | 0           | 0       | 418101812    | 5030047   | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/25   | up    | up   | control-plane | 347649443    | 3360094   | 0           | 0       | 196258271    | 633947    | 0           | 0       | 
|                      |           |       |      | level3        | 171749839057 | 351329037 | 0           | 0       | 9636238272   | 63613173  | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/27   | up    | up   | control-plane | 67095440     | 311206    | 0           | 0       | 95538974     | 311195    | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/35   | up    | up   | control-plane | 3320640710   | 24569282  | 0           | 0       | 7091479453   | 8164325   | 0           | 0       | 
|                      |           |       |      | level3        | 5879249500   | 33036166  | 0           | 0       | 108476194481 | 181564262 | 3033436     | 14675   | 
|                      |           |       |      | policy-plane  | 0            | 0         | 0           | 0       | 9653964821   | 23640021  | 0           | 0       | 
| pod-1/bl2205-eu-spdc | eth1/36   | up    | up   | control-plane | 56032214899  | 78861110  | 0           | 0       | 6194423381   | 17890954  | 0           | 0       | 
|                      |           |       |      | level3        | 8073326956   | 33235728  | 0           | 0       | 85326890785  | 175803082 | 642         | 9       | 
|                      |           |       |      | policy-plane  | 66930        | 549       | 0           | 0       | 4210052837   | 25146762  | 0           | 0       | 
+----------------------+-----------+-------+------+---------------+--------------+-----------+-------------+---------+--------------+-----------+-------------+---------+
Interface context: phy
```

Example: ports with drops

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --qos drops
    --view qos

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+-----------+-------------+---------+
| Node                 | Interface | Admin | Oper | Class  | Rx Admit [B] | Rx Admin | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin  | Tx Drop [B] | Tx Drop |
+----------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+-----------+-------------+---------+
| pod-1/bl2205-eu-spdc | eth1/35   | up    | up   | level3 | 5879303945   | 33036460 | 0           | 0       | 108476377537 | 181564691 | 3033436     | 14675   | 
| pod-1/bl2205-eu-spdc | eth1/36   | up    | up   | level3 | 8073385377   | 33236061 | 0           | 0       | 85327258470  | 175804368 | 642         | 9       | 
+----------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+-----------+-------------+---------+
Interface context: phy
```

Example: ports with transmit drops

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --qos drops-tx
    --view qos

Apic: apic21 (mode:online, cache:off)
Pod: 1
Node: bl2205-eu-spdc

+----------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+-----------+-------------+---------+
| Node                 | Interface | Admin | Oper | Class  | Rx Admit [B] | Rx Admin | Rx Drop [B] | Rx Drop | Tx Admit [B] | Tx Admin  | Tx Drop [B] | Tx Drop |
+----------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+-----------+-------------+---------+
| pod-1/bl2205-eu-spdc | eth1/35   | up    | up   | level3 | 5879310219   | 33036500 | 0           | 0       | 108476405649 | 181564804 | 3033436     | 14675   | 
| pod-1/bl2205-eu-spdc | eth1/36   | up    | up   | level3 | 8073393338   | 33236113 | 0           | 0       | 85327540529  | 175806005 | 642         | 9       | 
+----------------------+-----------+-------+------+--------+--------------+----------+-------------+---------+--------------+-----------+-------------+---------+
Interface context: phy
```

Developer

```
# iserver get aci intf phy
    --apic apic21
    --node bl2205-eu-spdc
    --qos data
    --view qos

{
    "duration": 2707,
    "apic": {
        "read": true,
        "success": 5,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 4,
        "connect_time": 413,
        "disconnect_time": 0,
        "mo_time": 1889,
        "total_time": 2302
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

True	413	-	connect apic21o.emea-sp.cisco.com:443
True	313	15	apic21o.emea-sp.cisco.com:443 class fabricNode
True	938	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/l1PhysIf query rsp-subtree=children&rsp-subtree-include=health,fault-count,required
True	290	36	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/ethpmPhysIf
True	348	324	apic21o.emea-sp.cisco.com:443 class topology/pod-1/node-2205/qosmIfClass
```

[[Back]](./InterfacePhy.md)