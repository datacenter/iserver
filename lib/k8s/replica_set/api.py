import time
import traceback


class K8sReplicaSetApi():
    def __init__(self):
        self.replica_set_mo = None

    def get_replica_set_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.replica_set_mo is not None:
                return self.replica_set_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps/v1',
                kind='ReplicaSet'
            )
            self.replica_set_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'replica_set',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_replica_set_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'replica_set',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'replica_set',
            self.replica_set_mo
        )

        return self.replica_set_mo
