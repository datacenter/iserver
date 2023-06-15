# Node Interface - SVI

## All nodes

```
# iserver get aci intf svi --apic apic11 --node any

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| Node                | Interface | Admin State | Oper State | Type        | Medium | Multicast | MTU  | Fabric Encap   |
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
| pod-1/bl205-eu-spdc | vlan1     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811132 | 
| pod-1/bl205-eu-spdc | vlan11    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/bl205-eu-spdc | vlan13    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/bl205-eu-spdc | vlan15    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/bl205-eu-spdc | vlan17    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/bl205-eu-spdc | vlan18    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942188 | 
| pod-1/bl205-eu-spdc | vlan19    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15531940 | 
| pod-1/bl205-eu-spdc | vlan2     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/bl205-eu-spdc | vlan20    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942189 | 
| pod-1/bl205-eu-spdc | vlan21    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/bl205-eu-spdc | vlan22    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/bl205-eu-spdc | vlan23    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/bl205-eu-spdc | vlan25    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/bl205-eu-spdc | vlan27    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/bl205-eu-spdc | vlan29    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/bl205-eu-spdc | vlan3     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/bl205-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/bl205-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/bl205-eu-spdc | vlan33    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/bl205-eu-spdc | vlan35    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/bl205-eu-spdc | vlan37    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/bl205-eu-spdc | vlan39    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14778362 | 
| pod-1/bl205-eu-spdc | vlan40    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/bl205-eu-spdc | vlan43    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335346 | 
| pod-1/bl205-eu-spdc | vlan44    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15499182 | 
| pod-1/bl205-eu-spdc | vlan45    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15597468 | 
| pod-1/bl205-eu-spdc | vlan49    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| pod-1/bl205-eu-spdc | vlan5     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106014 | 
| pod-1/bl205-eu-spdc | vlan56    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| pod-1/bl205-eu-spdc | vlan57    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909413 | 
| pod-1/bl205-eu-spdc | vlan59    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/bl205-eu-spdc | vlan6     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/bl205-eu-spdc | vlan61    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/bl205-eu-spdc | vlan65    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/bl205-eu-spdc | vlan67    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| pod-1/bl205-eu-spdc | vlan68    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/bl205-eu-spdc | vlan70    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
| pod-1/bl205-eu-spdc | vlan72    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106012 | 
| pod-1/bl206-eu-spdc | vlan11    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/bl206-eu-spdc | vlan13    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/bl206-eu-spdc | vlan15    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/bl206-eu-spdc | vlan17    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/bl206-eu-spdc | vlan18    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/bl206-eu-spdc | vlan2     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811132 | 
| pod-1/bl206-eu-spdc | vlan20    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/bl206-eu-spdc | vlan22    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/bl206-eu-spdc | vlan24    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/bl206-eu-spdc | vlan26    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/bl206-eu-spdc | vlan28    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/bl206-eu-spdc | vlan3     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106014 | 
| pod-1/bl206-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15499182 | 
| pod-1/bl206-eu-spdc | vlan31    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14778362 | 
| pod-1/bl206-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15597468 | 
| pod-1/bl206-eu-spdc | vlan33    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335346 | 
| pod-1/bl206-eu-spdc | vlan34    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942189 | 
| pod-1/bl206-eu-spdc | vlan35    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15531940 | 
| pod-1/bl206-eu-spdc | vlan36    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/bl206-eu-spdc | vlan37    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/bl206-eu-spdc | vlan38    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/bl206-eu-spdc | vlan39    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/bl206-eu-spdc | vlan4     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942188 | 
| pod-1/bl206-eu-spdc | vlan40    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/bl206-eu-spdc | vlan41    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/bl206-eu-spdc | vlan43    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/bl206-eu-spdc | vlan45    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/bl206-eu-spdc | vlan47    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/bl206-eu-spdc | vlan5     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/bl206-eu-spdc | vlan50    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106012 | 
| pod-1/bl206-eu-spdc | vlan51    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/bl206-eu-spdc | vlan53    | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15597457 | 
| pod-1/bl206-eu-spdc | vlan57    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040482 | 
| pod-1/bl206-eu-spdc | vlan58    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400881 | 
| pod-1/bl206-eu-spdc | vlan7     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/bl206-eu-spdc | vlan8     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl201-eu-spdc | vlan2     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/cl201-eu-spdc | vlan20    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/cl201-eu-spdc | vlan230   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14974941 | 
| pod-1/cl201-eu-spdc | vlan244   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/cl201-eu-spdc | vlan252   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl201-eu-spdc | vlan268   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15171555 | 
| pod-1/cl201-eu-spdc | vlan270   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/cl201-eu-spdc | vlan274   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876654 | 
| pod-1/cl201-eu-spdc | vlan276   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15564707 | 
| pod-1/cl201-eu-spdc | vlan278   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16220083 | 
| pod-1/cl201-eu-spdc | vlan280   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/cl201-eu-spdc | vlan282   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/cl201-eu-spdc | vlan286   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15237079 | 
| pod-1/cl201-eu-spdc | vlan288   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/cl201-eu-spdc | vlan290   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/cl201-eu-spdc | vlan293   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/cl201-eu-spdc | vlan295   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/cl201-eu-spdc | vlan310   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/cl201-eu-spdc | vlan312   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/cl201-eu-spdc | vlan316   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368109 | 
| pod-1/cl201-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15138766 | 
| pod-1/cl201-eu-spdc | vlan330   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335355 | 
| pod-1/cl201-eu-spdc | vlan334   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335344 | 
| pod-1/cl201-eu-spdc | vlan344   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14680100 | 
| pod-1/cl201-eu-spdc | vlan36    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15007732 | 
| pod-1/cl201-eu-spdc | vlan440   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15695752 | 
| pod-1/cl201-eu-spdc | vlan442   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106004 | 
| pod-1/cl201-eu-spdc | vlan444   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/cl201-eu-spdc | vlan460   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| pod-1/cl201-eu-spdc | vlan461   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| pod-1/cl201-eu-spdc | vlan468   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| pod-1/cl201-eu-spdc | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| pod-1/cl201-eu-spdc | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| pod-1/cl201-eu-spdc | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| pod-1/cl201-eu-spdc | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| pod-1/cl201-eu-spdc | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| pod-1/cl201-eu-spdc | vlan474   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| pod-1/cl201-eu-spdc | vlan479   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| pod-1/cl201-eu-spdc | vlan480   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| pod-1/cl201-eu-spdc | vlan481   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/cl201-eu-spdc | vlan487   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/cl201-eu-spdc | vlan489   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/cl201-eu-spdc | vlan492   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| pod-1/cl201-eu-spdc | vlan493   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| pod-1/cl201-eu-spdc | vlan494   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| pod-1/cl201-eu-spdc | vlan495   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| pod-1/cl201-eu-spdc | vlan496   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| pod-1/cl201-eu-spdc | vlan497   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| pod-1/cl201-eu-spdc | vlan498   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| pod-1/cl201-eu-spdc | vlan499   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| pod-1/cl201-eu-spdc | vlan58    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/cl201-eu-spdc | vlan60    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/cl201-eu-spdc | vlan74    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876676 | 
| pod-1/cl201-eu-spdc | vlan80    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/cl201-eu-spdc | vlan88    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/cl201-eu-spdc | vlan9     | up          | up         | bd-control  | bcast  | no        | 9216 | vxlan-16777209 | 
| pod-1/cl202-eu-spdc | vlan12    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023531 | 
| pod-1/cl202-eu-spdc | vlan14    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16121819 | 
| pod-1/cl202-eu-spdc | vlan146   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/cl202-eu-spdc | vlan148   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876654 | 
| pod-1/cl202-eu-spdc | vlan150   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15826914 | 
| pod-1/cl202-eu-spdc | vlan152   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613266 | 
| pod-1/cl202-eu-spdc | vlan164   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15925228 | 
| pod-1/cl202-eu-spdc | vlan182   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/cl202-eu-spdc | vlan186   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15138766 | 
| pod-1/cl202-eu-spdc | vlan192   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15007732 | 
| pod-1/cl202-eu-spdc | vlan282   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580520 | 
| pod-1/cl202-eu-spdc | vlan284   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14680100 | 
| pod-1/cl202-eu-spdc | vlan316   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15171555 | 
| pod-1/cl202-eu-spdc | vlan34    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990757 | 
| pod-1/cl202-eu-spdc | vlan362   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/cl202-eu-spdc | vlan388   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14974941 | 
| pod-1/cl202-eu-spdc | vlan390   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16220083 | 
| pod-1/cl202-eu-spdc | vlan410   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/cl202-eu-spdc | vlan412   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/cl202-eu-spdc | vlan414   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15564707 | 
| pod-1/cl202-eu-spdc | vlan416   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16023498 | 
| pod-1/cl202-eu-spdc | vlan420   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/cl202-eu-spdc | vlan422   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15237079 | 
| pod-1/cl202-eu-spdc | vlan424   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/cl202-eu-spdc | vlan426   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335344 | 
| pod-1/cl202-eu-spdc | vlan428   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15761410 | 
| pod-1/cl202-eu-spdc | vlan430   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368109 | 
| pod-1/cl202-eu-spdc | vlan432   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/cl202-eu-spdc | vlan434   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106004 | 
| pod-1/cl202-eu-spdc | vlan437   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335355 | 
| pod-1/cl202-eu-spdc | vlan439   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/cl202-eu-spdc | vlan441   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/cl202-eu-spdc | vlan465   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-14974945 | 
| pod-1/cl202-eu-spdc | vlan466   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974946 | 
| pod-1/cl202-eu-spdc | vlan467   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15630240 | 
| pod-1/cl202-eu-spdc | vlan468   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007727 | 
| pod-1/cl202-eu-spdc | vlan469   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15695753 | 
| pod-1/cl202-eu-spdc | vlan470   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237063 | 
| pod-1/cl202-eu-spdc | vlan471   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15237064 | 
| pod-1/cl202-eu-spdc | vlan472   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400908 | 
| pod-1/cl202-eu-spdc | vlan473   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15073248 | 
| pod-1/cl202-eu-spdc | vlan482   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15564695 | 
| pod-1/cl202-eu-spdc | vlan483   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15040493 | 
| pod-1/cl202-eu-spdc | vlan484   | up          | up         | bd-external | bcast  | no        | 1500 | vxlan-15663008 | 
| pod-1/cl202-eu-spdc | vlan485   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14843889 | 
| pod-1/cl202-eu-spdc | vlan486   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368123 | 
| pod-1/cl202-eu-spdc | vlan487   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15433637 | 
| pod-1/cl202-eu-spdc | vlan488   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15007742 | 
| pod-1/cl202-eu-spdc | vlan489   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14778380 | 
| pod-1/cl202-eu-spdc | vlan490   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15302600 | 
| pod-1/cl202-eu-spdc | vlan491   | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-14974957 | 
| pod-1/cl202-eu-spdc | vlan492   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089048 | 
| pod-1/cl202-eu-spdc | vlan494   | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/cl202-eu-spdc | vlan6     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14876676 | 
| pod-1/cl202-eu-spdc | vlan9     | up          | up         | bd-control  | bcast  | no        | 9216 | vxlan-16777209 | 
| pod-1/rl301-eu-spdc | vlan10    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/rl301-eu-spdc | vlan12    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942188 | 
| pod-1/rl301-eu-spdc | vlan13    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106014 | 
| pod-1/rl301-eu-spdc | vlan14    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942189 | 
| pod-1/rl301-eu-spdc | vlan15    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/rl301-eu-spdc | vlan16    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106012 | 
| pod-1/rl301-eu-spdc | vlan17    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15597468 | 
| pod-1/rl301-eu-spdc | vlan18    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811132 | 
| pod-1/rl301-eu-spdc | vlan19    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/rl301-eu-spdc | vlan20    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335346 | 
| pod-1/rl301-eu-spdc | vlan21    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15499182 | 
| pod-1/rl301-eu-spdc | vlan22    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15466426 | 
| pod-1/rl301-eu-spdc | vlan23    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15531941 | 
| pod-1/rl301-eu-spdc | vlan24    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368121 | 
| pod-1/rl301-eu-spdc | vlan25    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400882 | 
| pod-1/rl301-eu-spdc | vlan26    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/rl301-eu-spdc | vlan28    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/rl301-eu-spdc | vlan29    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14778362 | 
| pod-1/rl301-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/rl301-eu-spdc | vlan31    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/rl301-eu-spdc | vlan33    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/rl301-eu-spdc | vlan34    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580517 | 
| pod-1/rl301-eu-spdc | vlan36    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/rl301-eu-spdc | vlan37    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/rl301-eu-spdc | vlan38    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/rl301-eu-spdc | vlan39    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/rl301-eu-spdc | vlan41    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/rl301-eu-spdc | vlan9     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15531940 | 
| pod-1/rl302-eu-spdc | vlan10    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957988 | 
| pod-1/rl302-eu-spdc | vlan12    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942188 | 
| pod-1/rl302-eu-spdc | vlan13    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106014 | 
| pod-1/rl302-eu-spdc | vlan14    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14942189 | 
| pod-1/rl302-eu-spdc | vlan15    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15302605 | 
| pod-1/rl302-eu-spdc | vlan16    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811132 | 
| pod-1/rl302-eu-spdc | vlan17    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15957992 | 
| pod-1/rl302-eu-spdc | vlan18    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15106012 | 
| pod-1/rl302-eu-spdc | vlan19    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15499182 | 
| pod-1/rl302-eu-spdc | vlan20    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15597468 | 
| pod-1/rl302-eu-spdc | vlan21    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15335346 | 
| pod-1/rl302-eu-spdc | vlan22    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15466426 | 
| pod-1/rl302-eu-spdc | vlan23    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15368121 | 
| pod-1/rl302-eu-spdc | vlan24    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15400882 | 
| pod-1/rl302-eu-spdc | vlan25    | up          | up         | bd-external | bcast  | no        | 9000 | vxlan-15531941 | 
| pod-1/rl302-eu-spdc | vlan26    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14811140 | 
| pod-1/rl302-eu-spdc | vlan28    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909416 | 
| pod-1/rl302-eu-spdc | vlan29    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14778362 | 
| pod-1/rl302-eu-spdc | vlan30    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16613250 | 
| pod-1/rl302-eu-spdc | vlan32    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-14909414 | 
| pod-1/rl302-eu-spdc | vlan33    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16580517 | 
| pod-1/rl302-eu-spdc | vlan35    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15368120 | 
| pod-1/rl302-eu-spdc | vlan36    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15040489 | 
| pod-1/rl302-eu-spdc | vlan37    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285628 | 
| pod-1/rl302-eu-spdc | vlan38    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16089039 | 
| pod-1/rl302-eu-spdc | vlan39    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15990761 | 
| pod-1/rl302-eu-spdc | vlan41    | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-16285610 | 
| pod-1/rl302-eu-spdc | vlan9     | up          | up         | bd-regular  | bcast  | no        | 9000 | vxlan-15531940 | 
+---------------------+-----------+-------------+------------+-------------+--------+-----------+------+----------------+
```

