```
    {
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Ancestors": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5ffede86696f6e2d306283ec",
            "ObjectType": "workflow.WorkflowInfo",
            "link": "https://www.intersight.com/api/v1/workflow/WorkflowInfos/5ffede86696f6e2d306283ec"
            }
        ],
        "ClassId": "workflow.TaskInfo",
        "CreateTime": "2021-01-13T12:18:18.686Z",
        "Description": "",
        "DisplayNames": {
            "hierarchical": [
            "Validate Cluster Configuration Before Deployment"
            ],
            "short": [
            "Validate Cluster Configuration Before Deployment"
            ]
        },
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "EndTime": "2021-01-13T12:21:52.789Z",
        "FailureReason": "Error Running Validations: Target HX1 failed with error: Failed to get cpu mode from ESX",
        "Input": {
            "hypervisorType": "0"
        },
        "InstId": "5ddad97b-ef4b-4f60-b1e3-a28f0df85bbb",
        "Internal": false,
        "Label": "Validate Cluster Configuration Before Deployment",
        "Message": [],
        "ModTime": "2021-01-13T12:21:52.789Z",
        "Moid": "5ffee50a696f6e2d30638a59",
        "Name": "hyperflex.PreDeployClusterValidationTask",
        "ObjectType": "workflow.TaskInfo",
        "Output": {
            "ConfigResultEntry": {
            "AccountMoid": "",
            "Ancestors": null,
            "ClassId": "hyperflex.ConfigResultEntry",
            "CompletedTime": "",
            "ConfigResult": null,
            "Context": {
                "ClassId": "policy.ConfigResultContext",
                "EntityData": null,
                "EntityMoid": "",
                "EntityName": "",
                "EntityType": "",
                "ObjectType": "policy.ConfigResultContext"
            },
            "CreateTime": "0001-01-01T00:00:00Z",
            "DomainGroupMoid": "",
            "Message": "",
            "ModTime": "0001-01-01T00:00:00Z",
            "Moid": "5ffee50a616c652d3025aede",
            "ObjectType": "hyperflex.ConfigResultEntry",
            "OwnerId": "{moId:5ffee50a696f6e2d30638a59,instId:5ddad97b-ef4b-4f60-b1e3-a28f0df85bbb}",
            "Owners": null,
            "PermissionResources": null,
            "SharedScope": "",
            "State": "Errored",
            "Tags": [],
            "Type": "Config"
            }
        },
        "Owners": [
            "5be4b2ce67626c6d661ca38d"
        ],
        "Parent": {
            "ClassId": "mo.MoRef",
            "Moid": "5ffede86696f6e2d306283ec",
            "ObjectType": "workflow.WorkflowInfo",
            "link": "https://www.intersight.com/api/v1/workflow/WorkflowInfos/5ffede86696f6e2d306283ec"
        },
        "PermissionResources": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            }
        ],
        "RefName": "hyperflex.PreDeployClusterValidationTask",
        "RetryCount": 0,
        "RollbackDisabled": false,
        "RunningInstId": "5ddad97b-ef4b-4f60-b1e3-a28f0df85bbb",
        "SharedScope": "",
        "StartTime": "2021-01-13T12:18:18.686Z",
        "Status": "FAILED",
        "SubWorkflowInfo": null,
        "SubWorkflowRetryHistory": null,
        "Tags": [],
        "TaskDefinition": {
            "ClassId": "mo.MoRef",
            "Moid": "5ff7c66a696f6e2d305c3256",
            "ObjectType": "workflow.TaskDefinition",
            "link": "https://www.intersight.com/api/v1/workflow/TaskDefinitions/5ff7c66a696f6e2d305c3256"
        },
        "TaskInstIdList": [],
        "TaskLoopInfo": null,
        "WorkflowInfo": {
            "ClassId": "mo.MoRef",
            "Moid": "5ffede86696f6e2d306283ec",
            "ObjectType": "workflow.WorkflowInfo",
            "link": "https://www.intersight.com/api/v1/workflow/WorkflowInfos/5ffede86696f6e2d306283ec"
        }
    }
```