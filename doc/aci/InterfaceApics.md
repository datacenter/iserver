# Node Interface

## Multi-APIC node selection

Usage:
- define apic name as 'any' or 'all'
- define apic name in 'dom:<domain>' format where domain value is defined in [controller](./Controller.md) entries

Note:
- node name value defaults to 'any' unless defined by the user

Example:

```
# iserver get aci intf mgmt --apic dom:milan --node any

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
Apic: apic21o.emea-sp.cisco.com
Pod: 1
- node: bl2205-eu-spdc
- node: bl2206-eu-spdc
- node: cl2201-eu-spdc
- node: cl2202-eu-spdc
- node: cl2207-eu-spdc
- node: cl2208-eu-spdc
- node: rl2701-eu-spdc
- node: rl2702-eu-spdc
- node: s2101-eu-spdc
- node: s2102-eu-spdc

+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| Apic   | Node                 | Name  | Admin State | Switching State | OperState | Auto Negotiation | Duplex | MTU  | Speed | Last Link State Change        |
+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
| apic11 | pod-1/bl205-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:13:34.502+02:00 | 
| apic11 | pod-1/bl206-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:37:10.362+02:00 | 
| apic11 | pod-1/cl201-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:15:14.143+02:00 | 
| apic11 | pod-1/cl202-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:39:11.176+02:00 | 
| apic11 | pod-1/rl301-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:10:01.724+02:00 | 
| apic11 | pod-1/rl302-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T10:33:50.626+02:00 | 
| apic11 | pod-1/s101-eu-spdc   | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-03T01:12:44.643+02:00 | 
| apic11 | pod-1/s102-eu-spdc   | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-04-28T11:27:42.302+02:00 | 
| apic21 | pod-1/bl2205-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:42:07.364+02:00 | 
| apic21 | pod-1/bl2206-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:20:58.587+02:00 | 
| apic21 | pod-1/cl2201-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:40:11.007+02:00 | 
| apic21 | pod-1/cl2202-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:18:48.158+02:00 | 
| apic21 | pod-1/cl2207-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:39:24.929+02:00 | 
| apic21 | pod-1/cl2208-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:18:36.886+02:00 | 
| apic21 | pod-1/rl2701-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:44:47.287+02:00 | 
| apic21 | pod-1/rl2702-eu-spdc | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:18:07.223+02:00 | 
| apic21 | pod-1/s2101-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T20:35:07.559+02:00 | 
| apic21 | pod-1/s2102-eu-spdc  | mgmt0 | up          | disabled        | up        | on               | full   | 1500 | 1G    | 2023-03-02T21:14:04.440+02:00 | 
+--------+----------------------+-------+-------------+-----------------+-----------+------------------+--------+------+-------+-------------------------------+
```

[[Back]](./Interface.md)