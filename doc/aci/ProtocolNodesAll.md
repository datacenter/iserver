# Node Protocol

## All nodes

Usage:
- define name 'any' or 'all' as node name

Example:

```
# iserver get aci proto cdp --apic apic11 --node any --view intf

Apic: apic11
Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc
- node: s101-eu-spdc
- node: s102-eu-spdc

+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors                    | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/bl205-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 62220   | 62210       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 62213   | 62220       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 62214   | 62211       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 62219   | 62221       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 62228   | 62234       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 62228   | 62226       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 62229   | 62226       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 62228   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 61670   | 61655       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 61661   | 61664       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 61655   | 61647       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 61670   | 61667       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 61671   | 61671       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 61670   | 61666       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 61671   | 61664       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 61671   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 62227   | 58912       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 61869   | 61860       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 62213   | 62206       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 62216   | 62207       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 62227   | 62224       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 62167   | 62108       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 62227   | 62225       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 62227   | 62227       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 62228   | 62223       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 61310   | 61296       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 61654   | 61642       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 61657   | 61643       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 61607   | 61544       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 61668   | 61661       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn22-eu-spdc                | 61668   | 61662       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 61668   | 61659       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 62235   | 62232       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 62225   | 62230       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 62226   | 62219       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 62234   | 62236       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 61677   | 61668       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 61676   | 61674       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 61676   | 61662       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 61676   | 61672       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s101-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 62230   | 62233       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s102-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 46522   | 46519       | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

[[Back]](./Protocol.md)