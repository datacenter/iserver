# Link Aggregation Control Protocol (LACP)

## JSON output

```
# iserver get nx lacp --device ipn11 -o json

[
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel5",
        "port": [
            {
                "port": "Ethernet1/33",
                "partner_system_id": "32768,0-a3-8e-eb-b3-3f",
                "partner_port_num": "0x311",
                "partner_age": 12274296,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0x4",
                "partner_port_state": "0x3d",
                "partner_mac": "00:a3:8e:eb:b3:3f"
            },
            {
                "port": "Ethernet1/34",
                "partner_system_id": "32768,0-a3-8e-eb-b3-3f",
                "partner_port_num": "0x315",
                "partner_age": 12274295,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0x4",
                "partner_port_state": "0x3d",
                "partner_mac": "00:a3:8e:eb:b3:3f"
            }
        ]
    },
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel11",
        "port": [
            {
                "port": "Ethernet1/32/1",
                "partner_system_id": "32768,d0-9-c8-50-dd-ff",
                "partner_port_num": "0x1c9",
                "partner_age": 12274301,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0xa",
                "partner_port_state": "0x3d",
                "partner_mac": "d0:09:c8:50:dd:ff"
            }
        ]
    },
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel12",
        "port": [
            {
                "port": "Ethernet1/32/2",
                "partner_system_id": "32768,d0-9-c8-50-b3-3f",
                "partner_port_num": "0x1c9",
                "partner_age": 12274300,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0xb",
                "partner_port_state": "0x2065723d",
                "partner_mac": "d0:09:c8:50:b3:3f"
            }
        ]
    },
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel13",
        "port": [
            {
                "port": "Ethernet1/32/3",
                "partner_system_id": "32768,d0-9-c8-50-e0-87",
                "partner_port_num": "0x1c9",
                "partner_age": 12274299,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0xc",
                "partner_port_state": "0x3d",
                "partner_mac": "d0:09:c8:50:e0:87"
            }
        ]
    },
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel14",
        "port": [
            {
                "port": "Ethernet1/32/4",
                "partner_system_id": "32768,d0-9-c8-50-ad-f",
                "partner_port_num": "0x1c9",
                "partner_age": 12274300,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0xd",
                "partner_port_state": "0x3d",
                "partner_mac": "d0:09:c8:50:ad:0f"
            }
        ]
    },
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel100",
        "port": [
            {
                "port": "Ethernet1/35",
                "partner_system_id": "32768,a0-b4-39-71-f6-d3",
                "partner_port_num": "0x189",
                "partner_age": 12188026,
                "partner_flags": "SA",
                "partner_port_priority": 32768,
                "partner_oper_key": "0x63",
                "partner_port_state": "0x3d",
                "partner_mac": "a0:b4:39:71:f6:d3"
            }
        ]
    },
    {
        "__Output": {},
        "nexus_name": "ipn11",
        "interface": "port-channel800",
        "port": [
            {
                "port": "Ethernet1/3",
                "partner_system_id": "65535,14-a2-a0-ec-75-4",
                "partner_port_num": "0x1",
                "partner_age": 171066,
                "partner_flags": "SA",
                "partner_port_priority": 255,
                "partner_oper_key": "0x17",
                "partner_port_state": "0x2e37003d",
                "partner_mac": "14:a2:a0:ec:75:04"
            }
        ]
    }
]
```

[[Back]](./Lldp.md)