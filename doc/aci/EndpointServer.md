# Endpoint

## Filter by server's ip address

- Server must be found by IP address in intersight account
- MAC address of every network adapter is added to endpoint search criteria

```
# iserver get aci ep --apic apic11 --xd server:10.58.29.58

Apic: apic11 (mode:online, cache:off)
Resolve xd server...

+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 384 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

+----+-------------------+----------------+--------+------------+------------------+-------+----------------------------+-------------------+
| SF | MAC Address       | IP Address     | Tenant | AP         | EPG              | Encap | BD                         | VRF               |
+----+-------------------+----------------+--------+------------+------------------+-------+----------------------------+-------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.152.14 | cvim4a | cvim4a_ANP | cvim4a-MX-mgmt   | 152   | cvim4a/cvim4a-MX-mgmt_BD   | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+--------+------------+------------------+-------+----------------------------+-------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.157.14 | cvim4a | cvim4a_ANP | cvim4a-S-storage | 157   | cvim4a/cvim4a-S-storage_BD | cvim4a/cvim4a_VRF | 
+----+-------------------+----------------+--------+------------+------------------+-------+----------------------------+-------------------+
```

- Use -o fabric option to get interface related information for get_aci_endpoint.server

```
# iserver get aci ep --apic apic11 --xd server:10.58.29.58 --view fabric

Apic: apic11 (mode:online, cache:off)
Resolve xd server...

+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| Name                          | Model              | Serial      | IP          | CPU        | Memory    |
+-------------------------------+--------------------+-------------+-------------+------------+-----------+
| comp2-p4a-eu-spdc-WZP22520B04 | (R) UCSC-C220-M5SX | WZP22520B04 | 10.58.29.58 | 2S 48C 96T | 384 [GiB] | 
+-------------------------------+--------------------+-------------+-------------+------------+-----------+

+----+-------------------+----------------+------------------+---------------+---------------------------------------------------+
| SF | MAC Address       | IP Address     | EPG              | Encapsulation | Fabric                                            |
+----+-------------------+----------------+------------------+---------------+---------------------------------------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.152.14 | cvim4a-MX-mgmt   | 152           | pod-1 node-202 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
|    |                   |                |                  |               | pod-1 node-201 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
+----+-------------------+----------------+------------------+---------------+---------------------------------------------------+
| L  | 3C:FD:FE:CB:F5:18 | 192.168.157.14 | cvim4a-S-storage | 157           | pod-1 node-202 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
|    |                   |                |                  |               | pod-1 node-201 eth1/61 (pod4a-COMP-2-SAMX_PolGrp) | 
+----+-------------------+----------------+------------------+---------------+---------------------------------------------------+
Interface context: ep
```

- Use context to get interface details

```
# iserver get aci intf phy --apic apic11 --role leaf --ctx ep

Apic: apic11 (mode:online, cache:off)
Pod: 1
- node: cl201-eu-spdc
- node: cl202-eu-spdc

+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| Node                | Interface | Admin | Switching | Oper | Reason    | Type | Layer    | PC   | MAC               | Mode  | Speed | Duplex | MTU  | FEC         |
+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
| pod-1/cl201-eu-spdc | 1/61      | up    | enabled   | up   | connected | leaf | switched | po16 | 4C:71:0D:23:FA:75 | trunk | 10G   | full   | 9000 | disable-fec | 
| pod-1/cl202-eu-spdc | 1/61      | up    | enabled   | up   | connected | leaf | switched | po19 | 10:B3:D5:B5:62:59 | trunk | 10G   | full   | 9000 | disable-fec | 
+---------------------+-----------+-------+-----------+------+-----------+------+----------+------+-------------------+-------+-------+--------+------+-------------+
Interface context: phy
```

[[Back Endpoint]](./Endpoint.md) [[Back Cross Domain]](./XdServer.md)