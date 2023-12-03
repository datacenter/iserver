# Security Group

## All view

```
# iserver get osp sg --cluster pod1 -v all

Cluster: pod1

Security Group [#7]
-------------------

+---------+---------+------------+--------+--------+
| Tenant  | Name    | Rule Count | Create | Update |
+---------+---------+------------+--------+--------+
| --      | default | 4          | 474d   | 474d   | 
| admin   | default | 4          | 474d   | 474d   | 
| ialonso | default | 5          | 35d    | 28d    | 
| service | default | 4          | 474d   | 474d   | 
| smi5gc  | default | 39         | 473d   | 473d   | 
| smi5gc  | esc     | 7          | 4d     | 4d     | 
| smi5gc  | portal  | 20         | 473d   | 473d   | 
+---------+---------+------------+--------+--------+

Security Group - Identifier [#7]
--------------------------------

+---------+----------------------------------+--------------------------------------+
| Name    | Tenant                           | Rule                                 |
+---------+----------------------------------+--------------------------------------+
| default |                                  | 09868919-41d1-419c-abc4-fb0bc4ddb34d | 
|         |                                  | 283e6f7d-5d81-40de-aca4-ad4c026ed4ad | 
|         |                                  | f5edcccb-a604-40b0-9fbc-b298e1e9aa1c | 
|         |                                  | fa0f5de0-7199-40cd-905b-25ee5ce3d85b | 
+---------+----------------------------------+--------------------------------------+
| default | 2cced286b74c45ea95c83cc2e5d3b413 | 09700ca8-6339-4395-88fb-74130a335071 | 
|         |                                  | 89072767-80c2-4260-8d6f-fa4f984be4d2 | 
|         |                                  | fe1f29f8-fe61-44ef-b375-d559c17229ac | 
|         |                                  | 8ee22091-b196-4d00-be36-51da89dceec5 | 
+---------+----------------------------------+--------------------------------------+
| default | 9b50a8dba82f4c14802c4554482882b8 | a2cc64e9-5ddd-412a-9dea-12a659f29357 | 
|         |                                  | 50f4859b-6ae6-4692-9527-8e406cbf9505 | 
|         |                                  | c15fd4cc-2bb9-4dda-8e2f-a349595adf51 | 
|         |                                  | f91eff6d-8a81-4b9b-bf10-7af90304a9e5 | 
|         |                                  | d64a38e0-2d2d-402d-b041-880f3a6886fd | 
+---------+----------------------------------+--------------------------------------+
| default | c4a93dc9499e40f78e32a83d914e6a87 | 828fb3fc-4e3b-440e-bb6d-61a04abd7503 | 
|         |                                  | 252e079d-c45d-46b0-a629-45fc78beae06 | 
|         |                                  | 5ce58fbb-c286-4817-bd51-731b2623fde3 | 
|         |                                  | 9dd91972-ea6e-4461-a73e-74839f2bdc24 | 
+---------+----------------------------------+--------------------------------------+
| default | 05b8e996f0654e4491d2e925a91c6250 | accc2487-4273-4eee-a008-d1ed98804cff | 
|         |                                  | 01cd497b-8e42-447d-bb32-2c62813ed868 | 
|         |                                  | 0d6b5ca6-e7ce-4e2e-87cb-e6c1a1217417 | 
|         |                                  | 14a7d385-5118-49fb-bf11-9e128c6240e6 | 
|         |                                  | 1b377be8-676e-4212-bfcd-c7b9778c7f6c | 
|         |                                  | 2ce8f2d9-db88-4633-9a35-96547a55a6a9 | 
|         |                                  | 2d35a6ab-9de0-48b2-b16f-b1244502e7e1 | 
|         |                                  | 33bbc6d0-252c-423a-a431-7e45cd3aae9f | 
|         |                                  | 39cb967a-59e6-4471-b330-22220a6db723 | 
|         |                                  | 3a631fe4-4b1a-4ed0-8cba-ae6feebd73e0 | 
|         |                                  | 46dd4ad4-3ea1-4fd7-8102-88233931fd0b | 
|         |                                  | 526b509b-55c9-4e4e-989b-3441afd7c42c | 
|         |                                  | 5ba766ac-6b21-4532-b98e-182a189d1ca8 | 
|         |                                  | 65b722c4-67be-479e-b1b4-68bd66ef6fcd | 
|         |                                  | 7194647b-a6fd-44f8-8ea5-a57be7ce5a0a | 
|         |                                  | 8355b3dc-09b3-444b-9609-18b6d8e22ddf | 
|         |                                  | 94e6b62f-d42f-4046-86fc-7891460f050e | 
|         |                                  | 950bc184-01c6-4ac9-ad3f-a9b37ef13617 | 
|         |                                  | 96bd2e8d-ae1f-46c3-86ff-6da67a9c9110 | 
|         |                                  | 99580df3-8af9-4751-8c5a-93b8bc090a21 | 
|         |                                  | b3608de0-bfbd-4819-97f0-599b77c5d5d6 | 
|         |                                  | b7b37b4c-5481-4c57-b264-e0f295a3767b | 
|         |                                  | ba46f9c6-8914-4bd5-b3d6-4121a07f9e44 | 
|         |                                  | c65d888f-d777-4e1d-af22-c807fa19e189 | 
|         |                                  | c663e9b6-b044-4467-bf87-06830b72b02f | 
|         |                                  | d249a30b-4ec3-42fd-8eb3-a0e214e0a8dc | 
|         |                                  | d65bf5aa-44a1-4aa0-aa97-9416c1eef057 | 
|         |                                  | d8c8d8ba-a9e7-467e-980a-3f1e7373229e | 
|         |                                  | d91888dd-c989-488d-b07d-c8169640eda9 | 
|         |                                  | dbd96f97-742d-4626-9d5c-06cad6819c99 | 
|         |                                  | e5df190a-c050-4160-b6e2-c7b970d66831 | 
|         |                                  | e6d0a07e-ba88-4a72-9378-5c1ea4d80ea5 | 
|         |                                  | e83c05f2-032b-455e-99b1-68266b7d9d83 | 
|         |                                  | ebe4d27c-bfbe-43cb-b1d1-d309fec43920 | 
|         |                                  | ec95c547-dcfd-451b-aea6-d776dc9d977b | 
|         |                                  | ee566a63-5bae-44ef-80ac-880bd7b8a825 | 
|         |                                  | f4383fec-49ce-4309-a3e2-05eaa9702901 | 
|         |                                  | a23c9244-83ae-4b15-a402-0c49fb149314 | 
|         |                                  | 881d1a9b-d751-4a9f-8da8-7ec6ec430c7f | 
+---------+----------------------------------+--------------------------------------+
| esc     | 05b8e996f0654e4491d2e925a91c6250 | 76bb7897-fe98-40b7-b161-3226c904a807 | 
|         |                                  | 260a9b84-3d92-4edc-a5d0-cc4461f791b7 | 
|         |                                  | 28ad9d91-398d-4332-b4a5-5a441185eb62 | 
|         |                                  | 32196847-b806-43a6-916e-88109c2d5344 | 
|         |                                  | 6afba737-337b-4e15-83c7-1af3ddf8abe8 | 
|         |                                  | c8707327-e50c-4af8-9fd4-5590f09a5619 | 
|         |                                  | 8ffbf025-2b9f-4ffa-ae06-feee77186979 | 
+---------+----------------------------------+--------------------------------------+
| portal  | 05b8e996f0654e4491d2e925a91c6250 | 179ed758-6744-474f-a509-c3feb5453913 | 
|         |                                  | 20826c24-c6c0-4271-ae58-afdaa0561b25 | 
|         |                                  | 3a1fdc27-7b56-40ee-80a6-e95d1527e53c | 
|         |                                  | 47fc0bdd-4c79-4726-bcb7-6373d98d2f42 | 
|         |                                  | 48c808ae-f346-44ed-ad80-5d1fdaa21723 | 
|         |                                  | 4fed5e65-1b1a-42b7-a883-4434bc84eed9 | 
|         |                                  | 551f09be-08ac-42c0-a288-388068f44d76 | 
|         |                                  | 5d4e1e76-7663-4eee-bf53-ad3f657727e7 | 
|         |                                  | 5feeaaad-469a-44ae-9a07-f83e1b43beca | 
|         |                                  | 7aaf2b8f-c7be-417e-8212-a3e476423422 | 
|         |                                  | 812f423d-24be-4641-bc4e-3ed09b1c7a2f | 
|         |                                  | 85a0cff9-eeff-4317-9bf5-73d1a6aaca7e | 
|         |                                  | 899f6b1e-ad47-4e31-bb81-528665001762 | 
|         |                                  | 8cafaf16-abcc-487c-9840-c62e14ae59de | 
|         |                                  | 8e55269e-3ca4-40bc-a7f7-8a4de889e99e | 
|         |                                  | a7261e16-ccdf-4593-90e7-3a695d9e0cfe | 
|         |                                  | b0b46750-d29a-40db-bb1f-c99622e5d4cb | 
|         |                                  | b281d3e7-72d4-4674-a2cf-f31291daadf2 | 
|         |                                  | bc2c79a5-484e-4b6d-81b6-c181b261c216 | 
|         |                                  | c2682112-6b71-4f22-af31-9d26c46e8d87 | 
+---------+----------------------------------+--------------------------------------+

Security Group - Rule [#7]
--------------------------

+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| Tenant  | Name    | EtherType | Direction | Protocol | Port Range  | Remote Prefix | Remote Group    | Create | Update |
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| --      | default | IPv4      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | --/default      | 474d   | 474d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | --/default      | 474d   | 474d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| admin   | default | IPv4      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | admin/default   | 474d   | 474d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | admin/default   | 474d   | 474d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| ialonso | default | IPv4      | egress    | --       | --          | --            | --              | 35d    | 35d    | 
|         |         | IPv4      | ingress   | --       | --          | 0.0.0.0/0     | --              | 28d    | 28d    | 
|         |         | IPv4      | ingress   | --       | --          | --            | ialonso/default | 35d    | 35d    | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 35d    | 35d    | 
|         |         | IPv6      | ingress   | --       | --          | --            | ialonso/default | 35d    | 35d    | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| service | default | IPv4      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | service/default | 474d   | 474d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 474d   | 474d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | service/default | 474d   | 474d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| smi5gc  | default | IPv4      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9830-9830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 4022-4022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 4830-4830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 1022-1022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5022-5022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 179-179     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 6443-6443   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 7022-7022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 6022-6022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8081-8081   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 6830-6830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 2123-2123   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9022-9022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 7830-7830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2022-2022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | sctp     | 38412-38412 | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 1812-1812   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 1830-1830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2153-2153   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 20001-20004 | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2024-2024   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | --       | --          | --            | smi5gc/default  | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3830-3830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 2830-2830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 2152-2152   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8022-8022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3868-3868   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5021-5091   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8830-8830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 1813-1813   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5830-5830   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3022-3022   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
|         |         | IPv6      | ingress   | --       | --          | --            | smi5gc/default  | 473d   | 473d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| smi5gc  | esc     | IPv4      | egress    | --       | --          | --            | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 8250-8250   | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 4d     | 4d     | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 4d     | 4d     | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+
| smi5gc  | portal  | IPv4      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 123-123     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 24224-24224 | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8010-8010   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3142-3142   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8280-8280   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 3000-3000   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9095-9095   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9191-9191   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 5141-5141   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9080-9080   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 5601-5601   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | udp      | 53-53       | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv4      | ingress   | tcp      | 9090-9090   | 0.0.0.0/0     | --              | 473d   | 473d   | 
|         |         | IPv6      | egress    | --       | --          | --            | --              | 473d   | 473d   | 
+---------+---------+-----------+-----------+----------+-------------+---------------+-----------------+--------+--------+

Security Group - Port and Rule [#7]
-----------------------------------

+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| Tenant  | Name    | MAC               | VM                    | EtherType | Direction | Protocol | Port Range  | Remote Prefix | Remote Group    |
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| --      | default | fa:16:3e:5c:b7:b8 | ialonso/ORANGE-C8KV-1 | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:3b:d5:c6 | ialonso/SDWAN-C8KV01B | IPv4      | ingress   | --       | --          | --            | --/default      | 
|         |         | fa:16:3e:67:1b:48 | ialonso/ORANGE-C8KV-2 | IPv6      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:ae:32:44 | admin/c8koncinder     | IPv6      | ingress   | --       | --          | --            | --/default      | 
|         |         | fa:16:3e:c3:6b:06 | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:38:40:30 | smi5gc/server         |           |           |          |             |               |                 | 
|         |         | fa:16:3e:22:8e:23 | smi5gc/VPC-SI-mme     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:6b:57:aa | admin/my-c8kv         |           |           |          |             |               |                 | 
|         |         | fa:16:3e:a4:f5:53 | ialonso/ORANGE-C8KV-2 |           |           |          |             |               |                 | 
|         |         | fa:16:3e:22:9c:e2 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:01:17:1c | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:8f:6a:55 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:b3:23:ae | --                    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:97:c1:38 | ialonso/ORANGE-C8KV-1 |           |           |          |             |               |                 | 
|         |         | fa:16:3e:0c:78:90 | admin/c8koncinder     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:78:dd:45 | --                    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:14:7d:d0 | ialonso/SDWAN-C8KV01B |           |           |          |             |               |                 | 
|         |         | fa:16:3e:bb:2b:cd | smi5gc/esc            |           |           |          |             |               |                 | 
|         |         | fa:16:3e:15:b1:7f | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:57:23:38 | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:13:75:c2 | admin/my-cirros-img   |           |           |          |             |               |                 | 
|         |         | fa:16:3e:dd:d2:9d | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:18:11:ba | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:e8:f1:d5 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:48:32:31 | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:fc:e6:60 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:89:e6:2b | admin/test-sriov      |           |           |          |             |               |                 | 
|         |         | fa:16:3e:c3:ad:0b | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:1e:c2:e6 | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:e7:65:c7 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:74:59:71 | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:7d:a2:a1 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:88:5f:dd | smi5gc/VPC-SI-mme     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:cf:4b:b5 | smi5gc/VPC-SI-upf1    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:d8:3b:77 | smi5gc/VPC-SI-upf2    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:8f:e0:92 | smi5gc/VPC-SI-upf8    |           |           |          |             |               |                 | 
|         |         | fa:16:3e:2d:58:f2 | smi5gc/esc            |           |           |          |             |               |                 | 
|         |         | fa:16:3e:6f:c4:6a | smi5gc/VPC-SI-saegw1  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:92:89:86 | smi5gc/VPC-SI-saegw2  |           |           |          |             |               |                 | 
|         |         | fa:16:3e:cc:7f:24 | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:63:7d:aa | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:fe:4d:de | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:70:4d:85 | smi5gc/lattice        |           |           |          |             |               |                 | 
|         |         | fa:16:3e:7c:ff:47 | smi5gc/VPC-SI-mme     |           |           |          |             |               |                 | 
|         |         | fa:16:3e:b4:94:eb | smi5gc/server         |           |           |          |             |               |                 | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| admin   | default | fa:16:3e:ae:32:44 | admin/c8koncinder     | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:6b:57:aa | admin/my-c8kv         | IPv4      | ingress   | --       | --          | --            | admin/default   | 
|         |         | fa:16:3e:0c:78:90 | admin/c8koncinder     | IPv6      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:13:75:c2 | admin/my-cirros-img   | IPv6      | ingress   | --       | --          | --            | admin/default   | 
|         |         | fa:16:3e:89:e6:2b | admin/test-sriov      |           |           |          |             |               |                 | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| ialonso | default | fa:16:3e:5c:b7:b8 | ialonso/ORANGE-C8KV-1 | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:3b:d5:c6 | ialonso/SDWAN-C8KV01B | IPv4      | ingress   | --       | --          | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:67:1b:48 | ialonso/ORANGE-C8KV-2 | IPv4      | ingress   | --       | --          | --            | ialonso/default | 
|         |         | fa:16:3e:a4:f5:53 | ialonso/ORANGE-C8KV-2 | IPv6      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:97:c1:38 | ialonso/ORANGE-C8KV-1 | IPv6      | ingress   | --       | --          | --            | ialonso/default | 
|         |         | fa:16:3e:14:7d:d0 | ialonso/SDWAN-C8KV01B |           |           |          |             |               |                 | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| service | default |                   |                       | IPv4      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv4      | ingress   | --       | --          | --            | service/default | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv6      | ingress   | --       | --          | --            | service/default | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| smi5gc  | default | fa:16:3e:c3:6b:06 | smi5gc/lattice        | IPv4      | egress    | --       | --          | --            | --              | 
|         |         | fa:16:3e:38:40:30 | smi5gc/server         | IPv4      | ingress   | tcp      | 9830-9830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:22:8e:23 | smi5gc/VPC-SI-mme     | IPv4      | ingress   | tcp      | 4022-4022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:22:9c:e2 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | tcp      | 4830-4830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:01:17:1c | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | tcp      | 1022-1022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:8f:6a:55 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | tcp      | 5022-5022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:b3:23:ae | --                    | IPv4      | ingress   | tcp      | 179-179     | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:78:dd:45 | --                    | IPv4      | ingress   | tcp      | 6443-6443   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:bb:2b:cd | smi5gc/esc            | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:15:b1:7f | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 7022-7022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:57:23:38 | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 6022-6022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:dd:d2:9d | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 8081-8081   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:18:11:ba | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:e8:f1:d5 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | tcp      | 6830-6830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:48:32:31 | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | udp      | 2123-2123   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:fc:e6:60 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | tcp      | 9022-9022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:c3:ad:0b | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 7830-7830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:1e:c2:e6 | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 2022-2022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:e7:65:c7 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | sctp     | 38412-38412 | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:74:59:71 | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:7d:a2:a1 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | udp      | 1812-1812   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:88:5f:dd | smi5gc/VPC-SI-mme     | IPv4      | ingress   | tcp      | 1830-1830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:cf:4b:b5 | smi5gc/VPC-SI-upf1    | IPv4      | ingress   | tcp      | 2153-2153   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:d8:3b:77 | smi5gc/VPC-SI-upf2    | IPv4      | ingress   | tcp      | 20001-20004 | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:8f:e0:92 | smi5gc/VPC-SI-upf8    | IPv4      | ingress   | tcp      | 2024-2024   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:2d:58:f2 | smi5gc/esc            | IPv4      | ingress   | --       | --          | --            | smi5gc/default  | 
|         |         | fa:16:3e:6f:c4:6a | smi5gc/VPC-SI-saegw1  | IPv4      | ingress   | tcp      | 3830-3830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:92:89:86 | smi5gc/VPC-SI-saegw2  | IPv4      | ingress   | tcp      | 2830-2830   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:cc:7f:24 | smi5gc/lattice        | IPv4      | ingress   | udp      | 2152-2152   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:63:7d:aa | smi5gc/lattice        | IPv4      | ingress   | tcp      | 8022-8022   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:fe:4d:de | smi5gc/lattice        | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:70:4d:85 | smi5gc/lattice        | IPv4      | ingress   | tcp      | 3868-3868   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:7c:ff:47 | smi5gc/VPC-SI-mme     | IPv4      | ingress   | tcp      | 5021-5091   | 0.0.0.0/0     | --              | 
|         |         | fa:16:3e:b4:94:eb | smi5gc/server         | IPv4      | ingress   | tcp      | 8830-8830   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 1813-1813   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 5830-5830   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 3022-3022   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv6      | ingress   | --       | --          | --            | smi5gc/default  | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| smi5gc  | esc     | fa:16:3e:bb:2b:cd | smi5gc/esc            | IPv4      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 830-830     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8250-8250   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+
| smi5gc  | portal  | fa:16:3e:cc:97:82 | smi5gc/portal         | IPv4      | egress    | --       | --          | --            | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 123-123     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 80-80       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 24224-24224 | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 22-22       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8010-8010   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 3142-3142   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8280-8280   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 8080-8080   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 3000-3000   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 443-443     | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9095-9095   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9191-9191   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | icmp     | --          | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 5141-5141   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9080-9080   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 5601-5601   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | udp      | 53-53       | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv4      | ingress   | tcp      | 9090-9090   | 0.0.0.0/0     | --              | 
|         |         |                   |                       | IPv6      | egress    | --       | --          | --            | --              | 
+---------+---------+-------------------+-----------------------+-----------+-----------+----------+-------------+---------------+-----------------+

Filter: name, tenant, mac, vm
View:   state (def), id, rule, port, all
```

Developer

```
# iserver get osp sg --cluster pod1 -v all

{
    "duration": 7689,
    "osp": {
        "read": true,
        "success": 4,
        "failed": 0,
        "mo": 4,
        "mo_time": 5364,
        "total_time": 5364
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

2023-11-20 18:23:11.575777	True	2173	get	security_groups
2023-11-20 18:23:11.980057	True	383	get	tenants
2023-11-20 18:23:12.279823	True	285	get	ports
2023-11-20 18:23:15.443216	True	2523	get	virtual_machines
```

[[Back]](./SecurityGroupGet.md)