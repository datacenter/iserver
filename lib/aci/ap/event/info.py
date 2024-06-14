import time
from datetime import datetime

from lib import filter_helper


class ApplicationProfileEventInfo():
    def __init__(self):
        self.application_profile_event = None

    def get_application_profile_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['apName'] = None
        info['epgName'] = None

        if 'affected' in info:
            if 'uni/tn-' in info['affected']:
                # uni/tn-k8s/ap-k8s_ANP/epg-vk8s_1
                info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

            if '/ap-' in info['affected']:
                info['apName'] = info['affected'].split('/ap-')[1].split('/')[0]

            if '/epg-' in info['affected']:
                info['epgName'] = info['affected'].split('/epg-')[1].split('/')[0]

        if 'affected' not in info and 'dn' in info:
            if 'uni/tn-' in info['dn']:
                info['tenantName'] = info['dn'].split('uni/tn-')[1].split('/')[0]

            if '/ap-' in info['dn']:
                info['apName'] = info['dn'].split('/ap-')[1].split('/')[0]

            if '/epg-' in info['dn']:
                info['epgName'] = info['dn'].split('/epg-')[1].split('/')[0]

        info['nameTenant'] = '--'
        if info['tenantName'] is not None and info['apName'] is not None:
            info['nameTenant'] = '%s/%s' % (
                info['tenantName'],
                info['apName']
            )

        info['descrT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['descr']
            ),
            80
        )

        info['changeSetT'] = filter_helper.get_string_chunks(
            filter_helper.sanitize_string(
                info['changeSet']
            ),
            80
        )

        info['dnT'] = filter_helper.get_string_chunks(
            info['dn'],
            40,
            separator='/'
        )

        # "2022-04-29T13:32:45.167+02:00"
        info['timestamp'] = int(
            time.mktime(
                datetime.strptime(
                    info['created'],
                    '%Y-%m-%dT%H:%M:%S.%f%z'
                ).timetuple()
            )
        )

        info['severityT'] = self.system_fault_severity_name[info['severity']]
        info['__Output']['severityT'] = self.system_fault_severity_color[info['severity']]

        return info

    def get_application_profile_event(self, deduplicate=True):
        if self.application_profile_event is not None:
            return self.application_profile_event

        managed_objects = self.get_application_profile_event_mo()
        if managed_objects is None:
            return None

        self.application_profile_event = []
        transaction_ids = []
        for managed_object in managed_objects:
            event_info = self.get_application_profile_event_info(
                managed_object
            )
            if not deduplicate or event_info['txId'] not in transaction_ids:
                self.application_profile_event.append(
                    event_info
                )
                transaction_ids.append(
                    event_info['txId']
                )

        self.log.apic_mo(
            'fvAp.eventLog.info',
            self.application_profile_event
        )

        return self.application_profile_event

    def get_application_profile_id_event(self, tenant_name, ap_name, event_filter=None):
        events = []

        all_events = self.get_application_profile_event()
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['tenantName'] is not None and event_info['apName'] is not None:
                if event_info['tenantName'] == tenant_name and event_info['apName'] == ap_name:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
