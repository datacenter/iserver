import time
import traceback


class K8sNodeFeatureDiscoveryApi():
    def __init__(self):
        self.node_feature_discovery_mo = None

    def get_node_feature_discovery_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.node_feature_discovery_mo is not None:
                return self.node_feature_discovery_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='nfd.openshift.io/v1',
                kind='NodeFeatureDiscovery'
            )
            self.node_feature_discovery_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'node_feature_discovery',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_node_feature_discovery_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'node_feature_discovery',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'node_feature_discovery',
            self.node_feature_discovery_mo
        )

        return self.node_feature_discovery_mo

    def create_node_feature_discovery_mo(self, node_feature_discovery):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nfd.openshift.io/v1', kind='NodeFeatureDiscovery')
            success = True
            response = obj_list.create(
                body=node_feature_discovery,
                namespace=node_feature_discovery['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_node_feature_discovery_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'node_feature_discovery',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_node_feature_discovery_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nfd.openshift.io/v1', kind='NodeFeatureDiscovery')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_node_feature_discovery_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_node_feature_discovery',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
