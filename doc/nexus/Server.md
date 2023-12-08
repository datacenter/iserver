# Cross Domain

## Server

This feature combines Intersight and NX-OS API. Select the server via CIMC IP (--address) and define the nexus device search domain.
- server's interfaces are discovered via Intersight API
- nexus device lldp, lacp and mac address table are collected

Server's connectivity to nexus devices is shown.

```
# iserver get nx server --device dom:milan --address 10.58.53.43

Device: ipn11,ipn12,ipn13,ipn14,ipn21,ipn22,ipn25,ipn26

Server Summary [#1]
-------------------

+-------------------------------+---------------+-------------------+-------------+-------------+-------------+-----------+
| Name                          | Tag           | Model             | Serial      | IP          | CPU         | Memory    |
+-------------------------------+---------------+-------------------+-------------+-------------+-------------+-----------+
| comp3-p1c-eu-spdc-WZP26040BNX | status:unused | (R) UCSC-C240-M6N | WZP26040BNX | 10.58.53.43 | 2S 64C 128T | 512 [GiB] | 
|                               | psirt:ready   |                   |             |             |             |           | 
|                               | ocp:bm4       |                   |             |             |             |           | 
+-------------------------------+---------------+-------------------+-------------+-------------+-------------+-----------+

Interface - Nexus Summary [#14]
-------------------------------

+-------------------+---------------+---------------------------------------------------+----------+-------+-----+------+------+
| MAC Address       | Interface     | Adapter                                           | Pci Slot | Nexus | MAC | LACP | LLDP |
+-------------------+---------------+---------------------------------------------------+----------+-------+-----+------+------+
| b4:96:91:f9:34:c0 | eth-1         | Cisco - Intel E810CQDA2 2x100 GbE QSFP28 PCIe NIC | 6        | X     | X   | X    | X    | 
| b4:96:91:f9:3c:28 | eth-1         | Cisco - Intel E810CQDA2 2x100 GbE QSFP28 PCIe NIC | 3        | X     | X   | X    | X    | 
| b4:96:91:f9:34:c1 | eth-2         | Cisco - Intel E810CQDA2 2x100 GbE QSFP28 PCIe NIC | 6        | X     | X   | X    | X    | 
| b4:96:91:f9:3c:29 | eth-2         | Cisco - Intel E810CQDA2 2x100 GbE QSFP28 PCIe NIC | 3        | X     | X   | X    | X    | 
| ec:f4:0c:0d:80:da | eth-1         | Cisco(R) LOM X550-TX 10 Gig LOM                   | L        | X     | X   | X    | X    | 
| ec:f4:0c:0d:80:db | eth-2         | Cisco(R) LOM X550-TX 10 Gig LOM                   | L        | X     | X   | X    | X    | 
| 3c:fd:fe:cb:a5:48 | eth-1         | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC  | 1        | X     | X   | X    | X    | 
| 3c:fd:fe:cb:a5:49 | eth-2         | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC  | 1        | X     | X   | X    | X    | 
| 3c:fd:fe:cb:a5:4a | eth-3         | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC  | 1        | X     | X   | X    | X    | 
| 3c:fd:fe:cb:a5:4b | eth-4         | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC  | 1        | X     | X   | X    | X    | 
| 14:a2:a0:ec:74:fc | ext-eth-0     | UCSC-M-V100-04                                    | MLOM     | X     | X   | X    | X    | 
| 14:a2:a0:ec:74:fd | ext-eth-1     | UCSC-M-V100-04                                    | MLOM     | X     | X   | X    | X    | 
| 14:a2:a0:ec:75:04 | host-eth-eth0 | UCSC-M-V100-04                                    | MLOM     | V     | V   | V    | X    | 
| 14:a2:a0:ec:75:05 | host-eth-eth1 | UCSC-M-V100-04                                    | MLOM     | X     | X   | X    | X    | 
+-------------------+---------------+---------------------------------------------------+----------+-------+-----+------+------+

MAC Address Table [#1]
----------------------

+-------------------+---------------+----------------+----------+--------+------+----------------+---------+-----+-----+------+-------+
| MAC Address       | Interface     | Adapter        | Pci Slot | Device | VLAN | MAC            | Type    | Age | Sec | Ntfy | Port  |
+-------------------+---------------+----------------+----------+--------+------+----------------+---------+-----+-----+------+-------+
| 14:a2:a0:ec:75:04 | host-eth-eth0 | UCSC-M-V100-04 | MLOM     | ipn12  | 800  | 14a2.a0ec.7504 | dynamic | 0   | F   | F    | Po800 | 
+-------------------+---------------+----------------+----------+--------+------+----------------+---------+-----+-----+------+-------+

LACP [#1]
---------

+-------------------+---------------+----------------+----------+--------+-----------+-------------+-------------------+--------------+---------------+
| MAC Address       | Interface     | Adapter        | Pci Slot | Device | Interface | Port        | Partner MAC       | Partner Port | Partner State |
+-------------------+---------------+----------------+----------+--------+-----------+-------------+-------------------+--------------+---------------+
| 14:a2:a0:ec:75:04 | host-eth-eth0 | UCSC-M-V100-04 | MLOM     |        |           | Ethernet1/3 | 14:a2:a0:ec:75:04 | 0x2          | 0x3d          | 
+-------------------+---------------+----------------+----------+--------+-----------+-------------+-------------------+--------------+---------------+

Filter: --
View:   lacp, lldp, mac, all (def)
```

[[Back]](./README.md)