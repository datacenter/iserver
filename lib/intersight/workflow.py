import time
from datetime import datetime

from lib.intersight.intersight_common import IntersightCommon


class Workflow(IntersightCommon):
    """Class for intersight workflowinfo object
    {
        "Account": null,
        "AccountMoid": "5be4b2ce67626c6d661ca38d",
        "Action": "None",
        "Ancestors": [],
        "AssociatedObject": {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
        },
        "ClassId": "workflow.WorkflowInfo",
        "CleanupTime": "0001-01-01T00:00:00Z",
        "CreateTime": "2022-04-13T19:53:12.956Z",
        "DomainGroupMoid": "5be4b2ce67626c6d661ca39c",
        "Email": "akaliwod@cisco.com",
        "EndTime": "0001-01-01T00:00:00Z",
        "FailedWorkflowCleanupDuration": 2160,
        "Input": {
            "ActionProfile": {
            "Moid": "624b3dfc7a6f722d3046b689",
            "ObjectType": "kubernetes.ClusterProfile"
            }
        },
        "InstId": "f762caae-d921-46d3-bbf4-ea52f8ac2376",
        "Internal": false,
        "LastAction": "Start",
        "Message": [],
        "MetaVersion": 0,
        "ModTime": "2022-04-13T19:53:26.878Z",
        "Moid": "62572a28696f6e2d30a20838",
        "Name": "Deploy Kubernetes Cluster Profile",
        "ObjectType": "workflow.WorkflowInfo",
        "Organization": null,
        "Output": null,
        "Owners": [
            "5be4b2ce67626c6d661ca38d"
        ],
        "ParentTaskInfo": null,
        "PauseReason": "None",
        "PendingDynamicWorkflowInfo": null,
        "PermissionResources": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "5dee1d736972652d321d26b5",
            "ObjectType": "organization.Organization",
            "link": "https://www.intersight.com/api/v1/organization/Organizations/5dee1d736972652d321d26b5"
            }
        ],
        "Progress": 10.97561,
        "Properties": {
            "Cancelable": {
            "CancelableStates": [],
            "ClassId": "workflow.CancelableType",
            "Enabled": true,
            "Mode": "ApiOnly",
            "ObjectType": "workflow.CancelableType"
            },
            "ClassId": "workflow.WorkflowInfoProperties",
            "ObjectType": "workflow.WorkflowInfoProperties",
            "Retryable": false,
            "RollbackAction": "Disabled",
            "RollbackOnFailure": false
        },
        "RetryFromTaskName": "",
        "SharedScope": "",
        "Src": "razor",
        "StartTime": "2022-04-13T19:53:12.977Z",
        "Status": "RUNNING",
        "SuccessWorkflowCleanupDuration": 2160,
        "Tags": [],
        "TaskInfos": [
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a29696f6e2d30a20845",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a29696f6e2d30a20845"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a29696f6e2d30a20855",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a29696f6e2d30a20855"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2a696f6e2d30a20861",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2a696f6e2d30a20861"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2b696f6e2d30a20876",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2b696f6e2d30a20876"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2b696f6e2d30a2087c",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2b696f6e2d30a2087c"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2c696f6e2d30a2088e",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2c696f6e2d30a2088e"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2d696f6e2d30a2089f",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2d696f6e2d30a2089f"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2d696f6e2d30a208ab",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2d696f6e2d30a208ab"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2e696f6e2d30a208b9",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2e696f6e2d30a208b9"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a2f696f6e2d30a208c5",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a2f696f6e2d30a208c5"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a30696f6e2d30a208d1",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a30696f6e2d30a208d1"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a31696f6e2d30a208dd",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a31696f6e2d30a208dd"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a32696f6e2d30a208ef",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a32696f6e2d30a208ef"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a34696f6e2d30a20933",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a34696f6e2d30a20933"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a35696f6e2d30a2094c",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a35696f6e2d30a2094c"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a35696f6e2d30a2095f",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a35696f6e2d30a2095f"
            },
            {
            "ClassId": "mo.MoRef",
            "Moid": "62572a36696f6e2d30a20971",
            "ObjectType": "workflow.TaskInfo",
            "link": "https://www.intersight.com/api/v1/workflow/TaskInfos/62572a36696f6e2d30a20971"
            }
        ],
        "TraceId": "NB181ae694abcb5ab28b4eba75540327a9",
        "Type": "UserDefined",
        "UserActionRequired": false,
        "UserId": "5f9ff9d37564612d306e9e5b",
        "Variable": null,
        "WaitReason": "None",
        "WorkflowCtx": {
            "ClassId": "workflow.WorkflowCtx",
            "InitiatorCtx": {
            "ClassId": "workflow.InitiatorContext",
            "InitiatorMoid": "624b3dfc7a6f722d3046b689",
            "InitiatorName": "milan-kali",
            "InitiatorType": "kubernetes.ClusterProfile",
            "ObjectType": "workflow.InitiatorContext"
            },
            "ObjectType": "workflow.WorkflowCtx",
            "TargetCtxList": [
            {
                "ClassId": "workflow.TargetContext",
                "ObjectType": "workflow.TargetContext",
                "TargetMoid": "624b3dfc7a6f722d3046b689",
                "TargetName": "milan-kali",
                "TargetType": "kubernetes.ClusterProfile"
            }
            ],
            "WorkflowMetaName": "",
            "WorkflowSubtype": "",
            "WorkflowType": "Deploy Kubernetes Cluster Profile"
        },
        "WorkflowDefinition": {
            "ClassId": "mo.MoRef",
            "Moid": "5fdc0b65696f6e2d309790b0",
            "ObjectType": "workflow.WorkflowDefinition",
            "link": "https://www.intersight.com/api/v1/workflow/WorkflowDefinitions/5fdc0b65696f6e2d309790b0"
        },
        "WorkflowMetaType": "UserDefined",
        "WorkflowTaskCount": 36,
        "WorkflowWorkerTaskCount": 82
    }

    """
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'workflow workflowinfo'
        self.cache_key = 'workflow'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id, cache_key=self.cache_key)

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

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        for key in ['Moid', 'Name', 'Progress', 'CreateTime', 'StartTime', 'EndTime', 'Status', 'Type']:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        for key in ['CreateTime', 'StartTime', 'EndTime']:
            info['%sEpoch' % (key)] = self.convert_time_epoch(info[key])

        info['Running'] = False
        info['Completed'] = False
        if managed_object['Status'] == 'RUNNING':
            info['Running'] = True

        if not info['Running']:
            if managed_object['Status'] in ['COMPLETED', 'FAILED']:
                info['Completed'] = True

            if info['Status'].lower() == 'completed':
                info['__Output']['Status'] = 'Green'

            if info['Status'].lower() == 'failed':
                info['__Output']['Status'] = 'Red'

        if info['Completed']:
            try:
                seconds = int(info['EndTimeEpoch'] / 1000) - int(info['StartTimeEpoch'] / 1000)
                info['Duration'] = time.strftime('%H:%M:%S', time.gmtime(seconds))
            except BaseException:
                info['Duration'] = ''
        else:
            try:
                seconds = int(time.time()) - int(info['StartTimeEpoch'] / 1000)
                info['Duration'] = time.strftime('%H:%M:%S', time.gmtime(seconds))
            except BaseException:
                info['Duration'] = ''

        return info

    def is_server_workflow(self, server_id, managed_object):
        try:
            if managed_object['Input']['Server']['Moid'] == server_id:
                return True
        except BaseException:
            pass

        try:
            if managed_object['Input']['ServerMoId'] == server_id:
                return True
        except BaseException:
            pass

        try:
            for target in managed_object['Input']['workflowContext']['TargetCtxList']:
                if target['TargetMoid'] == server_id:
                    return True
        except BaseException:
            pass

        return False
