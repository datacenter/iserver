# Intersight Chassis

## psuc view

```
# iserver get chassis -v psuc

iaccount isctl (cache: off)
Select chassis...
Selected chassis: 4
Collect chassis api objects...

PSU Control [#4]
----------------

+--------------------------+--------------------+---------------------+-------------------+-----------------+
| Chassis                  | Input Power Health | Output Power Health | Redundancy Health | Redundancy Mode |
+--------------------------+--------------------+---------------------+-------------------+-----------------+
| ynas-eu-spdc-FOX2034GCLV | --                 | --                  | --                | --              | 
| ucsx-eu-spdc-1           | V                  | V                   | V                 | Grid            | 
| FI-ucsb1-eu-spdc-1       | V                  | V                   | V                 | n+1             | 
| FI-ucsb1-eu-spdc-2       | V                  | V                   | V                 | n+1             | 
+--------------------------+--------------------+---------------------+-------------------+-----------------+

Power Control [#4]
------------------

+--------------------------+-----------+--------------+-----------------+--------------+---------+---------+-----------------------------+----------------------+-----------------+-----------------+
| Chassis                  | Save Mode | Ext Capacity | Dyn Rebalancing | Alloc Budget | Max Req | Min Req | Max Avail Non-Redundant (N) | Max Avail Grid (N+N) | Max Avail (N+1) | Max Avail (N+2) |
+--------------------------+-----------+--------------+-----------------+--------------+---------+---------+-----------------------------+----------------------+-----------------+-----------------+
| ynas-eu-spdc-FOX2034GCLV | --        | --           | --              | --           | --      | --      | --                          | --                   | --              | --              | 
| ucsx-eu-spdc-1           | Disabled  | Enabled      | Enabled         | --           | 6680 W  | 3773 W  | 15218 W                     | 10500 W              | 17500 W         | 14000 W         | 
| FI-ucsb1-eu-spdc-1       | Disabled  | Enabled      | Enabled         | --           | 2812 W  | 2100 W  | 0 W                         | 0 W                  | 0 W             | 0 W             | 
| FI-ucsb1-eu-spdc-2       | Disabled  | Enabled      | Enabled         | --           | 2900 W  | 2100 W  | 0 W                         | 0 W                  | 0 W             | 0 W             | 
+--------------------------+-----------+--------------+-----------------+--------------+---------+---------+-----------------------------+----------------------+-----------------+-----------------+

Filter: name, serial, model
View:   state (def), adv, alarm, contract, istate, node, fi, io, exp, port, net, fan, psu, psuc, hw, inv
```

Developer

```
# iserver get chassis -v psuc

{
    "duration": 9650,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 7375
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
        "lines": 5
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 14:35:43.795746	True	2548	4	isctl get equipment chassis  --expand "RegisteredDevice" -o json --top 100
2023-12-03 14:35:46.589146	True	2774	3	isctl get equipment psucontrol --filter "Parent/Moid in ('61bb973576752d3139b05c2e', '64be876876752d39013ea7f4', '6501db4b76752d3901eb37bf', '6501db4b76752d3901eb37c1')"  -o json --top 100
2023-12-03 14:35:48.651587	True	2053	3	isctl get power controlstate --filter "Parent/Moid in ('61bb973576752d3139b05c2e', '64be876876752d39013ea7f4', '6501db4b76752d3901eb37bf', '6501db4b76752d3901eb37c1')"  -o json --top 100
```

[[Back]](./ChassisInventory.md)