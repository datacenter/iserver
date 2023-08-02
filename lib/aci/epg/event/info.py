import time
from datetime import datetime

from lib import filter_helper


class EpgEventInfo():
    def __init__(self):
        self.epg_event = None

    def get_epg_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['apName'] = None
        info['epgName'] = None

        if 'affected' in info:
            if 'uni/tn-' in info['affected']:
                # uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_prov
                info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

            if '/ap-' in info['affected']:
                info['apName'] = info['affected'].split('/ap-')[1].split('/')[0]

            if '/epg-' in info['affected']:
                info['epgName'] = info['affected'].split('/epg-')[1].split('/')[0]

        if 'affected' not in info and 'dn' in info:
            if 'uni/tn-' in info['dn']:
                # uni/tn-k8s/ap-k8s_ANP/epg-bmk8s_prov
                info['tenantName'] = info['dn'].split('uni/tn-')[1].split('/')[0]

            if '/ap-' in info['dn']:
                info['apName'] = info['dn'].split('/ap-')[1].split('/')[0]

            if '/epg-' in info['dn']:
                info['epgName'] = info['dn'].split('/epg-')[1].split('/')[0]

        info['nameApTenant'] = '--'
        if info['tenantName'] is not None and info['apName'] is not None and info['epgName'] is not None:
            info['nameApTenant'] = '%s/%s/%s' % (
                info['tenantName'],
                info['apName'],
                info['epgName']
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

    def get_epg_event(self, deduplicate=True):
        if self.epg_event is not None:
            return self.epg_event

        managed_objects = self.get_epg_event_mo()
        if managed_objects is None:
            return None

        self.epg_event = []
        transaction_ids = []
        for managed_object in managed_objects:
            event_info = self.get_epg_event_info(
                managed_object
            )
            if not deduplicate or event_info['txId'] not in transaction_ids:
                self.epg_event.append(
                    event_info
                )
                transaction_ids.append(
                    event_info['txId']
                )

        self.log.apic_mo(
            'fvAEPg.eventLog.info',
            self.epg_event
        )

        return self.epg_event

    def get_epg_id_event(self, tenant_name, ap_name, epg_name, event_filter=None):
        events = []

        all_events = self.get_epg_event()
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['tenantName'] is not None and event_info['apName'] is not None and event_info['epgName'] is not None:
                if event_info['tenantName'] == tenant_name and event_info['apName'] == ap_name and event_info['epgName'] == epg_name:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
