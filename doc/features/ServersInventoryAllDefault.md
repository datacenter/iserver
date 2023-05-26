# Servers inventory in table mode

Use default output (-o) format.

```
# iserver get servers

+---------+-----+----+------------------------------------------+-------------------------------+----------------+---------------+--------------+-----------+
| SF      | MF  | WF | Name                                     | Model                         | Serial         | IP            | CPU          | Memory    |
+---------+-----+----+------------------------------------------+-------------------------------+----------------+---------------+--------------+-----------+
| P+ H    | Cri |    |  C220-WZP23350ZAQ                        | (R) UCSC-C220-M5SX            | WZP23350ZAQ    | 10.58.244.186 | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    |  C220-WZP23360FH9                        | (R) UCSC-C220-M5SX            | WZP23360FH9    | 10.58.244.70  | 2S 40C 80T   | 384 [GiB] | 
| P+ C(1) | Cri |    | C220-231                                 | (R) UCSC-C220-M5SX            | WZP23240NNZ    | 10.58.250.241 | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    | C240-WZP232102PH                         | (R) UCSC-C240-M5SX            | WZP232102PH    | 10.58.244.236 | 2S 56C 112T  | 512 [GiB] | 
| P- H    | cri |    | C3X60M4-FCH21067808                      | (B) UCSC-C3K-M4SRB            | FCH21067808    |               | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | Cri |    | Dell-PowerEdge R650-YGFCBTJSO8WOMR       | (R) PowerEdge R650            | YGFCBTJSO8WOMR | 10.44.182.90  | 2S 56C 112T  | 128 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-1                     | (B) UCSB-B200-M4              | FCH205371PZ    | 10.58.52.33   | 2S 24C 48T   | 512 [GiB] | 
| P+ C(9) | CU  |    | FI-ucsb1-eu-spdc-1-2                     | (B) UCSB-B200-M4              | FCH20527XXD    | 10.58.52.34   | 2S 24C 48T   | 512 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-3                     | (B) UCSB-B200-M4              | FCH20437VXH    | 10.58.52.35   | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-1-4                     | (B) UCSB-B200-M4              | FCH205371UU    | 10.58.52.36   | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-1                     | (B) UCSB-B200-M5              | FLM241501FB    | 10.58.52.41   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-2                     | (B) UCSB-B200-M5              | FLM24140BJB    | 10.58.52.42   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-3                     | (B) UCSB-B200-M5              | FLM241501CT    | 10.58.52.43   | 2S 40C 80T   | 192 [GiB] | 
| P+ H    | CU  |    | FI-ucsb1-eu-spdc-2-4                     | (B) UCSB-B200-M5              | FLM24140B0B    | 10.58.52.44   | 2S 40C 80T   | 192 [GiB] | 
| P+ H    | Cri |    | HPE-ProLiant DL360 Gen10 Plus-VYRBX9UJ4S | (R) ProLiant DL360 Gen10 Plus | VYRBX9UJ4S     | 10.242.29.174 | 2S 56C 112T  | 32 [GiB]  | 
| P- C(2) | Cu  |    | HX1-eu-spdc-1                            | (R) HXAF220C-M5SN             | WZP24100SMV    | 10.58.24.56   | 2S 40C 80T   | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-2                            | (R) HXAF220C-M5SN             | WZP24100SN0    | 10.58.24.55   | 2S 40C 80T   | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-3                            | (R) HXAF220C-M5SN             | WZP24100SML    | 10.58.24.53   | 2S 40C 80T   | 384 [GiB] | 
| P+ C(3) | Cu  |    | HX1-eu-spdc-4                            | (R) HXAF220C-M5SN             | WZP24100SMP    | 10.58.24.57   | 2S 40C 80T   | 384 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-5                            | (R) HXAF240C-M5SX             | WMP250901B0    | 10.58.24.58   | 2S 52C 104T  | 768 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-6                            | (R) HXAF240C-M5SX             | WMP250901AY    | 10.58.24.59   | 2S 52C 104T  | 768 [GiB] | 
| P- H    | Cu  |    | HX1-eu-spdc-7                            | (R) HXAF240C-M5SX             | WMP2509019D    | 10.58.24.54   | 2S 52C 104T  | 768 [GiB] | 
| P+ H    | Cri |    | POD-4A-AIO-1-WZP23400AK9                 | (R) UCSC-C240-M5SN            | WZP23400AK9    | 10.58.29.55   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    | POD-4A-AIO-2-WZP23400AK7                 | (R) UCSC-C240-M5SN            | WZP23400AK7    | 10.58.29.56   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    | POD-4A-AIO-3-WZP23400AM2                 | (R) UCSC-C240-M5SN            | WZP23400AM2    | 10.58.29.57   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    | aio-1-p1-eu-spdc-WZP22490ZCU             | (R) UCSC-C220-M5SX            | WZP22490ZCU    | 10.58.28.41   | 2S 44C 88T   | 256 [GiB] | 
| P+ H    | Cri |    | aio-2-p1-eu-spdc-WZP22520Y69             | (R) UCSC-C220-M5SX            | WZP22520Y69    | 10.58.28.42   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | aio-3-p1-eu-spdc-WZP22520Y54             | (R) UCSC-C220-M5SX            | WZP22520Y54    | 10.58.28.43   | 2S 44C 88T   | 256 [GiB] | 
| P- H    | cri |    | aio1-p5g-eu-spdc-WZP23450C7D             | (R) UCSC-C240-M5SX            | WZP23450C7D    | 10.58.25.41   | 2S 48C 96T   | 512 [GiB] | 
| P- H    | cri |    | aio2-p5g-eu-spdc-WZP23450C8M             | (R) UCSC-C240-M5SX            | WZP23450C8M    | 10.58.25.42   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | CRi |    | aio3-p5g-eu-spdc-WZP23450C8K             | (R) UCSC-C240-M5SX            | WZP23450C8K    | 10.58.50.51   | 2S 48C 96T   | 384 [GiB] | 
| P- H    | Cu  |    | berlin-ucsm-1                            | (R) UCSC-C240-M5SX            | WZP21490417    | 10.49.234.199 | 2S 28C 56T   | 704 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-2                            | (R) UCSC-C240-M4S             | FCH1930V0PH    | 10.49.234.198 | 2S 24C 48T   | 384 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-3                            | (R) UCSC-C220-M4S             | FCH2031V0YM    | 10.49.234.196 | 2S 28C 56T   | 672 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-4                            | (R) UCSC-C240-M4SX            | FCH1916V1CT    | 10.49.234.197 | 2S 24C 48T   | 256 [GiB] | 
| P+ W(2) | Cu  |    | berlin-ucsm-5                            | (R) UCSC-C240-M4SX            | FCH1916V0UY    | 10.49.234.206 | 2S 24C 48T   | 256 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-6                            | (R) UCSC-C240-M4S             | FCH1930V0KM    | 10.49.234.195 | 2S 24C 48T   | 384 [GiB] | 
| P- W(1) | Cu  |    | berlin-ucsm-7                            | (R) UCSC-C240-M4S             | FCH1930V1LA    | 10.49.234.205 | 2S 28C 56T   | 768 [GiB] | 
| P+ W(1) | Cu  |    | berlin-ucsm-8                            | (R) UCSC-C220-M4S             | FCH1849V26H    | 10.49.234.194 | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | CRi |    | comp-1-p2b-eu-spdc-WZP23400AJW           | (R) UCSC-C240-M5SN            | WZP23400AJW    | 10.58.50.41   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | CRi |    | comp-2-p2b-eu-spdc-WZP23400AK4           | (R) UCSC-C240-M5SN            | WZP23400AK4    | 10.58.50.42   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | CRi |    | comp-3-p2b-eu-spdc-WZP23400AKL           | (R) UCSC-C240-M5SN            | WZP23400AKL    | 10.58.50.43   | 2S 40C 80T   | 384 [GiB] | 
| P- H    | CRi |    | comp-4-p2b-eu-spdc-WMP240400FM           | (R) UCSC-C220-M5SX            | WMP240400FM    | 10.58.50.44   | 2S 40C 80T   | 384 [GiB] | 
| P- H    | CRi |    | comp-5-p2b-eu-spdc-WMP2404000R           | (R) UCSC-C220-M5SX            | WMP2404000R    | 10.58.50.45   | 2S 40C 80T   | 384 [GiB] | 
| P- H    | CRi |    | comp-6-p2b-eu-spdc-WMP24040059           | (R) UCSC-C220-M5SX            | WMP24040059    | 10.58.50.46   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | CRi |    | comp-7-p2b-eu-spdc-WMP24040061           | (R) UCSC-C220-M5SX            | WMP24040061    | 10.58.50.47   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    | comp1-p1-eu-spdc-WZP22520Y9J             | (R) UCSC-C220-M5SX            | WZP22520Y9J    | 10.58.28.44   | 2S 48C 96T   | 256 [GiB] | 
| P- C(1) | Cri |    | comp1-p2a-eu-spdc-WZP22511E6V            | (R) UCSC-C240-M5SX            | WZP22511E6V    | 10.58.28.51   | 2S 24C 48T   | 192 [GiB] | 
| P- H    | CRi |    | comp1-p3b-eu-spdc-FCH2017V1J7            | (R) UCSC-C240-M4SX            | FCH2017V1J7    | 10.58.50.48   | 2S 16C 32T   | 128 [GiB] | 
| P+ H    | Cri |    | comp1-p4A-eu-spdc                        | (R) UCSC-C220-M5SX            | WMP24040045    | 10.58.29.54   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | Cri |    | comp1-p4b-eu-spdc-WZP26360D36            | (R) UCSC-C245-M6SX            | WZP26360D36    | 10.58.53.33   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | comp2-p1-spdc-WZP22520Y95                | (R) UCSC-C220-M5SX            | WZP22520Y95    | 10.58.28.45   | 2S 48C 96T   | 256 [GiB] | 
| P- H    | Cri |    | comp2-p2a-eu-spdc-WZP22511E6G            | (R) UCSC-C240-M5SX            | WZP22511E6G    | 10.58.28.52   | 2S 24C 48T   | 192 [GiB] | 
| P- H    | Cri |    | comp2-p3b-eu-spdc-FCH2017V1J8            | (R) UCSC-C240-M4SX            | FCH2017V1J8    | 10.58.50.49   | 2S 16C 32T   | 128 [GiB] | 
| P+ H    | Cri |    | comp2-p4a-eu-spdc-WZP22520B04            | (R) UCSC-C220-M5SX            | WZP22520B04    | 10.58.29.58   | 2S 48C 96T   | 256 [GiB] | 
| P+ H    | Cri |    | comp2-p4b-eu-spdc-WZP26360D3D            | (R) UCSC-C245-M6SX            | WZP26360D3D    | 10.58.53.34   | 2S 128C 256T | 512 [GiB] | 
| P- C(1) | cri |    | comp3-p2a-eu-spdc-WZP2335149W            | (R) UCSC-C220-M5SX            | WZP2335149W    | 10.58.28.53   | 2S 16C 32T   | 192 [GiB] | 
| P- H    | Cri |    | comp3-p3b-eu-spdc-FCH2017V1J5            | (R) UCSC-C240-M4SX            | FCH2017V1J5    | 10.58.50.50   | 2S 16C 32T   | 128 [GiB] | 
| P+ H    | Cri |    | comp3-p4a-eu-spdc-WZP22520Y8X            | (R) UCSC-C220-M5SX            | WZP22520Y8X    | 10.58.29.59   | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | Cri |    | comp3-p4b-eu-spdc-WZP262207UM            | (R) UCSC-C225-M6S             | WZP262207UM    | 10.58.53.35   | 1S 64C 128T  | 512 [GiB] | 
| P+ H    | cri |    | comp4-p1-eu-spdc-FCH2016V23J             | (R) UCSC-C220-M4S             | FCH2016V23J    | 10.58.28.47   | 2S 28C 56T   | 256 [GiB] | 
| P- H    | Cri |    | comp4-p2a-eu-spdc-WZP22520Y8W            | (R) UCSC-C220-M5SX            | WZP22520Y8W    | 10.58.28.54   | 2S 24C 48T   | 192 [GiB] | 
| P- H    | Cri |    | comp4-p3b-eu-spdc-FCH2108V1FC            | (R) UCSC-C220-M4S             | FCH2108V1FC    | 10.58.50.57   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | comp4-p4b-eu-spdc-WZP262207VP            | (R) UCSC-C225-M6S             | WZP262207VP    | 10.58.53.36   | 1S 32C 64T   | 512 [GiB] | 
| P+ H    | cri |    | comp5-p1-eu-spdc-FCH2017V0TN             | (R) UCSC-C220-M4S             | FCH2017V0TN    | 10.58.28.48   | 2S 28C 56T   | 256 [GiB] | 
| P- H    | Cri |    | comp5-p3b-eu-spdc-FCH2017V1Y6            | (R) UCSC-C220-M4S             | FCH2017V1Y6    | 10.58.50.58   | 2S 28C 56T   | 256 [GiB] | 
| P- H    | CRi |    | comp6-p3b-eu-spdc-FCH2017V24J            | (R) UCSC-C220-M4S             | FCH2017V24J    | 10.58.50.59   | 2S 28C 56T   | 256 [GiB] | 
| P+ C(1) | CRi |    | comp7-p3b-eu-spdc-FCH2023V2A4            | (R) UCSC-C220-M4S             | FCH2023V2A4    | 10.58.50.60   | 2S 28C 56T   | 256 [GiB] | 
| P+ H L  | cri |    | core-p5g-eu-spdc-WZP23440N02             | (R) UCSC-C220-M5SX            | WZP23440N02    | 10.58.29.50   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | cu-p5g-eu-spdc-WZP23440N11               | (R) UCSC-C220-M5SX            | WZP23440N11    | 10.58.29.49   | 2S 48C 96T   | 384 [GiB] | 
| P+ H    | Cri |    | du-p5g-eu-spdc-WZP2526088F               | (R) UCSC-C240-M5SX            | WZP2526088F    | 10.58.29.48   | 2S 48C 48T   | 384 [GiB] | 
| P+ H    | Cri |    | esx00-eu-spdc-WZP22520AXQ                | (R) UCSC-C220-M5SX            | WZP22520AXQ    | 10.58.29.36   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | esx01-eu-spdc-WZP22520Y99                | (R) UCSC-C220-M5SX            | WZP22520Y99    | 10.58.29.37   | 2S 24C 48T   | 384 [GiB] | 
| P+ H    | Cri |    | esx1-eu-spdc-FCH2017V0T3                 | (R) UCSC-C220-M4S             | FCH2017V0T3    | 10.58.28.33   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | esx10-eu-spdc-FCH2017V0TN                | (R) UCSC-C220-M4S             | FCH2017V0TN    | 10.58.28.61   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | esx11-eu-spdc-FCH2050V125                | (R) UCSC-C220-M4S             | FCH2050V125    | 10.58.29.51   | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | Cri |    | esx12-eu-spdc-FCH2049V1WU                | (R) UCSC-C220-M4S             | FCH2049V1WU    | 10.58.29.52   | 2S 24C 48T   | 256 [GiB] | 
| P+ W(1) | Cri |    | esx13-eu-spdc-FCH2018V027                | (R) UCSC-C220-M4S             | FCH2018V027    | 10.58.29.53   | 2S 16C 32T   | 256 [GiB] | 
| P+ H    | Cri |    | esx14-eu-spdc-FCH2017V0TE                | (R) UCSC-C220-M4S             | FCH2017V0TE    | 10.58.29.42   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | esx2-eu-spdc-FCH2004V1PV                 | (R) UCSC-C220-M4S             | FCH2004V1PV    | 10.58.28.34   | 2S 16C 32T   | 256 [GiB] | 
| P+ H    | CRi |    | esx20-eu-spdc-WMP24040053                | (R) UCSC-C220-M5SX            | WMP24040053    | 10.58.50.40   | 2S 40C 80T   | 384 [GiB] | 
| P+ H    | CRi |    | esx21-eu-spdc-WZP23440N1P                | (R) UCSC-C220-M5SX            | WZP23440N1P    | 10.58.50.38   | 2S 48C 96T   | 512 [GiB] | 
| P- H    | CRi |    | esx22-eu-spdc-WZP2343171Y                | (R) UCSC-C220-M5SX            | WZP2343171Y    | 10.58.50.39   | 2S 48C 96T   | 512 [GiB] | 
| P+ H    | Cri |    | esx3-eu-spdc-FCH2004V0RW                 | (R) UCSC-C220-M4S             | FCH2004V0RW    | 10.58.28.35   | 2S 16C 32T   | 256 [GiB] | 
| P+ H    | Cri |    | esx4-eu-spdc-FCH2016V2BE                 | (R) UCSC-C220-M4S             | FCH2016V2BE    | 10.58.28.36   | 2S 36C 72T   | 512 [GiB] | 
| P+ H    | Cri |    | esx5-eu-spdc-FCH2017V024                 | (R) UCSC-C220-M4S             | FCH2017V024    | 10.58.28.50   | 2S 36C 72T   | 512 [GiB] | 
| P+ H    | Cri |    | esx6-eu-spdc-FCH2006V04E                 | (R) UCSC-C220-M4S             | FCH2006V04E    | 10.58.28.57   | 2S 16C 32T   | 256 [GiB] | 
| P+ C(1) | Cri |    | esx7-eu-spdc-FCH2004V0M6                 | (R) UCSC-C220-M4S             | FCH2004V0M6    | 10.58.28.58   | 2S 16C 32T   | 256 [GiB] | 
| P+ H    | Cri |    | esx8-eu-spdc-FCH2017V0T1                 | (R) UCSC-C220-M4S             | FCH2017V0T1    | 10.58.28.59   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | esx9-eu-spdc-FCH2016V23J                 | (R) UCSC-C220-M4S             | FCH2016V23J    | 10.58.28.60   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | esx91-eu-spdc-WZP234411LW                | (R) UCSC-C240-M5SX            | WZP234411LW    | 10.58.25.33   | 2S 28C 56T   | 256 [GiB] | 
| P+ W(1) | Cri |    | esx92-eu-spdc-FCH2017V2AF                | (R) UCSC-C220-M4S             | FCH2017V2AF    | 10.58.25.34   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | esx93-eu-spdc-FCH2108V1HE                | (R) UCSC-C220-M4S             | FCH2108V1HE    | 10.58.25.35   | 2S 28C 56T   | 256 [GiB] | 
| P- W(2) | Cri |    | esx94-eu-spdc-FCH2017V2AH                | (R) UCSC-C220-M4S             | FCH2017V2AH    | 10.58.25.36   | 2S 28C 56T   | 256 [GiB] | 
| P- H    | Cri |    | esx95-eu-spdc-FCH2017V241                | (R) UCSC-C220-M4S             | FCH2017V241    | 10.58.25.37   | 2S 16C 32T   | 256 [GiB] | 
| P+ H    | Cri |    | mgmt-p1-eu-spdc-WZP2252176Z              | (R) UCSC-C220-M5SX            | WZP2252176Z    | 10.58.28.40   | 2S 48C 96T   | 256 [GiB] | 
| P+ H    | Cri |    | mgmt-p4a-eu-spdc-WZP22520Y9D             | (R) UCSC-C220-M5SX            | WZP22520Y9D    | 10.58.29.60   | 2S 48C 96T   | 256 [GiB] | 
| P+ H    | Cri |    | sn11-eu-spdc-WZP23430C4N                 | (R) SE-NODE-G2                | WZP23430C4N    | 10.58.29.33   | 2S 20C 40T   | 256 [GiB] | 
| P+ H    | Cri |    | sn12-eu-spdc-WZP23430C4D                 | (R) SE-NODE-G2                | WZP23430C4D    | 10.58.29.34   | 2S 20C 40T   | 256 [GiB] | 
| P+ C(1) | Cri |    | sn13-eu-spdc-WZP234301R9                 | (R) SE-NODE-G2                | WZP234301R9    | 10.58.29.35   | 2S 20C 40T   | 256 [GiB] | 
| P+ H    | Cri |    | tnas-eu-spdc-WZP22511E68                 | (R) UCSC-C240-M5SX            | WZP22511E68    | 10.58.25.52   | 2S 28C 56T   | 256 [GiB] | 
| P+ H    | Cri |    | ynas-eu-spdc-FCH21067808                 | (B) UCSC-C3K-M4SRB            | FCH21067808    |               | 2S 24C 48T   | 256 [GiB] | 
| P+ H    | cri |    | znas-eu-spdc-WZP22511E3P                 | (R) UCSC-C240-M5SX            | WZP22511E3P    | 10.58.28.56   | 2S 24C 48T   | 256 [GiB] | 
+---------+-----+----+------------------------------------------+-------------------------------+----------------+---------------+--------------+-----------+
```

