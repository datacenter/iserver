from lib import filter_helper


class K8sNetworkAttachmentDefinitionMatch():
    def __init__(self):
        pass

    def match_nad(self, info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'resource':
                key_found = True
                if not filter_helper.match_string(value, info['resource_name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_nad',
                    'Unsupported key: %s' % (key)
                )

        return True