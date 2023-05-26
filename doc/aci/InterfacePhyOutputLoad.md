# Node Interface - Physical

## Load interval focused output

```
# iserver get aci intf phy --apic apic11 --node bl205-eu-spdc -o load

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
Node: bl205-eu-spdc

+---------------------+-----------+------+-----------------+-----------------+-----------------+
| Node                | Interface | Oper | Load Interval 1 | Load Interval 2 | Load Interval 3 |
+---------------------+-----------+------+-----------------+-----------------+-----------------+
| pod-1/bl205-eu-spdc | 1/1       | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/2       | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/3       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/4       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/5       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/6       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/7       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/8       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/9       | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/10      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/11      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/12      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/13      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/14      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/15      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/16      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/17      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/18      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/19      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/20      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/21      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/22      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/23      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/24      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/25      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/26      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/27      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/28      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/29      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/30      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/31      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/32      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/33      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/34      | down | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/35      | up   | 30              | 300             | 0               | 
| pod-1/bl205-eu-spdc | 1/36      | up   | 30              | 300             | 0               | 
+---------------------+-----------+------+-----------------+-----------------+-----------------+
```

[[Back]](./InterfacePhy.md)