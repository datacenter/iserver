import time
import traceback


class K8sNimBuildApi():
    def __init__(self):
        self.nim_build_mo = None

    def get_nim_build_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.nim_build_mo is not None:
                return self.nim_build_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps.nvidia.com/v1alpha1',
                kind='NIMBuild'
            )
            self.nim_build_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'nim_build',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_nim_build_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'nim_build',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'nim_build',
            self.nim_build_mo
        )

        return self.nim_build_mo

    def create_nim_build_mo(self, nim_build):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NIMBuild')
            success = True
            response = obj_list.create(
                body=nim_build,
                namespace=nim_build['metadata']['namespace']
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_nim_build_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'nim_build',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_nim_build_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='apps.nvidia.com/v1alpha1', kind='NIMBuild')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_nim_build_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_nim_build',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
