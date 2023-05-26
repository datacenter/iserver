# Redfish Access Configuration - Delete

Select redfish access configuration entries to be deleted upon confirmation based on:
- redfish endpoint type
- IP address (exact match or subnet)
- Serial number (exact match)
- failed authentication

If no filtering criteria is set, all entries are deleted.

## Example: IP address

```
# iserver delete redfish access --ip 10.58.53.34

+----------------+-------------+-------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
| Product        | S/N         | Name                          | Type | IP          | Port | Username | Password | FI Inventory Type | FI Inventory ID |
+----------------+-------------+-------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
| UCSC-C245-M6SX | WZP26360D3D | comp2-p4b-eu-spdc-WZP26360D3D | ucsc | 10.58.53.34 | 443  | admin    | ******   |                   |                 |
+----------------+-------------+-------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
Continue [Y/N]? y

Progress |################################| 1/1
```

## Example: IP subnet

```
# iserver delete redfish access --ip 10.58.53.0/24

+----------------+-------------+-------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
| Product        | S/N         | Name                          | Type | IP          | Port | Username | Password | FI Inventory Type | FI Inventory ID |
+----------------+-------------+-------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
| UCSC-C245-M6SX | WZP26360D3D | comp2-p4b-eu-spdc-WZP26360D3D | ucsc | 10.58.53.34 | 443  | admin    | ******   |                   |                 |
| UCSC-C225-M6S  | WZP262207UM | comp3-p4b-eu-spdc-WZP262207UM | ucsc | 10.58.53.35 | 443  | admin    | ******   |                   |                 |
| UCSC-C225-M6S  | WZP262207VP | comp4-p4b-eu-spdc-WZP262207VP | ucsc | 10.58.53.36 | 443  | admin    | ******   |                   |                 |
+----------------+-------------+-------------------------------+------+-------------+------+----------+----------+-------------------+-----------------+
Continue [Y/N]? y

Progress |################################| 3/3
```

## Example: failed authentication

```
# iserver delete redfish access --failed
Progress |################################| 28/28

+--------------+-------------+--------------+------+-------------+------+----------+-----------+-------------------+-----------------+
| Product      | S/N         | Name         | Type | IP          | Port | Username | Password  | FI Inventory Type | FI Inventory ID |
+--------------+-------------+--------------+------+-------------+------+----------+-----------+-------------------+-----------------+
| UCSX-210C-M6 | FCH25337EHM | UCSX-210C-M6 | fi   | 10.62.0.206 | 443  | admin    | ******    | Server            | FI4-1-1         |
| UCSX-210C-M6 | FCH25337EHW | UCSX-210C-M6 | fi   | 10.62.0.206 | 443  | admin    | ******    | Server            | FI4-1-7         |
| UCSX-210C-M6 | FCH25337EJ9 | UCSX-210C-M6 | fi   | 10.62.0.206 | 443  | admin    | ******    | Server            | FI4-1-5         |
| UCSX-9508    | FOX2521P34M | None         | fi   | 10.62.0.206 | 443  | admin    | ******    | Chassis           | IoCard-1-1      |
+--------------+-------------+--------------+------+-------------+------+----------+-----------+-------------------+-----------------+
Continue [Y/N]? y

Progress |################################| 4/4
```
