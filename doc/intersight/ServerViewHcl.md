# Intersight Server

## hcl view

```
# iserver get server --group test -v hcl

iaccount isctl (cache: off)
Select servers...
Selected servers: 8
Collect server api objects...


HCL Summary [#8]
----------------

+--------------------------------+------------+
| Server                         | Overall    |
+--------------------------------+------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated  | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated  | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Incomplete | 
| comp3-p4b-eu-spdc-WZP262207UM  | Incomplete | 
| FI-ucsb1-eu-spdc-2-1           | Not-Listed | 
| FI-ucsb1-eu-spdc-2-2           | Not-Listed | 
| FI-ucsb1-eu-spdc-2-3           | Not-Listed | 
| FI-ucsb1-eu-spdc-2-4           | Not-Listed | 
+--------------------------------+------------+

HCL Server Hardware Compliance [#8]
-----------------------------------

+--------------------------------+-----------+----------------+-------------------------------------------------+----------+
| Server                         | Status    | Model          | CPU                                             | Firmware |
+--------------------------------+-----------+----------------+-------------------------------------------------+----------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 4.2(2)   | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 4.2(2)   | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| comp3-p4b-eu-spdc-WZP262207UM  | Validated | UCSC-C225-M6S  | AMD EPYC 7763 64-Core Processor                 | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-1           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-2           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-3           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
| FI-ucsb1-eu-spdc-2-4           | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 4.2(3)   | 
+--------------------------------+-----------+----------------+-------------------------------------------------+----------+

HCL Server Software Compliance [#8]
-----------------------------------

+--------------------------------+------------+-------------------------+-----------+-------------+
| Server                         | Status     | Reason                  | OS Vendor | OS Version  |
+--------------------------------+------------+-------------------------+-----------+-------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated  | Compatible              | VMware    | ESXi 7.0 U3 | 
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated  | Compatible              | VMware    | ESXi 7.0 U3 | 
| comp-3-p2b-eu-spdc-WZP23400AKL | Incomplete | Missing-Os-Info         |           |             | 
| comp3-p4b-eu-spdc-WZP262207UM  | Incomplete | Missing-Os-Info         |           |             | 
| FI-ucsb1-eu-spdc-2-1           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
| FI-ucsb1-eu-spdc-2-2           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
| FI-ucsb1-eu-spdc-2-3           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
| FI-ucsb1-eu-spdc-2-4           | Validated  | Incompatible-Components | VMware    | ESXi 7.0 U3 | 
+--------------------------------+------------+-------------------------+-----------+-------------+

HCL Server Adapter Compliance [#8]
----------------------------------

+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| Server                         | Status        | Component  | Hardware      | Software            | Reason                 | Model                                                            | Cimc Version | Driver Name | Driver Version | Firmware Version   |
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp-1-p2b-eu-spdc-WZP23400AJW | Validated     | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) LOM X550-T2                                             | 4.2(2)       | ixgben      | 1.12.3.0       | 0x800016F9-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(2)       | lsi_mr3     | 7.718.02.00    | 51.19.0-4296       | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | UCSC-MLOM-C25Q-04                                                | 4.2(2)       | nenic       | 1.0.42.0       | 5.2(2)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp-2-p2b-eu-spdc-WZP23400AK4 | Validated     | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(2)       | i40en       | 2.2.7.0        | 0x8000B900-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco(R) LOM X550-T2                                             | 4.2(2)       | ixgben      | 1.12.3.0       | 0x800016F9-1.826.0 | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(2)       | lsi_mr3     | 7.718.02.00    | 51.19.0-4296       | 
|                                |               | Validated  | Compatible    | Compatible          | Compatible             | UCSC-MLOM-C25Q-04                                                | 4.2(2)       | nenic       | 1.0.42.0       | 5.2(2)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp-3-p2b-eu-spdc-WZP23400AKL | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 4.2(3)       |             |                | 51.19.0-4532       | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 4.2(3)       |             |                | 0x800016F9-1.826.0 | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(3)       |             |                | 0x8000CC0F-1.826.0 | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 4.2(3)       |             |                | 0x8000CC0F-1.826.0 | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 4.2(3)       |             |                | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| comp3-p4b-eu-spdc-WZP262207UM  | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco Boot optimized M.2 Raid controller                         | 4.2(3)       |             |                | 2.3.17.1014        | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)          | 4.2(3)       |             |                | 52.20.0-4523       | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | UCSC-PCIE-C25Q-04                                                | 4.2(3)       |             |                | 5.2(3)             | 
|                                |               | Incomplete | Not-Evaluated | Not-Evaluated       | Missing-Os-Driver-Info | UCSC-M-V100-04                                                   | 4.2(3)       |             |                | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-1           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-2           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.42.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-3           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+
| FI-ucsb1-eu-spdc-2-4           | Not-Listed    | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MRAID12G-HE                                                 | 4.2(3)       | lsi_mr3     | 7.718.02.00    | 24.21.0-0156       | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-VIC-M84-4P                                                  | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
|                                |               | Not-Listed | Compatible    | Incompatible-Driver | Incompatible-Driver    | UCSB-MLOM-40G-04                                                 | 4.2(3)       | nenic       | 1.0.33.0       | 5.2(3)             | 
+--------------------------------+---------------+------------+---------------+---------------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+--------------------+

Filter: ip, name, serial, model, type, group, loc, power, psu, fan, alarm, ucsm
        disconnected, standalone, cname, cmodel, cserial, pci, mac, cpu, mem
View:   state (def), adv, alarm, board, boot, connector, contract, cpu|, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, storage, sw, thermal, tpm, workflow, summary
```

Developer

```
# iserver get server --group test -v hcl

{
    "duration": 20182,
    "isctl": {
        "read": true,
        "calls": 10,
        "success": 10,
        "failed": 0,
        "total_time": 18331
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
        "lines": 25
    },
    "cache_hits": 0
}

Log: isctl
-----------

2023-12-03 15:22:35.676243	True	2344	100	isctl get compute rackunit   -o json --top 100
2023-12-03 15:22:37.218161	True	1539	9	isctl get compute rackunit   -o json --top 100 --skip 100
2023-12-03 15:22:38.769440	True	1487	12	isctl get compute blade   -o json --top 100
2023-12-03 15:22:40.755592	True	1955	8	isctl get cond hclstatus --filter "ManagedObject/Moid in ('5fdf9c016176752d35e44795', '5fdf9c786176752d35e47110', '5fdf9d026176752d35e4ac4e', '6385018e76752d313964b3b5', '6501db4c76752d3901eb3803', '6501db4c76752d3901eb3817', '6501db4c76752d3901eb3851', '6501db4c76752d3901eb387e')"  -o json --top 100
2023-12-03 15:22:42.759871	True	1985	100	isctl get cond hclstatusdetail   -o json --top 100
2023-12-03 15:22:44.461888	True	1697	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 100
2023-12-03 15:22:46.284192	True	1820	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 200
2023-12-03 15:22:48.108560	True	1821	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 300
2023-12-03 15:22:49.988106	True	1876	100	isctl get cond hclstatusdetail   -o json --top 100 --skip 400
2023-12-03 15:22:51.855753	True	1807	80	isctl get cond hclstatusdetail   -o json --top 100 --skip 500
```

[[Back]](./ServerInventory.md)