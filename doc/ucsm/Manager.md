# UCS Manager Endpoint

## Example: Get

```
# iserver get ucsm manager

+-------+-----------------------------+----------+----------+
| Name  | IP                          | Username | Password |
+-------+-----------------------------+----------+----------+
| milan | vip-ucsb1.emea-sp.cisco.com | admin    | ******   | 
+-------+-----------------------------+----------+----------+
```

## Example: Create or Set

Note: UCSM API verification must be successfull

```
# iserver set ucsm manager
    --name test
    --ip vip-ucsb1.emea-sp.cisco.com
    --username admin
    --password ******

UCSM authentication successful
UCSM entry created: test
```

## Example: Delete

```
# iserver delete ucsm manager --name test

UCSM entry deleted: test
```