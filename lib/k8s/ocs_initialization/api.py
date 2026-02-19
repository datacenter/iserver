import time
import traceback


class K8sOcsInitializationApi():
    def __init__(self):
        self.ocs_initialization_mo = None

    def get_ocs_initialization_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.ocs_initialization_mo is not None:
                return self.ocs_initialization_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='ocs.openshift.io/v1',
                kind='OCSInitialization'
            )
            self.ocs_initialization_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'ocs_initialization',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_ocs_initialization_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'ocs_initialization',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'ocs_initialization',
            self.ocs_initialization_mo
        )

        return self.ocs_initialization_mo

    def delete_ocs_initialization_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='ocs.openshift.io/v1', kind='OCSInitialization')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ocs_initialization', traceback.format_exc())

        self.log.ocp(
            'delete',
            'ocs_initialization',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
