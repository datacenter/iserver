# Intersight Hardware Discovery - Get server

Use OpenShift cluster filtering rule in [Server Inventory](../../intersight/ServerInventory.md) feature.

```
# iserver get server --ocp my-cluster
iaccount isctl (cache: off)
Select servers...
Selected servers: 1
Collect server api objects...
Collect server information |################################| 1/1


Server Summary [#1]
-------------------

+------+-----+-------+-------+------------+--------------------+-------------+-------------+------------+-----------+
| SF   | MF  | Name  | Moid  | Tag        | Model              | Serial      | IP          | CPU        | Memory    |
+------+-----+-------+-------+------------+--------------------+-------------+-------------+------------+-----------+
| P+ H | CRi | comp1 | 222   | ---        | (R) UCSC-C220-M5SX | Serial123   | 10.10.10.10 | 2S 40C 80T | 384 [GiB] |
+------+-----+-------+-------+------------+--------------------+-------------+-------------+------------+-----------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

```
# iserver get server --ocp my-cluster:node1 -v pci
iaccount isctl (cache: off)
Select servers...
Selected servers: 1
Collect server api objects...
Collect server information |################################| 1/1


PCI [#5]
--------

+--------+-----------------------------------------+-------------------+--------+--------+-------------+
| Server | PCI Device Model                        | Pid               | SlotId | Vendor | Firmware    |
+--------+-----------------------------------------+-------------------+--------+--------+-------------+
| comp1  | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | 1      | 0x8086 | 1.0.0       |
|        | XXV710-DA2                              |                   |        |        |             |
+--------+-----------------------------------------+-------------------+--------+--------+-------------+
| comp1  | Cisco(R) Ethernet Converged NIC         | UCSC-PCIE-ID25GF  | 2      | 0x8086 | 1.0.0       |
|        | XXV710-DA2                              |                   |        |        |             |
+--------+-----------------------------------------+-------------------+--------+--------+-------------+
| comp1  | Intel X550 LOM                          | NA                | L      | 0x8086 | 1.0.0       |
+--------+-----------------------------------------+-------------------+--------+--------+-------------+
| comp1  | Cisco UCS VIC 1457 MLOM                 | UCSC-MLOM-C25Q-04 | MLOM   | 0x1137 | 1.0.0       |
+--------+-----------------------------------------+-------------------+--------+--------+-------------+
| comp1  | Cisco 12G Modular Raid Controller with  | UCSC-RAID-M5      | MRAID  | 0x1000 | 1.0.0       |
|        | 2GB cache (max 16 drives)               |                   |        |        |             |
+--------+-----------------------------------------+-------------------+--------+--------+-------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./README.md)