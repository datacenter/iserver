# Node Protocol - LLDP

## Filter by device name

```
# iserver get aci proto lldp --apic apic11 --role leaf --device esx* --view nei

Apic: apic11 (mode:online, cache:on)
Pod: 1
- node: bl205-eu-spdc
- node: bl206-eu-spdc
- node: cl201-eu-spdc
- node: cl202-eu-spdc
- node: cl209-eu-spdc
- node: cl210-eu-spdc
- node: rl301-eu-spdc
- node: rl302-eu-spdc

+---------------------+--------------+-----------+------------------------+-------------------+------+------+-----------------------------------------------+--------------+
| Node                | Interface ID | Hold Time | Neighbor Device        | MAC               | Port | VLAN | Port Description                              | Capabilities |
+---------------------+--------------+-----------+------------------------+-------------------+------+------+-----------------------------------------------+--------------+
| pod-1/rl301-eu-spdc | eth1/27/1    | 180       | esx10-eu-spdc          | 3c:fd:fe:cb:fa:43 |      |      | port 853 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/27/2    | 180       | esx11-eu-spdc          | 3c:fd:fe:cb:ec:eb |      |      | port 851 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/27/3    | 180       | esx12-eu-spdc          | 40:a6:b7:15:53:cb |      |      | port 867 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/27/4    | 180       | esx13-eu-spdc          | 3c:fd:fe:f0:13:0b |      |      | port 865 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/26/1    | 180       | esx6-eu-spdc.cisco.com | 3c:fd:fe:f0:3e:62 |      |      | port 374 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/26/2    | 180       | esx7-eu-spdc.cisco.com | 3c:fd:fe:ef:63:7b |      |      | port 373 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/26/3    | 180       | esx8-eu-spdc.cisco.com | 3c:fd:fe:cb:f5:13 |      |      | port 371 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/26/4    | 180       | esx9-eu-spdc           | 3c:fd:fe:cb:f5:53 |      |      | port 849 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/24/1    | 180       | esx14-eu-spdc          | 3c:fd:fe:cb:a5:6b |      |      | port 986 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/24/2    | 180       | esx1-eu-spdc           | 3c:fd:fe:cb:b0:03 |      |      | port 988 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl301-eu-spdc | eth1/25/1    | 180       | esx2-eu-spdc           | 3c:fd:fe:ce:11:43 |      |      | port 19 on dvSwitch EU-SPDC-R3DC (cswitch)    | bridge       | 
| pod-1/rl301-eu-spdc | eth1/25/2    | 180       | esx3-eu-spdc           | 3c:fd:fe:ce:19:f3 |      |      | port 1 on dvSwitch EU-SPDC-R3DC (cswitch)     | bridge       | 
| pod-1/rl301-eu-spdc | eth1/25/3    | 180       | esx4-eu-spdc           | 3c:fd:fe:ce:1b:13 |      |      | port 512 on dvSwitch EU-SPDC-CDC-22 (cswitch) | bridge       | 
| pod-1/rl301-eu-spdc | eth1/25/4    | 180       | esx5-eu-spdc           | 3c:fd:fe:cb:fa:9b |      |      | port 257 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/25/1    | 180       | esx2-eu-spdc           | 3c:fd:fe:ce:11:42 |      |      | port 18 on dvSwitch EU-SPDC-R3DC (cswitch)    | bridge       | 
| pod-1/rl302-eu-spdc | eth1/25/2    | 180       | esx3-eu-spdc           | 3c:fd:fe:ce:19:f2 |      |      | port 0 on dvSwitch EU-SPDC-R3DC (cswitch)     | bridge       | 
| pod-1/rl302-eu-spdc | eth1/25/3    | 180       | esx4-eu-spdc           | 3c:fd:fe:ce:1b:12 |      |      | port 513 on dvSwitch EU-SPDC-CDC-22 (cswitch) | bridge       | 
| pod-1/rl302-eu-spdc | eth1/25/4    | 180       | esx5-eu-spdc           | 3c:fd:fe:cb:fa:9a |      |      | port 256 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/24/1    | 180       | esx14-eu-spdc          | 3c:fd:fe:cb:a5:6a |      |      | port 987 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/24/2    | 180       | esx1-eu-spdc           | 3c:fd:fe:cb:b0:02 |      |      | port 989 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/26/1    | 180       | esx6-eu-spdc.cisco.com | 3c:fd:fe:f0:3e:63 |      |      | port 375 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/26/2    | 180       | esx7-eu-spdc.cisco.com | 3c:fd:fe:ef:63:7a |      |      | port 372 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/26/3    | 180       | esx12-eu-spdc          | 40:a6:b7:15:53:ca |      |      | port 866 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/26/4    | 180       | esx13-eu-spdc          | 3c:fd:fe:f0:13:0a |      |      | port 864 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/27/1    | 180       | esx10-eu-spdc          | 3c:fd:fe:cb:fa:42 |      |      | port 852 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/27/2    | 180       | esx11-eu-spdc          | 3c:fd:fe:cb:ec:ea |      |      | port 850 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/27/3    | 180       | esx8-eu-spdc.cisco.com | 3c:fd:fe:cb:f5:12 |      |      | port 370 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
| pod-1/rl302-eu-spdc | eth1/27/4    | 180       | esx9-eu-spdc           | 3c:fd:fe:cb:f5:52 |      |      | port 848 on dvSwitch EU-SPDC-R3DC (cswitch)   | bridge       | 
+---------------------+--------------+-----------+------------------------+-------------------+------+------+-----------------------------------------------+--------------+
Interface context: lldp
```

Developer

```
# iserver get aci proto lldp --apic apic11 --role leaf --device esx* --view nei

{
    "duration": 253,
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
    "cache_hits": 10
}
```

[[Back]](./ProtocolLldp.md)