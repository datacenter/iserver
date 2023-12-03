import time
from datetime import datetime


class WorkflowInfo():
    def __init__(self):
        pass

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
