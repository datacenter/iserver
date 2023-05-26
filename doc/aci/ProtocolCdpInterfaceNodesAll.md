# Node Protocol - CDP

## Show CDP interface counters for all nodes

```
# iserver get aci proto cdp --apic apic11 --node any -o intf

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
| pod-1/bl205-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 53133   | 53123       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 53126   | 53132       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 53127   | 53124       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 53132   | 53133       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 53141   | 53146       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 53141   | 53138       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 53142   | 53139       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 53141   | 53137       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 52582   | 52568       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 52573   | 52576       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 52567   | 52560       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 52582   | 52579       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 52583   | 52583       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 52582   | 52578       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 52583   | 52577       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 52583   | 52574       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 53140   | 53138       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 53140   | 53138       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 53140   | 40738       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 53140   | 53137       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 53140   | 53138       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 52781   | 52773       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 53140   | 53136       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 53140   | 53137       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 53125   | 53118       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 53128   | 53120       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 53140   | 53138       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 53140   | 53136       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 53079   | 53021       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 53140   | 53137       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 53140   | 53140       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 53140   | 53136       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 52580   | 52574       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 52580   | 52574       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 52580   | 52573       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 52580   | 52574       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 52222   | 52209       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 52580   | 52573       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 52580   | 52573       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 52566   | 52554       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 52569   | 52556       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 52580   | 52574       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 52580   | 52573       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 52519   | 52457       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 52580   | 52573       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn22-eu-spdc                | 52580   | 52575       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 52581   | 52572       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 53147   | 53145       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 53138   | 53142       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 53139   | 53133       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 53146   | 53148       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 52589   | 52581       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 52588   | 52587       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 52588   | 52576       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 52588   | 52585       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s101-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 53143   | 53146       | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s102-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 37434   | 37431       | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

[[Back]](./ProtocolCdp.md)