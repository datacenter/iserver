# Policy - Link Level

## Verbose output

```
# iserver get aci policy link --apic apic11 --name default --view verbose

Apic: apic11

Link Level Policy Properties
----------------------------
- Policy Name          : default
- TF                   : False
- PHY Type             : auto
- Auto Neg             : on
- Speed                : inherit
- Delay [msec]         : 0
- Link Debounce [msec] : 100
- FEC Mode             : inherit
- EMI Retrain          : disable
- Interfaces           : 339
- Ref Policies         : 54


+---------------------+-----------+
| Node                | Interface |
+---------------------+-----------+
| pod-1/cl201-eu-spdc | eth1/1    | 
| pod-1/cl201-eu-spdc | eth1/10   | 
| pod-1/cl201-eu-spdc | eth1/100  | 
| pod-1/cl201-eu-spdc | eth1/101  | 
| pod-1/cl201-eu-spdc | eth1/102  | 
| pod-1/cl201-eu-spdc | eth1/11   | 
| pod-1/cl201-eu-spdc | eth1/13   | 
| pod-1/cl201-eu-spdc | eth1/14   | 
| pod-1/cl201-eu-spdc | eth1/16   | 
| pod-1/cl201-eu-spdc | eth1/17   | 
| pod-1/cl201-eu-spdc | eth1/18   | 
| pod-1/cl201-eu-spdc | eth1/19   | 
| pod-1/cl201-eu-spdc | eth1/2    | 
| pod-1/cl201-eu-spdc | eth1/20   | 
| pod-1/cl201-eu-spdc | eth1/21   | 
| pod-1/cl201-eu-spdc | eth1/22   | 
| pod-1/cl201-eu-spdc | eth1/23   | 
| pod-1/cl201-eu-spdc | eth1/25   | 
| pod-1/cl201-eu-spdc | eth1/26   | 
| pod-1/cl201-eu-spdc | eth1/27   | 
| pod-1/cl201-eu-spdc | eth1/28   | 
| pod-1/cl201-eu-spdc | eth1/29   | 
| pod-1/cl201-eu-spdc | eth1/30   | 
| pod-1/cl201-eu-spdc | eth1/31   | 
| pod-1/cl201-eu-spdc | eth1/32   | 
| pod-1/cl201-eu-spdc | eth1/33   | 
| pod-1/cl201-eu-spdc | eth1/34   | 
| pod-1/cl201-eu-spdc | eth1/35   | 
| pod-1/cl201-eu-spdc | eth1/36   | 
| pod-1/cl201-eu-spdc | eth1/37   | 
| pod-1/cl201-eu-spdc | eth1/38   | 
| pod-1/cl201-eu-spdc | eth1/39   | 
| pod-1/cl201-eu-spdc | eth1/4    | 
| pod-1/cl201-eu-spdc | eth1/40   | 
| pod-1/cl201-eu-spdc | eth1/41   | 
| pod-1/cl201-eu-spdc | eth1/42   | 
| pod-1/cl201-eu-spdc | eth1/43   | 
| pod-1/cl201-eu-spdc | eth1/44   | 
| pod-1/cl201-eu-spdc | eth1/45   | 
| pod-1/cl201-eu-spdc | eth1/46   | 
| pod-1/cl201-eu-spdc | eth1/47   | 
| pod-1/cl201-eu-spdc | eth1/48   | 
| pod-1/cl201-eu-spdc | eth1/49   | 
| pod-1/cl201-eu-spdc | eth1/5    | 
| pod-1/cl201-eu-spdc | eth1/50   | 
| pod-1/cl201-eu-spdc | eth1/51   | 
| pod-1/cl201-eu-spdc | eth1/52   | 
| pod-1/cl201-eu-spdc | eth1/53   | 
| pod-1/cl201-eu-spdc | eth1/54   | 
| pod-1/cl201-eu-spdc | eth1/55   | 
| pod-1/cl201-eu-spdc | eth1/56   | 
| pod-1/cl201-eu-spdc | eth1/57   | 
| pod-1/cl201-eu-spdc | eth1/58   | 
| pod-1/cl201-eu-spdc | eth1/59   | 
| pod-1/cl201-eu-spdc | eth1/60   | 
| pod-1/cl201-eu-spdc | eth1/61   | 
| pod-1/cl201-eu-spdc | eth1/62   | 
| pod-1/cl201-eu-spdc | eth1/63   | 
| pod-1/cl201-eu-spdc | eth1/64   | 
| pod-1/cl201-eu-spdc | eth1/65   | 
| pod-1/cl201-eu-spdc | eth1/66   | 
| pod-1/cl201-eu-spdc | eth1/67   | 
| pod-1/cl201-eu-spdc | eth1/69   | 
| pod-1/cl201-eu-spdc | eth1/7    | 
| pod-1/cl201-eu-spdc | eth1/70   | 
| pod-1/cl201-eu-spdc | eth1/73   | 
| pod-1/cl201-eu-spdc | eth1/74   | 
| pod-1/cl201-eu-spdc | eth1/75   | 
| pod-1/cl201-eu-spdc | eth1/76   | 
| pod-1/cl201-eu-spdc | eth1/77   | 
| pod-1/cl201-eu-spdc | eth1/78   | 
| pod-1/cl201-eu-spdc | eth1/79   | 
| pod-1/cl201-eu-spdc | eth1/8    | 
| pod-1/cl201-eu-spdc | eth1/80   | 
| pod-1/cl201-eu-spdc | eth1/85   | 
| pod-1/cl201-eu-spdc | eth1/86   | 
| pod-1/cl201-eu-spdc | eth1/87   | 
| pod-1/cl201-eu-spdc | eth1/88   | 
| pod-1/cl201-eu-spdc | eth1/89   | 
| pod-1/cl201-eu-spdc | eth1/90   | 
| pod-1/cl201-eu-spdc | eth1/94   | 
| pod-1/cl201-eu-spdc | eth1/95   | 
| pod-1/cl201-eu-spdc | eth1/97   | 
| pod-1/cl201-eu-spdc | eth1/98   | 
| pod-1/cl201-eu-spdc | eth1/99   | 
| pod-1/cl201-eu-spdc | po10      | 
| pod-1/cl201-eu-spdc | po11      | 
| pod-1/cl201-eu-spdc | po12      | 
| pod-1/cl201-eu-spdc | po13      | 
| pod-1/cl201-eu-spdc | po14      | 
| pod-1/cl201-eu-spdc | po16      | 
| pod-1/cl201-eu-spdc | po17      | 
| pod-1/cl201-eu-spdc | po18      | 
| pod-1/cl201-eu-spdc | po19      | 
| pod-1/cl201-eu-spdc | po20      | 
| pod-1/cl201-eu-spdc | po21      | 
| pod-1/cl201-eu-spdc | po22      | 
| pod-1/cl201-eu-spdc | po23      | 
| pod-1/cl201-eu-spdc | po24      | 
| pod-1/cl201-eu-spdc | po25      | 
| pod-1/cl201-eu-spdc | po26      | 
| pod-1/cl201-eu-spdc | po27      | 
| pod-1/cl201-eu-spdc | po28      | 
| pod-1/cl201-eu-spdc | po3       | 
| pod-1/cl201-eu-spdc | po4       | 
| pod-1/cl201-eu-spdc | po5       | 
| pod-1/cl201-eu-spdc | po6       | 
| pod-1/cl201-eu-spdc | po7       | 
| pod-1/cl201-eu-spdc | po8       | 
| pod-1/cl201-eu-spdc | po9       | 
| pod-1/cl202-eu-spdc | eth1/1    | 
| pod-1/cl202-eu-spdc | eth1/10   | 
| pod-1/cl202-eu-spdc | eth1/100  | 
| pod-1/cl202-eu-spdc | eth1/101  | 
| pod-1/cl202-eu-spdc | eth1/102  | 
| pod-1/cl202-eu-spdc | eth1/11   | 
| pod-1/cl202-eu-spdc | eth1/13   | 
| pod-1/cl202-eu-spdc | eth1/14   | 
| pod-1/cl202-eu-spdc | eth1/16   | 
| pod-1/cl202-eu-spdc | eth1/17   | 
| pod-1/cl202-eu-spdc | eth1/18   | 
| pod-1/cl202-eu-spdc | eth1/19   | 
| pod-1/cl202-eu-spdc | eth1/2    | 
| pod-1/cl202-eu-spdc | eth1/20   | 
| pod-1/cl202-eu-spdc | eth1/21   | 
| pod-1/cl202-eu-spdc | eth1/22   | 
| pod-1/cl202-eu-spdc | eth1/23   | 
| pod-1/cl202-eu-spdc | eth1/25   | 
| pod-1/cl202-eu-spdc | eth1/26   | 
| pod-1/cl202-eu-spdc | eth1/27   | 
| pod-1/cl202-eu-spdc | eth1/28   | 
| pod-1/cl202-eu-spdc | eth1/29   | 
| pod-1/cl202-eu-spdc | eth1/30   | 
| pod-1/cl202-eu-spdc | eth1/31   | 
| pod-1/cl202-eu-spdc | eth1/32   | 
| pod-1/cl202-eu-spdc | eth1/33   | 
| pod-1/cl202-eu-spdc | eth1/34   | 
| pod-1/cl202-eu-spdc | eth1/35   | 
| pod-1/cl202-eu-spdc | eth1/36   | 
| pod-1/cl202-eu-spdc | eth1/37   | 
| pod-1/cl202-eu-spdc | eth1/38   | 
| pod-1/cl202-eu-spdc | eth1/39   | 
| pod-1/cl202-eu-spdc | eth1/4    | 
| pod-1/cl202-eu-spdc | eth1/40   | 
| pod-1/cl202-eu-spdc | eth1/41   | 
| pod-1/cl202-eu-spdc | eth1/42   | 
| pod-1/cl202-eu-spdc | eth1/43   | 
| pod-1/cl202-eu-spdc | eth1/44   | 
| pod-1/cl202-eu-spdc | eth1/45   | 
| pod-1/cl202-eu-spdc | eth1/46   | 
| pod-1/cl202-eu-spdc | eth1/47   | 
| pod-1/cl202-eu-spdc | eth1/48   | 
| pod-1/cl202-eu-spdc | eth1/49   | 
| pod-1/cl202-eu-spdc | eth1/5    | 
| pod-1/cl202-eu-spdc | eth1/50   | 
| pod-1/cl202-eu-spdc | eth1/51   | 
| pod-1/cl202-eu-spdc | eth1/52   | 
| pod-1/cl202-eu-spdc | eth1/53   | 
| pod-1/cl202-eu-spdc | eth1/54   | 
| pod-1/cl202-eu-spdc | eth1/55   | 
| pod-1/cl202-eu-spdc | eth1/56   | 
| pod-1/cl202-eu-spdc | eth1/57   | 
| pod-1/cl202-eu-spdc | eth1/58   | 
| pod-1/cl202-eu-spdc | eth1/59   | 
| pod-1/cl202-eu-spdc | eth1/60   | 
| pod-1/cl202-eu-spdc | eth1/61   | 
| pod-1/cl202-eu-spdc | eth1/62   | 
| pod-1/cl202-eu-spdc | eth1/63   | 
| pod-1/cl202-eu-spdc | eth1/64   | 
| pod-1/cl202-eu-spdc | eth1/65   | 
| pod-1/cl202-eu-spdc | eth1/66   | 
| pod-1/cl202-eu-spdc | eth1/67   | 
| pod-1/cl202-eu-spdc | eth1/69   | 
| pod-1/cl202-eu-spdc | eth1/7    | 
| pod-1/cl202-eu-spdc | eth1/70   | 
| pod-1/cl202-eu-spdc | eth1/73   | 
| pod-1/cl202-eu-spdc | eth1/74   | 
| pod-1/cl202-eu-spdc | eth1/75   | 
| pod-1/cl202-eu-spdc | eth1/76   | 
| pod-1/cl202-eu-spdc | eth1/77   | 
| pod-1/cl202-eu-spdc | eth1/78   | 
| pod-1/cl202-eu-spdc | eth1/79   | 
| pod-1/cl202-eu-spdc | eth1/8    | 
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
| pod-1/cl202-eu-spdc | eth1/94   | 
| pod-1/cl202-eu-spdc | eth1/95   | 
| pod-1/cl202-eu-spdc | eth1/97   | 
| pod-1/cl202-eu-spdc | eth1/98   | 
| pod-1/cl202-eu-spdc | eth1/99   | 
| pod-1/cl202-eu-spdc | po1       | 
| pod-1/cl202-eu-spdc | po10      | 
| pod-1/cl202-eu-spdc | po11      | 
| pod-1/cl202-eu-spdc | po12      | 
| pod-1/cl202-eu-spdc | po13      | 
| pod-1/cl202-eu-spdc | po15      | 
| pod-1/cl202-eu-spdc | po16      | 
| pod-1/cl202-eu-spdc | po17      | 
| pod-1/cl202-eu-spdc | po18      | 
| pod-1/cl202-eu-spdc | po19      | 
| pod-1/cl202-eu-spdc | po2       | 
| pod-1/cl202-eu-spdc | po20      | 
| pod-1/cl202-eu-spdc | po21      | 
| pod-1/cl202-eu-spdc | po22      | 
| pod-1/cl202-eu-spdc | po23      | 
| pod-1/cl202-eu-spdc | po24      | 
| pod-1/cl202-eu-spdc | po25      | 
| pod-1/cl202-eu-spdc | po27      | 
| pod-1/cl202-eu-spdc | po28      | 
| pod-1/cl202-eu-spdc | po3       | 
| pod-1/cl202-eu-spdc | po4       | 
| pod-1/cl202-eu-spdc | po5       | 
| pod-1/cl202-eu-spdc | po6       | 
| pod-1/cl202-eu-spdc | po7       | 
| pod-1/cl202-eu-spdc | po8       | 
| pod-1/bl205-eu-spdc | eth1/10   | 
| pod-1/bl205-eu-spdc | eth1/13   | 
| pod-1/bl205-eu-spdc | eth1/14   | 
| pod-1/bl205-eu-spdc | eth1/20   | 
| pod-1/bl205-eu-spdc | eth1/21   | 
| pod-1/bl205-eu-spdc | eth1/22   | 
| pod-1/bl205-eu-spdc | eth1/23   | 
| pod-1/bl205-eu-spdc | eth1/24   | 
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
| pod-1/bl206-eu-spdc | eth1/24   | 
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
| pod-1/rl301-eu-spdc | eth1/24/1 | 
| pod-1/rl301-eu-spdc | eth1/24/2 | 
| pod-1/rl301-eu-spdc | eth1/24/3 | 
| pod-1/rl301-eu-spdc | eth1/24/4 | 
| pod-1/rl301-eu-spdc | eth1/25/1 | 
| pod-1/rl301-eu-spdc | eth1/25/2 | 
| pod-1/rl301-eu-spdc | eth1/25/3 | 
| pod-1/rl301-eu-spdc | eth1/25/4 | 
| pod-1/rl301-eu-spdc | eth1/26/1 | 
| pod-1/rl301-eu-spdc | eth1/26/2 | 
| pod-1/rl301-eu-spdc | eth1/26/3 | 
| pod-1/rl301-eu-spdc | eth1/26/4 | 
| pod-1/rl301-eu-spdc | eth1/27/1 | 
| pod-1/rl301-eu-spdc | eth1/27/2 | 
| pod-1/rl301-eu-spdc | eth1/27/3 | 
| pod-1/rl301-eu-spdc | eth1/27/4 | 
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
| pod-1/rl302-eu-spdc | eth1/24/1 | 
| pod-1/rl302-eu-spdc | eth1/24/2 | 
| pod-1/rl302-eu-spdc | eth1/24/3 | 
| pod-1/rl302-eu-spdc | eth1/24/4 | 
| pod-1/rl302-eu-spdc | eth1/25/1 | 
| pod-1/rl302-eu-spdc | eth1/25/2 | 
| pod-1/rl302-eu-spdc | eth1/25/3 | 
| pod-1/rl302-eu-spdc | eth1/25/4 | 
| pod-1/rl302-eu-spdc | eth1/26/1 | 
| pod-1/rl302-eu-spdc | eth1/26/2 | 
| pod-1/rl302-eu-spdc | eth1/26/3 | 
| pod-1/rl302-eu-spdc | eth1/26/4 | 
| pod-1/rl302-eu-spdc | eth1/27/1 | 
| pod-1/rl302-eu-spdc | eth1/27/2 | 
| pod-1/rl302-eu-spdc | eth1/27/3 | 
| pod-1/rl302-eu-spdc | eth1/27/4 | 
| pod-1/rl302-eu-spdc | eth1/30   | 
| pod-1/rl302-eu-spdc | eth1/5    | 
| pod-1/rl302-eu-spdc | eth1/6    | 
| pod-1/rl302-eu-spdc | eth1/7    | 
| pod-1/rl302-eu-spdc | eth1/8    | 
| pod-1/rl302-eu-spdc | eth1/9    | 
+---------------------+-----------+

+-----------------------------+--------------------------------+-------------------+
| Policy Name                 | Policy Type                    | Policy Class      |
+-----------------------------+--------------------------------+-------------------+
| infra                       | Access Infra                   | infraInfra        | 
| ESX-CDC-DVS_PolGrp          | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| ESX-R3DC-DVS_PolGrp         | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| Infra-BGP_PolGrp            | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-1-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-1-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-2-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-2-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-3-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-3-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-COMP-1-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-COMP-1-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-COMP-2-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-COMP-2-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-AIO-1-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-AIO-1-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-AIO-2-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-AIO-2-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-AIO-3-SRIoV-0_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-AIO-3-SRIoV-1_PolGrp  | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-COMP-1-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-COMP-1-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-COMP-2-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-COMP-2-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-COMP-3-SRIoV-0_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod4a-COMP-3-SRIoV-1_PolGrp | Leaf Access Port Policy Group  | infraAccPortGrp   | 
| pod1a-AIO-1-PET_PolGrp      | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-AIO-1-SAMX_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-AIO-2-PET_PolGrp      | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-AIO-2-SAMX_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-AIO-3-PET_PolGrp      | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-AIO-3-SAMX_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-COMP-1-PET_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-COMP-1-SAMX_PolGrp    | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-COMP-2-PET_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-COMP-2-SAMX_PolGrp    | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-MX_PolGrp             | PC/VPC Interface               | infraAccBndlGrp   | 
| pod1a-NVBench_PolGrp        | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-AIO-1-PET_PolGrp      | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-AIO-1-SAMX_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-AIO-2-PET_PolGrp      | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-AIO-2-SAMX_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-AIO-3-PET_PolGrp      | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-AIO-3-SAMX_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-COMP-1-PET_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-COMP-1-SAMX_PolGrp    | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-COMP-2-PET_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-COMP-2-SAMX_PolGrp    | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-COMP-3-PET_PolGrp     | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-COMP-3-SAMX_PolGrp    | PC/VPC Interface               | infraAccBndlGrp   | 
| pod4a-MX_PolGrp             | PC/VPC Interface               | infraAccBndlGrp   | 
| RL-L3Out_policyGroup        | Spine Access Port Policy Group | infraSpAccPortGrp | 
| multipodL3Out_PolGrp        | Spine Access Port Policy Group | infraSpAccPortGrp | 
| multipodL3Out_policyGroup   | Spine Access Port Policy Group | infraSpAccPortGrp | 
+-----------------------------+--------------------------------+-------------------+
Context: phy
```

Developer

```
# iserver get aci policy link --apic apic11 --name default --view verbose

{
    "duration": 1829,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 408,
        "disconnect_time": 0,
        "mo_time": 1038,
        "total_time": 1446
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

True	408	-	connect apic11o.emea-sp.cisco.com
True	344	29	apic11o.emea-sp.cisco.com class fabricHIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	393	408	apic11o.emea-sp.cisco.com class l1RsHIfPolCons
True	301	11	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyLink.md)