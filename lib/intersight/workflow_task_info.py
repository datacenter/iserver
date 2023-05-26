import time
from datetime import datetime

from lib.intersight.intersight_common import IntersightCommon


class WorkflowTaskInfo(IntersightCommon):
    """Class for intersight workflow taskinfo object
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
    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'workflow taskinfo'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

    def convert_time_epoch(self, time_string):
        """Return epoch ms time from string in workflow info object

        Args:
            time_string (string): time string

        Returns:
            int: epoch ms
        """
        try:
            time_string = time_string.replace('T', ' ').replace('Z', '000')
            return int(datetime.strptime(time_string, '%Y-%m-%d %H:%M:%S.%f').timestamp() * 1000)
        except BaseException:
            return None

    def get_workflow_task_info(self, workflow_task_object):
        info = {}
        info['__Output'] = {}
        for key in ['Moid', 'Name', 'Label', 'CreateTime', 'StartTime', 'EndTime', 'Status', 'FailureReason']:
            info[key] = None
            if key in workflow_task_object:
                info[key] = workflow_task_object[key]

        info['Description'] = info['Name']
        if len(info['Label']) > 0:
            info['Description'] = info['Label']

        for key in ['CreateTime', 'StartTime', 'EndTime']:
            info['%sEpoch' % (key)] = self.convert_time_epoch(info[key])

        try:
            seconds = int(info['EndTimeEpoch'] / 1000) - int(info['StartTimeEpoch'] / 1000)
            info['Duration'] = time.strftime('%H:%M:%S', time.gmtime(seconds))
        except BaseException:
            info['Duration'] = ''

        if info['Status'].lower() == 'completed':
            info['__Output']['Status'] = 'Green'

        if info['Status'].lower() == 'failed':
            info['__Output']['Status'] = 'Red'

        return info

    def get_workflow_tasks_info(self, workflow_id):
        tasks = []
        self.set_get_filter("WorkflowInfo/Moid eq '%s'" % (workflow_id))
        workflow_task_objects = self.get_all()
        if workflow_task_objects is not None:
            for workflow_task_object in workflow_task_objects:
                tasks.append(
                    self.get_workflow_task_info(
                        workflow_task_object
                    )
                )
        tasks = sorted(tasks, key=lambda i: i['CreateTimeEpoch'])
        return tasks
