import time
from datetime import datetime

from lib import filter_helper


class CondAlarmInfo():
    def __init__(self):
        self.cond_alarm = None

    def get_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['AffectedType'] = managed_object['AffectedMo']['ObjectType']
        info['AffectedMoid'] = managed_object['AffectedMo']['Moid']
        info['AffectedName'] = managed_object['AffectedMoDisplayName']
        info['AncestorMoId'] = managed_object['AncestorMoId']
        info['AncestorMoType'] = managed_object['AncestorMoType']
        info['CreateTime'] = managed_object['CreateTime']
        info['LastTransitionTime'] = managed_object['LastTransitionTime']
        if '.' in managed_object['LastTransitionTime']:
            info['Timestamp'] = int(
                time.mktime(
                    datetime.strptime(
                        info['LastTransitionTime'],
                        '%Y-%m-%dT%H:%M:%S.%f%z'
                    ).timetuple()
                )
            )
        else:
            info['Timestamp'] = int(
                time.mktime(
                    datetime.strptime(
                        info['LastTransitionTime'],
                        '%Y-%m-%dT%H:%M:%SZ'
                    ).timetuple()
                )
            )

        info['Description'] = managed_object['Description']
        info['Acknowledge'] = managed_object['Acknowledge']
        info['Moid'] = managed_object['Moid']
        info['Name'] = managed_object['Name']
        info['Code'] = managed_object['Code']

        info['Severity'] = managed_object['Severity']
        if info['Severity'] == 'Critical':
            info['__Output']['Severity'] = 'Red'

        if info['Severity'] == 'Warning':
            info['__Output']['Severity'] = 'Yellow'

        if info['Severity'] == 'Info':
            info['__Output']['Severity'] = 'Blue'

        return info

    def get_infos(self):
        if self.cond_alarm is not None:
            return self.cond_alarm

        managed_objects = self.get_all()
        if managed_objects is None:
            return None

        self.cond_alarm = []
        for managed_object in managed_objects:
            self.cond_alarm.append(
                self.get_info(
                    managed_object
                )
            )

        self.log.intersight_mo(
            'cond_alarm.info',
            self.cond_alarm
        )

        return self.cond_alarm

    def match_cond_alarm(self, cond_alarm_info, cond_alarm_filter, last_moids):
        if cond_alarm_filter is None or len(cond_alarm_filter) == 0:
            return True

        for rule in cond_alarm_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key == 'timestamp':
                key_found = True
                if not filter_helper.match_timestamp(value, cond_alarm_info['Timestamp']):
                    return False

            if key == 'severity':
                key_found = True
                if value != 'any':
                    if not filter_helper.match_string(value, cond_alarm_info['Severity']):
                        return False

            if key == 'code':
                key_found = True
                if not filter_helper.match_string(value, cond_alarm_info['Code']) and not filter_helper.match_string(value, cond_alarm_info['Name']):
                    return False

            if key == 'cleared':
                key_found = True
                if value == 'False':
                    if cond_alarm_info['Severity'] == 'Cleared':
                        return False

            if key == 'new':
                key_found = True
                if value == 'True':
                    if last_moids is not None:
                        if cond_alarm_info['Moid'] in last_moids and cond_alarm_info['LastTransitionTime'] == last_moids[cond_alarm_info['Moid']]:
                            return False

            if not key_found:
                self.log.error(
                    'match_cond_alarm',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cond_alarms(self, cond_alarm_filter=None, update_moid_cache=False):
        all_cond_alarms = self.get_infos()
        if all_cond_alarms is None:
            return None

        last_moids = self.get_iaccount_json_file('cond_alarm_moids')
        cond_alarms = []

        for cond_alarm_info in all_cond_alarms:
            if not self.match_cond_alarm(cond_alarm_info, cond_alarm_filter, last_moids):
                continue

            cond_alarms.append(cond_alarm_info)

        cond_alarms = sorted(
            cond_alarms,
            key=lambda i: i['Timestamp'],
            reverse=True
        )

        if update_moid_cache:
            moids = {}
            for cond_alarm in all_cond_alarms:
                moids[cond_alarm['Moid']] = cond_alarm['LastTransitionTime']
            self.set_iaccount_json_file('cond_alarm_moids', moids)

        return cond_alarms
