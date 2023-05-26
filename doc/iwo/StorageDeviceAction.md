# Intersight Workload Optimizer

## Show selected storage devices With action details

```
# iserver get iwo storage --name EU-SPDC-Datastore-SNAS --show-actions

Summary
-------
- Active   : 1/1
- Severity : 0/0/1/0
- Current  : 1/1


+--------+-----------+-----------+------------------------+----------+---------+------------+-----------------+------------------+
| State  | Severity  | Staleness | Storage Device Name    | Location | Type    | Disk Array | Virtual Machine | Physical Machine |
+--------+-----------+-----------+------------------------+----------+---------+------------+-----------------+------------------+
| ACTIVE | Minor (9) | CURRENT   | EU-SPDC-Datastore-SNAS | ONPREM   | vCenter | 1          | 0/0/32/5        | 1/0/2/30         | 
+--------+-----------+-----------+------------------------+----------+---------+------------+-----------------+------------------+

+----------+------------------------+------------------------+----------------------------------------------------------------------------------------------------------+
| Severity | Description            | Category               | Details                                                                                                  |
+----------+------------------------+------------------------+----------------------------------------------------------------------------------------------------------+
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_2.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 10 GB  | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_7.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 1 GB   | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_3.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 12 GB  | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_4.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 1 GB   | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_6.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 31 MB  | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_5.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 237 MB | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'vmware.log' from Storage EU-SPDC-Datastore-SNAS to free up 13 MB                     | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 6 GB     | 
| minor    | Idle or non-productive | Efficiency Improvement | Delete wasted file 'SPDC-intersight-assist_1.vmdk' from Storage EU-SPDC-Datastore-SNAS to free up 4 GB   | 
+----------+------------------------+------------------------+----------------------------------------------------------------------------------------------------------+
```