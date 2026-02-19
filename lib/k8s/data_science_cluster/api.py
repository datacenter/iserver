import time
import traceback


class K8sDataScienceClusterApi():
    def __init__(self):
        self.data_science_cluster_mo = None

    def get_data_science_cluster_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.data_science_cluster_mo is not None:
                return self.data_science_cluster_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='datasciencecluster.opendatahub.io/v1',
                kind='DataScienceCluster'
            )
            self.data_science_cluster_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'data_science_cluster',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_data_science_cluster_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'data_science_cluster',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'data_science_cluster',
            self.data_science_cluster_mo
        )

        return self.data_science_cluster_mo

    def create_data_science_cluster_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='datasciencecluster.opendatahub.io/v1', kind='DataScienceCluster')
            success = True
            response = obj_list.create(
                body=body
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_data_science_cluster_mo', traceback.format_exc())

        self.log.ocp(
            'create',
            'data_science_cluster',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_data_science_cluster_mo(self, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='datasciencecluster.opendatahub.io/v1', kind='DataScienceCluster')
            success = True
            response = obj_list.delete(
                name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_data_science_cluster_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'delete_data_science_cluster',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
