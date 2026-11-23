# Intersight Server

## Filter by mac address

Examples

```
--mac 1234
--mac 85ab --mac 0a0d
```

## Example

```
# iserver get server
    --group test
    --mac ee2c
    --mac cc14 -v net

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


IMC [#2]
--------

+-----------+------------+---------------+------------+-------------------+
| Server    | IP         | Mask          | Gateway    | MAC               |
+-----------+------------+---------------+------------+-------------------+
| Server688 | 10.1.1.27  | 255.255.255.0 | 10.1.1.254 | aa:bb:43:77:61:99 |
| Server868 | 10.1.1.145 | 255.255.255.0 | 10.1.1.254 | aa:bb:83:42:65:51 |
+-----------+------------+---------------+------------+-------------------+

Network Adapters [#8]
---------------------

+-----------+--------------+---------+--------------------------------------------+--------------------------------------------+--------+-------------------+-----+-----+-----+
| Server    | Name         | PciSlot | Model                                      | PID                                        | Serial | Vendor            | Eth | HBA | DCE |
+-----------+--------------+---------+--------------------------------------------+--------------------------------------------+--------+-------------------+-----+-----+-----+
| Server688 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-89  | 0x8086            | 2   | 0   | 0   |
| Server688 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-18  | 0x8086            | 2   | 0   | 0   |
| Server688 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | Cisco(R) LOM X550-T2                       | SN-29  | 0x8086            | 2   | 0   | 0   |
| Server688 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04                          | SN-31  | Cisco Systems Inc | 4   | 4   | 4   |
| Server868 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-15  | 0x8086            | 2   | 0   | 0   |
| Server868 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-85  | 0x8086            | 2   | 0   | 0   |
| Server868 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | Cisco(R) LOM X550-T2                       | SN-33  | 0x8086            | 2   | 0   | 0   |
| Server868 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04                          | SN-41  | Cisco Systems Inc | 4   | 4   | 4   |
+-----------+--------------+---------+--------------------------------------------+--------------------------------------------+--------+-------------------+-----+-----+-----+

External Ethernet (MLOM) [#4]
-----------------------------

+-----------+-------------------+--------------+-------------------+
| Server    | Adapter Model     | Interface ID | MAC Address       |
+-----------+-------------------+--------------+-------------------+
| Server868 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:89:63:73:37 |
| Server868 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:15:41:73:41 |
| Server868 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:99:31:55:26 |
| Server868 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:67:34:82:76 |
+-----------+-------------------+--------------+-------------------+

Host Ethernet [#6]
------------------

+-----------+--------------+--------------------------------------------+----------------+-------------------+
| Server    | Adapter Name | Adapter Model                              | Interface Name | MAC Address       |
+-----------+--------------+--------------------------------------------+----------------+-------------------+
| Server688 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-58        | aa:bb:10:42:40:21 |
| Server688 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-42        | aa:bb:88:45:63:49 |
| Server868 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-55        | aa:bb:65:74:20:36 |
| Server868 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-22        | aa:bb:75:18:10:81 |
| Server868 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-60        | aa:bb:50:91:18:94 |
| Server868 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-97        | aa:bb:47:92:94:68 |
+-----------+--------------+--------------------------------------------+----------------+-------------------+

Host FC [#0]
------------
None

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)