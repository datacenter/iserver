# Resource: /redfish/v1/TaskService

Vendor | Model
--- | ---
HPE | vServer

## /redfish/v1/TaskService

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService.TaskService",
    "@odata.etag": "W/\"538CCB4A\"",
    "@odata.id": "/redfish/v1/TaskService",
    "@odata.type": "#TaskService.v1_1_1.TaskService",
    "CompletedTaskOverWritePolicy": "Manual",
    "DateTime": "2022-08-03T17:15:12Z",
    "Description": "iLO Task Service",
    "Id": "TaskService",
    "LifeCycleEventOnTaskStateChange": true,
    "Name": "Task Service",
    "ServiceEnabled": true,
    "Status": {
        "Health": "OK",
        "HealthRollup": "OK",
        "State": "Enabled"
    },
    "Tasks": {
        "@odata.id": "/redfish/v1/TaskService/Tasks"
    }
}
```

## /redfish/v1/TaskService/Tasks

```{
    "@odata.context": "/redfish/v1/$metadata#TaskCollection.TaskCollection",
    "@odata.etag": "W/\"75983E8D\"",
    "@odata.id": "/redfish/v1/TaskService/Tasks",
    "@odata.type": "#TaskCollection.TaskCollection",
    "Description": "iLO Tasks",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Tasks"
}
```

