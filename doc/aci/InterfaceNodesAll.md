# Node Interface

## All nodes

Usage:
- define name 'any' or 'all' as node name

Example:

```
# iserver get aci intf mgmt --apic apic11 --node any

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

+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Node                | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| pod-1/bl205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:04.036+02:00 | 
| pod-1/bl206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:46.234+02:00 | 
| pod-1/cl201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:02.581+02:00 | 
| pod-1/cl202-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:14:08.264+02:00 | 
| pod-1/cl209-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:55:12.934+02:00 | 
| pod-1/cl210-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T16:55:06.883+02:00 | 
| pod-1/rl301-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:13:40.873+02:00 | 
| pod-1/rl302-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:13:53.167+02:00 | 
| pod-1/s101-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:12:56.045+02:00 | 
| pod-1/s102-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-06-12T09:12:57.357+02:00 | 
+---------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

[[Back]](./Interface.md)