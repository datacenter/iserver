import time
import traceback


class K8sNmstateApi():
    def __init__(self):
        self.nmstate_mo = None

    def get_nmstate_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nmstate_mo is not None:
                return self.nmstate_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='nmstate.io/v1',
                kind='NMState'
            )
            self.nmstate_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nmstate',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nmstate_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nmstate',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nmstate',
            self.nmstate_mo
        )

        return self.nmstate_mo

    def create_nmstate_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nmstate.io/v1', kind='NMState')
            success = True
            response = obj_list.create(
                body=body
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_nmstate', traceback.format_exc())

        self.log.ocp(
            'create',
            'nmstate',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nmstate_mo(self, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='nmstate.io/v1', kind='NMState')
            success = True
            response = obj_list.delete(
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_nmstate', traceback.format_exc())

        self.log.ocp(
            'delete',
            'nmstate',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
