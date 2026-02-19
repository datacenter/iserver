from lib import filter_helper


class K8sNodeFeatureInfo():
    def __init__(self):
        self.node_feature = None

    def get_node_feature_info(self, node_feature_mo):
        if node_feature_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            node_feature_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(node_feature_mo, 'spec')
        return info

    def get_node_features_info(self, cache_enabled=True):
        if cache_enabled:
            if self.node_feature is not None:
                return self.node_feature

        managed_objects = self.get_node_feature_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.node_feature = []
        for managed_object in managed_objects:
            node_feature_info = {}
            node_feature_info['info'] = self.get_node_feature_info(
                managed_object
            )
            node_feature_info['mo'] = managed_object
            self.node_feature.append(
                node_feature_info
            )

        return self.node_feature

    def match_node_feature(self, node_feature_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, node_feature_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, node_feature_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_node_feature',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_node_features(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_node_features = self.get_node_features_info(cache_enabled=cache_enabled)
        if all_node_features is None:
            return None

        node_features = []

        for node_feature_info in all_node_features:
            if not self.match_node_feature(node_feature_info['info'], object_filter):
                continue

            if return_mo:
                node_features.append(
                    node_feature_info['mo']
                )
                continue

            node_features.append(
                node_feature_info['info']
            )

        return node_features

    def is_node_feature(self, namespace, name, cache_enabled=True):
        if self.get_node_feature(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_node_feature(self, namespace, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'namespace:%s' % (namespace)
        )
        object_filter.append(
            'name:%s' % (name)
        )
        node_features = self.get_node_features(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if node_features is None:
            return None

        if len(node_features) == 1:
            return node_features[0]

        return None
