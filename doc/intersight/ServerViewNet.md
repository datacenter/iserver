# Intersight Server

## net view

```
# iserver get server --group test -v net

iaccount demo (cache: any)
Select servers...
Selected servers: 8
Collect server api objects...


IMC [#4]
--------

+-----------+------------+---------------+------------+-------------------+
| Server    | IP         | Mask          | Gateway    | MAC               |
+-----------+------------+---------------+------------+-------------------+
| Server663 | 10.1.1.233 | 255.255.255.0 | 10.1.1.254 | aa:bb:24:52:36:99 |
| Server511 | 10.1.1.96  | 255.255.255.0 | 10.1.1.254 | aa:bb:61:38:29:24 |
| Server515 | 10.1.1.158 | 255.255.255.0 | 10.1.1.254 | aa:bb:63:73:71:33 |
| Server354 | 10.1.1.185 | 255.255.255.0 | 10.1.1.254 | aa:bb:78:13:99:88 |
+-----------+------------+---------------+------------+-------------------+

Network Adapters [#22]
----------------------

+-----------+--------------+---------+--------------------------------------------+--------------------------------------------+--------+-------------------+-----+-----+-----+
| Server    | Name         | PciSlot | Model                                      | PID                                        | Serial | Vendor            | Eth | HBA | DCE |
+-----------+--------------+---------+--------------------------------------------+--------------------------------------------+--------+-------------------+-----+-----+-----+
| Server663 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-79  | 0x8086            | 2   | 0   | 0   |
| Server663 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-57  | 0x8086            | 2   | 0   | 0   |
| Server663 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | Cisco(R) LOM X550-T2                       | SN-40  | 0x8086            | 2   | 0   | 0   |
| Server663 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04                          | SN-36  | Cisco Systems Inc | 4   | 4   | 4   |
| Server511 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-26  | 0x8086            | 2   | 0   | 0   |
| Server511 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-98  | 0x8086            | 2   | 0   | 0   |
| Server511 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | Cisco(R) LOM X550-T2                       | SN-47  | 0x8086            | 2   | 0   | 0   |
| Server511 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04                          | SN-50  | Cisco Systems Inc | 4   | 4   | 4   |
| Server515 | Adapter 3    | 3       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-49  | 0x8086            | 2   | 0   | 0   |
| Server515 | Adapter 6    | 6       | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Cisco(R) Ethernet Converged NIC XXV710-DA2 | SN-12  | 0x8086            | 2   | 0   | 0   |
| Server515 | Adapter L    | L       | Cisco(R) LOM X550-T2                       | Cisco(R) LOM X550-T2                       | SN-68  | 0x8086            | 2   | 0   | 0   |
| Server515 | Adapter MLOM | MLOM    | UCSC-MLOM-C25Q-04                          | UCSC-MLOM-C25Q-04                          | SN-35  | Cisco Systems Inc | 4   | 4   | 4   |
| Server354 | Adapter 1    | 1       | UCSC-PCIE-C25Q-04                          | UCSC-PCIE-C25Q-04                          | SN-30  | Cisco Systems Inc | 8   | 4   | 4   |
| Server354 | Adapter MLOM | MLOM    | UCSC-M-V100-04                             | UCSC-M-V100-04                             | SN-30  | Cisco Systems Inc | 6   | 2   | 2   |
| Server401 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                                         | SN-38  | Cisco Systems Inc | 4   | 0   | 4   |
| Server401 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                                         | SN-16  | Cisco Systems Inc | 4   | 0   | 4   |
| Server818 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                                         | SN-10  | Cisco Systems Inc | 4   | 0   | 4   |
| Server818 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                                         | SN-32  | Cisco Systems Inc | 4   | 0   | 4   |
| Server641 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                                         | SN-61  | Cisco Systems Inc | 4   | 0   | 4   |
| Server641 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                                         | SN-30  | Cisco Systems Inc | 4   | 0   | 4   |
| Server378 | Adapter 1    | N/A     | UCSB-MLOM-40G-04                           | --                                         | SN-79  | Cisco Systems Inc | 4   | 0   | 4   |
| Server378 | Adapter 2    | N/A     | UCSB-VIC-M84-4P                            | --                                         | SN-91  | Cisco Systems Inc | 4   | 0   | 4   |
+-----------+--------------+---------+--------------------------------------------+--------------------------------------------+--------+-------------------+-----+-----+-----+

External Ethernet (MLOM) [#50]
------------------------------

+-----------+-------------------+--------------+-------------------+
| Server    | Adapter Model     | Interface ID | MAC Address       |
+-----------+-------------------+--------------+-------------------+
| Server663 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:49:38:47:10 |
| Server663 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:78:52:14:68 |
| Server663 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:18:27:83:62 |
| Server663 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:70:15:69:51 |
| Server511 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:56:85:43:65 |
| Server511 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:51:57:59:59 |
| Server511 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:78:38:16:46 |
| Server511 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:16:93:32:99 |
| Server515 | UCSC-MLOM-C25Q-04 | 0            | aa:bb:65:25:84:50 |
| Server515 | UCSC-MLOM-C25Q-04 | 1            | aa:bb:29:42:42:80 |
| Server515 | UCSC-MLOM-C25Q-04 | 2            | aa:bb:30:98:74:58 |
| Server515 | UCSC-MLOM-C25Q-04 | 3            | aa:bb:20:91:79:83 |
| Server354 | UCSC-PCIE-C25Q-04 | 0            | aa:bb:87:80:59:93 |
| Server354 | UCSC-PCIE-C25Q-04 | 1            | aa:bb:95:92:20:11 |
| Server354 | UCSC-PCIE-C25Q-04 | 2            | aa:bb:15:92:76:71 |
| Server354 | UCSC-PCIE-C25Q-04 | 3            | aa:bb:18:46:35:84 |
| Server354 | UCSC-M-V100-04    | 0            | aa:bb:59:86:17:26 |
| Server354 | UCSC-M-V100-04    | 1            | aa:bb:66:36:67:45 |
| Server401 | UCSB-MLOM-40G-04  | 1            | aa:bb:58:29:83:24 |
| Server401 | UCSB-MLOM-40G-04  | 3            | aa:bb:45:62:58:39 |
| Server401 | UCSB-MLOM-40G-04  | 5            | aa:bb:78:87:70:86 |
| Server401 | UCSB-MLOM-40G-04  | 7            | aa:bb:14:23:61:77 |
| Server401 | UCSB-VIC-M84-4P   | 1            | aa:bb:63:26:50:82 |
| Server401 | UCSB-VIC-M84-4P   | 3            | aa:bb:92:58:46:99 |
| Server401 | UCSB-VIC-M84-4P   | 5            | aa:bb:51:89:87:21 |
| Server401 | UCSB-VIC-M84-4P   | 7            | aa:bb:42:42:86:58 |
| Server818 | UCSB-MLOM-40G-04  | 1            | aa:bb:62:44:48:65 |
| Server818 | UCSB-MLOM-40G-04  | 3            | aa:bb:52:59:56:87 |
| Server818 | UCSB-MLOM-40G-04  | 5            | aa:bb:22:79:73:29 |
| Server818 | UCSB-MLOM-40G-04  | 7            | aa:bb:67:69:33:12 |
| Server818 | UCSB-VIC-M84-4P   | 1            | aa:bb:73:44:51:21 |
| Server818 | UCSB-VIC-M84-4P   | 3            | aa:bb:76:11:84:88 |
| Server818 | UCSB-VIC-M84-4P   | 5            | aa:bb:31:52:84:96 |
| Server818 | UCSB-VIC-M84-4P   | 7            | aa:bb:22:74:72:33 |
| Server641 | UCSB-MLOM-40G-04  | 1            | aa:bb:76:91:83:59 |
| Server641 | UCSB-MLOM-40G-04  | 3            | aa:bb:94:31:68:91 |
| Server641 | UCSB-MLOM-40G-04  | 5            | aa:bb:62:63:10:86 |
| Server641 | UCSB-MLOM-40G-04  | 7            | aa:bb:39:46:27:27 |
| Server641 | UCSB-VIC-M84-4P   | 1            | aa:bb:85:17:74:52 |
| Server641 | UCSB-VIC-M84-4P   | 3            | aa:bb:33:13:78:94 |
| Server641 | UCSB-VIC-M84-4P   | 5            | aa:bb:72:38:47:55 |
| Server641 | UCSB-VIC-M84-4P   | 7            | aa:bb:17:26:64:63 |
| Server378 | UCSB-MLOM-40G-04  | 1            | aa:bb:35:58:48:42 |
| Server378 | UCSB-MLOM-40G-04  | 3            | aa:bb:78:29:86:79 |
| Server378 | UCSB-MLOM-40G-04  | 5            | aa:bb:72:64:98:54 |
| Server378 | UCSB-MLOM-40G-04  | 7            | aa:bb:81:74:85:84 |
| Server378 | UCSB-VIC-M84-4P   | 1            | aa:bb:54:13:43:48 |
| Server378 | UCSB-VIC-M84-4P   | 3            | aa:bb:49:76:18:50 |
| Server378 | UCSB-VIC-M84-4P   | 5            | aa:bb:48:38:57:32 |
| Server378 | UCSB-VIC-M84-4P   | 7            | aa:bb:69:25:53:23 |
+-----------+-------------------+--------------+-------------------+

Host Ethernet [#76]
-------------------

+-----------+--------------+--------------------------------------------+----------------+-------------------+
| Server    | Adapter Name | Adapter Model                              | Interface Name | MAC Address       |
+-----------+--------------+--------------------------------------------+----------------+-------------------+
| Server663 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-32        | aa:bb:17:82:13:94 |
| Server663 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-62        | aa:bb:97:71:31:78 |
| Server663 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-77        | aa:bb:50:57:43:67 |
| Server663 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-20        | aa:bb:54:56:61:92 |
| Server663 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-17        | aa:bb:23:71:96:67 |
| Server663 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-85        | aa:bb:36:81:78:79 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-20        | aa:bb:15:25:17:16 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-62        | aa:bb:15:39:86:70 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-63        | aa:bb:15:20:62:45 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-53        | aa:bb:23:89:38:72 |
| Server511 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-42        | aa:bb:23:37:99:29 |
| Server511 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-32        | aa:bb:66:11:46:24 |
| Server511 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-31        | aa:bb:16:82:67:83 |
| Server511 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-93        | aa:bb:35:90:21:90 |
| Server511 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-10        | aa:bb:57:51:59:65 |
| Server511 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-59        | aa:bb:48:42:68:22 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-90        | aa:bb:70:49:97:61 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-13        | aa:bb:73:53:46:87 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-65        | aa:bb:74:71:96:43 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-41        | aa:bb:29:58:68:65 |
| Server515 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-90        | aa:bb:42:91:37:77 |
| Server515 | Adapter 3    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-15        | aa:bb:59:63:98:14 |
| Server515 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-44        | aa:bb:47:34:63:26 |
| Server515 | Adapter 6    | Cisco(R) Ethernet Converged NIC XXV710-DA2 | Name-18        | aa:bb:97:44:11:38 |
| Server515 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-12        | aa:bb:74:30:91:50 |
| Server515 | Adapter L    | Cisco(R) LOM X550-T2                       | Name-78        | aa:bb:19:28:14:61 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-77        | aa:bb:93:93:49:61 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-49        | aa:bb:14:75:66:69 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-88        | aa:bb:43:62:62:13 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04                          | Name-43        | aa:bb:78:32:39:81 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-35        | aa:bb:15:78:29:66 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-15        | aa:bb:85:42:10:94 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-45        | aa:bb:20:70:80:88 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-80        | aa:bb:19:17:48:53 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-86        | aa:bb:96:74:45:26 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-89        | aa:bb:46:39:52:30 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-69        | aa:bb:42:63:50:16 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04                          | Name-44        | aa:bb:87:83:87:63 |
| Server354 | Adapter MLOM | UCSC-M-V100-04                             | Name-60        | aa:bb:17:31:47:28 |
| Server354 | Adapter MLOM | UCSC-M-V100-04                             | Name-70        | aa:bb:28:41:55:52 |
| Server354 | Adapter MLOM | UCSC-M-V100-04                             | Name-74        | aa:bb:42:44:85:49 |
| Server354 | Adapter MLOM | UCSC-M-V100-04                             | Name-41        | aa:bb:49:26:34:82 |
| Server354 | Adapter MLOM | UCSC-M-V100-04                             | Name-90        | aa:bb:39:77:44:91 |
| Server354 | Adapter MLOM | UCSC-M-V100-04                             | Name-97        | aa:bb:86:71:64:69 |
| Server401 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-16        | aa:bb:16:23:26:46 |
| Server401 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-76        | aa:bb:77:82:11:14 |
| Server401 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-95        | aa:bb:55:37:47:89 |
| Server401 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-63        | aa:bb:89:17:64:18 |
| Server401 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-25        | aa:bb:36:43:82:88 |
| Server401 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-85        | aa:bb:12:35:94:36 |
| Server401 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-85        | aa:bb:93:14:43:14 |
| Server401 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-28        | aa:bb:27:33:92:27 |
| Server818 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-43        | aa:bb:82:99:28:59 |
| Server818 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-45        | aa:bb:19:76:82:97 |
| Server818 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-47        | aa:bb:86:62:72:67 |
| Server818 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-67        | aa:bb:46:24:27:91 |
| Server818 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-48        | aa:bb:24:54:18:58 |
| Server818 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-45        | aa:bb:47:26:76:94 |
| Server818 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-56        | aa:bb:64:92:47:32 |
| Server818 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-56        | aa:bb:86:53:99:52 |
| Server641 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-41        | aa:bb:32:20:59:91 |
| Server641 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-49        | aa:bb:71:17:42:91 |
| Server641 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-37        | aa:bb:26:64:35:73 |
| Server641 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-41        | aa:bb:54:93:43:17 |
| Server641 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-23        | aa:bb:67:15:76:95 |
| Server641 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-58        | aa:bb:36:35:12:54 |
| Server641 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-96        | aa:bb:73:15:22:99 |
| Server641 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-49        | aa:bb:70:69:93:93 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-81        | aa:bb:58:58:56:22 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-78        | aa:bb:53:35:49:71 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-37        | aa:bb:88:80:94:97 |
| Server378 | Adapter 1    | UCSB-MLOM-40G-04                           | Name-98        | aa:bb:21:20:68:81 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-99        | aa:bb:63:10:43:20 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-40        | aa:bb:59:51:98:66 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-31        | aa:bb:27:85:76:98 |
| Server378 | Adapter 2    | UCSB-VIC-M84-4P                            | Name-56        | aa:bb:97:71:83:94 |
+-----------+--------------+--------------------------------------------+----------------+-------------------+

Host FC [#18]
-------------

+-----------+--------------+-------------------+----------------+-------------------------+-------------------------+
| Server    | Adapter Name | Adapter Model     | Interface Name | WWNN                    | WWPN                    |
+-----------+--------------+-------------------+----------------+-------------------------+-------------------------+
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc0            | 10:10:aa:bb:83:55:78:45 | 20:20:aa:bb:61:49:80:63 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc1            | 10:10:aa:bb:43:90:53:24 | 20:20:aa:bb:28:60:83:82 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc2            | 10:10:aa:bb:54:66:14:48 | 20:20:aa:bb:85:11:64:69 |
| Server663 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc3            | 10:10:aa:bb:95:49:43:17 | 20:20:aa:bb:12:25:84:36 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc0            | 10:10:aa:bb:15:59:17:68 | 20:20:aa:bb:56:37:48:27 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc1            | 10:10:aa:bb:42:12:83:66 | 20:20:aa:bb:29:88:37:28 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc2            | 10:10:aa:bb:35:71:89:99 | 20:20:aa:bb:40:42:96:14 |
| Server511 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc3            | 10:10:aa:bb:63:46:19:22 | 20:20:aa:bb:95:23:24:26 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc0            | 10:10:aa:bb:93:87:30:12 | 20:20:aa:bb:43:75:31:58 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc1            | 10:10:aa:bb:30:39:25:25 | 20:20:aa:bb:61:26:26:94 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc2            | 10:10:aa:bb:58:14:77:69 | 20:20:aa:bb:66:67:67:32 |
| Server515 | Adapter MLOM | UCSC-MLOM-C25Q-04 | fc3            | 10:10:aa:bb:86:52:82:33 | 20:20:aa:bb:13:93:53:70 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc0            | 10:10:aa:bb:12:63:20:27 | 20:20:aa:bb:54:81:85:54 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc1            | 10:10:aa:bb:41:50:38:97 | 20:20:aa:bb:85:30:73:54 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc2            | 10:10:aa:bb:70:64:19:40 | 20:20:aa:bb:47:46:86:84 |
| Server354 | Adapter 1    | UCSC-PCIE-C25Q-04 | fc3            | 10:10:aa:bb:31:45:33:92 | 20:20:aa:bb:76:76:70:93 |
| Server354 | Adapter MLOM | UCSC-M-V100-04    | fc0            | 10:10:aa:bb:78:11:17:63 | 20:20:aa:bb:46:44:21:41 |
| Server354 | Adapter MLOM | UCSC-M-V100-04    | fc1            | 10:10:aa:bb:74:96:76:81 | 20:20:aa:bb:68:86:17:64 |
+-----------+--------------+-------------------+----------------+-------------------------+-------------------------+

Filter: ip, name, serial, model, type, group, led, power, alarm, mode
        disc, cname, cmodel, cserial, cpu, gpu, mem, pci, mac, sc, pd, vd, fan, psu
View:   state (def), adv, alarm, board, boot, connector, contract, cpu, env, fan, fw, gpu, hcl, hw, inv, istate
        kvm, lic, mem, net, pci, power, profile, psu, sc, pd, vd, storage, sw, thermal, tpm, workflow, summary
Ctx:    ip, mac
```

[[Back]](./ServerInventory.md)