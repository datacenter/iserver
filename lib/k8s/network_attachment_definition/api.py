import time
import traceback


class K8sNetworkAttachmentDefinitionApi():
    def __init__(self):
        self.nad_mo = None

    def get_nad_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nad_mo is not None:
                return self.nad_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='k8s.cni.cncf.io/v1',
                kind='NetworkAttachmentDefinition'
            )
            self.nad_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nad',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nad_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nad',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nad',
            self.nad_mo
        )

        return self.nad_mo

    def create_nad(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='k8s.cni.cncf.io/v1', kind='NetworkAttachmentDefinition')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_ocp_nad', traceback.format_exc())

        self.log.ocp(
            'create',
            'nad',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nad(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='k8s.cni.cncf.io/v1', kind='NetworkAttachmentDefinition')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_ocp_nad', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_ocp_nad',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
