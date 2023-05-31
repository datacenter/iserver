# Policy - LLDP

## Interface specific output

```
# iserver get aci policy lldp --apic apic11 --name default --view intf

Apic: apic11

+-------------+---------------------+-----------+
| Policy Name | Node                | Interface |
+-------------+---------------------+-----------+
| default     |                     |           | 
| default     | pod-1/cl201-eu-spdc | eth1/1    | 
|             | pod-1/cl201-eu-spdc | eth1/10   | 
|             | pod-1/cl201-eu-spdc | eth1/100  | 
|             | pod-1/cl201-eu-spdc | eth1/101  | 
|             | pod-1/cl201-eu-spdc | eth1/102  | 
|             | pod-1/cl201-eu-spdc | eth1/11   | 
|             | pod-1/cl201-eu-spdc | eth1/12   | 
|             | pod-1/cl201-eu-spdc | eth1/13   | 
|             | pod-1/cl201-eu-spdc | eth1/14   | 
|             | pod-1/cl201-eu-spdc | eth1/15   | 
|             | pod-1/cl201-eu-spdc | eth1/16   | 
|             | pod-1/cl201-eu-spdc | eth1/17   | 
|             | pod-1/cl201-eu-spdc | eth1/18   | 
|             | pod-1/cl201-eu-spdc | eth1/19   | 
|             | pod-1/cl201-eu-spdc | eth1/2    | 
|             | pod-1/cl201-eu-spdc | eth1/20   | 
|             | pod-1/cl201-eu-spdc | eth1/21   | 
|             | pod-1/cl201-eu-spdc | eth1/22   | 
|             | pod-1/cl201-eu-spdc | eth1/23   | 
|             | pod-1/cl201-eu-spdc | eth1/25   | 
|             | pod-1/cl201-eu-spdc | eth1/26   | 
|             | pod-1/cl201-eu-spdc | eth1/27   | 
|             | pod-1/cl201-eu-spdc | eth1/28   | 
|             | pod-1/cl201-eu-spdc | eth1/29   | 
|             | pod-1/cl201-eu-spdc | eth1/3    | 
|             | pod-1/cl201-eu-spdc | eth1/30   | 
|             | pod-1/cl201-eu-spdc | eth1/31   | 
|             | pod-1/cl201-eu-spdc | eth1/32   | 
|             | pod-1/cl201-eu-spdc | eth1/4    | 
|             | pod-1/cl201-eu-spdc | eth1/48   | 
|             | pod-1/cl201-eu-spdc | eth1/49   | 
|             | pod-1/cl201-eu-spdc | eth1/5    | 
|             | pod-1/cl201-eu-spdc | eth1/50   | 
|             | pod-1/cl201-eu-spdc | eth1/51   | 
|             | pod-1/cl201-eu-spdc | eth1/52   | 
|             | pod-1/cl201-eu-spdc | eth1/53   | 
|             | pod-1/cl201-eu-spdc | eth1/54   | 
|             | pod-1/cl201-eu-spdc | eth1/55   | 
|             | pod-1/cl201-eu-spdc | eth1/56   | 
|             | pod-1/cl201-eu-spdc | eth1/57   | 
|             | pod-1/cl201-eu-spdc | eth1/58   | 
|             | pod-1/cl201-eu-spdc | eth1/59   | 
|             | pod-1/cl201-eu-spdc | eth1/6    | 
|             | pod-1/cl201-eu-spdc | eth1/60   | 
|             | pod-1/cl201-eu-spdc | eth1/61   | 
|             | pod-1/cl201-eu-spdc | eth1/62   | 
|             | pod-1/cl201-eu-spdc | eth1/63   | 
|             | pod-1/cl201-eu-spdc | eth1/64   | 
|             | pod-1/cl201-eu-spdc | eth1/65   | 
|             | pod-1/cl201-eu-spdc | eth1/66   | 
|             | pod-1/cl201-eu-spdc | eth1/69   | 
|             | pod-1/cl201-eu-spdc | eth1/7    | 
|             | pod-1/cl201-eu-spdc | eth1/70   | 
|             | pod-1/cl201-eu-spdc | eth1/73   | 
|             | pod-1/cl201-eu-spdc | eth1/74   | 
|             | pod-1/cl201-eu-spdc | eth1/75   | 
|             | pod-1/cl201-eu-spdc | eth1/76   | 
|             | pod-1/cl201-eu-spdc | eth1/77   | 
|             | pod-1/cl201-eu-spdc | eth1/78   | 
|             | pod-1/cl201-eu-spdc | eth1/79   | 
|             | pod-1/cl201-eu-spdc | eth1/8    | 
|             | pod-1/cl201-eu-spdc | eth1/80   | 
|             | pod-1/cl201-eu-spdc | eth1/85   | 
|             | pod-1/cl201-eu-spdc | eth1/86   | 
|             | pod-1/cl201-eu-spdc | eth1/87   | 
|             | pod-1/cl201-eu-spdc | eth1/88   | 
|             | pod-1/cl201-eu-spdc | eth1/89   | 
|             | pod-1/cl201-eu-spdc | eth1/9    | 
|             | pod-1/cl201-eu-spdc | eth1/90   | 
|             | pod-1/cl201-eu-spdc | eth1/94   | 
|             | pod-1/cl201-eu-spdc | eth1/95   | 
|             | pod-1/cl201-eu-spdc | eth1/97   | 
|             | pod-1/cl201-eu-spdc | eth1/98   | 
|             | pod-1/cl201-eu-spdc | eth1/99   | 
|             | pod-1/cl202-eu-spdc | eth1/1    | 
|             | pod-1/cl202-eu-spdc | eth1/10   | 
|             | pod-1/cl202-eu-spdc | eth1/100  | 
|             | pod-1/cl202-eu-spdc | eth1/101  | 
|             | pod-1/cl202-eu-spdc | eth1/102  | 
|             | pod-1/cl202-eu-spdc | eth1/11   | 
|             | pod-1/cl202-eu-spdc | eth1/12   | 
|             | pod-1/cl202-eu-spdc | eth1/13   | 
|             | pod-1/cl202-eu-spdc | eth1/14   | 
|             | pod-1/cl202-eu-spdc | eth1/15   | 
|             | pod-1/cl202-eu-spdc | eth1/16   | 
|             | pod-1/cl202-eu-spdc | eth1/17   | 
|             | pod-1/cl202-eu-spdc | eth1/18   | 
|             | pod-1/cl202-eu-spdc | eth1/19   | 
|             | pod-1/cl202-eu-spdc | eth1/2    | 
|             | pod-1/cl202-eu-spdc | eth1/20   | 
|             | pod-1/cl202-eu-spdc | eth1/21   | 
|             | pod-1/cl202-eu-spdc | eth1/22   | 
|             | pod-1/cl202-eu-spdc | eth1/23   | 
|             | pod-1/cl202-eu-spdc | eth1/25   | 
|             | pod-1/cl202-eu-spdc | eth1/26   | 
|             | pod-1/cl202-eu-spdc | eth1/27   | 
|             | pod-1/cl202-eu-spdc | eth1/28   | 
|             | pod-1/cl202-eu-spdc | eth1/29   | 
|             | pod-1/cl202-eu-spdc | eth1/3    | 
|             | pod-1/cl202-eu-spdc | eth1/30   | 
|             | pod-1/cl202-eu-spdc | eth1/31   | 
|             | pod-1/cl202-eu-spdc | eth1/32   | 
|             | pod-1/cl202-eu-spdc | eth1/4    | 
|             | pod-1/cl202-eu-spdc | eth1/48   | 
|             | pod-1/cl202-eu-spdc | eth1/49   | 
|             | pod-1/cl202-eu-spdc | eth1/5    | 
|             | pod-1/cl202-eu-spdc | eth1/50   | 
|             | pod-1/cl202-eu-spdc | eth1/51   | 
|             | pod-1/cl202-eu-spdc | eth1/52   | 
|             | pod-1/cl202-eu-spdc | eth1/53   | 
|             | pod-1/cl202-eu-spdc | eth1/54   | 
|             | pod-1/cl202-eu-spdc | eth1/55   | 
|             | pod-1/cl202-eu-spdc | eth1/56   | 
|             | pod-1/cl202-eu-spdc | eth1/57   | 
|             | pod-1/cl202-eu-spdc | eth1/58   | 
|             | pod-1/cl202-eu-spdc | eth1/59   | 
|             | pod-1/cl202-eu-spdc | eth1/6    | 
|             | pod-1/cl202-eu-spdc | eth1/60   | 
|             | pod-1/cl202-eu-spdc | eth1/61   | 
|             | pod-1/cl202-eu-spdc | eth1/62   | 
|             | pod-1/cl202-eu-spdc | eth1/63   | 
|             | pod-1/cl202-eu-spdc | eth1/64   | 
|             | pod-1/cl202-eu-spdc | eth1/65   | 
|             | pod-1/cl202-eu-spdc | eth1/66   | 
|             | pod-1/cl202-eu-spdc | eth1/69   | 
|             | pod-1/cl202-eu-spdc | eth1/7    | 
|             | pod-1/cl202-eu-spdc | eth1/70   | 
|             | pod-1/cl202-eu-spdc | eth1/73   | 
|             | pod-1/cl202-eu-spdc | eth1/74   | 
|             | pod-1/cl202-eu-spdc | eth1/75   | 
|             | pod-1/cl202-eu-spdc | eth1/76   | 
|             | pod-1/cl202-eu-spdc | eth1/77   | 
|             | pod-1/cl202-eu-spdc | eth1/78   | 
|             | pod-1/cl202-eu-spdc | eth1/79   | 
|             | pod-1/cl202-eu-spdc | eth1/8    | 
|             | pod-1/cl202-eu-spdc | eth1/80   | 
|             | pod-1/cl202-eu-spdc | eth1/81   | 
|             | pod-1/cl202-eu-spdc | eth1/82   | 
|             | pod-1/cl202-eu-spdc | eth1/83   | 
|             | pod-1/cl202-eu-spdc | eth1/84   | 
|             | pod-1/cl202-eu-spdc | eth1/85   | 
|             | pod-1/cl202-eu-spdc | eth1/86   | 
|             | pod-1/cl202-eu-spdc | eth1/87   | 
|             | pod-1/cl202-eu-spdc | eth1/88   | 
|             | pod-1/cl202-eu-spdc | eth1/89   | 
|             | pod-1/cl202-eu-spdc | eth1/9    | 
|             | pod-1/cl202-eu-spdc | eth1/90   | 
|             | pod-1/cl202-eu-spdc | eth1/94   | 
|             | pod-1/cl202-eu-spdc | eth1/95   | 
|             | pod-1/cl202-eu-spdc | eth1/97   | 
|             | pod-1/cl202-eu-spdc | eth1/98   | 
|             | pod-1/cl202-eu-spdc | eth1/99   | 
|             | pod-1/bl205-eu-spdc | eth1/10   | 
|             | pod-1/bl205-eu-spdc | eth1/13   | 
|             | pod-1/bl205-eu-spdc | eth1/14   | 
|             | pod-1/bl205-eu-spdc | eth1/20   | 
|             | pod-1/bl205-eu-spdc | eth1/21   | 
|             | pod-1/bl205-eu-spdc | eth1/22   | 
|             | pod-1/bl205-eu-spdc | eth1/23   | 
|             | pod-1/bl205-eu-spdc | eth1/25   | 
|             | pod-1/bl205-eu-spdc | eth1/26   | 
|             | pod-1/bl205-eu-spdc | eth1/3    | 
|             | pod-1/bl205-eu-spdc | eth1/4    | 
|             | pod-1/bl205-eu-spdc | eth1/5    | 
|             | pod-1/bl205-eu-spdc | eth1/6    | 
|             | pod-1/bl205-eu-spdc | eth1/7    | 
|             | pod-1/bl205-eu-spdc | eth1/8    | 
|             | pod-1/bl205-eu-spdc | eth1/9    | 
|             | pod-1/bl206-eu-spdc | eth1/10   | 
|             | pod-1/bl206-eu-spdc | eth1/13   | 
|             | pod-1/bl206-eu-spdc | eth1/14   | 
|             | pod-1/bl206-eu-spdc | eth1/15   | 
|             | pod-1/bl206-eu-spdc | eth1/16   | 
|             | pod-1/bl206-eu-spdc | eth1/17   | 
|             | pod-1/bl206-eu-spdc | eth1/18   | 
|             | pod-1/bl206-eu-spdc | eth1/19   | 
|             | pod-1/bl206-eu-spdc | eth1/20   | 
|             | pod-1/bl206-eu-spdc | eth1/21   | 
|             | pod-1/bl206-eu-spdc | eth1/22   | 
|             | pod-1/bl206-eu-spdc | eth1/23   | 
|             | pod-1/bl206-eu-spdc | eth1/25   | 
|             | pod-1/bl206-eu-spdc | eth1/26   | 
|             | pod-1/bl206-eu-spdc | eth1/3    | 
|             | pod-1/bl206-eu-spdc | eth1/4    | 
|             | pod-1/bl206-eu-spdc | eth1/5    | 
|             | pod-1/bl206-eu-spdc | eth1/6    | 
|             | pod-1/bl206-eu-spdc | eth1/7    | 
|             | pod-1/bl206-eu-spdc | eth1/8    | 
|             | pod-1/bl206-eu-spdc | eth1/9    | 
|             | pod-1/rl301-eu-spdc | eth1/1    | 
|             | pod-1/rl301-eu-spdc | eth1/10   | 
|             | pod-1/rl301-eu-spdc | eth1/11   | 
|             | pod-1/rl301-eu-spdc | eth1/12   | 
|             | pod-1/rl301-eu-spdc | eth1/13   | 
|             | pod-1/rl301-eu-spdc | eth1/14   | 
|             | pod-1/rl301-eu-spdc | eth1/15   | 
|             | pod-1/rl301-eu-spdc | eth1/16   | 
|             | pod-1/rl301-eu-spdc | eth1/17   | 
|             | pod-1/rl301-eu-spdc | eth1/18   | 
|             | pod-1/rl301-eu-spdc | eth1/19   | 
|             | pod-1/rl301-eu-spdc | eth1/2    | 
|             | pod-1/rl301-eu-spdc | eth1/20   | 
|             | pod-1/rl301-eu-spdc | eth1/21   | 
|             | pod-1/rl301-eu-spdc | eth1/22   | 
|             | pod-1/rl301-eu-spdc | eth1/23   | 
|             | pod-1/rl301-eu-spdc | eth1/24/3 | 
|             | pod-1/rl301-eu-spdc | eth1/24/4 | 
|             | pod-1/rl301-eu-spdc | eth1/30   | 
|             | pod-1/rl301-eu-spdc | eth1/5    | 
|             | pod-1/rl301-eu-spdc | eth1/6    | 
|             | pod-1/rl301-eu-spdc | eth1/7    | 
|             | pod-1/rl301-eu-spdc | eth1/8    | 
|             | pod-1/rl301-eu-spdc | eth1/9    | 
|             | pod-1/rl302-eu-spdc | eth1/1    | 
|             | pod-1/rl302-eu-spdc | eth1/10   | 
|             | pod-1/rl302-eu-spdc | eth1/11   | 
|             | pod-1/rl302-eu-spdc | eth1/12   | 
|             | pod-1/rl302-eu-spdc | eth1/13   | 
|             | pod-1/rl302-eu-spdc | eth1/14   | 
|             | pod-1/rl302-eu-spdc | eth1/15   | 
|             | pod-1/rl302-eu-spdc | eth1/16   | 
|             | pod-1/rl302-eu-spdc | eth1/17   | 
|             | pod-1/rl302-eu-spdc | eth1/18   | 
|             | pod-1/rl302-eu-spdc | eth1/19   | 
|             | pod-1/rl302-eu-spdc | eth1/2    | 
|             | pod-1/rl302-eu-spdc | eth1/20   | 
|             | pod-1/rl302-eu-spdc | eth1/21   | 
|             | pod-1/rl302-eu-spdc | eth1/22   | 
|             | pod-1/rl302-eu-spdc | eth1/23   | 
|             | pod-1/rl302-eu-spdc | eth1/24/3 | 
|             | pod-1/rl302-eu-spdc | eth1/24/4 | 
|             | pod-1/rl302-eu-spdc | eth1/30   | 
|             | pod-1/rl302-eu-spdc | eth1/5    | 
|             | pod-1/rl302-eu-spdc | eth1/6    | 
|             | pod-1/rl302-eu-spdc | eth1/7    | 
|             | pod-1/rl302-eu-spdc | eth1/8    | 
|             | pod-1/rl302-eu-spdc | eth1/9    | 
+-------------+---------------------+-----------+
Context: phy
```

Developer

```
# iserver get aci policy lldp --apic apic11 --name default --view intf

{
    "duration": 2096,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 373,
        "disconnect_time": 0,
        "mo_time": 1000,
        "total_time": 1373
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

True	373	-	connect apic11o.emea-sp.cisco.com
True	310	10	apic11o.emea-sp.cisco.com class lldpIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	401	338	apic11o.emea-sp.cisco.com class l1RsLldpIfPolCons
True	289	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLldp.md)