# MAC Table

## Filter by vlan

```
# iserver get nx mac --device ipn11 --vlan 50

Device: ipn11

MAC [#31]
---------

+--------+------+----------------+---------+-----+-----+------+------+
| Device | VLAN | MAC            | Type    | Age | Sec | Ntfy | Port |
+--------+------+----------------+---------+-----+-----+------+------+
| ipn11  | 50   | 000c.2989.2224 | dynamic | 0   | F   | F    | Po14 | 
| ipn11  | 50   | 0050.56b2.0b65 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.1237 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.3818 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.4ec8 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.4fc8 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.5807 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.5b66 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.6eeb | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.7c63 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.83cd | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.88a1 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.8a8e | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.8e36 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.9759 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.ae7d | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.c4ce | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.d570 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.d647 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.d68e | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.d727 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.dcda | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.e844 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.fa48 | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b2.fe4a | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 0050.56b4.f2ce | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 00a3.8eeb.b33f | dynamic | 0   | F   | F    | Po5  | 
| ipn11  | 50   | 500f.80dd.dbba | dynamic | 0   | F   | F    | Po14 | 
| ipn11  | 50   | 500f.80de.222e | dynamic | 0   | F   | F    | Po14 | 
| ipn11  | 50   | 54a2.7424.60a0 | dynamic | 0   | F   | F    | Po14 | 
| ipn11  | 50   | 84f1.4762.b366 | dynamic | 0   | F   | F    | Po14 | 
+--------+------+----------------+---------+-----+-----+------+------+

Filter: mac, vlan
View:   state (def)
```

Developer

```
# iserver get nx mac --device ipn11 --vlan 50

{
    "duration": 3040,
    "nexus": {
        "read": true,
        "success": 3,
        "failed": 0,
        "connect": 2,
        "disconnect": 0,
        "mo": 1,
        "connect_time": 2303,
        "disconnect_time": 0,
        "mo_time": 429,
        "total_time": 2732
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

Log: nexus
-----------

2023-12-08 16:46:52.323776	True	2301	connect ipn11.emea-sp.cisco.com
2023-12-08 16:46:52.758091	True	429	ipn11.emea-sp.cisco.com show mac address-table
2023-12-08 16:46:52.940675	True	2	disconnect ipn11.emea-sp.cisco.com
```

[[Back]](./Mac.md)