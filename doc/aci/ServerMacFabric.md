# Cross Domain

## Add fabric connectivity information to server's interfaces

- triggered by the combination of --mac and --fabric options
- ACI and NX-OS domains are scanned searching for the MAC address (LLDP neighborship)

```
# iserver get is server --ip 10.58.29.58 --mac --fabric

Get base server info from cache...
Get selected server details from cache...


+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 256 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

+-------------------+-----------+--------------------------------------------------+----------+-------------+------------+----------------+---------+--------+
| MAC Address       | Interface | Adapter                                          | Pci Slot | Fabric Type | Controller | Node           | Port    | Source |
+-------------------+-----------+--------------------------------------------------+----------+-------------+------------+----------------+---------+--------+
| 3c:fd:fe:cb:f5:18 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | ACI         | apic11     | pod-1/node-201 | eth1/61 | lldp   | 
| 3c:fd:fe:cb:f5:19 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | ACI         | apic11     | pod-1/node-201 | eth1/62 | lldp   | 
| 3c:fd:fe:cb:f5:1a | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | ACI         | apic11     | pod-1/node-201 | eth1/63 | lldp   | 
| 3c:fd:fe:cb:f5:1b | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        |             |            |                |         |        | 
| 40:a6:b7:08:fb:b0 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | ACI         | apic11     | pod-1/node-202 | eth1/61 | lldp   | 
| 40:a6:b7:08:fb:b1 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | ACI         | apic11     | pod-1/node-202 | eth1/62 | lldp   | 
| 40:a6:b7:08:fb:b2 | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | ACI         | apic11     | pod-1/node-202 | eth1/63 | lldp   | 
| 40:a6:b7:08:fb:b3 | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        |             |            |                |         |        | 
| 70:ea:1a:fc:34:72 | eth-1     | Cisco(R) LOM X550-T2                             | L        |             |            |                |         |        | 
| 70:ea:1a:fc:34:73 | eth-2     | Cisco(R) LOM X550-T2                             | L        |             |            |                |         |        | 
+-------------------+-----------+--------------------------------------------------+----------+-------------+------------+----------------+---------+--------+
```

[[Back Cross Domain]](./XdServer.md)