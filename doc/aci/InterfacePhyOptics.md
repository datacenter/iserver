# Node Interface - Physical

## Filter by transceiver optics

```
# iserver get aci intf phy
    --apic apic11
    --node bl205-eu-spdc
    --optics xfp -o trans

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+---------+----------+--------+---------------+---------------+------------------+------+---------------+
| Node                | Interface | Oper | Present | State    | Optics | Name          | Type          | PN               | Rev  | SN            |
+---------------------+-----------+------+---------+----------+--------+---------------+---------------+------------------+------+---------------+
| pod-1/bl205-eu-spdc | 1/27      | up   | yes     | inserted | xfp    | CISCO-AVAGO   | SFP-10G-LR    | SFCT-739SMZ      | G3.1 | AVD2047K5FA   | 
| pod-1/bl205-eu-spdc | 1/28      | up   | yes     | inserted | xfp    | CISCO-FINISAR | SFP-10G-AOC1M | FCBG110SD1C01-CS | A    | FIW205300M9-B | 
+---------------------+-----------+------+---------+----------+--------+---------------+---------------+------------------+------+---------------+
```

[[Back]](./InterfacePhy.md)