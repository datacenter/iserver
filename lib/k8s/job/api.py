import time
import traceback


class K8sJobApi():
    def __init__(self):
        self.job_mo = None

    def get_job_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.job_mo is not None:
                return self.job_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='batch/v1',
                kind='Job'
            )
            self.job_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'job',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_job_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'job',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'job',
            self.job_mo
        )

        return self.job_mo

    def delete_job_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='batch/v1', kind='Job')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_job', traceback.format_exc())

        self.log.ocp(
            'delete',
            'job',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
