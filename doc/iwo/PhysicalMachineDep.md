# Intersight Workload Optimizer

## List of physical machines with dependencies severity summary

```
# iserver get iwo phy --show-dep

Summary
-------
- Active   : 115/123
- Severity : 1/0/3/119
- Current  : 123/123


+-------------+--------------+-----------+--------------------------------------------------+----------+----------------+----------------+----------+-----------------+---------------------+
| State       | Severity     | Staleness | Name                                             | Location | Type           | Data Center    | Storage  | Virtual Machine | Virtual Data Center |
+-------------+--------------+-----------+--------------------------------------------------+----------+----------------+----------------+----------+-----------------+---------------------+
| SUSPEND     | Normal       | CURRENT   | 10.49.234.242                                    | ONPREM   | vCenter        | Berlin Lab     | 0/0/0/1  | 0/0/0/1         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | 10.49.234.246                                    | ONPREM   | vCenter        | Berlin Lab     | 0/0/0/1  | 0/0/2/14        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | aio-1-p1-eu-spdc-WZP22490ZCU: sys/rack-unit-1    | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | aio-2-p1-eu-spdc-WZP22520Y69: sys/rack-unit-1    | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | aio-3-p1-eu-spdc-WZP22520Y54: sys/rack-unit-1    | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | aio3-p5g-eu-spdc-WZP23450C8K: sys/rack-unit-1    | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | ant1-eu-spdc-FCH2017V2GH: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | berlin-esxi.cisco.com                            | ONPREM   | vCenter        | Berlin Lab     | 0/0/0/1  | 0/0/2/15        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | berlin-ucsm: sys/rack-unit-4                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | berlin-ucsm: sys/rack-unit-5                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | berlin-ucsm: sys/rack-unit-6                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | berlin-ucsm: sys/rack-unit-7                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | berlin-ucsm: sys/rack-unit-8                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | C220-231: sys/rack-unit-1                        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | C220-WZP23350ZAQ: sys/rack-unit-1                | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | C220-WZP23360FH9: sys/rack-unit-1                | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | C240-WZP232102PH: sys/rack-unit-1                | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-1-p2b-eu-spdc-WZP23400AJW: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-2-p2b-eu-spdc-WZP23400AK4: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-3-p2b-eu-spdc-WZP23400AKL: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-4-p2b-eu-spdc-WMP240400FM: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-5-p2b-eu-spdc-WMP2404000R: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-6-p2b-eu-spdc-WMP24040059: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp-7-p2b-eu-spdc-WMP24040061: sys/rack-unit-1  | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp1-p1-eu-spdc-WZP22520Y9J: sys/rack-unit-1    | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp1-p2a-eu-spdc-WZP22511E6V: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp1-p3b-eu-spdc-FCH2017V1J7: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp1-p4A-eu-spdc: sys/rack-unit-1               | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp2-p1-spdc-WZP22520Y95: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp2-p2a-eu-spdc-WZP22511E6G: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp2-p3b-eu-spdc-FCH2017V1J8: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp2-p4a-eu-spdc-WZP22520B04: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp3-p2a-eu-spdc-WZP2335149W: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp3-p3b-eu-spdc-FCH2017V1J5: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp3-p4a-eu-spdc-WZP22520Y8X: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp4-p2a-eu-spdc-WZP22520Y8W: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp4-p3b-eu-spdc-FCH2108V1FC: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp5-p3b-eu-spdc-FCH2017V1Y6: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp6-p3b-eu-spdc-FCH2017V24J: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | comp7-p3b-eu-spdc-FCH2023V2A4: sys/rack-unit-1   | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | cu-p5g-eu-spdc-WZP23440N11: sys/rack-unit-1      | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | du-p5g-eu-spdc-WZP2526088F: sys/rack-unit-1      | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx00-eu-spdc-WZP22520AXQ: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx00-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/4/2         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx01-eu-spdc-WZP22520Y99: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx01-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/1/1  | 0/0/3/1         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx1-eu-spdc-FCH2017V0T3: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx1-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/1/1  |                 | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx10-eu-spdc-FCH2017V0TN: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx10-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/5/11        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx11-eu-spdc-FCH2050V125: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx11-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 1/0/6/2         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx12-eu-spdc-FCH2049V1WU: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx12-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/13/10       | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx13-eu-spdc-FCH2018V027: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx13-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/6/4         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx14-eu-spdc-FCH2017V0TE: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx14-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/1/1  |                 | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx2-eu-spdc-FCH2004V1PV: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Critical (1) | CURRENT   | esx2-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/2/8         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx20-eu-spdc-WMP24040053: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx20-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  | 0/0/0/9         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx21-eu-spdc-WZP23440N1P: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx21-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  |                 | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx22-eu-spdc-WZP2343171Y: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx22-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/0/1  | 0/0/0/8         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx3-eu-spdc-FCH2004V0RW: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx3-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/14/3        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx31-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/1/1  | 0/0/1/0         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx32-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/1/1  | 0/0/1/0         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx33-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/1/1  | 0/0/1/0         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx34-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  | 0/0/1/1         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx35-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  | 0/0/1/0         | 0/0/0/1             | 
| ACTIVE      | Minor (1)    | CURRENT   | esx36-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  | 0/0/0/1         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx37-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  | 1/0/7/3         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx4-eu-spdc-FCH2016V2BE: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx4-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/1  | 0/0/5/2         | 0/0/0/1             | 
| ACTIVE      | Minor (1)    | CURRENT   | esx41-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 0/0/9/1         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx42-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 1/0/7/3         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx43-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 0/0/7/6         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx44-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/0  | 0/0/1/3         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx5-eu-spdc-FCH2017V024: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx5-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/1  | 0/0/4/3         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx51-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 0/0/19/7        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx52-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 0/0/5/30        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx53-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 0/0/7/0         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx54-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/3/0  | 0/0/6/1         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx6-eu-spdc-FCH2006V04E: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx6-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/8/3         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx7-eu-spdc-FCH2004V0M6: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx7-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/10/6        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx8-eu-spdc-FCH2017V0T1: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx8-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/8/7         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx9-eu-spdc-FCH2016V23J: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx9-eu-spdc.cisco.com                           | ONPREM   | vCenter        | eu-spdc-dc     | 1/2/2/1  | 0/0/3/4         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx91-eu-spdc-WZP234411LW: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx91-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dmz-dc | 0/0/3/18 | 0/0/9/2         | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx92-eu-spdc-FCH2017V2AF: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | esx92-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dmz-dc | 0/0/3/0  | 0/0/4/13        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx93-eu-spdc-FCH2108V1HE: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Minor (1)    | CURRENT   | esx93-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dmz-dc | 0/0/3/0  | 0/0/1/13        | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx94-eu-spdc-FCH2017V2AH: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx94-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dmz-dc | 0/0/2/1  |                 | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | esx95-eu-spdc-FCH2017V241: sys/rack-unit-1       | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| MAINTENANCE | Normal       | CURRENT   | esx95-eu-spdc.cisco.com                          | ONPREM   | vCenter        | eu-spdc-dmz-dc | 0/0/2/1  |                 | 0/0/0/1             | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-1                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-2                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-3                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-4                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-5                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-6                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | HX1-eu-spdc: sys/rack-unit-7                     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | mgmt-p1-eu-spdc-WZP2252176Z: sys/rack-unit-1     | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | mgmt-p4a-eu-spdc-WZP22520Y9D: sys/rack-unit-1    | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | POD-4A-AIO-1-WZP23400AK9: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | POD-4A-AIO-2-WZP23400AK7: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | POD-4A-AIO-3-WZP23400AM2: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | sn11-eu-spdc-WZP23430C4N: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | sn12-eu-spdc-WZP23430C4D: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | sn13-eu-spdc-WZP234301R9: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | snas-eu-spdc-WZP23450C7D: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | tnas-eu-spdc-WZP22511E68: sys/rack-unit-1        | ONPREM   | Intersight UCS | UCS-DC         |          |                 |                     | 
| ACTIVE      | Normal       | CURRENT   | ynas-eu-spdc-FCH21067808: sys/chassis-1/server-1 | ONPREM   | Intersight UCS |                |          |                 |                     | 
+-------------+--------------+-----------+--------------------------------------------------+----------+----------------+----------------+----------+-----------------+---------------------+
```