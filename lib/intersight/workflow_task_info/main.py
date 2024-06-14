import time

from lib.intersight.intersight_common import IntersightCommon


class WorkflowTaskInfo(IntersightCommon):
    def __init__(self, iaccount, get_filter=None, log_id=None):
        self.iobject = 'workflow taskinfo'
        IntersightCommon.__init__(self, iaccount, self.iobject, get_filter=get_filter, log_id=log_id)

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

        try:
            tasks = sorted(tasks, key=lambda i: i['CreateTimeEpoch'])
        except BaseException:
            pass

        return tasks
