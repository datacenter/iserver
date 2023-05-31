# Endpoint

## Filter by server's ip address

- Server must be found by IP address in intersight account
- MAC address of every network adapter is added to endpoint search criteria

```
# iserver get aci ep --apic apic11 --xd server:10.58.29.58

Apic: apic11
Resolve xd server...

+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 256 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

+-------------------+-----------+--------------------------------------------------+----------+
| MAC Address       | Interface | Adapter                                          | Pci Slot |
+-------------------+-----------+--------------------------------------------------+----------+
| 3c:fd:fe:cb:f5:18 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:19 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:1a | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:1b | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 40:a6:b7:08:fb:b0 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b1 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b2 | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b3 | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 70:ea:1a:fc:34:72 | eth-1     | Cisco(R) LOM X550-T2                             | L        | 
| 70:ea:1a:fc:34:73 | eth-2     | Cisco(R) LOM X550-T2                             | L        | 
+-------------------+-----------+--------------------------------------------------+----------+

+----+-------------------+----------------+--------+----------------------------+------------------+------------+-------------------+
| SF | MAC Address       | IP Address     | Tenant | BD                         | EPG              | Ap         | VRF               |
+----+-------------------+----------------+--------+----------------------------+------------------+------------+-------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.152.14 | cvim4a | cvim4a/cvim4a-MX-mgmt_BD   | cvim4a-MX-mgmt   | cvim4a_ANP | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+--------+----------------------------+------------------+------------+-------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.157.14 | cvim4a | cvim4a/cvim4a-S-storage_BD | cvim4a-S-storage | cvim4a_ANP | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+--------+----------------------------+------------------+------------+-------------------+
```

- Use -o fabric option to get interface related information for get_aci_endpoint.server

```
# iserver get aci ep --apic apic11 --xd server:10.58.29.58 --view fabric

Apic: apic11
Resolve xd server...

+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 256 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

+-------------------+-----------+--------------------------------------------------+----------+
| MAC Address       | Interface | Adapter                                          | Pci Slot |
+-------------------+-----------+--------------------------------------------------+----------+
| 3c:fd:fe:cb:f5:18 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:19 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:1a | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 3c:fd:fe:cb:f5:1b | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 1        | 
| 40:a6:b7:08:fb:b0 | eth-1     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b1 | eth-2     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b2 | eth-3     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 40:a6:b7:08:fb:b3 | eth-4     | Intel X710-DA4 Quad Port 10Gb SFP+ converged NIC | 2        | 
| 70:ea:1a:fc:34:72 | eth-1     | Cisco(R) LOM X550-T2                             | L        | 
| 70:ea:1a:fc:34:73 | eth-2     | Cisco(R) LOM X550-T2                             | L        | 
+-------------------+-----------+--------------------------------------------------+----------+

+----+-------------------+----------------+---------------------------------------------------+
| SF | MAC Address       | IP Address     | Fabric                                            |
+----+-------------------+----------------+---------------------------------------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.152.14 | pod-1 node-202 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
|    |                   |                | pod-1 node-201 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
+----+-------------------+----------------+---------------------------------------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.157.14 | pod-1 node-202 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
|    |                   |                | pod-1 node-201 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
+----+-------------------+----------------+---------------------------------------------------+
Interface context: ep
```

- Use context to get interface details

```
# iserver get aci intf phy --apic apic11 --role leaf --ctx ep

Apic: apic11o.emea-sp.cisco.com
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC   | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| pod-1/cl201-eu-spdc | 1/61      | up    | enabled   | up   | connected | leaf | switched | po14 | 4C:71:0D:23:FA:75 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/61      | up    | enabled   | up   | connected | leaf | switched | po5  | 10:B3:D5:B5:62:59 | trunk | 10G   | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

[[Back Endpoint]](./Endpoint.md) [[Back Cross Domain]](./XdServer.md)