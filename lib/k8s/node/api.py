import time
import traceback


class K8sNodeApi():
    def __init__(self):
        self.node_mo = None

    def get_node_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.node_mo is not None:
                return self.node_mo

        api_handler = self.get_api()
        if api_handler is None:
            return None

        # https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1NodeList.md
        try:
            start_time = int(time.time() * 1000)
            response = api_handler.list_node(
                timeout_seconds=self.api_timeout_seconds
            )
            self.log.k8s(
                'get',
                'node',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s_nodes.get_nodes', traceback.format_exc())
            self.log.k8s(
                'get',
                'node',
                True,
                int(time.time() * 1000) - start_time
            )
            return False

        self.node_mo = []
        for item in response.items:
            node_mo = self.convert_object(item.to_dict())
            self.node_mo.append(
                node_mo
            )

        self.log.k8s_mo(
            'node',
            self.node_mo
        )

        return self.node_mo
