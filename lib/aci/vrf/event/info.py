import time
from datetime import datetime

from lib import filter_helper


class VrfEventInfo():
    def __init__(self):
        self.vrf_event = None

    def get_vrf_event_info(self, managed_object):
        info = {}
        info['__Output'] = {}
        for key in managed_object:
            info[key] = managed_object[key]

        info['tenantName'] = None
        info['vrfName'] = None

        if 'affected' in info:
            if 'uni/tn-' in info['affected']:
                # uni/tn-k8s/ctx-bmk8s_2_BD
                info['tenantName'] = info['affected'].split('uni/tn-')[1].split('/')[0]

            if '/ctx-' in info['affected']:
                info['vrfName'] = info['affected'].split('/ctx-')[1].split('/')[0]

        if 'affected' not in info and 'dn' in info:
            if 'uni/tn-' in info['dn']:
                # uni/tn-k8s/ctx-bmk8s_2_BD
                info['tenantName'] = info['dn'].split('uni/tn-')[1].split('/')[0]

            if '/ctx-' in info['dn']:
                info['vrfName'] = info['dn'].split('/ctx-')[1].split('/')[0]

        info['nameTenant'] = '--'
        if info['tenantName'] is not None and info['vrfName'] is not None:
            info['nameTenant'] = '%s/%s' % (
                info['tenantName'],
                info['vrfName']
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

    def get_vrf_event(self, deduplicate=True):
        if self.vrf_event is not None:
            return self.vrf_event

        managed_objects = self.get_vrf_event_mo()
        if managed_objects is None:
            return None

        self.vrf_event = []
        transaction_ids = []
        for managed_object in managed_objects:
            event_info = self.get_vrf_event_info(
                managed_object
            )
            if not deduplicate or event_info['txId'] not in transaction_ids:
                self.vrf_event.append(
                    event_info
                )
                transaction_ids.append(
                    event_info['txId']
                )

        self.log.apic_mo(
            'fvCtx.eventLog.info',
            self.vrf_event
        )

        return self.vrf_event

    def get_vrf_id_event(self, tenant_name, vrf_name, event_filter=None):
        events = []

        all_events = self.get_vrf_event()
        if all_events is None:
            return events

        for event_info in all_events:
            if event_info['tenantName'] is not None and event_info['vrfName'] is not None:
                if event_info['tenantName'] == tenant_name and event_info['vrfName'] == vrf_name:
                    if not self.match_system_fault(event_info, event_filter):
                        continue

                    events.append(
                        event_info
                    )

        return events
