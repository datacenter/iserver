from lib import filter_helper


class K8sEventInfo():
    def __init__(self):
        self.event = None

    def get_event_info(self, event_mo):
        if event_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['message'] = self.get(event_mo, 'message')
        info['count'] = self.get(event_mo, 'count')
        info['action'] = self.get(event_mo, 'action')
        info['reason'] = self.get(event_mo, 'reason')
        info['type'] = self.get(event_mo, 'type')
        info['obj_kind'] = self.get(event_mo, 'involved_object:kind')
        info['obj_namespace'] = self.get(event_mo, 'involved_object:namespace')
        if info['obj_namespace'] is None:
            info['obj_namespace'] = self.get(event_mo, 'metadata:namespace')
        info['obj_name'] = self.get(event_mo, 'involved_object:name')
        info['obj_uid'] = self.get(event_mo, 'involved_object:uid')
        info['src_component'] = self.get(event_mo, 'source:component')
        info['src_host'] = self.get(event_mo, 'source:host')

        info['first_timestamp'] = self.get(event_mo, 'first_timestamp')
        info['first_timestamp_epoch'] = self.convert_timestamp(
            self.get(event_mo, 'first_timestamp')
        )
        info['first_timestamp_age'] = self.convert_timestamp_to_age(
            info['first_timestamp'],
            on_error='--'
        )

        info['last_timestamp'] = self.get(event_mo, 'last_timestamp')
        info['last_timestamp_epoch'] = self.convert_timestamp(
            self.get(event_mo, 'last_timestamp')
        )
        info['last_timestamp_age'] = self.convert_timestamp_to_age(
            info['last_timestamp'],
            on_error='--'
        )

        return info

    def get_events_info(self, cache_enabled=True):
        if cache_enabled:
            if self.event is not None:
                return self.event

        managed_objects = self.get_event_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.event = []
        for managed_object in managed_objects:
            event_info = {}
            event_info['info'] = self.get_event_info(
                managed_object
            )
            event_info['mo'] = managed_object
            self.event.append(
                event_info
            )

        return self.event

    def match_event(self, event_info, event_filter):
        if event_filter is None or len(event_filter) == 0:
            return True

        for ap_rule in event_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'kind':
                key_found = True
                if not filter_helper.match_string(value, event_info['obj_kind']):
                    return False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, event_info['obj_namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, event_info['obj_name']):
                    return False

            if key == 'uid':
                key_found = True
                if not filter_helper.match_string(value, event_info['obj_uid']):
                    return False

            if key == 'message':
                key_found = True
                if not filter_helper.match_string(value, event_info['message']):
                    return False

            if not key_found:
                self.log.error(
                    'match_event',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_events(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_events = self.get_events_info(cache_enabled=cache_enabled)
        if all_events is None:
            return None

        events = []

        for event_info in all_events:
            if not self.match_event(event_info['info'], object_filter):
                continue

            if return_mo:
                events.append(
                    event_info['mo']
                )
                continue

            events.append(
                event_info['info']
            )

        if not return_mo:
            events = sorted(
                events,
                key=lambda i: i['last_timestamp_epoch']
            )

        return events
