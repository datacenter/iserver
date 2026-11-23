import time
from datetime import datetime

from lib import filter_helper


class DomainL3EventInfo():
    def __init__(self):
        self.domain_l3_event = None

    def get_domain_l3_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['domainName'] = None
        if 'affected' in info:
            if 'uni/l3dom-' in info['affected']:
                info['domainName'] = info['affected'].split('uni/l3dom-')[1].split('/')[0]

        if 'affected' not in info and 'dn' in info:
            if 'uni/l3dom-' in info['dn']:
                info['domainName'] = info['dn'].split('uni/l3dom-')[1].split('/')[0]

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

    def get_domain_l3_event(self, deduplicate=True):
        if self.domain_l3_event is not None:
            return self.domain_l3_event

        managed_objects = self.get_domain_l3_event_mo()
        if managed_objects is None:
            return None

        self.domain_l3_event = []
        transaction_ids = []
        for managed_object in managed_objects:
            event_info = self.get_domain_l3_event_info(
                managed_object
            )
            if not deduplicate or event_info['txId'] not in transaction_ids:
                self.domain_l3_event.append(
                    event_info
                )
                transaction_ids.append(
                    event_info['txId']
                )

        self.log.apic_mo(
            'l3extDomP.eventLog.info',
            self.domain_l3_event
        )

        return self.domain_l3_event

    def get_domain_l3_id_event(self, domain_name, event_filter=None):
        events = []

        all_events = self.get_domain_l3_event()
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['domainName'] is not None:
                if event_info['domainName'] == domain_name:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
