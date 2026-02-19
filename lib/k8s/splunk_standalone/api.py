import time
import traceback


class K8sSplunkStandaloneApi():
    def __init__(self):
        self.splunk_standalone_mo = None

    def get_splunk_standalone_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.splunk_standalone_mo is not None:
                return self.splunk_standalone_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='enterprise.splunk.com/v4',
                kind='Standalone'
            )
            self.splunk_standalone_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'splunk_standalone',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_splunk_standalone_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'splunk_standalone',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'splunk_standalone',
            self.splunk_standalone_mo
        )

        return self.splunk_standalone_mo

    def create_splunk_standalone_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='enterprise.splunk.com/v4', kind='Standalone')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_splunk_standalone', traceback.format_exc())

        self.log.ocp(
            'create',
            'splunk_standalone',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_splunk_standalone_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='enterprise.splunk.com/v4', kind='Standalone')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_splunk_standalone_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'splunk_standalone',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_splunk_standalone_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='enterprise.splunk.com/v4', kind='Standalone')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_splunk_standalone_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'splunk_standalone',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    