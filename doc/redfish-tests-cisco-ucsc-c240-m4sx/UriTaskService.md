# Resource: /redfish/v1/TaskService

Vendor | Model
--- | ---
Cisco | UCSC-C240-M4SX

## /redfish/v1/TaskService

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService",
    "@odata.id": "/redfish/v1/TaskService",
    "@odata.type": "#TaskService.v1_1_2.TaskService",
    "CompletedTaskOverWritePolicy": "Oldest",
    "Description": "Tasks Service",
    "Id": "TaskService",
    "LifeCycleEventOnTaskStateChange": false,
    "Name": "Tasks Service",
    "ServiceEnabled": true,
    "Status": {
        "Health": "OK",
        "State": "Enabled"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService/Tasks"
    }
}
```

## /redfish/v1/TaskService/Tasks

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks",
    "@odata.id": "/redfish/v1/TaskService/Tasks",
    "@odata.type": "#TaskCollection.TaskCollection",
    "Description": "Tasks",
    "Members": [
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/BmcFwUpdate"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/BiosFwUpdate"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/BmcTechSupportExport"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/ImportBmcConfig"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/ExportBmcConfig"
        }
    ],
    "Members@odata.count": 5,
    "Name": "Tasks"
}
```

## /redfish/v1/TaskService/Tasks/BiosFwUpdate

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BiosFwUpdate",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "BIOS firmware version",
    "Id": "BiosFwUpdate",
    "Name": "Task BiosFwUpdate",
    "Oem": {
        "Cisco": {
            "FWVersion": "C240M4.3.0.4b.0.0610182318",
            "UpdateStatus": "None, OK"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/BmcFwUpdate

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BmcFwUpdate",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Cisco IMC backup firmware version",
    "Id": "BmcFwUpdate",
    "Name": "Task BmcFwUpdate",
    "Oem": {
        "Cisco": {
            "FWVersion": "3.0(4i)",
            "UpdateStatus": "Success (100%)"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/BmcTechSupportExport

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BmcTechSupportExport",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "BMC Technical Support Export",
    "Id": "BmcTechSupportExport",
    "Name": "Task BmcTechSupportExport",
    "Oem": {
        "Cisco": {
            "ExportStatus": "None",
            "Protocol": "tftp",
            "RemoteHostName": "0.0.0.0",
            "RemotePath": "default.tar.gz",
            "RemoteUsername": ""
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/ExportBmcConfig

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/ExportBmcConfig",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Export BMC Configuration",
    "Id": "ExportBmcConfig",
    "Name": "Task ExportBmcConfig",
    "Oem": {
        "Cisco": {
            "ExportStatus": "None"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/ImportBmcConfig

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/ImportBmcConfig",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Import BMC Configuration",
    "Id": "ImportBmcConfig",
    "Name": "Task ImportBmcConfig",
    "Oem": {
        "Cisco": {
            "ImportStatus": "Completed Successfully"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