Developer output

```
# iserver get servers

Developer output

{
    "duration": 6085,
    "isctl": {
        "read": true,
        "calls": 6,
        "success": 6,
        "failed": 0,
        "total_time": 5739
    },
    "redfish": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "path": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "path_time": 0,
        "total_time": 0
    },
    "ucsm": {
        "read": false,
        "success": 0,
        "failed": 0,
        "connect": 0,
        "disconnect": 0,
        "mo": 0,
        "connect_time": 0,
        "disconnect_time": 0,
        "mo_time": 0,
        "total_time": 0
    },
    "ssh": {
        "read": false,
        "calls": 0,
        "total_time": 0
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
        "lines": 48
    }
}

Log: isctl
-----------

2022-12-13 16:57:27.187255	True	2282	93	isctl get compute rackunit   -o json --top 100
2022-12-13 16:57:27.886829	True	698	10	isctl get compute blade   -o json --top 100
2022-12-13 16:57:28.348131	True	420	1	isctl get equipment locatorled --filter "OperState eq 'on'"  -o json --top 100
2022-12-13 16:57:28.488295	True	549	0	isctl get workflow workflowinfo --filter "CreateTime gt 2022-12-12T16:57:27.000Z"  -o json --top 100
2022-12-13 16:57:29.314337	True	1384	100	isctl get asset deviceregistration   -o json --top 100
2022-12-13 16:57:29.720945	True	406	9	isctl get asset deviceregistration   -o json --top 100 --skip 100
```
