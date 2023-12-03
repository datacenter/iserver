# Network

## All view

```
# iserver get osp net --cluster pod1 -v all

Cluster: pod1

Network [#15]
-------------

+----------------------------------------------------+---------+-------+--------+--------+-----+-----+------+---------------------------------------------------+------------------+------+
| Name                                               | Tenant  | Admin | Status | Shared | Ext | Sec | MTU  | Subnet                                            | CIDR             | Age  |
+----------------------------------------------------+---------+-------+--------+--------+-----+-----+------+---------------------------------------------------+------------------+------+
| C8KV01_LAN01                                       | ialonso | V     | ACTIVE | X      | X   | V   | 9000 | C8KV01_LAN01                                      | 10.0.11.0/24     | 33d  | 
| C8KV_ORANGE_LAN01                                  | ialonso | V     | ACTIVE | X      | X   | V   | 9000 | C8KV_ORANGE_LAN01                                 | 10.0.21.0/24     | 26d  | 
| control-k8s                                        | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-k8s-subnet                                | 15.100.3.0/24    | 472d | 
| control-N2                                         | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-N2-subnet                                 | 15.100.5.0/24    | 472d | 
| control-N4                                         | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-N4-subnet                                 | 15.100.6.0/24    | 472d | 
| control-SBI                                        | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | control-SBI-subnet                                | 15.100.4.0/24    | 472d | 
| data-N3                                            | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | data-N3-subnet                                    | 15.100.7.0/24    | 472d | 
| data-N6                                            | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | data-N6-subnet                                    | 15.100.8.0/24    | 472d | 
| di-internal1                                       | smi5gc  | V     | ACTIVE | X      | X   | X   | 9000 | di-internal1-subnet                               | 172.16.0.0/18    | 457d | 
| external                                           | admin   | V     | ACTIVE | V      | V   | V   | 9000 | subnet-ext                                        | 10.58.28.80/28   | 472d | 
| HA network tenant 05b8e996f0654e4491d2e925a91c6250 | --      | V     | ACTIVE | X      | X   | V   | 9000 | HA subnet tenant 05b8e996f0654e4491d2e925a91c6250 | 169.254.192.0/18 | 472d | 
| management                                         | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | management-subnet                                 | 15.100.1.0/24    | 472d | 
| orchestration                                      | smi5gc  | V     | ACTIVE | X      | X   | V   | 9000 | orchestration-subnet                              | 15.100.2.0/24    | 472d | 
| sriov0                                             | smi5gc  | V     | ACTIVE | V      | X   | V   | 9000 | sriov0-subnet                                     | 15.100.105.0/24  | 472d | 
| sriov1                                             | smi5gc  | V     | ACTIVE | V      | X   | V   | 9000 | sriov1-subnet                                     | 15.100.106.0/24  | 472d | 
+----------------------------------------------------+---------+-------+--------+--------+-----+-----+------+---------------------------------------------------+------------------+------+

Network - Identifier [#15]
--------------------------

+--------------------------------------+----------------------------------------------------+----------------------------------+--------------------------------------+
| Id                                   | Name                                               | Tenant                           | Subnet                               |
+--------------------------------------+----------------------------------------------------+----------------------------------+--------------------------------------+
| d6a76040-e0f7-47d2-a4b8-542e896cc2ec | C8KV01_LAN01                                       | 9b50a8dba82f4c14802c4554482882b8 | db2b80bf-65d0-4836-9eb3-929eefb8fff0 | 
| 15c99bd1-25e1-445b-8c97-daf8eb5c66f2 | C8KV_ORANGE_LAN01                                  | 9b50a8dba82f4c14802c4554482882b8 | afd52863-ee94-4880-80be-fc6fd7788f6e | 
| a4fe3f25-a010-4cad-a945-0e36256b3783 | control-k8s                                        | 05b8e996f0654e4491d2e925a91c6250 | 4299410e-e562-46d6-93b0-d839669a5bca | 
| 25fe8889-15f4-4c9f-b1a6-fc3fd95c3d43 | control-N2                                         | 05b8e996f0654e4491d2e925a91c6250 | 1786aa38-3ab1-4a86-9966-f4dae5411bab | 
| 0d6676b5-6fbc-4b51-bf29-1380cef97fcd | control-N4                                         | 05b8e996f0654e4491d2e925a91c6250 | ac4e33d4-9061-4f8e-bed7-40e5bb0d1b7a | 
| 02c949a8-1b9c-4162-a8ad-f8941a8f37d1 | control-SBI                                        | 05b8e996f0654e4491d2e925a91c6250 | 84b1de29-b4be-4508-8ad9-6c68c930dac5 | 
| bb3bf0cd-6361-4d79-8764-92eaa9de7880 | data-N3                                            | 05b8e996f0654e4491d2e925a91c6250 | addec922-7181-4039-be79-4da3d88d2c0a | 
| 10885efc-c3cf-41cf-b5ec-264996f1d78c | data-N6                                            | 05b8e996f0654e4491d2e925a91c6250 | ba7cff90-beb1-4061-ba6c-5c223ed56586 | 
| 4510e325-db2f-48ce-8e93-c1dcd6065825 | di-internal1                                       | 05b8e996f0654e4491d2e925a91c6250 | 4f59eb25-f662-490a-8e08-c427478857c1 | 
| e7474314-438a-43f6-9ddf-319f0578ca30 | external                                           | 2cced286b74c45ea95c83cc2e5d3b413 | 379bd679-fea7-4aa6-b8c3-0368ab2790a9 | 
| 68a6f31c-a4a1-4990-8654-3d00c6e9115e | HA network tenant 05b8e996f0654e4491d2e925a91c6250 |                                  | e122cda4-5250-467e-ba83-1e4fcfeb0b1b | 
| fe1e3247-64b8-45ae-aa40-468a9a768954 | management                                         | 05b8e996f0654e4491d2e925a91c6250 | 14b5c631-8d81-46b9-b3d9-abbb4acc0191 | 
| 3065667d-94c9-442c-87c1-bec9cffa0d50 | orchestration                                      | 05b8e996f0654e4491d2e925a91c6250 | 3ab58791-ba30-45a9-b185-d9f3809f2556 | 
| 7fa67775-1f5f-4dca-baaa-15ea5b55c4e2 | sriov0                                             | 05b8e996f0654e4491d2e925a91c6250 | 195953ed-add3-4c59-b81a-ee372dcd7838 | 
| cd63e7ec-39b2-4f47-9f46-df5d3e25c967 | sriov1                                             | 05b8e996f0654e4491d2e925a91c6250 | 1cbf95c8-b46c-4684-92da-7199481236c3 | 
+--------------------------------------+----------------------------------------------------+----------------------------------+--------------------------------------+

Network - Port [#15]
--------------------

+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| Name                                               | CIDR             | MAC               | IP              | Type     | VM                    | HV               |
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| ialonso/C8KV01_LAN01                               | 10.0.11.0/24     | fa:16:3e:5c:b7:b8 | 10.0.11.1       | Compute  | ialonso/ORANGE-C8KV-1 | AIO-server-1     | 
|                                                    |                  | fa:16:3e:3b:d5:c6 | 10.0.11.2       | Compute  | ialonso/SDWAN-C8KV01B | AIO-server-1     | 
|                                                    |                  | fa:16:3e:79:74:6e | 10.0.11.5       | DHCP     | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:91:2f:04 | 10.0.11.6       | DHCP     | --                    | AIO-server-3     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| ialonso/C8KV_ORANGE_LAN01                          | 10.0.21.0/24     | fa:16:3e:67:1b:48 | 10.0.21.1       | Compute  | ialonso/ORANGE-C8KV-2 | AIO-server-1     | 
|                                                    |                  | fa:16:3e:ae:32:44 | 10.0.21.2       | Compute  | admin/c8koncinder     | compute-server-2 | 
|                                                    |                  | fa:16:3e:db:b8:4b | 10.0.21.5       | DHCP     | --                    | AIO-server-2     | 
|                                                    |                  | fa:16:3e:d6:0f:0c | 10.0.21.6       | DHCP     | --                    | AIO-server-3     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/control-k8s                                 | 15.100.3.0/24    | fa:16:3e:ea:51:30 | 15.100.3.1      | DHCP     | --                    | AIO-server-2     | 
|                                                    |                  | fa:16:3e:5b:72:42 | 15.100.3.2      | DHCP     | --                    | AIO-server-1     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/control-N2                                  | 15.100.5.0/24    | fa:16:3e:c9:c1:51 | 15.100.5.1      | DHCP     | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:63:7d:aa | 15.100.5.101    | Compute  | smi5gc/lattice        | compute-server-2 | 
|                                                    |                  | fa:16:3e:8b:2c:b8 | 15.100.5.2      | DHCP     | --                    | AIO-server-2     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/control-N4                                  | 15.100.6.0/24    | fa:16:3e:6b:5b:ab | 15.100.6.1      | DHCP     | --                    | AIO-server-2     | 
|                                                    |                  | fa:16:3e:fe:4d:de | 15.100.6.101    | Compute  | smi5gc/lattice        | compute-server-2 | 
|                                                    |                  | fa:16:3e:6f:c6:b7 | 15.100.6.2      | DHCP     | --                    | AIO-server-1     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/control-SBI                                 | 15.100.4.0/24    | fa:16:3e:9b:b6:b0 | 15.100.4.1      | DHCP     | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:cc:7f:24 | 15.100.4.101    | Compute  | smi5gc/lattice        | compute-server-2 | 
|                                                    |                  | fa:16:3e:77:f7:73 | 15.100.4.2      | DHCP     | --                    | AIO-server-3     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/data-N3                                     | 15.100.7.0/24    | fa:16:3e:8b:39:88 | 15.100.7.1      | DHCP     | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:70:4d:85 | 15.100.7.101    | Compute  | smi5gc/lattice        | compute-server-2 | 
|                                                    |                  | fa:16:3e:00:0b:d6 | 15.100.7.2      | DHCP     | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:7c:ff:47 | 15.100.7.41     | Compute  | smi5gc/VPC-SI-mme     | AIO-server-1     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/data-N6                                     | 15.100.8.0/24    | fa:16:3e:1e:37:ac | 15.100.8.1      | DHCP     | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:b4:94:eb | 15.100.8.102    | Compute  | smi5gc/server         | compute-server-1 | 
|                                                    |                  | fa:16:3e:46:ab:b0 | 15.100.8.2      | DHCP     | --                    | AIO-server-2     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/di-internal1                                | 172.16.0.0/18    | --                | --              | --       | --                    | --               | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| admin/external                                     | 10.58.28.80/28   | fa:16:3e:c1:37:01 | 10.58.28.81     | Gateway  | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:f3:63:1f | 10.58.28.82     | Floating | --                    |                  | 
|                                                    |                  | fa:16:3e:b8:e4:f3 | 10.58.28.83     | Floating | --                    |                  | 
|                                                    |                  | fa:16:3e:32:07:87 | 10.58.28.84     | Floating | --                    |                  | 
|                                                    |                  | fa:16:3e:93:e6:fe | 10.58.28.85     | Floating | --                    |                  | 
|                                                    |                  | fa:16:3e:e7:04:c9 | 10.58.28.90     | Floating | --                    |                  | 
|                                                    |                  | fa:16:3e:7c:67:22 | 10.58.28.91     | Floating | --                    |                  | 
|                                                    |                  | fa:16:3e:fc:2b:eb | 10.58.28.92     | Floating | --                    |                  | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| HA network tenant 05b8e996f0654e4491d2e925a91c6250 | 169.254.192.0/18 | fa:16:3e:10:57:8d | 169.254.192.170 | HA       | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:c4:3b:0f | 169.254.192.5   | HA       | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:c2:ed:bb | 169.254.193.193 | HA       | --                    | AIO-server-2     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/management                                  | 15.100.1.0/24    | fa:16:3e:d3:81:f1 | 15.100.1.1      | DHCP     | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:cc:97:82 | 15.100.1.100    | Compute  | smi5gc/portal         | AIO-server-1     | 
|                                                    |                  | fa:16:3e:c3:6b:06 | 15.100.1.101    | Compute  | smi5gc/lattice        | compute-server-2 | 
|                                                    |                  | fa:16:3e:38:40:30 | 15.100.1.102    | Compute  | smi5gc/server         | compute-server-1 | 
|                                                    |                  | fa:16:3e:22:8e:23 | 15.100.1.103    | Compute  | smi5gc/VPC-SI-mme     | AIO-server-1     | 
|                                                    |                  | fa:16:3e:6b:57:aa | 15.100.1.117    | Compute  | admin/my-c8kv         | compute-server-2 | 
|                                                    |                  | fa:16:3e:a4:f5:53 | 15.100.1.179    | Compute  | ialonso/ORANGE-C8KV-2 | AIO-server-1     | 
|                                                    |                  | fa:16:3e:22:9c:e2 | 15.100.1.191    | Compute  | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                                                    |                  | fa:16:3e:01:17:1c | 15.100.1.192    | Compute  | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                                                    |                  | fa:16:3e:8f:6a:55 | 15.100.1.198    | Compute  | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:2e:aa:e4 | 15.100.1.2      | DHCP     | --                    | AIO-server-2     | 
|                                                    |                  | fa:16:3e:b3:23:ae | 15.100.1.201    | None     | --                    |                  | 
|                                                    |                  | fa:16:3e:97:c1:38 | 15.100.1.219    | Compute  | ialonso/ORANGE-C8KV-1 | AIO-server-1     | 
|                                                    |                  | fa:16:3e:0c:78:90 | 15.100.1.220    | Compute  | admin/c8koncinder     | compute-server-2 | 
|                                                    |                  | fa:16:3e:78:dd:45 | 15.100.1.254    | HA       | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:14:7d:d0 | 15.100.1.30     | Compute  | ialonso/SDWAN-C8KV01B | AIO-server-1     | 
|                                                    |                  | fa:16:3e:bb:2b:cd | 15.100.1.36     | Compute  | smi5gc/esc            | AIO-server-2     | 
|                                                    |                  | fa:16:3e:15:b1:7f | 15.100.1.51     | Compute  | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                                                    |                  | fa:16:3e:57:23:38 | 15.100.1.52     | Compute  | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                                                    |                  | fa:16:3e:13:75:c2 | 15.100.1.69     | Compute  | admin/my-cirros-img   | compute-server-2 | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/orchestration                               | 15.100.2.0/24    | fa:16:3e:e2:ff:72 | 15.100.2.1      | DHCP     | --                    | AIO-server-2     | 
|                                                    |                  | fa:16:3e:88:5f:dd | 15.100.2.103    | Compute  | smi5gc/VPC-SI-mme     | AIO-server-1     | 
|                                                    |                  | fa:16:3e:cf:4b:b5 | 15.100.2.191    | Compute  | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                                                    |                  | fa:16:3e:d8:3b:77 | 15.100.2.192    | Compute  | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                                                    |                  | fa:16:3e:8f:e0:92 | 15.100.2.198    | Compute  | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:9e:96:65 | 15.100.2.2      | DHCP     | --                    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:2d:58:f2 | 15.100.2.36     | Compute  | smi5gc/esc            | AIO-server-2     | 
|                                                    |                  | fa:16:3e:6f:c4:6a | 15.100.2.51     | Compute  | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                                                    |                  | fa:16:3e:92:89:86 | 15.100.2.52     | Compute  | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/sriov0                                      | 15.100.105.0/24  | fa:16:3e:51:c2:e3 | 15.100.105.1    | DHCP     | --                    | AIO-server-2     | 
|                                                    |                  | fa:16:3e:dd:d2:9d | 15.100.105.151  | Compute  | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                                                    |                  | fa:16:3e:18:11:ba | 15.100.105.152  | Compute  | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                                                    |                  | fa:16:3e:e8:f1:d5 | 15.100.105.191  | Compute  | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                                                    |                  | fa:16:3e:48:32:31 | 15.100.105.192  | Compute  | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                                                    |                  | fa:16:3e:fc:e6:60 | 15.100.105.198  | Compute  | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
|                                                    |                  | fa:16:3e:15:37:ec | 15.100.105.2    | DHCP     | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:89:e6:2b | 15.100.105.245  | Compute  | admin/test-sriov      | compute-server-1 | 
|                                                    |                  | fa:16:3e:c3:ad:0b | 15.100.105.51   | Compute  | smi5gc/VPC-SI-saegw1  | AIO-server-3     | 
|                                                    |                  | fa:16:3e:1e:c2:e6 | 15.100.105.52   | Compute  | smi5gc/VPC-SI-saegw2  | AIO-server-2     | 
|                                                    |                  | fa:16:3e:e7:65:c7 | 15.100.105.91   | Compute  | smi5gc/VPC-SI-upf1    | compute-server-1 | 
|                                                    |                  | fa:16:3e:74:59:71 | 15.100.105.92   | Compute  | smi5gc/VPC-SI-upf2    | compute-server-2 | 
|                                                    |                  | fa:16:3e:7d:a2:a1 | 15.100.105.98   | Compute  | smi5gc/VPC-SI-upf8    | AIO-server-3     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+
| smi5gc/sriov1                                      | 15.100.106.0/24  | fa:16:3e:8e:cf:5c | 15.100.106.1    | DHCP     | --                    | AIO-server-1     | 
|                                                    |                  | fa:16:3e:ac:78:eb | 15.100.106.2    | DHCP     | --                    | AIO-server-3     | 
+----------------------------------------------------+------------------+-------------------+-----------------+----------+-----------------------+------------------+

Network - Phy [#15]
-------------------

+----------------------------------------------------+-------+--------+--------------+------------------+-----------------+
| Name                                               | Admin | Status | Network Type | Physical Network | Segmentation ID |
+----------------------------------------------------+-------+--------+--------------+------------------+-----------------+
| ialonso/C8KV01_LAN01                               | V     | ACTIVE | vlan         | physnet1         | 1205            | 
| ialonso/C8KV_ORANGE_LAN01                          | V     | ACTIVE | vlan         | physnet1         | 1206            | 
| smi5gc/control-k8s                                 | V     | ACTIVE | vlan         | physnet1         | 1203            | 
| smi5gc/control-N2                                  | V     | ACTIVE | vlan         | physnet1         | 1105            | 
| smi5gc/control-N4                                  | V     | ACTIVE | vlan         | physnet1         | 1106            | 
| smi5gc/control-SBI                                 | V     | ACTIVE | vlan         | physnet1         | 1193            | 
| smi5gc/data-N3                                     | V     | ACTIVE | vlan         | physnet1         | 1191            | 
| smi5gc/data-N6                                     | V     | ACTIVE | vlan         | physnet1         | 1192            | 
| smi5gc/di-internal1                                | V     | ACTIVE | vlan         | physnet1         | 1204            | 
| admin/external                                     | V     | ACTIVE | vlan         | physnet1         | 113             | 
| HA network tenant 05b8e996f0654e4491d2e925a91c6250 | V     | ACTIVE | vlan         | physnet1         | 1200            | 
| smi5gc/management                                  | V     | ACTIVE | vlan         | physnet1         | 1201            | 
| smi5gc/orchestration                               | V     | ACTIVE | vlan         | physnet1         | 1202            | 
| smi5gc/sriov0                                      | V     | ACTIVE | flat         | phys_sriov0      | --              | 
| smi5gc/sriov1                                      | V     | ACTIVE | flat         | phys_sriov1      | --              | 
+----------------------------------------------------+-------+--------+--------------+------------------+-----------------+

Filter: name, tenant, address, mac, vm, hv, vlan
View:   state (def), id, port, phy, all
```

Developer

```
# iserver get osp net --cluster pod1 -v all

{
    "duration": 9083,
    "osp": {
        "read": true,
        "success": 5,
        "failed": 0,
        "mo": 5,
        "mo_time": 5946,
        "total_time": 5946
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
        "lines": 4
    },
    "cache_hits": 0
}

Log: osp
---------

2023-11-19 13:15:21.206447	True	1526	get	networks
2023-11-19 13:15:23.845983	True	653	get	tenants
2023-11-19 13:15:24.039882	True	187	get	subnets
2023-11-19 13:15:24.446574	True	393	get	ports
2023-11-19 13:15:28.099643	True	3187	get	virtual_machines
```

[[Back]](./NetworkGet.md)