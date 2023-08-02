# Node Protocol - CDP

## Intf view

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view intf

Apic: apic11 (mode:online, cache:off)
Pod: 1
Node: cl201-eu-spdc

Protocol CDP - Interface Stats [#100]
-------------------------------------

+---------------------+--------------+-------------+------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/cl201-eu-spdc | eth1/1       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/10      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/100     | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/101     | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/102     | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/11      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/12      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/13      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/14      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/15      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/16      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/17      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/18      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/19      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/2       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/20      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/21      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/22      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/23      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/24      | enabled     | up         | 8131    | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/25      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/26      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/27      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/28      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/29      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/3       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/30      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/31      | enabled     | up         | 61964   | 61912       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/32      | enabled     | up         | 61963   | 61926       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/33      | enabled     | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 8125    | 8119        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 8127    | 8118        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 8126    | 16234       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 8126    | 8117        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 8126    | 8117        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 8126    | 8117        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/4       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 8126    | 8117        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 8125    | 8119        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 8127    | 8118        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 8127    | 8118        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 8127    | 8117        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 8126    | 8116        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 8126    | 8116        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 8127    | 8118        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/48      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/49      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/5       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/50      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/51      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/52      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/53      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/54      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/55      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/56      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/57      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/58      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/59      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/6       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/60      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/61      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/62      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/63      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/64      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/65      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/66      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/67      | enabled     | up         | 8130    | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/68      | enabled     | up         | 8127    | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/69      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/7       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/70      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/71      | enabled     | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/72      | enabled     | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/73      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/74      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/75      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/76      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/77      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/78      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/79      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/8       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/80      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/81      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/82      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/83      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/84      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/85      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/86      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/87      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/88      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/89      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/9       | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/90      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/94      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/95      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 8153    | 8152        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/97      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/98      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/99      | disabled    | down       | 0       | 0           | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 8151    | 8149        | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

Developer

```
# iserver get aci proto cdp --apic apic11 --node cl201-eu-spdc --view intf

{
    "duration": 1359,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 423,
        "disconnect_time": 0,
        "mo_time": 619,
        "total_time": 1042
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

True	423	-	connect apic11o.emea-sp.cisco.com:443
True	305	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	314	100	apic11o.emea-sp.cisco.com:443 class topology/pod-1/node-201/cdpIf query rsp-subtree=children&rsp-subtree-class=cdpIf,cdpIfStats&rsp-subtree-include=required
```

[[Back]](./ProtocolCdp.md)