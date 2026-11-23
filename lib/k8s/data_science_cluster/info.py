from lib import filter_helper


class K8sDataScienceClusterInfo():
    def __init__(self):
        self.data_science_cluster = None

    def get_data_science_cluster_info(self, managed_object):
        if managed_object is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            managed_object
        )
        info.update(metadata_info)

        info['spec'] = self.get(managed_object, 'spec')
        info['status'] = self.get(managed_object, 'status')

        info['release_name'] = self.get(managed_object, 'status:release:name')
        info['release_version'] = self.get(managed_object, 'status:release:version')
        info['release'] = None
        if info['release_name'] is not None and info['release_version'] is not None:
            info['release'] = '%s v%s' % (
                info['release_name'],
                info['release_version']
            )

        info['phase'] = self.get(managed_object, 'status:phase')
        if info['phase'] is not None and info['phase'].lower() == 'ready':
            info['ready'] = True
            info['readyTick'] = '\u2713'
            info['__Output']['phase'] = 'Green'
            info['__Output']['readyTick'] = 'Green'
        else:
            info['ready'] = False
            info['readyTick'] = '\u2717'
            info['__Output']['phase'] = 'Red'
            info['__Output']['readyTick'] = 'Red'

        info['conditions'] = self.get_conditions(
            self.get(managed_object, 'status:conditions')
        )
        
        info['url'] = self.get(managed_object, 'status:components:dashboard:url')
        info['component'] = []
        info['componentT'] = []
        info['componentReady'] = []
        info['componentNotReady'] = []
        info['disabled'] = []
        info['release_name'] = []
        info['release_version'] = []

        component_map = {}
        component_map['codeflare'] = 'Code Flare'
        component_map['dashboard'] = 'Dashboard'
        component_map['datasciencepipelines'] = 'Data Science Pipeline'
        component_map['feastoperator'] = 'Feast Operator'
        component_map['kserve'] = 'Kserver'
        component_map['kueue'] = 'Kqueue'
        component_map['llamastackoperator'] = 'Llama Stack Operator'
        component_map['modelmeshserving'] = 'Model Mesh Serving'
        component_map['modelregistry'] = 'Model Registry'
        component_map['ray'] = 'Ray'
        component_map['trainingoperator'] = 'Training Operator'
        component_map['trustyai'] = 'TrustyAI'
        component_map['workbenches'] = 'Workbench'

        condition_map = {}
        condition_map['codeflare'] = 'CodeFlareReady'
        condition_map['dashboard'] = 'DashboardReady'
        condition_map['datasciencepipelines'] = 'DataSciencePipelinesReady'
        condition_map['feastoperator'] = 'FeastOperatorReady'
        condition_map['kserve'] = 'KserveReady'
        condition_map['kueue'] = 'KueueReady'
        condition_map['llamastackoperator'] = 'LlamaStackOperatorReady'
        condition_map['modelmeshserving'] = 'ModelMeshServingReady'
        condition_map['modelregistry'] = 'ModelRegistryReady'
        condition_map['ray'] = 'RayReady'
        condition_map['trainingoperator'] = 'TrainingOperatorReady'
        condition_map['trustyai'] = 'TrustyAIReady'
        condition_map['workbenches'] = 'WorkbenchesReady'

        for component in component_map:
            item_mo = self.get(managed_object, 'status:components:%s' % (component))
            if item_mo is None or item_mo['managementState'] != 'Managed':
                info['disabled'].append(
                    component_map[component]
                )
                continue

            info['component'].append(
                component_map[component]
            )
            if condition_map[component] in info['conditions']:
                info['componentT'].append('\u2713 %s' % (component_map[component]))
                info['componentReady'].append(
                    component_map[component]
                )
            else:
                info['componentT'].append('\u2717 %s' % (component_map[component]))
                info['componentNotReady'].append(
                    component_map[component]
                )                

            if 'releases' in item_mo:
                for release_mo in item_mo['releases']:
                    info['release_name'].append(release_mo['name'])
                    info['release_version'].append(release_mo['version'])

        return info

    def get_data_science_clusters_info(self, cache_enabled=True):
        if cache_enabled:
            if self.data_science_cluster is not None:
                return self.data_science_cluster

        managed_objects = self.get_data_science_cluster_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.data_science_cluster = []
        for managed_object in managed_objects:
            data_science_cluster_info = {}
            data_science_cluster_info['info'] = self.get_data_science_cluster_info(
                managed_object
            )
            data_science_cluster_info['mo'] = managed_object
            self.data_science_cluster.append(
                data_science_cluster_info
            )

        return self.data_science_cluster

    def match_data_science_cluster(self, data_science_cluster_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, data_science_cluster_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_data_science_cluster',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_data_science_clusters(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_data_science_clusters = self.get_data_science_clusters_info(cache_enabled=cache_enabled)
        if all_data_science_clusters is None:
            return None

        data_science_clusters = []

        for data_science_cluster_info in all_data_science_clusters:
            if not self.match_data_science_cluster(data_science_cluster_info['info'], object_filter):
                continue

            if return_mo:
                data_science_clusters.append(
                    data_science_cluster_info['mo']
                )
                continue

            data_science_clusters.append(
                data_science_cluster_info['info']
            )

        return data_science_clusters

    def is_data_science_cluster(self, name, cache_enabled=True):
        if self.get_data_science_cluster(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def is_any_data_science_cluster(self, cache_enabled=True):
        policies = self.get_data_science_clusters(cache_enabled=cache_enabled)
        if policies is None or len(policies) == 0:
            return False
        return True

    def get_data_science_cluster(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        data_science_clusters = self.get_data_science_clusters(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if data_science_clusters is None:
            return None

        if len(data_science_clusters) == 1:
            return data_science_clusters[0]

        return None
