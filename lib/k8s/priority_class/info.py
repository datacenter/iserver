from lib import filter_helper


class K8sPriorityClassInfo():
    def __init__(self):
        self.priority_class = None

    def get_priority_class_info(self, priority_class_mo):
        if priority_class_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        return info

    def get_priority_classes_info(self, cache_enabled=True):
        if cache_enabled:
            if self.priority_class is not None:
                return self.priority_class

        managed_objects = self.get_priority_class_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.priority_class = []
        for managed_object in managed_objects:
            priority_class_info = {}
            priority_class_info['info'] = self.get_priority_class_info(
                managed_object
            )
            priority_class_info['mo'] = managed_object
            self.priority_class.append(
                priority_class_info
            )

        return self.priority_class

    def match_priority_class(self, priority_class_info, priority_class_filter):
        if priority_class_filter is None or len(priority_class_filter) == 0:
            return True

        for ap_rule in priority_class_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_priority_class',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_priority_classes(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_priority_classes = self.get_priority_classes_info(cache_enabled=cache_enabled)
        if all_priority_classes is None:
            return None

        priority_classes = []

        for priority_class_info in all_priority_classes:
            if not self.match_priority_class(priority_class_info['info'], object_filter):
                continue

            if return_mo:
                priority_classes.append(
                    priority_class_info['mo']
                )
                continue

            priority_classes.append(
                priority_class_info['info']
            )

        return priority_classes
