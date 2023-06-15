# Policy - Storm Control

## Interface specific output

```
# iserver get aci policy storm --apic apic11 --name default --view intf

Apic: apic11 (mode:online, cache:off)

+-------------+---------------------+-----------+
| Policy Name | Node                | Interface |
+-------------+---------------------+-----------+
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
|             | pod-1/cl201-eu-spdc | eth1/24   | 
|             | pod-1/cl201-eu-spdc | eth1/25   | 
|             | pod-1/cl201-eu-spdc | eth1/26   | 
|             | pod-1/cl201-eu-spdc | eth1/27   | 
|             | pod-1/cl201-eu-spdc | eth1/28   | 
|             | pod-1/cl201-eu-spdc | eth1/29   | 
|             | pod-1/cl201-eu-spdc | eth1/3    | 
|             | pod-1/cl201-eu-spdc | eth1/30   | 
|             | pod-1/cl201-eu-spdc | eth1/31   | 
|             | pod-1/cl201-eu-spdc | eth1/32   | 
|             | pod-1/cl201-eu-spdc | eth1/33   | 
|             | pod-1/cl201-eu-spdc | eth1/34   | 
|             | pod-1/cl201-eu-spdc | eth1/35   | 
|             | pod-1/cl201-eu-spdc | eth1/36   | 
|             | pod-1/cl201-eu-spdc | eth1/37   | 
|             | pod-1/cl201-eu-spdc | eth1/38   | 
|             | pod-1/cl201-eu-spdc | eth1/39   | 
|             | pod-1/cl201-eu-spdc | eth1/4    | 
|             | pod-1/cl201-eu-spdc | eth1/40   | 
|             | pod-1/cl201-eu-spdc | eth1/41   | 
|             | pod-1/cl201-eu-spdc | eth1/42   | 
|             | pod-1/cl201-eu-spdc | eth1/43   | 
|             | pod-1/cl201-eu-spdc | eth1/44   | 
|             | pod-1/cl201-eu-spdc | eth1/45   | 
|             | pod-1/cl201-eu-spdc | eth1/46   | 
|             | pod-1/cl201-eu-spdc | eth1/47   | 
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
|             | pod-1/cl201-eu-spdc | eth1/67   | 
|             | pod-1/cl201-eu-spdc | eth1/68   | 
|             | pod-1/cl201-eu-spdc | eth1/69   | 
|             | pod-1/cl201-eu-spdc | eth1/7    | 
|             | pod-1/cl201-eu-spdc | eth1/70   | 
|             | pod-1/cl201-eu-spdc | eth1/71   | 
|             | pod-1/cl201-eu-spdc | eth1/72   | 
|             | pod-1/cl201-eu-spdc | eth1/73   | 
|             | pod-1/cl201-eu-spdc | eth1/74   | 
|             | pod-1/cl201-eu-spdc | eth1/75   | 
|             | pod-1/cl201-eu-spdc | eth1/76   | 
|             | pod-1/cl201-eu-spdc | eth1/77   | 
|             | pod-1/cl201-eu-spdc | eth1/78   | 
|             | pod-1/cl201-eu-spdc | eth1/79   | 
|             | pod-1/cl201-eu-spdc | eth1/8    | 
|             | pod-1/cl201-eu-spdc | eth1/80   | 
|             | pod-1/cl201-eu-spdc | eth1/81   | 
|             | pod-1/cl201-eu-spdc | eth1/82   | 
|             | pod-1/cl201-eu-spdc | eth1/83   | 
|             | pod-1/cl201-eu-spdc | eth1/84   | 
|             | pod-1/cl201-eu-spdc | eth1/85   | 
|             | pod-1/cl201-eu-spdc | eth1/86   | 
|             | pod-1/cl201-eu-spdc | eth1/87   | 
|             | pod-1/cl201-eu-spdc | eth1/88   | 
|             | pod-1/cl201-eu-spdc | eth1/89   | 
|             | pod-1/cl201-eu-spdc | eth1/9    | 
|             | pod-1/cl201-eu-spdc | eth1/90   | 
|             | pod-1/cl201-eu-spdc | eth1/91   | 
|             | pod-1/cl201-eu-spdc | eth1/92   | 
|             | pod-1/cl201-eu-spdc | eth1/93   | 
|             | pod-1/cl201-eu-spdc | eth1/94   | 
|             | pod-1/cl201-eu-spdc | eth1/95   | 
|             | pod-1/cl201-eu-spdc | eth1/96   | 
|             | pod-1/cl201-eu-spdc | eth1/97   | 
|             | pod-1/cl201-eu-spdc | eth1/98   | 
|             | pod-1/cl201-eu-spdc | eth1/99   | 
|             | pod-1/cl201-eu-spdc | po1       | 
|             | pod-1/cl201-eu-spdc | po10      | 
|             | pod-1/cl201-eu-spdc | po11      | 
|             | pod-1/cl201-eu-spdc | po12      | 
|             | pod-1/cl201-eu-spdc | po13      | 
|             | pod-1/cl201-eu-spdc | po14      | 
|             | pod-1/cl201-eu-spdc | po15      | 
|             | pod-1/cl201-eu-spdc | po16      | 
|             | pod-1/cl201-eu-spdc | po17      | 
|             | pod-1/cl201-eu-spdc | po18      | 
|             | pod-1/cl201-eu-spdc | po19      | 
|             | pod-1/cl201-eu-spdc | po2       | 
|             | pod-1/cl201-eu-spdc | po20      | 
|             | pod-1/cl201-eu-spdc | po21      | 
|             | pod-1/cl201-eu-spdc | po22      | 
|             | pod-1/cl201-eu-spdc | po23      | 
|             | pod-1/cl201-eu-spdc | po24      | 
|             | pod-1/cl201-eu-spdc | po25      | 
|             | pod-1/cl201-eu-spdc | po26      | 
|             | pod-1/cl201-eu-spdc | po27      | 
|             | pod-1/cl201-eu-spdc | po28      | 
|             | pod-1/cl201-eu-spdc | po3       | 
|             | pod-1/cl201-eu-spdc | po4       | 
|             | pod-1/cl201-eu-spdc | po5       | 
|             | pod-1/cl201-eu-spdc | po6       | 
|             | pod-1/cl201-eu-spdc | po7       | 
|             | pod-1/cl201-eu-spdc | po8       | 
|             | pod-1/cl201-eu-spdc | po9       | 
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
|             | pod-1/cl202-eu-spdc | eth1/24   | 
|             | pod-1/cl202-eu-spdc | eth1/25   | 
|             | pod-1/cl202-eu-spdc | eth1/26   | 
|             | pod-1/cl202-eu-spdc | eth1/27   | 
|             | pod-1/cl202-eu-spdc | eth1/28   | 
|             | pod-1/cl202-eu-spdc | eth1/29   | 
|             | pod-1/cl202-eu-spdc | eth1/3    | 
|             | pod-1/cl202-eu-spdc | eth1/30   | 
|             | pod-1/cl202-eu-spdc | eth1/31   | 
|             | pod-1/cl202-eu-spdc | eth1/32   | 
|             | pod-1/cl202-eu-spdc | eth1/33   | 
|             | pod-1/cl202-eu-spdc | eth1/34   | 
|             | pod-1/cl202-eu-spdc | eth1/35   | 
|             | pod-1/cl202-eu-spdc | eth1/36   | 
|             | pod-1/cl202-eu-spdc | eth1/37   | 
|             | pod-1/cl202-eu-spdc | eth1/38   | 
|             | pod-1/cl202-eu-spdc | eth1/39   | 
|             | pod-1/cl202-eu-spdc | eth1/4    | 
|             | pod-1/cl202-eu-spdc | eth1/40   | 
|             | pod-1/cl202-eu-spdc | eth1/41   | 
|             | pod-1/cl202-eu-spdc | eth1/42   | 
|             | pod-1/cl202-eu-spdc | eth1/43   | 
|             | pod-1/cl202-eu-spdc | eth1/44   | 
|             | pod-1/cl202-eu-spdc | eth1/45   | 
|             | pod-1/cl202-eu-spdc | eth1/46   | 
|             | pod-1/cl202-eu-spdc | eth1/47   | 
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
|             | pod-1/cl202-eu-spdc | eth1/67   | 
|             | pod-1/cl202-eu-spdc | eth1/68   | 
|             | pod-1/cl202-eu-spdc | eth1/69   | 
|             | pod-1/cl202-eu-spdc | eth1/7    | 
|             | pod-1/cl202-eu-spdc | eth1/70   | 
|             | pod-1/cl202-eu-spdc | eth1/71   | 
|             | pod-1/cl202-eu-spdc | eth1/72   | 
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
|             | pod-1/cl202-eu-spdc | eth1/91   | 
|             | pod-1/cl202-eu-spdc | eth1/92   | 
|             | pod-1/cl202-eu-spdc | eth1/93   | 
|             | pod-1/cl202-eu-spdc | eth1/94   | 
|             | pod-1/cl202-eu-spdc | eth1/95   | 
|             | pod-1/cl202-eu-spdc | eth1/96   | 
|             | pod-1/cl202-eu-spdc | eth1/97   | 
|             | pod-1/cl202-eu-spdc | eth1/98   | 
|             | pod-1/cl202-eu-spdc | eth1/99   | 
|             | pod-1/cl202-eu-spdc | po1       | 
|             | pod-1/cl202-eu-spdc | po10      | 
|             | pod-1/cl202-eu-spdc | po11      | 
|             | pod-1/cl202-eu-spdc | po12      | 
|             | pod-1/cl202-eu-spdc | po13      | 
|             | pod-1/cl202-eu-spdc | po14      | 
|             | pod-1/cl202-eu-spdc | po15      | 
|             | pod-1/cl202-eu-spdc | po16      | 
|             | pod-1/cl202-eu-spdc | po17      | 
|             | pod-1/cl202-eu-spdc | po18      | 
|             | pod-1/cl202-eu-spdc | po19      | 
|             | pod-1/cl202-eu-spdc | po2       | 
|             | pod-1/cl202-eu-spdc | po20      | 
|             | pod-1/cl202-eu-spdc | po21      | 
|             | pod-1/cl202-eu-spdc | po22      | 
|             | pod-1/cl202-eu-spdc | po23      | 
|             | pod-1/cl202-eu-spdc | po24      | 
|             | pod-1/cl202-eu-spdc | po25      | 
|             | pod-1/cl202-eu-spdc | po26      | 
|             | pod-1/cl202-eu-spdc | po27      | 
|             | pod-1/cl202-eu-spdc | po28      | 
|             | pod-1/cl202-eu-spdc | po3       | 
|             | pod-1/cl202-eu-spdc | po4       | 
|             | pod-1/cl202-eu-spdc | po5       | 
|             | pod-1/cl202-eu-spdc | po6       | 
|             | pod-1/cl202-eu-spdc | po7       | 
|             | pod-1/cl202-eu-spdc | po8       | 
|             | pod-1/cl202-eu-spdc | po9       | 
|             | pod-1/bl205-eu-spdc | eth1/1    | 
|             | pod-1/bl205-eu-spdc | eth1/10   | 
|             | pod-1/bl205-eu-spdc | eth1/11   | 
|             | pod-1/bl205-eu-spdc | eth1/12   | 
|             | pod-1/bl205-eu-spdc | eth1/13   | 
|             | pod-1/bl205-eu-spdc | eth1/14   | 
|             | pod-1/bl205-eu-spdc | eth1/15   | 
|             | pod-1/bl205-eu-spdc | eth1/16   | 
|             | pod-1/bl205-eu-spdc | eth1/17   | 
|             | pod-1/bl205-eu-spdc | eth1/18   | 
|             | pod-1/bl205-eu-spdc | eth1/19   | 
|             | pod-1/bl205-eu-spdc | eth1/2    | 
|             | pod-1/bl205-eu-spdc | eth1/20   | 
|             | pod-1/bl205-eu-spdc | eth1/21   | 
|             | pod-1/bl205-eu-spdc | eth1/22   | 
|             | pod-1/bl205-eu-spdc | eth1/23   | 
|             | pod-1/bl205-eu-spdc | eth1/24   | 
|             | pod-1/bl205-eu-spdc | eth1/25   | 
|             | pod-1/bl205-eu-spdc | eth1/26   | 
|             | pod-1/bl205-eu-spdc | eth1/27   | 
|             | pod-1/bl205-eu-spdc | eth1/28   | 
|             | pod-1/bl205-eu-spdc | eth1/3    | 
|             | pod-1/bl205-eu-spdc | eth1/4    | 
|             | pod-1/bl205-eu-spdc | eth1/5    | 
|             | pod-1/bl205-eu-spdc | eth1/6    | 
|             | pod-1/bl205-eu-spdc | eth1/7    | 
|             | pod-1/bl205-eu-spdc | eth1/8    | 
|             | pod-1/bl205-eu-spdc | eth1/9    | 
|             | pod-1/bl205-eu-spdc | po1       | 
|             | pod-1/bl205-eu-spdc | po2       | 
|             | pod-1/bl205-eu-spdc | po3       | 
|             | pod-1/bl205-eu-spdc | po4       | 
|             | pod-1/bl205-eu-spdc | po5       | 
|             | pod-1/bl206-eu-spdc | eth1/1    | 
|             | pod-1/bl206-eu-spdc | eth1/10   | 
|             | pod-1/bl206-eu-spdc | eth1/11   | 
|             | pod-1/bl206-eu-spdc | eth1/12   | 
|             | pod-1/bl206-eu-spdc | eth1/13   | 
|             | pod-1/bl206-eu-spdc | eth1/14   | 
|             | pod-1/bl206-eu-spdc | eth1/15   | 
|             | pod-1/bl206-eu-spdc | eth1/16   | 
|             | pod-1/bl206-eu-spdc | eth1/17   | 
|             | pod-1/bl206-eu-spdc | eth1/18   | 
|             | pod-1/bl206-eu-spdc | eth1/19   | 
|             | pod-1/bl206-eu-spdc | eth1/2    | 
|             | pod-1/bl206-eu-spdc | eth1/20   | 
|             | pod-1/bl206-eu-spdc | eth1/21   | 
|             | pod-1/bl206-eu-spdc | eth1/22   | 
|             | pod-1/bl206-eu-spdc | eth1/23   | 
|             | pod-1/bl206-eu-spdc | eth1/24   | 
|             | pod-1/bl206-eu-spdc | eth1/25   | 
|             | pod-1/bl206-eu-spdc | eth1/26   | 
|             | pod-1/bl206-eu-spdc | eth1/27   | 
|             | pod-1/bl206-eu-spdc | eth1/28   | 
|             | pod-1/bl206-eu-spdc | eth1/3    | 
|             | pod-1/bl206-eu-spdc | eth1/4    | 
|             | pod-1/bl206-eu-spdc | eth1/5    | 
|             | pod-1/bl206-eu-spdc | eth1/6    | 
|             | pod-1/bl206-eu-spdc | eth1/7    | 
|             | pod-1/bl206-eu-spdc | eth1/8    | 
|             | pod-1/bl206-eu-spdc | eth1/9    | 
|             | pod-1/bl206-eu-spdc | po1       | 
|             | pod-1/bl206-eu-spdc | po2       | 
|             | pod-1/bl206-eu-spdc | po3       | 
|             | pod-1/bl206-eu-spdc | po4       | 
|             | pod-1/bl206-eu-spdc | po5       | 
|             | pod-1/cl209-eu-spdc | eth1/1    | 
|             | pod-1/cl209-eu-spdc | eth1/10   | 
|             | pod-1/cl209-eu-spdc | eth1/11   | 
|             | pod-1/cl209-eu-spdc | eth1/12   | 
|             | pod-1/cl209-eu-spdc | eth1/13   | 
|             | pod-1/cl209-eu-spdc | eth1/14   | 
|             | pod-1/cl209-eu-spdc | eth1/15   | 
|             | pod-1/cl209-eu-spdc | eth1/16   | 
|             | pod-1/cl209-eu-spdc | eth1/17   | 
|             | pod-1/cl209-eu-spdc | eth1/18   | 
|             | pod-1/cl209-eu-spdc | eth1/19   | 
|             | pod-1/cl209-eu-spdc | eth1/2    | 
|             | pod-1/cl209-eu-spdc | eth1/20   | 
|             | pod-1/cl209-eu-spdc | eth1/21   | 
|             | pod-1/cl209-eu-spdc | eth1/22   | 
|             | pod-1/cl209-eu-spdc | eth1/23   | 
|             | pod-1/cl209-eu-spdc | eth1/24   | 
|             | pod-1/cl209-eu-spdc | eth1/25   | 
|             | pod-1/cl209-eu-spdc | eth1/26   | 
|             | pod-1/cl209-eu-spdc | eth1/27   | 
|             | pod-1/cl209-eu-spdc | eth1/28   | 
|             | pod-1/cl209-eu-spdc | eth1/3    | 
|             | pod-1/cl209-eu-spdc | eth1/4    | 
|             | pod-1/cl209-eu-spdc | eth1/5    | 
|             | pod-1/cl209-eu-spdc | eth1/6    | 
|             | pod-1/cl209-eu-spdc | eth1/7    | 
|             | pod-1/cl209-eu-spdc | eth1/8    | 
|             | pod-1/cl209-eu-spdc | eth1/9    | 
|             | pod-1/cl210-eu-spdc | eth1/1    | 
|             | pod-1/cl210-eu-spdc | eth1/10   | 
|             | pod-1/cl210-eu-spdc | eth1/11   | 
|             | pod-1/cl210-eu-spdc | eth1/12   | 
|             | pod-1/cl210-eu-spdc | eth1/13   | 
|             | pod-1/cl210-eu-spdc | eth1/14   | 
|             | pod-1/cl210-eu-spdc | eth1/15   | 
|             | pod-1/cl210-eu-spdc | eth1/16   | 
|             | pod-1/cl210-eu-spdc | eth1/17   | 
|             | pod-1/cl210-eu-spdc | eth1/18   | 
|             | pod-1/cl210-eu-spdc | eth1/19   | 
|             | pod-1/cl210-eu-spdc | eth1/2    | 
|             | pod-1/cl210-eu-spdc | eth1/20   | 
|             | pod-1/cl210-eu-spdc | eth1/21   | 
|             | pod-1/cl210-eu-spdc | eth1/22   | 
|             | pod-1/cl210-eu-spdc | eth1/23   | 
|             | pod-1/cl210-eu-spdc | eth1/24   | 
|             | pod-1/cl210-eu-spdc | eth1/25   | 
|             | pod-1/cl210-eu-spdc | eth1/26   | 
|             | pod-1/cl210-eu-spdc | eth1/27   | 
|             | pod-1/cl210-eu-spdc | eth1/28   | 
|             | pod-1/cl210-eu-spdc | eth1/3    | 
|             | pod-1/cl210-eu-spdc | eth1/4    | 
|             | pod-1/cl210-eu-spdc | eth1/5    | 
|             | pod-1/cl210-eu-spdc | eth1/6    | 
|             | pod-1/cl210-eu-spdc | eth1/7    | 
|             | pod-1/cl210-eu-spdc | eth1/8    | 
|             | pod-1/cl210-eu-spdc | eth1/9    | 
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
|             | pod-1/rl301-eu-spdc | eth1/24/1 | 
|             | pod-1/rl301-eu-spdc | eth1/24/2 | 
|             | pod-1/rl301-eu-spdc | eth1/24/3 | 
|             | pod-1/rl301-eu-spdc | eth1/24/4 | 
|             | pod-1/rl301-eu-spdc | eth1/25/1 | 
|             | pod-1/rl301-eu-spdc | eth1/25/2 | 
|             | pod-1/rl301-eu-spdc | eth1/25/3 | 
|             | pod-1/rl301-eu-spdc | eth1/25/4 | 
|             | pod-1/rl301-eu-spdc | eth1/26/1 | 
|             | pod-1/rl301-eu-spdc | eth1/26/2 | 
|             | pod-1/rl301-eu-spdc | eth1/26/3 | 
|             | pod-1/rl301-eu-spdc | eth1/26/4 | 
|             | pod-1/rl301-eu-spdc | eth1/27/1 | 
|             | pod-1/rl301-eu-spdc | eth1/27/2 | 
|             | pod-1/rl301-eu-spdc | eth1/27/3 | 
|             | pod-1/rl301-eu-spdc | eth1/27/4 | 
|             | pod-1/rl301-eu-spdc | eth1/28   | 
|             | pod-1/rl301-eu-spdc | eth1/29   | 
|             | pod-1/rl301-eu-spdc | eth1/3    | 
|             | pod-1/rl301-eu-spdc | eth1/30   | 
|             | pod-1/rl301-eu-spdc | eth1/4    | 
|             | pod-1/rl301-eu-spdc | eth1/5    | 
|             | pod-1/rl301-eu-spdc | eth1/6    | 
|             | pod-1/rl301-eu-spdc | eth1/7    | 
|             | pod-1/rl301-eu-spdc | eth1/8    | 
|             | pod-1/rl301-eu-spdc | eth1/9    | 
|             | pod-1/rl301-eu-spdc | po1       | 
|             | pod-1/rl301-eu-spdc | po2       | 
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
|             | pod-1/rl302-eu-spdc | eth1/24/1 | 
|             | pod-1/rl302-eu-spdc | eth1/24/2 | 
|             | pod-1/rl302-eu-spdc | eth1/24/3 | 
|             | pod-1/rl302-eu-spdc | eth1/24/4 | 
|             | pod-1/rl302-eu-spdc | eth1/25/1 | 
|             | pod-1/rl302-eu-spdc | eth1/25/2 | 
|             | pod-1/rl302-eu-spdc | eth1/25/3 | 
|             | pod-1/rl302-eu-spdc | eth1/25/4 | 
|             | pod-1/rl302-eu-spdc | eth1/26/1 | 
|             | pod-1/rl302-eu-spdc | eth1/26/2 | 
|             | pod-1/rl302-eu-spdc | eth1/26/3 | 
|             | pod-1/rl302-eu-spdc | eth1/26/4 | 
|             | pod-1/rl302-eu-spdc | eth1/27/1 | 
|             | pod-1/rl302-eu-spdc | eth1/27/2 | 
|             | pod-1/rl302-eu-spdc | eth1/27/3 | 
|             | pod-1/rl302-eu-spdc | eth1/27/4 | 
|             | pod-1/rl302-eu-spdc | eth1/28   | 
|             | pod-1/rl302-eu-spdc | eth1/29   | 
|             | pod-1/rl302-eu-spdc | eth1/3    | 
|             | pod-1/rl302-eu-spdc | eth1/30   | 
|             | pod-1/rl302-eu-spdc | eth1/4    | 
|             | pod-1/rl302-eu-spdc | eth1/5    | 
|             | pod-1/rl302-eu-spdc | eth1/6    | 
|             | pod-1/rl302-eu-spdc | eth1/7    | 
|             | pod-1/rl302-eu-spdc | eth1/8    | 
|             | pod-1/rl302-eu-spdc | eth1/9    | 
|             | pod-1/rl302-eu-spdc | po1       | 
|             | pod-1/rl302-eu-spdc | po2       | 
+-------------+---------------------+-----------+
Context: phy
```

Developer

```
# iserver get aci policy storm --apic apic11 --name default --view intf

{
    "duration": 6966,
    "apic": {
        "read": true,
        "success": 4,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 3,
        "connect_time": 442,
        "disconnect_time": 0,
        "mo_time": 1957,
        "total_time": 2399
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

True	442	-	connect apic11o.emea-sp.cisco.com
True	1208	1	apic11o.emea-sp.cisco.com class stormctrlIfPol query rsp-subtree=children&rsp-subtree-class=relnFrom
True	411	470	apic11o.emea-sp.cisco.com class l1RsStormctrlIfPolCons
True	338	13	apic11o.emea-sp.cisco.com class fabricNode
```

[[Back]](./PolicyStorm.md)