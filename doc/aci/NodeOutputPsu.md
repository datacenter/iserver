# Node

## PSU specific output

```
# iserver get aci node --apic apic11 --view psu

Apic: apic11 (mode:online, cache:off)

Node - PSU [#13]
----------------

+---------------------+-------------+-----------------+-------------------+---------------+---------+---------+------------+
| Node                | PSU Slot ID | Description     | Model             | Serial Number | Current | Voltage | Oper State |
+---------------------+-------------+-----------------+-------------------+---------------+---------+---------+------------+
| pod-1/apic1         | 5           | FRU_PSU1 (ID 4) | UCSC-PSU1-770W    | APS234101KU   | 0.0     | 12.0    | ok         | 
| pod-1/apic1         | 6           | FRU_PSU2 (ID 5) | UCSC-PSU1-770W    | APS23480229   | 0.0     | 12.0    | ok         | 
| pod-1/apic2         | 5           | FRU_PSU1 (ID 4) | UCSC-PSU1-770W    | APS234101K8   | 0.0     | 12.0    | ok         | 
| pod-1/apic2         | 6           | FRU_PSU2 (ID 5) | UCSC-PSU1-770W    | APS23480226   | 0.0     | 12.0    | ok         | 
| pod-1/apic3         | 5           | FRU_PSU1 (ID 4) | UCSC-PSU1-770W    | APS234101K1   | 0.0     | 12.0    | ok         | 
| pod-1/apic3         | 6           | FRU_PSU2 (ID 5) | UCSC-PSU1-770W    | APS23480228   | 0.0     | 12.0    | ok         | 
| pod-1/bl205-eu-spdc | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2330F8ZA   | 0.0     | 12.0    | ok         | 
| pod-1/bl205-eu-spdc | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2330F96G   | 0.0     | 12.0    | ok         | 
| pod-1/bl206-eu-spdc | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2429FCTC   | 0.0     | 12.0    | ok         | 
| pod-1/bl206-eu-spdc | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2429FCSK   | 0.0     | 12.0    | ok         | 
| pod-1/cl201-eu-spdc | 1           | PSU             | NXA-PAC-1200W-PE  | LIT23103NFN   | 0.0     | 12.0    | ok         | 
| pod-1/cl201-eu-spdc | 2           | PSU             | NXA-PAC-1200W-PE  | LIT23103NJH   | 0.0     | 12.0    | ok         | 
| pod-1/cl202-eu-spdc | 1           | PSU             | NXA-PAC-1200W-PE  | LIT23103NEJ   | 0.0     | 12.0    | ok         | 
| pod-1/cl202-eu-spdc | 2           | PSU             | NXA-PAC-1200W-PE  | LIT23103NKC   | 0.0     | 12.0    | ok         | 
| pod-1/cl209-eu-spdc | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2714FCN3   | 0.0     | 12.0    | ok         | 
| pod-1/cl209-eu-spdc | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2714FDAV   | 0.0     | 12.0    | ok         | 
| pod-1/cl210-eu-spdc | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2714FDAU   | 0.0     | 12.0    | ok         | 
| pod-1/cl210-eu-spdc | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2714FDCJ   | 0.0     | 12.0    | ok         | 
| pod-1/rl301-eu-spdc | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2338F0XZ   | 0.0     | 12.0    | ok         | 
| pod-1/rl301-eu-spdc | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2338F0UG   | 0.0     | 12.0    | ok         | 
| pod-1/rl302-eu-spdc | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2338F0RF   | 0.0     | 12.0    | ok         | 
| pod-1/rl302-eu-spdc | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2335FBHW   | 0.0     | 12.0    | ok         | 
| pod-1/s101-eu-spdc  | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2329F90Z   | 0.0     | 12.0    | ok         | 
| pod-1/s101-eu-spdc  | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2329F96A   | 0.0     | 12.0    | ok         | 
| pod-1/s102-eu-spdc  | 1           | PSU             | NXA-PAC-1100W-PE2 | ART2329F96C   | 0.0     | 12.0    | ok         | 
| pod-1/s102-eu-spdc  | 2           | PSU             | NXA-PAC-1100W-PE2 | ART2329F90C   | 0.0     | 12.0    | ok         | 
+---------------------+-------------+-----------------+-------------------+---------------+---------+---------+------------+
```

Developer

```
# iserver get aci node --apic apic11 --view psu

{
    "duration": 1081,
    "apic": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 1,
        "disconnect": 0,
        "mo": 2,
        "connect_time": 378,
        "disconnect_time": 0,
        "mo_time": 580,
        "total_time": 958
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

True	378	-	connect apic11o.emea-sp.cisco.com:443
True	297	13	apic11o.emea-sp.cisco.com:443 class fabricNode
True	283	26	apic11o.emea-sp.cisco.com:443 class eqptPsu
```

[[Back]](./Node.md)