import time
import traceback


class K8sNodeFeatureApi():
    def __init__(self):
        self.node_feature_mo = None

    def get_node_feature_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.node_feature_mo is not None:
                return self.node_feature_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='nfd.openshift.io/v1alpha1',
                kind='NodeFeature'
            )
            self.node_feature_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'node_feature',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_node_feature_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'node_feature',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'node_feature',
            self.node_feature_mo
        )

        return self.node_feature_mo
