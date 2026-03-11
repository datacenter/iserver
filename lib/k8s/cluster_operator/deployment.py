class K8sClusterOperatorDeployment():
    def __init__(self):
        pass

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
