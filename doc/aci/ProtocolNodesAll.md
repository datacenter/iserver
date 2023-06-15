# Node Protocol

## All nodes

Usage:
- define name 'any' or 'all' as node name

Example:

```
# iserver get aci proto cdp --apic apic11 --node any --view intf

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

+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| Node                | Interface ID | Admin State | Oper State | Count | Neighbors                    | v2 Sent | v2 Received | v1 Sent | v2 Received | Failed Sent | Checksum Error | Malformed | Unsupported Version |
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
| pod-1/bl205-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl205-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/1       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/11      | enabled     | up         | 1     | HX1-eu-spdc-A                | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/12      | enabled     | up         | 1     | HX1-eu-spdc-B                | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/2       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/24      | enabled     | up         | 1     | ipn-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/27      | enabled     | up         | 1     | Yavin-129                    | 2752    | 2750        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | eth1/28      | enabled     | up         | 1     | Lisboa-54                    | 2752    | 2753        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/bl206-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 2726    | 2720        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/36      | enabled     | up         | 2     | esx12-eu-spdc, esx12-eu-spdc | 2728    | 5438        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 2726    | 2721        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 2729    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn21-eu-spdc                | 2755    | 2754        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl201-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/34      | enabled     | up         | 1     | esx14-eu-spdc                | 2726    | 2721        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/35      | enabled     | up         | 1     | esx13-eu-spdc                | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/37      | enabled     | up         | 1     | esx11-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/38      | enabled     | up         | 1     | esx10-eu-spdc                | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/39      | enabled     | up         | 1     | esx9-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/40      | enabled     | up         | 1     | esx8-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/41      | enabled     | up         | 1     | esx1-eu-spdc                 | 2726    | 2721        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/42      | enabled     | up         | 1     | esx2-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/43      | enabled     | up         | 1     | esx3-eu-spdc                 | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/44      | enabled     | up         | 1     | esx4-eu-spdc                 | 2729    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/45      | enabled     | up         | 1     | esx5-eu-spdc                 | 2728    | 2718        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/46      | enabled     | up         | 1     | esx6-eu-spdc.cisco.com       | 2728    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/47      | enabled     | up         | 1     | esx7-eu-spdc.cisco.com       | 2729    | 2719        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | eth1/96      | enabled     | up         | 1     | ipn22-eu-spdc                | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/cl202-eu-spdc | mgmt0        | enabled     | up         | 1     | r22-eu-spdc                  | 2752    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl301-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/29      | enabled     | up         | 1     | Berlin-35.cisco.com          | 2752    | 2753        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/3       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-B           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | eth1/4       | enabled     | up         | 1     | FI-ucsb1-eu-spdc-A           | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/rl302-eu-spdc | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2751    | 2751        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s101-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2753    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
| pod-1/s102-eu-spdc  | mgmt0        | enabled     | up         | 1     | r23-eu-spdc                  | 2752    | 2752        | 0       | 0           | 0           | 0              | 0         | 0                   | 
+---------------------+--------------+-------------+------------+-------+------------------------------+---------+-------------+---------+-------------+-------------+----------------+-----------+---------------------+
```

[[Back]](./Protocol.md)