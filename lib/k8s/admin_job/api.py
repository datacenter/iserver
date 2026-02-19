import time
import traceback


class K8sAdminJobApi():
    def __init__(self):
        self.admin_job_mo = None

    def get_admin_job_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.admin_job_mo is not None:
                return self.admin_job_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='aistor.min.io/v1alpha1',
                kind='AdminJob'
            )
            self.admin_job_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'admin_job',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_admin_job_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'admin_job',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'admin_job',
            self.admin_job_mo
        )

        return self.admin_job_mo

    def create_admin_job_mo(self, admin_job):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='aistor.min.io/v1alpha1', kind='AdminJob')
            success = True
            response = obj_list.create(
                body=admin_job,
                namespace=admin_job['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_admin_job_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'admin_job',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_admin_job_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='aistor.min.io/v1alpha1', kind='AdminJob')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_admin_job_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_admin_job',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
