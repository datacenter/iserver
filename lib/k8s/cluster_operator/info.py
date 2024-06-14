from lib import filter_helper


class K8sClusterOperatorInfo():
    def __init__(self):
        self.cluster_operator = None

    def get_cluster_operator_info(self, cluster_operator_mo):
        if cluster_operator_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            cluster_operator_mo
        )
        info.update(metadata_info)

        info['manager'] = None
        managed_fields = self.get(
            cluster_operator_mo,
            'metadata:managedFields'
        )
        if managed_fields is not None:
            for managed_field in managed_fields:
                try:
                    if len(managed_field['fieldsV1']['f:status']['f:conditions']) >= 0:
                        info['manager'] = managed_field['manager']
                except BaseException:
                    pass

        info['available'] = False
        info['availableSince'] = '--'
        info['availableTick'] = '\u2717'
        info['__Output']['availableTick'] = 'Red'

        info['progressing'] = False
        info['progressingTick'] = '\u2713'

        info['degraded'] = False
        info['degradedTick'] = '\u2713'

        info['upgradeable'] = False
        info['upgradeableTick'] = '\u2713'

        conditions_mo = self.get(
            cluster_operator_mo,
            'status:conditions'
        )
        if conditions_mo is not None:
            for condition_mo in conditions_mo:
                if condition_mo['type'] == 'Available':
                    if condition_mo['status'] == 'True':
                        info['available'] = True
                        info['availableTick'] = '\u2713'
                        info['__Output']['availableTick'] = 'Green'
                        info['availableSince'] = self.convert_timestamp_to_age(
                            self.get(
                                condition_mo,
                                'lastTransitionTime'
                            ),
                            on_error='--'
                        )

                if condition_mo['type'] == 'Degraded':
                    if condition_mo['status'] == 'True':
                        info['degraded'] = True
                        info['degradedTick'] = '\u2713'

                if condition_mo['type'] == 'Progressing':
                    if condition_mo['status'] == 'True':
                        info['progressing'] = True
                        info['progressingTick'] = '\u2713'

                if condition_mo['type'] == 'Upgradeable':
                    if condition_mo['status'] == 'True':
                        info['upgradeable'] = True
                        info['upgradeableTick'] = '\u2713'

        versions = self.get(
            cluster_operator_mo,
            'status:versions'
        )
        info['version'] = None
        if versions is not None:
            for version in versions:
                if version['name'] == 'operator':
                    info['version'] = version['version']

        info['related'] = self.get(
            cluster_operator_mo,
            'status:relatedObjects'
        )

        return info

    def get_cluster_operators_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cluster_operator is not None:
                return self.cluster_operator

        managed_objects = self.get_cluster_operator_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cluster_operator = []
        for managed_object in managed_objects:
            cluster_operator_info = {}
            cluster_operator_info['info'] = self.get_cluster_operator_info(
                managed_object
            )
            cluster_operator_info['mo'] = managed_object
            self.cluster_operator.append(
                cluster_operator_info
            )

        return self.cluster_operator

    def match_cluster_operator(self, cluster_operator_info, cluster_operator_filter):
        if cluster_operator_filter is None or len(cluster_operator_filter) == 0:
            return True

        for ap_rule in cluster_operator_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cluster_operator_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cluster_operator',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cluster_operator_deployment(self, cluster_operator_info, deployments):
        if cluster_operator_info['related'] is None:
            return None

        namespaces = []
        for related in cluster_operator_info['related']:
            if related['resource'] == 'namespaces':
                namespaces.append(
                    related['name']
                )

        names = []
        names.append(cluster_operator_info['name'])
        names.append('openshift-%s' % (cluster_operator_info['name']))
        names.append('%s-operator' % (cluster_operator_info['name']))
        names.append('openshift-%s-operator' % (cluster_operator_info['name']))
        names.append('cluster-%s-operator' % (cluster_operator_info['name']))

        if cluster_operator_info['name'] == 'openshift-samples':
            names.append('cluster-samples-operator')

        app_label_map = {}
        app_label_map['operator-lifecycle-manager'] = 'olm-operator'
        app_label_map['operator-lifecycle-manager-catalog'] = 'catalog-operator'
        app_label_map['operator-lifecycle-manager-packageserver'] = 'package-server-manager'

        for deployment in deployments:
            if deployment['owner_kind'] != 'ClusterVersion':
                continue

            if cluster_operator_info['name'] in app_label_map:
                for label in deployment['label']:
                    if label == 'app':
                        if deployment['label'][label] == app_label_map[cluster_operator_info['name']]:
                            return deployment

            if deployment['namespace'] not in namespaces:
                continue

            if deployment['name'] not in names:
                continue

            return deployment

        return None

    def get_cluster_operator_related_deployments(self, cluster_operator_info, deployments):
        related = []

        for deployment in deployments:
            for label in deployment['label']:
                if label == 'app.kubernetes.io/managed-by':
                    if deployment['label'][label] == cluster_operator_info['co_deployment']['name']:
                        related.append(
                            deployment
                        )
                        continue

        return related

    def get_cluster_operators(self, object_filter=None, return_mo=False, deployment_info=False, cache_enabled=True):
        all_cluster_operators = self.get_cluster_operators_info(cache_enabled=cache_enabled)
        if all_cluster_operators is None:
            return None

        cluster_operators = []

        if deployment_info:
            deployments = self.get_deployments()

        for cluster_operator_info in all_cluster_operators:
            if not self.match_cluster_operator(cluster_operator_info['info'], object_filter):
                continue

            if return_mo:
                cluster_operators.append(
                    cluster_operator_info['mo']
                )
                continue

            if deployment_info:
                cluster_operator_info['info']['co_deployment'] = None
                cluster_operator_info['info']['related_deployment'] = None

                cluster_operator_deployment = self.get_cluster_operator_deployment(
                    cluster_operator_info['info'],
                    deployments
                )
                if cluster_operator_deployment is not None:
                    cluster_operator_info['info']['co_deployment'] = {}
                    cluster_operator_info['info']['co_deployment']['namespace'] = cluster_operator_deployment['namespace']
                    cluster_operator_info['info']['co_deployment']['name'] = cluster_operator_deployment['name']
                    cluster_operator_related_deployments = self.get_cluster_operator_related_deployments(
                        cluster_operator_info['info'],
                        deployments
                    )
                    if cluster_operator_related_deployments is not None:
                        cluster_operator_info['info']['related_deployment'] = []
                        for related_deployment in cluster_operator_related_deployments:
                            item = {}
                            item['namespace'] = related_deployment['namespace']
                            item['name'] = related_deployment['name']
                            cluster_operator_info['info']['related_deployment'].append(
                                item
                            )

            cluster_operators.append(
                cluster_operator_info['info']
            )

        return cluster_operators
