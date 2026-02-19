import time
import traceback


class K8sNimPipelineApi():
    def __init__(self):
        self.nim_pipeline_mo = None

    def get_nim_pipeline_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_pipeline_mo is not None:
                return self.nim_pipeline_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps.nvidia.com/v1alpha1',
                kind='NIMPipeline'
            )
            self.nim_pipeline_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nim_pipeline',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nim_pipeline_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nim_pipeline',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nim_pipeline',
            self.nim_pipeline_mo
        )

        return self.nim_pipeline_mo

    def create_nim_pipeline_mo(self, nim_pipeline):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NIMPipeline')
            success = True
            response = obj_list.create(
                body=nim_pipeline,
                namespace=nim_pipeline['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_nim_pipeline_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'nim_pipeline',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nim_pipeline_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NIMPipeline')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_nim_pipeline_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_nim_pipeline',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
