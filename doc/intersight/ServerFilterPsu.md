# Intersight Server

## Filter by psu

Supported filtering rules:
- state:on selects servers with at least one psu on
- state:off selects servers with at least one psu off
- serial:pattern selects servers with psu serial number matching pattern
- model:pattern selects servers with psu serial number matching model

Multiple psu filters follow AND logic.

Select psu off

```
# iserver get server --psu state:off -v psu

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#6]
--------

+------------------------------+--------+-------+---------+---------+-------------------+-------------+-------------------+
| Server                       | Name   | State | Present | Voltage | Model             | Serial      | Vendor            |
+------------------------------+--------+-------+---------+---------+-------------------+-------------+-------------------+
| aio-2-p1-eu-spdc-WZP22520Y69 | PSU #1 | X     | X       | unknown |                   |             |                   | 
| aio-2-p1-eu-spdc-WZP22520Y69 | PSU #2 | X     | X       | unknown |                   |             |                   | 
| berlin-ucsm-5                | PSU #1 | X     | X       | unknown |                   |             |                   | 
| berlin-ucsm-5                | PSU #2 | V     | V       | ok      | UCSC-PSU2V2-1200W | DCH1853T0LH | Cisco Systems Inc | 
| wnas-eu-spdc-FCH2008V230     | PSU #1 | X     | V       | unknown | DPST-1200DB A     | DCH2003T1MD | Cisco Systems Inc | 
| wnas-eu-spdc-FCH2008V230     | PSU #2 | X     | V       | unknown | DPST-1200DB A     | DCH1952T09D | Cisco Systems Inc | 
+------------------------------+--------+-------+---------+---------+-------------------+-------------+-------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Select psu serial

```
# iserver get server --psu serial:*2338* -v psu

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#8]
--------

+-------------------------------+--------+-------+---------+---------+------------+-------------+-------------------+
| Server                        | Name   | State | Present | Voltage | Model      | Serial      | Vendor            |
+-------------------------------+--------+-------+---------+---------+------------+-------------+-------------------+
| aio3-p5g-eu-spdc-WZP23450C8K  | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382CHD | Cisco Systems Inc | 
| aio3-p5g-eu-spdc-WZP23450C8K  | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382DAH | Cisco Systems Inc | 
| comp0-p2a-eu-spdc-WZP23450C8M | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382CJH | Cisco Systems Inc | 
| comp0-p2a-eu-spdc-WZP23450C8M | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382CHN | Cisco Systems Inc | 
| esx91-eu-spdc-WZP234411LW     | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382D76 | Cisco Systems Inc | 
| esx91-eu-spdc-WZP234411LW     | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382D6K | Cisco Systems Inc | 
| snas-eu-spdc-WZP23450C7D      | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382DS3 | Cisco Systems Inc | 
| snas-eu-spdc-WZP23450C7D      | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382DFR | Cisco Systems Inc | 
+-------------------------------+--------+-------+---------+---------+------------+-------------+-------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Select psu model

