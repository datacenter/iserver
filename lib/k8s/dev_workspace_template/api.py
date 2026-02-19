import time
import traceback


class K8sDevWorkspaceTemplateApi():
    def __init__(self):
        self.dev_workspace_template_mo = None

    def get_dev_workspace_template_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.dev_workspace_template_mo is not None:
                return self.dev_workspace_template_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='workspace.devfile.io/v1alpha2',
                kind='DevWorkspaceTemplate'
            )
            self.dev_workspace_template_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'dev_workspace_template',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_dev_workspace_template_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'dev_workspace_template',
                True,
                int(time.time() * 1000) - start_time
            )
            return None

        self.log.k8s_mo(
            'dev_workspace_template',
            self.dev_workspace_template_mo
        )

        return self.dev_workspace_template_mo

    def delete_dev_workspace_template_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='workspace.devfile.io/v1alpha2', kind='DevWorkspaceTemplate')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_dev_workspace_template_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_dev_workspace_template',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
