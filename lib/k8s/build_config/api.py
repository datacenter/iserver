import time
import traceback


class K8sBuildConfigApi():
    def __init__(self):
        self.build_config_mo = None

    def get_build_config_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.build_config_mo is not None:
                return self.build_config_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='build.openshift.io/v1',
                kind='BuildConfig'
            )
            self.build_config_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'build_config',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_build_config_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'build_config',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'build_config',
            self.build_config_mo
        )

        return self.build_config_mo
    
    def delete_build_config_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='build.openshift.io/v1', kind='BuildConfig')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_build_config_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_build_config',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
