# Intersight Chassis

## io view

```
# iserver get chassis -v io

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

I/O Module [#6]
---------------

+--------------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+
| Chassis            | I/O Module      | Path | Presence | OperState | Model            | Serial      | P/N         | Version | Vendor            | Host Ports | Network Ports | Fans |
+--------------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+
| ucsx-eu-spdc-1     | I/O #1 (top)    | B    | equipped | V         | UCSX-I-9108-100G | FCH26417CDN | 73-20854-02 | 4.2(3c) | Cisco Systems Inc | 29         | 3             | 3    | 
| ucsx-eu-spdc-1     | I/O #2 (bottom) | A    | equipped | V         | UCSX-I-9108-100G | FCH26417CF0 | 73-20854-02 | 4.3(2a) | Cisco Systems Inc | 3          | 3             | 3    | 
| FI-ucsb1-eu-spdc-1 | I/O #1 (left)   | A    | equipped | V         | UCS-IOM-2408     | FCH24107GFQ | 73-19127-05 | 4.2(3c) | Cisco Systems Inc | 0          | 0             | 0    | 
| FI-ucsb1-eu-spdc-1 | I/O #2 (right)  | B    | equipped | V         | UCS-IOM-2408     | FCH24107GK5 | 73-19127-05 | 4.2(3c) | Cisco Systems Inc | 0          | 0             | 0    | 
| FI-ucsb1-eu-spdc-2 | I/O #1 (left)   | A    | equipped | V         | UCS-IOM-2408     | FCH24107G7R | 73-19127-05 | 4.2(3c) | Cisco Systems Inc | 0          | 0             | 0    | 
| FI-ucsb1-eu-spdc-2 | I/O #2 (right)  | B    | equipped | V         | UCS-IOM-2408     | FCH24107GJK | 73-19127-05 | 4.2(3c) | Cisco Systems Inc | 0          | 0             | 0    | 
+--------------------+-----------------+------+----------+-----------+------------------+-------------+-------------+---------+-------------------+------------+---------------+------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis -v io

{
    "duration": 6787,
    "isctl": {
        "read": true,
        "calls": 2,
        "success": 2,
        "failed": 0,
        "total_time": 4736
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
        "read": true,
        "lines": 4
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:32:55.823508	True	2503	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:32:58.068612	True	2233	6	isctl get equipment iocard --filter "EquipmentChassis/Moid in ('61bb973576752d3139b05c2e', '64be876876752d39013ea7f4', '6501db4b76752d3901eb37bf', '6501db4b76752d3901eb37c1')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)