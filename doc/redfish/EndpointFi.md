# Fabric Interconnect Redfish Endpoint Type

[[Next]](./EndpointStandard.md) [[Back]](./README.md)

Endpoint:
- Fabric Interconnect
- redfish-enabled
- the IP address and credentials below are the same as Fabric Interconnect management address and credentials

Fabric Interconnect endpoint allows getting Redfish information from the Chassis and Servers attached to it.

## Inventory

```
# iserver get redfish fi \
    --ip 10.10.10.10 \
    --username admin \
    --password secret

+-----------------+-------------+----------------------+----------------------+---------------+----------------+-----------------+
| Inventory Type  | Chassis Id  | Inventory Id (IOM1)  | Inventory Id (IOM2)  | Chassis Name  | Chassis Model  | Chassis Serial  |
+-----------------+-------------+----------------------+----------------------+---------------+----------------+-----------------+
| Chassis         | chassis-1   | IoCard-1-1           | IoCard-1-2           | FI4-1         | UCSX-9508      | Serial123       | 
+-----------------+-------------+----------------------+----------------------+---------------+----------------+-----------------+

+-----------------+---------------+-------------+---------------+----------------+
| Inventory Type  | Inventory Id  | Chassis Id  | Server Model  | Server Serial  |
+-----------------+---------------+-------------+---------------+----------------+
| Server          | FI4-1-1       | chassis-1   | UCSX-210C-M6  | Serial11111    | 
| Server          | FI4-1-3       | chassis-1   | UCSX-210C-M6  | Serial22222    | 
| Server          | FI4-1-5       | chassis-1   | UCSX-210C-M6  | Serial33333    | 
| Server          | FI4-1-7       | chassis-1   | UCSX-210C-M6  | Serial44444    | 
+-----------------+---------------+-------------+---------------+----------------+
```

## Chassis

```
# iserver get redfish uri
    --type fi \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --inventory-type Chassis \
    --inventory-id IoCard-1-1

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1",
    "@odata.type": "#ServiceRoot.v1_5_1.ServiceRoot",
    ...
}
```

## Server

```
# iserver get redfish endpoint
    --type fi \
    --ip 10.10.10.10 \
    --username admin \
    --password secret \
    --inventory-type Server \
    --inventory-id FI4-1-1

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1/",
    "@odata.type": "#ServiceRoot.v1_9_0.ServiceRoot",
    ...
}
```

[[Back]](./README.md)