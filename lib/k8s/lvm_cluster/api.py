import time
import traceback


class K8sLvmClusterApi():
    def __init__(self):
        self.lvm_cluster_mo = None

    def get_lvm_cluster_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.lvm_cluster_mo is not None:
                return self.lvm_cluster_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='lvm.topolvm.io/v1alpha1',
                kind='LVMCluster'
            )
            self.lvm_cluster_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'lvm_cluster',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_lvm_cluster_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'lvm_cluster',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'lvm_cluster',
            self.lvm_cluster_mo
        )

        return self.lvm_cluster_mo

    def create_lvm_cluster_mo(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='lvm.topolvm.io/v1alpha1', kind='LVMCluster')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_lvm_cluster_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'lvm_cluster',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_lvm_cluster_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='lvm.topolvm.io/v1alpha1', kind='LVMCluster')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_lvm_cluster', traceback.format_exc())

        self.log.ocp(
            'delete',
            'lvm_cluster',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def set_lvm_cluster_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='lvm.topolvm.io/v1alpha1', kind='LVMCluster')
            response = obj_list.replace(
                body=body
            )
            self.log.k8s(
                'set',
                'lvm_cluster',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.lvm_cluster', traceback.format_exc())
            self.log.k8s(
                'set',
                'lvm_cluster',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True
