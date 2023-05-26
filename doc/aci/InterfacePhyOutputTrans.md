# Node Interface - Physical

## Transceiver focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o trans

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+----------+---------+-----------------+-----------------+------------------+------+---------------+
| Node                | Interface | Oper | Present | State    | Optics  | Name            | Type            | PN               | Rev  | SN            |
+---------------------+-----------+------+---------+----------+---------+-----------------+-----------------+------------------+------+---------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | yes     | inserted | qsfp    | CISCO-AVAGO     | QSFP-40G-SR-BD  | AFBR-79EBPZ-CS1  | 01Bh | AVM1814S1HN   | 
| pod-1/bl205-eu-spdc | 1/2       | up   | yes     | inserted | qsfp    | CISCO-AVAGO     | QSFP-40G-SR-BD  | AFBR-79EBPZ-CS2  | 01Bh | AVM2118U15C   | 
| pod-1/bl205-eu-spdc | 1/3       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/4       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/5       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/6       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/7       | down | yes     | inserted | qsfp    | CISCO-AVAGO     | QSFP-40G-SR-BD  | AFBR-79EBPZ-CS2  | 01Bh | AVM2118U1G0   | 
| pod-1/bl205-eu-spdc | 1/8       | down | yes     | inserted | qsfp    | CISCO-AVAGO     | QSFP-40G-SR-BD  | AFBR-79EBPZ-CS2  | 01Bh | AVM2043U142   | 
| pod-1/bl205-eu-spdc | 1/9       | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/10      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/11      | up   | yes     | inserted | qsfp    | CISCO-AVAGO     | QSFP-40G-SR-BD  | AFBR-79EBPZ-CS2  | 01Bh | AVM2043U141   | 
| pod-1/bl205-eu-spdc | 1/12      | up   | yes     | inserted | qsfp    | CISCO-AVAGO     | QSFP-40G-SR-BD  | AFBR-79EBPZ-CS2  | 01Bh | AVM2043U120   | 
| pod-1/bl205-eu-spdc | 1/13      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/14      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/15      | up   | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01   | AVE1828E0TW-B | 
| pod-1/bl205-eu-spdc | 1/16      | up   | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01   | AVE1828E0UF-A | 
| pod-1/bl205-eu-spdc | 1/17      | down | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01   | AVE1828E0VF-B | 
| pod-1/bl205-eu-spdc | 1/18      | down | yes     | inserted | qsfp    | CISCO           | QSFP-H40G-AOC7M | AFBR-7QER07Z-CS1 | 01   | AVE1828E0U5-A | 
| pod-1/bl205-eu-spdc | 1/19      | up   | yes     | inserted | qsfp    | CISCO-DELTA     | QSFP-H40G-AOC3M | QAOC-40G4F1A03-C | A    | DTS2219A015-A | 
| pod-1/bl205-eu-spdc | 1/20      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/21      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/22      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/23      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/24      | up   | yes     | inserted | qsfp28  | CISCO-INNOLIGHT | QSFP-100G-AOC3M | TF-FC003-NC2     | 1B   | INL24358586-A | 
| pod-1/bl205-eu-spdc | 1/25      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/26      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/27      | up   | yes     | inserted | xfp     | CISCO-AVAGO     | SFP-10G-LR      | SFCT-739SMZ      | G3.1 | AVD2047K5FA   | 
| pod-1/bl205-eu-spdc | 1/28      | up   | yes     | inserted | xfp     | CISCO-FINISAR   | SFP-10G-AOC1M   | FCBG110SD1C01-CS | A    | FIW205300M9-B | 
| pod-1/bl205-eu-spdc | 1/29      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/30      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/31      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/32      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/33      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/34      | down | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/35      | up   | no      | removed  | unknown |                 |                 |                  |      |               | 
| pod-1/bl205-eu-spdc | 1/36      | up   | no      | removed  | unknown |                 |                 |                  |      |               | 
+---------------------+-----------+------+---------+----------+---------+-----------------+-----------------+------------------+------+---------------+
```

[[Back]](./InterfacePhy.md)