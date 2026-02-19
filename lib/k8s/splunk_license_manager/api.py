import time
import traceback


class K8sSplunkLicenseManagerApi():
    def __init__(self):
        self.splunk_license_manager_mo = None

    def get_splunk_license_manager_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.splunk_license_manager_mo is not None:
                return self.splunk_license_manager_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='enterprise.splunk.com/v4',
                kind='LicenseManager'
            )
            self.splunk_license_manager_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'splunk_license_manager',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_splunk_license_manager_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'splunk_license_manager',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'splunk_license_manager',
            self.splunk_license_manager_mo
        )

        return self.splunk_license_manager_mo

    def create_splunk_license_manager_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='enterprise.splunk.com/v4', kind='LicenseManager')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_splunk_license_manager_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'splunk_license_manager',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
