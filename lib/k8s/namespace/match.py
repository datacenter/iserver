class K8sNamespaceMatch():
    def __init__(self):
        pass

    def match_namespace_state(self, info, filter_rules):
        if filter_rules is None or len(filter_rules) == 0:
            return True

        for ap_rule in filter_rules:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key in self.get_common_match():
                key_found = True
                continue

            if key == 'label':
                key_found = True
                found = False
                labels = self.get(info, 'label')
                if labels is None:
                    return False

                for label in labels:
                    if label == value.split(':')[0]:
                        if len(value.split(':')) == 1:
                            found = True
                            break

                        if labels[label] == value.split(':')[1]:
                            found = True
                            break

                if not found:
                    return False
                                                
            if not key_found:
                self.log.error(
                    'match_namespace_state',
                    'Unsupported key: %s' % (key)
                )

        return True