Developer

```
# iserver get aci intf svi --apic apic11 --node any

{
    "duration": 8092,
    "apic": {
        "read": true,
        "success": 22,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 21,
        "connect_time": 382,
        "disconnect_time": 0,
        "mo_time": 6952,
        "total_time": 7334
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

True	382	-	connect apic11o.emea-sp.cisco.com
True	296	13	apic11o.emea-sp.cisco.com class fabricNode
True	386	38	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	285	61	apic11o.emea-sp.cisco.com class topology/pod-1/node-205/ipv4Addr
True	381	36	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	292	63	apic11o.emea-sp.cisco.com class topology/pod-1/node-206/ipv4Addr
True	481	56	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	304	91	apic11o.emea-sp.cisco.com class topology/pod-1/node-201/ipv4Addr
True	439	55	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	297	90	apic11o.emea-sp.cisco.com class topology/pod-1/node-202/ipv4Addr
True	316	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	342	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-209/ipv4Addr
True	303	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	334	2	apic11o.emea-sp.cisco.com class topology/pod-1/node-210/ipv4Addr
True	370	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	294	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-301/ipv4Addr
True	362	28	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	291	46	apic11o.emea-sp.cisco.com class topology/pod-1/node-302/ipv4Addr
True	300	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	286	23	apic11o.emea-sp.cisco.com class topology/pod-1/node-101/ipv4Addr
True	301	0	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/l2BD query rsp-subtree=full&rsp-subtree-class=sviIf&rsp-subtree-include=required
True	292	22	apic11o.emea-sp.cisco.com class topology/pod-1/node-102/ipv4Addr
```

[[Back]](./InterfaceSvi.md)