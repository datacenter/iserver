import time
import traceback


class K8sMigrationApi():
    def __init__(self):
        self.migration_mo = None

    def get_migration_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.migration_mo is not None:
                return self.migration_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='forklift.konveyor.io/v1beta1',
                kind='Migration'
            )
            self.migration_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'migration',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_migration_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'migration',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'migration',
            self.migration_mo
        )

        return self.migration_mo

    def create_migration_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Migration')
            success = True
            response = obj_list.create(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_migration', traceback.format_exc())

        self.log.ocp(
            'create',
            'migration',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def replace_migration_mo(self, body):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Migration')
            success = True
            response = obj_list.replace(
                body=body,
                namespace=body['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.replace_migration_mo', traceback.format_exc())

        self.log.ocp(
            'replace',
            'migration',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    
    def delete_migration_mo(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='forklift.konveyor.io/v1beta1', kind='Migration')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_migration_mo', traceback.format_exc())

        self.log.ocp(
            'delete',
            'migration',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
    