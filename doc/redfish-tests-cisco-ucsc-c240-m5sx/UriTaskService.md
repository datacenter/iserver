# Resource: /redfish/v1/TaskService

Vendor | Model
--- | ---
Cisco | UCSC-C240-M5SX

## /redfish/v1/TaskService

```{
    "@odata.context": "/redfish/v1/$metadata#TaskService.TaskService",
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
    "@odata.id": "/redfish/v1/TaskService/Tasks",
    "@odata.type": "#TaskCollection.TaskCollection",
    "Description": "Tasks",
    "Members": [],
    "Members@odata.count": 0,
    "Name": "Task Collection"
}
```

