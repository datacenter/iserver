import time
import traceback


class K8sReplicationControllerApi():
    def __init__(self):
        self.replication_controller_mo = None

    def get_replication_controller_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.replication_controller_mo is not None:
                return self.replication_controller_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='v1',
                kind='ReplicationController'
            )
            self.replication_controller_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'replication_controller',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_replication_controller_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'replication_controller',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'replication_controller',
            self.replication_controller_mo
        )

        return self.replication_controller_mo
