# Intersight Server

## hcl view

```
# iserver get server --group test -v hcl

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


HCL Summary [#8]
----------------

+-----------+------------+
| Server    | Overall    |
+-----------+------------+
| Server519 | Incomplete |
| Server589 | Incomplete |
| Server574 | Incomplete |
| Server797 | Incomplete |
| Server974 | Not-Listed |
| Server498 | Not-Listed |
| Server168 | Not-Listed |
| Server644 | Not-Listed |
+-----------+------------+

HCL Server Hardware Compliance [#8]
-----------------------------------

+-----------+-----------+----------------+-------------------------------------------------+----------+
| Server    | Status    | Model          | CPU                                             | Firmware |
+-----------+-----------+----------------+-------------------------------------------------+----------+
| Server519 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server589 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server574 | Validated | UCSC-C240-M5SN | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server797 | Validated | UCSC-C225-M6S  | AMD EPYC 7763 64-Core Processor                 | 1.0(1a)  |
| Server974 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server498 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server168 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
| Server644 | Validated | UCSB-B200-M5   | Intel Xeon Processor Scalable Family            | 1.0(1a)  |
+-----------+-----------+----------------+-------------------------------------------------+----------+

HCL Server Software Compliance [#8]
-----------------------------------

+-----------+------------+-------------------------+-----------+-------------+
| Server    | Status     | Reason                  | OS Vendor | OS Version  |
+-----------+------------+-------------------------+-----------+-------------+
| Server519 | Incomplete | Missing-Os-Info         |           |             |
| Server589 | Incomplete | Missing-Os-Info         |           |             |
| Server574 | Incomplete | Missing-Os-Info         |           |             |
| Server797 | Incomplete | Missing-Os-Info         |           |             |
| Server974 | Validated  | Incompatible-Components | Vendor    | Version     |
| Server498 | Validated  | Incompatible-Components | Vendor    | Version     |
| Server168 | Validated  | Incompatible-Components | Vendor    | Version     |
| Server644 | Validated  | Incompatible-Components | Vendor    | Version     |
+-----------+------------+-------------------------+-----------+-------------+

HCL Server Adapter Compliance [#8]
----------------------------------

+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server    | Status        | Component  | Hardware      | Software      | Reason                 | Model                                                            | Cimc Version | Driver Name | Driver Version | Firmware Version |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server519 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server589 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server574 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives) | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) LOM X550-T2                                             | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco(R) Ethernet Converged NIC XXV710-DA2                       | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-MLOM-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server797 | Not-Evaluated | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco Boot optimized M.2 Raid controller                         | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | Cisco 12G SAS RAID Controller with 4GB FBWC (16 Drives)          | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-PCIE-C25Q-04                                                | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Incomplete | Not-Evaluated | Not-Evaluated | Missing-Os-Driver-Info | UCSC-M-V100-04                                                   | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server974 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server498 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server168 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+
| Server644 | Not-Listed    | Not-Listed | Not-Evaluated | Not-Evaluated | Incompatible-Os-Info   | UCSB-MRAID12G-HE                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-MLOM-40G-04                                                 | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
|           |               | Validated  | Compatible    | Compatible    | Compatible             | UCSB-VIC-M84-4P                                                  | 1.0(1a)      | driver-name | 1.0(1a)        | 1.0(1a)          |
+-----------+---------------+------------+---------------+---------------+------------------------+------------------------------------------------------------------+--------------+-------------+----------------+------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)