# Intersight and Redfish Integration - API

## Redfish API in 'direct mode'

Running API in direct mode requires several inputs from the user i.e.
- Endpoint Type
- Endpoint IP
- Username and Password

In case of Fabric Interconnect extra inventory type and inventory identifier parameters are required to query the target chassis or server connected to Fabric Interconnect.

Example of Redfish API call in 'direct mode':

```
# iserver.py get redfish endpoint --type ucsc --ip 10.58.50.45 --username admin --password '!Cisc0_123' --uri / --property Product
/
/redfish/v1/
------------
{
    "Product": "UCSC-C220-M5SX"
}
```

## Redfish API in 'integrated mode'

```
# iserver get redfish server --ip 10.58.50.45 --uri / --property Product

/redfish/v1/
------------
{
    "Product": "UCSC-C220-M5SX"
}
```
