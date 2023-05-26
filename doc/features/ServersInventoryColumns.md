# Extra server information

Use -c|--column options to extend per server information from the base output i.e. State, Name, Model, Serial, IP, CPU and ServersInventoryMemory.md

Add extra columns using comma (,) seperated keywords from the list: id,fw,pci,fan,psu,group,storage

You can define as many columns as you want, just be mindful of your terminal width for nice display.

Note: extra columns is more information to be gathered from Intersight via API and thus more time you will likely wait to get the result.

## Base output (-c|--column not used)

```
# iserver get servers --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Server ID (id)

```
# iserver get servers --column id --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+---------------------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | Moid                      |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+---------------------------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 5fdf9c016176752d35e44795  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 5fdf9c786176752d35e47110  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 5fdf9d026176752d35e4ac4e  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 5fdfa1806176752d35e678c2  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 5fdfdc3b6176752d35fce0a9  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 5fdfe47f6176752d35001995  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 5fdfe80d6176752d3502b008  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+---------------------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Firmware Version (fw)

```
# iserver get servers --column fw --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+----------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | Fw       |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+----------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+----------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## PCI devices (pci)

```
# iserver get servers --column pci --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-------------------------------------------------------------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | PCI                                                               |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-------------------------------------------------------------------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | UCSC-MLOM-C25Q-04                                                 | 
|            |                                 |                 |              |              |             |            | UCSC-RAID-M5                                                      | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
|            |                                 |                 |              |              |             |            | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-PCIE-ID25GF                                                  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-MLOM-C25Q-04                                                 | 
|            |                                 |                 |              |              |             |            | UCSC-RAID-M5                                                      | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco UCS VIC 1457 MLOM                                           | 
|            |                                 |                 |              |              |             |            | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)  | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-MLOM-C25Q-04                                                 | 
|            |                                 |                 |              |              |             |            | UCSC-RAID-M5                                                      | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-MLOM-C25Q-04                                                 | 
|            |                                 |                 |              |              |             |            | UCSC-RAID-M5                                                      | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco(R) Ethernet Converged NIC XXV710-DA2                        | 
|            |                                 |                 |              |              |             |            | Cisco UCS VIC 1457 MLOM                                           | 
|            |                                 |                 |              |              |             |            | Cisco 12G Modular Raid Controller with 2GB cache (max 16 drives)  | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-PCIE-ID25GF                                                  | 
|            |                                 |                 |              |              |             |            | UCSC-MLOM-C25Q-04                                                 | 
|            |                                 |                 |              |              |             |            | UCSC-RAID-M5                                                      | 
|            |                                 |                 |              |              |             |            | Intel X550 LOM                                                    | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-------------------------------------------------------------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Fan State (fan)

```
# iserver get servers --column fan --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | Fan  |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 0/7  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 6/7  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 6/7  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 7/7  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 7/7  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 7/7  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 7/7  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## PSU State (psu)

```
# iserver get servers --column psu --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | Psu  |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 2/2  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Storage (storage)

```
# iserver get servers --column storage --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-----------------+------------------------------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | Storage Drives  | Storage Capacity             |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-----------------+------------------------------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 1C 6H 4S 1VD    | R 11.03 [TB] , VD 1.92 [TB]  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 1C 6H 4S 1VD    | R 11.03 [TB] , VD 1.92 [TB]  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 1C 6H 4S 1VD    | R 11.03 [TB] , VD 1.92 [TB]  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 1C 2H 0S 1VD    | R 2.4 [TB] , VD 1.2 [TB]     | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 1C 2H 0S 1VD    | R 2.4 [TB] , VD 1.2 [TB]     | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 1C 2H 0S 1VD    | R 2.4 [TB] , VD 1.2 [TB]     | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 1C 2H 0S 1VD    | R 2.4 [TB] , VD 1.2 [TB]     | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+-----------------+------------------------------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```

## Multiple choice

```
# iserver get servers --column fw,fan,psu --group p2b

+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+----------+------+------+
| Flags      | Name                            | Model           | Serial       | IP           | CPU         | Memory     | Fw       | Fan  | Psu  |
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+----------+------+------+
| P-HRS      | aio-1-p2b-eu-spdc-WZP23400AJW   | UCSC-C240-M5SN  | WZP23400AJW  | 10.58.50.41  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 0/7  | 2/2  | 
| P+HRS      | aio-2-p2b-eu-spdc-WZP23400AK4   | UCSC-C240-M5SN  | WZP23400AK4  | 10.58.50.42  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 6/7  | 2/2  | 
| P+HRS      | aio-3-p2b-eu-spdc-WZP23400AKL   | UCSC-C240-M5SN  | WZP23400AKL  | 10.58.50.43  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 6/7  | 2/2  | 
| P+HRS W16  | comp-1-p2b-eu-spdc-WMP240400FM  | UCSC-C220-M5SX  | WMP240400FM  | 10.58.50.44  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 7/7  | 2/2  | 
| P+HRS      | comp-2-p2b-eu-spdc-WMP2404000R  | UCSC-C220-M5SX  | WMP2404000R  | 10.58.50.45  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 7/7  | 2/2  | 
| P+HRS W39  | comp-3-p2b-eu-spdc-WMP24040059  | UCSC-C220-M5SX  | WMP24040059  | 10.58.50.46  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 7/7  | 2/2  | 
| P+HRS      | comp-4-p2b-eu-spdc-WMP24040061  | UCSC-C220-M5SX  | WMP24040061  | 10.58.50.47  | 2S 40C 80T  | 384 [GiB]  | 4.1(3d)  | 7/7  | 2/2  | 
+------------+---------------------------------+-----------------+--------------+--------------+-------------+------------+----------+------+------+

Flags
- Power      : (P+) on (P-) off
- Health     : (H)ealthy (W)arning (C)ritical
- Type       : (R)ack (B)lade
- Management : (U)CSM (S)tandalone
- Locator    : (L)ocator on
- Workflow   : W(R)(F)(f)n - (R)unning, Last (F)ailed, Some (f)ailed, n-workflows last 24 hours
```
