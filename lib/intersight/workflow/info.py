import time


class WorkflowInfo():
    def __init__(self):
        pass

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

    def get_last(self, count=10):
        self.set_get_order('StartTime desc')
        managed_objects = self.get_top(count)
        if managed_objects is None:
            self.log_handler.error(
                'workflow.get_last',
                'failed to get workflows'
            )
            return

        return managed_objects
