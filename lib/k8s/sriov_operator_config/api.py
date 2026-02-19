import time
import traceback


class K8sSriovOperatorConfigApi():
    def __init__(self):
        self.sriov_operator_config_mo = None

    def get_sriov_operator_config_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.sriov_operator_config_mo is not None:
                return self.sriov_operator_config_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='sriovnetwork.openshift.io/v1',
                kind='SriovOperatorConfig'
            )
            self.sriov_operator_config_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'sriov_operator_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_sriov_operator_config_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'sriov_operator_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'sriov_operator_config',
            self.sriov_operator_config_mo
        )

        return self.sriov_operator_config_mo

    def create_sriov_operator_config_mo(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovOperatorConfig')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('k8s.create_sriov_operator_config_mo', traceback.format_exc())

        self.log.k8s(
            'create',
            'sriov_operator_config',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_sriov_operator_config_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='sriovnetwork.openshift.io/v1', kind='SriovOperatorConfig')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_sriov_operator_config', traceback.format_exc())

        self.log.ocp(
            'delete',
            'sriov_operator_config',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
