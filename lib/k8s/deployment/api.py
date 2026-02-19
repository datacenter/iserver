import time
import traceback


class K8sDeploymentApi():
    def __init__(self):
        self.deployment_mo = None

    def get_deployment_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.deployment_mo is not None:
                return self.deployment_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='apps/v1',
                kind='Deployment'
            )
            self.deployment_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'deployment',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_deployment_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'deployment',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'deployment',
            self.deployment_mo
        )

        return self.deployment_mo

    def create_deployment_mo(self, body):
        api_handler = self.get_api(cluster_type='standard', api_type='apps')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.create_namespaced_deployment(
                body['metadata']['namespace'],
                body
            )

        except BaseException:
            self.log.error('k8s.create_deployment_mo', traceback.format_exc())
            self.log.k8s(
                'create',
                'deployment',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True

    def patch_deployment_mo(self, namespace, name, body):
        api_handler = self.get_api(cluster_type='standard', api_type='apps')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.patch_namespaced_deployment(
                name,
                namespace,
                body
            )

        except BaseException:
            self.log.error('k8s.patch_deployment_mo', traceback.format_exc())
            self.log.k8s(
                'patch',
                'deployment',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True

    def delete_deployment_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='standard', api_type='apps')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.delete_namespaced_deployment(
                name,
                namespace
            )

        except BaseException:
            self.log.error('k8s.delete_deployment_mo', traceback.format_exc())
            self.log.k8s(
                'delete',
                'deployment',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return False

        return True
    