class FeatureInfo():
    def __init__(self):
        self.features = None

    def get_feature_info(self, feature_mo):
        info = {}
        info['__Output'] = {}
        info['nexus_name'] = self.nexus_name
        info['index'] = feature_mo['cfcFeatureCtrlIndex2']
        info['instance'] = feature_mo['cfcFeatureCtrlInstanceNum2']
        info['name'] = feature_mo['cfcFeatureCtrlName2']
        info['status'] = feature_mo['cfcFeatureCtrlOpStatus2']
        info['enabled'] = False
        if info['status'] == 'enabled':
            info['enabled'] = True

        return info

    def get_features_info(self, feature_mo):
        self.features = []

        for item in feature_mo['TABLE_cfcFeatureCtrlTable']['ROW_cfcFeatureCtrlTable']:
            self.features.append(
                self.get_feature_info(
                    item
                )
            )

        self.features = sorted(
            self.features,
            key=lambda i: (
                i['name'],
                i['instance']
            )
        )

        return self.features

    def get_features(self, cache_enabled=True):
        if self.features is not None:
            return self.features

        feature_mo = self.get_feature_mo(cache_enabled=cache_enabled)
        if feature_mo is None:
            self.log.error(
                'get_features',
                'Failed to get features: %s' % (self.nexus_name)
            )
            return None

        return self.get_features_info(feature_mo)

    def is_feature_enabled(self, name, cache_enabled=True):
        features = self.get_features(cache_enabled=cache_enabled)
        if features is None:
            return False

        for feature in features:
            if feature['name'] == name:
                return feature['enabled']

        return False
