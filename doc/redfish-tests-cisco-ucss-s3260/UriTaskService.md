# Resource: /redfish/v1/TaskService

Vendor | Model
--- | ---
Cisco | UCSS-S3260

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
            "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1FwUpdate"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/Bios1FwUpdate"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1TechSupportExport"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1ImportConfig"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1ExportConfig"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCFwUpdate"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/PeerCMCFwUpdate"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCTechSupportExport"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCImportConfig"
        },
        {
            "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCExportConfig"
        }
    ],
    "Members@odata.count": 10,
    "Name": "Tasks"
}
```

## /redfish/v1/TaskService/Tasks/BMC1ExportConfig

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1ExportConfig",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Export Configuration",
    "Id": "BMC1ExportConfig",
    "Name": "Task BMC1ExportConfig",
    "Oem": {
        "Cisco": {
            "ExportStatus": "None"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/BMC1FwUpdate

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1FwUpdate",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Cisco IMC backup firmware version",
    "Id": "BMC1FwUpdate",
    "Name": "Task BMC1FwUpdate",
    "Oem": {
        "Cisco": {
            "FWVersion": "4.1(1f)",
            "UpdateStatus": "Success (100%)"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/BMC1ImportConfig

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1ImportConfig",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Import Configuration",
    "Id": "BMC1ImportConfig",
    "Name": "Task BMC1ImportConfig",
    "Oem": {
        "Cisco": {
            "ImportStatus": "Completed Successfully"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/BMC1TechSupportExport

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/BMC1TechSupportExport",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Technical Support Export",
    "Id": "BMC1TechSupportExport",
    "Name": "Task BMC1TechSupportExport",
    "Oem": {
        "Cisco": {
            "ExportStatus": "NA",
            "Protocol": "NA",
            "RemoteHostName": "NA",
            "RemotePath": "NA",
            "RemoteUsername": "NA"
        }
    },
    "TaskState": "New",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/Bios1FwUpdate

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/Bios1FwUpdate",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "BIOS firmware version",
    "Id": "Bios1FwUpdate",
    "Name": "Task Bios1FwUpdate",
    "Oem": {
        "Cisco": {
            "FWVersion": "C3X60M4.4.1.2c.0.0202211901",
            "UpdateStatus": "None, OK"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/CIMCExportConfig

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCExportConfig",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Export Configuration",
    "Id": "CIMCExportConfig",
    "Name": "Task CIMCExportConfig",
    "Oem": {
        "Cisco": {
            "ExportStatus": "None"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/CIMCFwUpdate

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCFwUpdate",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Cisco IMC backup firmware version",
    "Id": "CIMCFwUpdate",
    "Name": "Task CIMCFwUpdate",
    "Oem": {
        "Cisco": {
            "FWVersion": "4.1(1f)",
            "UpdateStatus": "Success (100%)"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/CIMCImportConfig

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCImportConfig",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Import Configuration",
    "Id": "CIMCImportConfig",
    "Name": "Task CIMCImportConfig",
    "Oem": {
        "Cisco": {
            "ImportStatus": "Completed Successfully"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/CIMCTechSupportExport

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/CIMCTechSupportExport",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Technical Support Export",
    "Id": "CIMCTechSupportExport",
    "Name": "Task CIMCTechSupportExport",
    "Oem": {
        "Cisco": {
            "ExportStatus": "NA",
            "Protocol": "NA",
            "RemoteHostName": "NA",
            "RemotePath": "NA",
            "RemoteUsername": "NA"
        }
    },
    "TaskState": "New",
    "TaskStatus": "OK"
}
```

## /redfish/v1/TaskService/Tasks/PeerCMCFwUpdate

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService/Tasks/Members/$entity",
    "@odata.id": "/redfish/v1/TaskService/Tasks/PeerCMCFwUpdate",
    "@odata.type": "#Task.v1_3_0.Task",
    "Description": "Cisco IMC backup firmware version",
    "Id": "PeerCMCFwUpdate",
    "Name": "Task PeerCMCFwUpdate",
    "Oem": {
        "Cisco": {
            "FWVersion": "N/A",
            "UpdateStatus": "Starting (0%)"
        }
    },
    "TaskState": "Completed",
    "TaskStatus": "OK"
}
```

