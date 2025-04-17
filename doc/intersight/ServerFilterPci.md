# Intersight Server

## Filter by pci

Examples

```
--pci slot:gt6
--pci model:xxv710
--pci pid:ID25GF
```

## Model

```
# iserver get server
    --pci model:xxv710 -v pci

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


PCI [#34]
---------

+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server    | PCI Device Model                 | Pid              | Serial | SlotId | Vendor | Firmware |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server117 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-75  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server117 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-91  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server594 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-37  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server594 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-16  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server641 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-87  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server641 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-49  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server141 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-55  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server141 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-96  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server419 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-63  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server419 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-90  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server714 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-60  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server714 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-77  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server127 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-91  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server127 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-83  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server752 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-91  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server752 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-77  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server469 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-32  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server469 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-78  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server531 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-38  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server531 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-80  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server545 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-98  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server545 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-70  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server206 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-47  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server206 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-61  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server831 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-92  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server849 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-74  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server849 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-57  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server249 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-29  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server249 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-49  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server618 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-35  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server618 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-93  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server397 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-82  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server397 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-14  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server203 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-94  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## PID

```
# iserver get server --pci pid:ID25GF -v pci

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


PCI [#34]
---------

+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server    | PCI Device Model                 | Pid              | Serial | SlotId | Vendor | Firmware |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server647 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-89  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server647 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-32  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server924 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-19  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server924 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-44  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server750 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-64  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server750 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-75  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server139 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-43  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server139 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-44  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server154 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-54  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server154 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-53  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server915 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-80  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server915 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-38  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server436 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-97  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server436 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-35  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server125 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-65  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server125 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-48  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server411 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-37  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server411 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-86  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server952 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-66  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server952 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-36  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server619 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-14  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server619 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-79  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server119 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-18  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server119 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-19  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server824 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-38  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server793 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-10  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server793 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-85  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server240 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-75  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server240 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-34  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server560 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-57  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server560 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-37  | 2      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server568 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-11  | 1      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server568 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-61  | 3      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+
| Server104 | Cisco(R) Ethernet Converged NIC  | UCSC-PCIE-ID25GF | SN-75  | 6      | 0x8086 | 1.0(1a)  |
|           | XXV710-DA2                       |                  |        |        |        |          |
+-----------+----------------------------------+------------------+--------+--------+--------+----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

## PCI slot count

```
# iserver get server --pci slot:gt6

iaccount demo (cache: any)
Select servers...
Selected servers: 121
Collect server api objects...


Server Summary [#13]
--------------------

+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| SF      | MF  | Name      | Moid       | Tag | Model              | Serial | IP             | CPU          | Memory    |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+
| P+ H    | Cri | Server241 | Moid-value | --  | (R) UCSC-C480-M5   | SN-81  | 10.221.166.181 | 4S 72C 144T  | 256 [GiB] |
| P+ C(1) | CRi | Server738 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-87  | 10.158.198.221 | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server150 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-71  | 10.92.96.81    | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server360 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-44  | 10.88.27.74    | 2S 48C 96T   | 512 [GiB] |
| P+ H    | CRi | Server608 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-86  | 10.144.113.171 | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server746 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-37  | 10.185.25.247  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server512 | Moid-value | --  | (R) UCSC-C245-M6SX | SN-70  | 10.127.173.251 | 2S 128C 256T | 512 [GiB] |
| P+ C(1) | CRi | Server129 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-66  | 10.48.163.192  | 2S 64C 128T  | 512 [GiB] |
| P+ H    | CRi | Server547 | Moid-value | --  | (R) UCSC-C240-M6N  | SN-92  | 10.250.247.181 | 2S 64C 128T  | 512 [GiB] |
| P+ H    | Cu  | Server275 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-18  | 10.102.200.227 | 2S 40C 80T   | 384 [GiB] |
| P+ H    | Cu  | Server629 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-16  | 10.169.152.50  | 2S 40C 80T   | 384 [GiB] |
| P+ H    | Cu  | Server351 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-48  | 10.108.44.106  | 2S 40C 80T   | 384 [GiB] |
| P+ H    | Cu  | Server346 | Moid-value | --  | (R) HXAF220C-M5SN  | SN-63  | 10.179.192.22  | 2S 40C 80T   | 384 [GiB] |
+---------+-----+-----------+------------+-----+--------------------+--------+----------------+--------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)