```
# iserver get server --psu model:*2162* -v psu

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#24]
---------

+-------------------------------+--------+-------+---------+---------+----------------------+-------------+-------------------+
| Server                        | Name   | State | Present | Voltage | Model                | Serial      | Vendor            |
+-------------------------------+--------+-------+---------+---------+----------------------+-------------+-------------------+
| aio3-p5g-eu-spdc-WZP23450C8K  | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT23382CHD | Cisco Systems Inc | 
| aio3-p5g-eu-spdc-WZP23450C8K  | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT23382DAH | Cisco Systems Inc | 
| C480-FCH2149W029              | PSU #1 | V     | V       | ok      | CIS-S-1600ADE000-301 | PST2227J0WN | Cisco Systems Inc | 
| C480-FCH2149W029              | PSU #2 | V     | V       | ok      | CIS-S-1600ADE000-301 | PST2227J0NS | Cisco Systems Inc | 
| C480-FCH2149W029              | PSU #3 | V     | V       | ok      | PS-2162-9S           | LIT2549A4YS | Cisco Systems Inc | 
| C480-FCH2149W029              | PSU #4 | V     | V       | ok      | PS-2162-9S           | LIT2549A55E | Cisco Systems Inc | 
| comp0-p2a-eu-spdc-WZP23450C8M | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT23382CJH | Cisco Systems Inc | 
| comp0-p2a-eu-spdc-WZP23450C8M | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT23382CHN | Cisco Systems Inc | 
| comp1-p4b-eu-spdc-WZP26360D36 | PSU #1 | V     | V       | ok      | PS-2162-9S           | LKH261423VE | Cisco Systems Inc | 
| comp1-p4b-eu-spdc-WZP26360D36 | PSU #2 | V     | V       | ok      | PS-2162-9S           | LKH261422ZW | Cisco Systems Inc | 
| comp2-p4b-eu-spdc-WZP26360D3D | PSU #1 | V     | V       | ok      | PS-2162-9S           | LKH2613226Y | Cisco Systems Inc | 
| comp2-p4b-eu-spdc-WZP26360D3D | PSU #2 | V     | V       | ok      | PS-2162-9S           | LKH261324Y4 | Cisco Systems Inc | 
| esx91-eu-spdc-WZP234411LW     | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT23382D76 | Cisco Systems Inc | 
| esx91-eu-spdc-WZP234411LW     | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT23382D6K | Cisco Systems Inc | 
| NX1-S1-eu-spdc-WZP24100SMV    | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT23472544 | Cisco Systems Inc | 
| NX1-S1-eu-spdc-WZP24100SMV    | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT234724Q3 | Cisco Systems Inc | 
| NX1-S2-eu-spdc-WZP24100SN0    | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT2347257V | Cisco Systems Inc | 
| NX1-S2-eu-spdc-WZP24100SN0    | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT23422GUM | Cisco Systems Inc | 
| NX1-S3-eu-spdc-WZP24100SML    | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT234726DX | Cisco Systems Inc | 
| NX1-S3-eu-spdc-WZP24100SML    | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT234724NZ | Cisco Systems Inc | 
| NX1-S4-eu-spdc-WZP24100SMP    | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT234724SZ | Cisco Systems Inc | 
| NX1-S4-eu-spdc-WZP24100SMP    | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT23422G3M | Cisco Systems Inc | 
| snas-eu-spdc-WZP23450C7D      | PSU #1 | V     | V       | ok      | PS-2162-9S           | LIT23382DS3 | Cisco Systems Inc | 
| snas-eu-spdc-WZP23450C7D      | PSU #2 | V     | V       | ok      | PS-2162-9S           | LIT23382DFR | Cisco Systems Inc | 
+-------------------------------+--------+-------+---------+---------+----------------------+-------------+-------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Select psu model and serial

```
# iserver get server --psu model:*2162* --psu serial:*2338* -v psu

iaccount isctl (cache: off)
Select servers...
Selected servers: 121
Collect server api objects...


PSU [#8]
--------

+-------------------------------+--------+-------+---------+---------+------------+-------------+-------------------+
| Server                        | Name   | State | Present | Voltage | Model      | Serial      | Vendor            |
+-------------------------------+--------+-------+---------+---------+------------+-------------+-------------------+
| aio3-p5g-eu-spdc-WZP23450C8K  | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382CHD | Cisco Systems Inc | 
| aio3-p5g-eu-spdc-WZP23450C8K  | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382DAH | Cisco Systems Inc | 
| comp0-p2a-eu-spdc-WZP23450C8M | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382CJH | Cisco Systems Inc | 
| comp0-p2a-eu-spdc-WZP23450C8M | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382CHN | Cisco Systems Inc | 
| esx91-eu-spdc-WZP234411LW     | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382D76 | Cisco Systems Inc | 
| esx91-eu-spdc-WZP234411LW     | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382D6K | Cisco Systems Inc | 
| snas-eu-spdc-WZP23450C7D      | PSU #1 | V     | V       | ok      | PS-2162-9S | LIT23382DS3 | Cisco Systems Inc | 
| snas-eu-spdc-WZP23450C7D      | PSU #2 | V     | V       | ok      | PS-2162-9S | LIT23382DFR | Cisco Systems Inc | 
+-------------------------------+--------+-------+---------+---------+------------+-------------+-------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer output

```
# iserver get server --psu state:off -v psu

{
    "duration": 24594,
    "isctl": {
        "read": true,
        "calls": 3,
        "success": 3,
        "failed": 0,
        "total_time": 9823
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
        "lines": 367
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:15:36.720966	True	5197	100	isctl get compute rackunit  --expand "Psus" -o json --top 100
2023-12-03 15:15:38.956828	True	2231	9	isctl get compute rackunit  --expand "Psus" -o json --top 100 --skip 100
2023-12-03 15:15:41.481780	True	2395	12	isctl get compute blade   -o json --top 100
```

[[Back]](./ServerInventory.md)