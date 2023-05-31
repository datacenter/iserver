# Policy - L2

## Verbose output

```
# iserver get aci policy l2 --apic apic11 --name default --view verbose

Apic: apic11

CDP Policy Properties
---------------------
- Policy Name  : default
- TF           : False
- QinQ         : disabled
- 802.1Qbg     : disabled
- VLAN Scope   : Global scope
- Interfaces   : 177
- Ref Policies : 2


+---------------------+-----------+
| Node                | Interface |
+---------------------+-----------+
| pod-1/cl201-eu-spdc | eth1/100  | 
| pod-1/cl201-eu-spdc | eth1/101  | 
| pod-1/cl201-eu-spdc | eth1/102  | 
| pod-1/cl201-eu-spdc | eth1/16   | 
| pod-1/cl201-eu-spdc | eth1/17   | 
| pod-1/cl201-eu-spdc | eth1/18   | 
| pod-1/cl201-eu-spdc | eth1/19   | 
| pod-1/cl201-eu-spdc | eth1/20   | 
| pod-1/cl201-eu-spdc | eth1/21   | 
| pod-1/cl201-eu-spdc | eth1/22   | 
| pod-1/cl201-eu-spdc | eth1/25   | 
| pod-1/cl201-eu-spdc | eth1/26   | 
| pod-1/cl201-eu-spdc | eth1/28   | 
| pod-1/cl201-eu-spdc | eth1/29   | 
| pod-1/cl201-eu-spdc | eth1/30   | 
| pod-1/cl201-eu-spdc | eth1/31   | 
| pod-1/cl201-eu-spdc | eth1/32   | 
| pod-1/cl201-eu-spdc | eth1/48   | 
| pod-1/cl201-eu-spdc | eth1/67   | 
| pod-1/cl201-eu-spdc | eth1/69   | 
| pod-1/cl201-eu-spdc | eth1/70   | 
| pod-1/cl201-eu-spdc | eth1/73   | 
| pod-1/cl201-eu-spdc | eth1/74   | 
| pod-1/cl201-eu-spdc | eth1/75   | 
| pod-1/cl201-eu-spdc | eth1/76   | 
| pod-1/cl201-eu-spdc | eth1/77   | 
| pod-1/cl201-eu-spdc | eth1/78   | 
| pod-1/cl201-eu-spdc | eth1/79   | 
| pod-1/cl201-eu-spdc | eth1/80   | 
| pod-1/cl201-eu-spdc | eth1/85   | 
| pod-1/cl201-eu-spdc | eth1/86   | 
| pod-1/cl201-eu-spdc | eth1/87   | 
| pod-1/cl201-eu-spdc | eth1/88   | 
| pod-1/cl201-eu-spdc | eth1/89   | 
| pod-1/cl201-eu-spdc | eth1/90   | 
| pod-1/cl201-eu-spdc | eth1/91   | 
| pod-1/cl201-eu-spdc | eth1/92   | 
| pod-1/cl201-eu-spdc | eth1/93   | 
| pod-1/cl201-eu-spdc | eth1/94   | 
| pod-1/cl201-eu-spdc | eth1/95   | 
| pod-1/cl201-eu-spdc | eth1/97   | 
| pod-1/cl201-eu-spdc | eth1/98   | 
| pod-1/cl201-eu-spdc | eth1/99   | 
| pod-1/cl201-eu-spdc | po23      | 
| pod-1/cl202-eu-spdc | eth1/100  | 
| pod-1/cl202-eu-spdc | eth1/101  | 
| pod-1/cl202-eu-spdc | eth1/102  | 
| pod-1/cl202-eu-spdc | eth1/16   | 
| pod-1/cl202-eu-spdc | eth1/17   | 
| pod-1/cl202-eu-spdc | eth1/18   | 
| pod-1/cl202-eu-spdc | eth1/19   | 
| pod-1/cl202-eu-spdc | eth1/20   | 
| pod-1/cl202-eu-spdc | eth1/21   | 
| pod-1/cl202-eu-spdc | eth1/22   | 
| pod-1/cl202-eu-spdc | eth1/25   | 
| pod-1/cl202-eu-spdc | eth1/26   | 
| pod-1/cl202-eu-spdc | eth1/28   | 
| pod-1/cl202-eu-spdc | eth1/29   | 
| pod-1/cl202-eu-spdc | eth1/30   | 
| pod-1/cl202-eu-spdc | eth1/31   | 
| pod-1/cl202-eu-spdc | eth1/32   | 
| pod-1/cl202-eu-spdc | eth1/48   | 
| pod-1/cl202-eu-spdc | eth1/67   | 
| pod-1/cl202-eu-spdc | eth1/69   | 
| pod-1/cl202-eu-spdc | eth1/70   | 
| pod-1/cl202-eu-spdc | eth1/73   | 
| pod-1/cl202-eu-spdc | eth1/74   | 
| pod-1/cl202-eu-spdc | eth1/75   | 
| pod-1/cl202-eu-spdc | eth1/76   | 
| pod-1/cl202-eu-spdc | eth1/77   | 
| pod-1/cl202-eu-spdc | eth1/78   | 
| pod-1/cl202-eu-spdc | eth1/79   | 
| pod-1/cl202-eu-spdc | eth1/80   | 
| pod-1/cl202-eu-spdc | eth1/81   | 
| pod-1/cl202-eu-spdc | eth1/82   | 
| pod-1/cl202-eu-spdc | eth1/83   | 
| pod-1/cl202-eu-spdc | eth1/84   | 
| pod-1/cl202-eu-spdc | eth1/85   | 
| pod-1/cl202-eu-spdc | eth1/86   | 
| pod-1/cl202-eu-spdc | eth1/87   | 
| pod-1/cl202-eu-spdc | eth1/88   | 
| pod-1/cl202-eu-spdc | eth1/89   | 
| pod-1/cl202-eu-spdc | eth1/90   | 
| pod-1/cl202-eu-spdc | eth1/91   | 
| pod-1/cl202-eu-spdc | eth1/92   | 
| pod-1/cl202-eu-spdc | eth1/93   | 
| pod-1/cl202-eu-spdc | eth1/94   | 
| pod-1/cl202-eu-spdc | eth1/95   | 
| pod-1/cl202-eu-spdc | eth1/97   | 
| pod-1/cl202-eu-spdc | eth1/98   | 
| pod-1/cl202-eu-spdc | eth1/99   | 
| pod-1/cl202-eu-spdc | po13      | 
| pod-1/bl205-eu-spdc | eth1/10   | 
| pod-1/bl205-eu-spdc | eth1/13   | 
| pod-1/bl205-eu-spdc | eth1/14   | 
| pod-1/bl205-eu-spdc | eth1/20   | 
| pod-1/bl205-eu-spdc | eth1/21   | 
| pod-1/bl205-eu-spdc | eth1/22   | 
| pod-1/bl205-eu-spdc | eth1/23   | 
| pod-1/bl205-eu-spdc | eth1/25   | 
| pod-1/bl205-eu-spdc | eth1/26   | 
| pod-1/bl205-eu-spdc | eth1/3    | 
| pod-1/bl205-eu-spdc | eth1/4    | 
| pod-1/bl205-eu-spdc | eth1/5    | 
| pod-1/bl205-eu-spdc | eth1/6    | 
| pod-1/bl205-eu-spdc | eth1/7    | 
| pod-1/bl205-eu-spdc | eth1/8    | 
| pod-1/bl205-eu-spdc | eth1/9    | 
| pod-1/bl206-eu-spdc | eth1/10   | 
| pod-1/bl206-eu-spdc | eth1/13   | 
| pod-1/bl206-eu-spdc | eth1/14   | 
| pod-1/bl206-eu-spdc | eth1/15   | 
| pod-1/bl206-eu-spdc | eth1/16   | 
| pod-1/bl206-eu-spdc | eth1/17   | 
| pod-1/bl206-eu-spdc | eth1/18   | 
| pod-1/bl206-eu-spdc | eth1/19   | 
| pod-1/bl206-eu-spdc | eth1/20   | 
| pod-1/bl206-eu-spdc | eth1/21   | 
| pod-1/bl206-eu-spdc | eth1/22   | 
| pod-1/bl206-eu-spdc | eth1/23   | 
| pod-1/bl206-eu-spdc | eth1/25   | 
| pod-1/bl206-eu-spdc | eth1/26   | 
| pod-1/bl206-eu-spdc | eth1/3    | 
| pod-1/bl206-eu-spdc | eth1/4    | 
| pod-1/bl206-eu-spdc | eth1/5    | 
| pod-1/bl206-eu-spdc | eth1/6    | 
| pod-1/bl206-eu-spdc | eth1/7    | 
| pod-1/bl206-eu-spdc | eth1/8    | 
| pod-1/bl206-eu-spdc | eth1/9    | 
| pod-1/rl301-eu-spdc | eth1/1    | 
| pod-1/rl301-eu-spdc | eth1/10   | 
| pod-1/rl301-eu-spdc | eth1/11   | 
| pod-1/rl301-eu-spdc | eth1/12   | 
| pod-1/rl301-eu-spdc | eth1/13   | 
| pod-1/rl301-eu-spdc | eth1/14   | 
| pod-1/rl301-eu-spdc | eth1/15   | 
| pod-1/rl301-eu-spdc | eth1/16   | 
| pod-1/rl301-eu-spdc | eth1/17   | 
| pod-1/rl301-eu-spdc | eth1/18   | 
| pod-1/rl301-eu-spdc | eth1/19   | 
| pod-1/rl301-eu-spdc | eth1/2    | 
| pod-1/rl301-eu-spdc | eth1/20   | 
| pod-1/rl301-eu-spdc | eth1/21   | 
| pod-1/rl301-eu-spdc | eth1/22   | 
| pod-1/rl301-eu-spdc | eth1/23   | 
| pod-1/rl301-eu-spdc | eth1/24/3 | 
| pod-1/rl301-eu-spdc | eth1/24/4 | 
| pod-1/rl301-eu-spdc | eth1/30   | 
| pod-1/rl301-eu-spdc | eth1/5    | 
| pod-1/rl301-eu-spdc | eth1/6    | 
| pod-1/rl301-eu-spdc | eth1/7    | 
| pod-1/rl301-eu-spdc | eth1/8    | 
| pod-1/rl301-eu-spdc | eth1/9    | 
| pod-1/rl302-eu-spdc | eth1/1    | 
| pod-1/rl302-eu-spdc | eth1/10   | 
| pod-1/rl302-eu-spdc | eth1/11   | 
| pod-1/rl302-eu-spdc | eth1/12   | 
| pod-1/rl302-eu-spdc | eth1/13   | 
| pod-1/rl302-eu-spdc | eth1/14   | 
| pod-1/rl302-eu-spdc | eth1/15   | 
| pod-1/rl302-eu-spdc | eth1/16   | 
| pod-1/rl302-eu-spdc | eth1/17   | 
| pod-1/rl302-eu-spdc | eth1/18   | 
| pod-1/rl302-eu-spdc | eth1/19   | 
| pod-1/rl302-eu-spdc | eth1/2    | 
| pod-1/rl302-eu-spdc | eth1/20   | 
| pod-1/rl302-eu-spdc | eth1/21   | 
| pod-1/rl302-eu-spdc | eth1/22   | 
| pod-1/rl302-eu-spdc | eth1/23   | 
| pod-1/rl302-eu-spdc | eth1/24/3 | 
| pod-1/rl302-eu-spdc | eth1/24/4 | 
| pod-1/rl302-eu-spdc | eth1/30   | 
| pod-1/rl302-eu-spdc | eth1/5    | 
| pod-1/rl302-eu-spdc | eth1/6    | 
| pod-1/rl302-eu-spdc | eth1/7    | 
| pod-1/rl302-eu-spdc | eth1/8    | 
| pod-1/rl302-eu-spdc | eth1/9    | 
+---------------------+-----------+

+--------------------+------------------+-----------------+
| Policy Name        | Policy Type      | Policy Class    |
+--------------------+------------------+-----------------+
| NXOS_FABRIC_PolGrp | PC/VPC Interface | infraAccBndlGrp | 
| pod4a-MX_PolGrp    | PC/VPC Interface | infraAccBndlGrp | 
+--------------------+------------------+-----------------+
Context: phy
```

Developer

```
# iserver get aci policy l2 --apic apic11 --name default --view verbose

{
    "duration": 1659,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 392,
        "disconnect_time": 0,
        "mo_time": 1049,
        "total_time": 1441
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

True	392	-	connect apic11o.emea-sp.cisco.com
True	328	6	apic11o.emea-sp.cisco.com class l2IfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	427	414	apic11o.emea-sp.cisco.com class l1RsL2IfPolCons
True	294	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyL2.md)