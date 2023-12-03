import time
import traceback


class K8sNodeNetworkConfigurationEnactmentApi():
    def __init__(self):
        self.node_network_configuration_enactment_mo = None

    def get_node_network_configuration_enactment_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.node_network_configuration_enactment_mo is not None:
                return self.node_network_configuration_enactment_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='nmstate.io/v1beta1',
                kind='NodeNetworkConfigurationEnactment'
            )
            self.node_network_configuration_enactment_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'node_network_configuration_enactment',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_node_network_configuration_enactment_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'node_network_configuration_enactment',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'node_network_configuration_enactment',
            self.node_network_configuration_enactment_mo
        )

        return self.node_network_configuration_enactment_mo
