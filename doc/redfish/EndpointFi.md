# Fabric Interconnect Redfish Endpoint Type

Fabric Interconnect (--type fi) endpoint allows getting Redfish information from the Chassis and FI-Attached server.

Redfish API calls are executed on Fabric Interconnect for all devices connected to it.

Fabric Interconnect connected devices support [template](./TemplateFi.md).

## Step 1: List of inventory

The first step is getting the list of inventory connected to FI i.e. chassis and servers.

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-list

+-----------------+-------------+----------------------+----------------------+---------------+----------------+-----------------+
| Inventory Type  | Chassis Id  | Inventory Id (IOM1)  | Inventory Id (IOM2)  | Chassis Name  | Chassis Model  | Chassis Serial  |
+-----------------+-------------+----------------------+----------------------+---------------+----------------+-----------------+
| Chassis         | chassis-1   | IoCard-1-1           | IoCard-1-2           | FI4-1         | UCSX-9508      | FOX2521P34M     | 
+-----------------+-------------+----------------------+----------------------+---------------+----------------+-----------------+

+-----------------+---------------+-------------+---------------+----------------+
| Inventory Type  | Inventory Id  | Chassis Id  | Server Model  | Server Serial  |
+-----------------+---------------+-------------+---------------+----------------+
| Server          | FI4-1-1       | chassis-1   | UCSX-210C-M6  | FCH25337EHM    | 
| Server          | FI4-1-3       | chassis-1   | UCSX-210C-M6  | FCH25337EM5    | 
| Server          | FI4-1-5       | chassis-1   | UCSX-210C-M6  | FCH25337EJ9    | 
| Server          | FI4-1-7       | chassis-1   | UCSX-210C-M6  | FCH25337EHW    | 
+-----------------+---------------+-------------+---------------+----------------+
```

## Step 2a: Chassis

Use Inventory Type and Inventory Id from the inventory list above to run Redfish calls on specific Chassis

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Chassis
    --inventory-id IoCard-1-1

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1",
    "@odata.type": "#ServiceRoot.v1_5_1.ServiceRoot",
    "AccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "Chassis": {
        "@odata.id": "/redfish/v1/Chassis"
    },
    "Description": "Root Service",
    "EventService": {
        "@odata.id": "/redfish/v1/EventService"
    },
    "Id": "RootService",
    "JsonSchemas": {
        "@odata.id": "/redfish/v1/JsonSchemas"
    },
    "Links": {
        "Sessions": {
            "@odata.id": "/redfish/v1/SessionService/Sessions"
        }
    },
    "Managers": {
        "@odata.id": "/redfish/v1/Managers"
    },
    "Name": "Cisco RESTful Root Service",
    "Oem": {
        "@odata.id": "/redfish/v1/Oem"
    },
    "RedfishVersion": "1.5.1",
    "Registries": {
        "@odata.id": "/redfish/v1/Registries"
    },
    "SessionService": {
        "@odata.id": "/redfish/v1/SessionService"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService"
    },
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    }
}
```

## Step 2b: FI-Attached Server

Use Inventory Type and Inventory Id from the inventory list to run Redfish calls on specific Server

```
# iserver get redfish endpoint
    --type fi
    --ip 10.62.0.206
    --username admin
    --password ******
    --inventory-type Server
    --inventory-id FI4-1-1

/api-explorer/resources/redfish/v1/
-----------------------------------
{
    "@odata.context": "/redfish/v1/$metadata#ServiceRoot.ServiceRoot",
    "@odata.id": "/redfish/v1/",
    "@odata.type": "#ServiceRoot.v1_9_0.ServiceRoot",
    "AccountService": {
        "@odata.id": "/redfish/v1/AccountService"
    },
    "CertificateService": {
        "@odata.id": "/redfish/v1/CertificateService"
    },
    "Chassis": {
        "@odata.id": "/redfish/v1/Chassis"
    },
    "Description": "Root Service",
    "EventService": {
        "@odata.id": "/redfish/v1/EventService"
    },
    "Id": "RootService",
    "JsonSchemas": {
        "@odata.id": "/redfish/v1/JsonSchemas"
    },
    "Links": {
        "Sessions": {
            "@odata.id": "/redfish/v1/SessionService/Sessions"
        }
    },
    "Managers": {
        "@odata.id": "/redfish/v1/Managers"
    },
    "Name": "Cisco RESTful Root Service",
    "RedfishVersion": "1.9.0",
    "Registries": {
        "@odata.id": "/redfish/v1/Registries"
    },
    "SessionService": {
        "@odata.id": "/redfish/v1/SessionService"
    },
    "Systems": {
        "@odata.id": "/redfish/v1/Systems"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService"
    },
    "UUID": "F4E8E18C-6C28-4C75-8814-BFBE341D0620",
    "UpdateService": {
        "@odata.id": "/redfish/v1/UpdateService"
    }
}
```
