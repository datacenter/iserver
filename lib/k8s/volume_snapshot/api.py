import time
import traceback


class K8sVolumeSnapshotApi():
    def __init__(self):
        self.volume_snapshot_mo = None

    def get_volume_snapshot_mo(self, cache_enabled=True):
        if cache_enabled:
            if self.volume_snapshot_mo is not None:
                return self.volume_snapshot_mo

        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return None

        try:
            start_time = int(time.time() * 1000)
            response = api_handler.resources.get(
                api_version='snapshot.storage.k8s.io/v1',
                kind='VolumeSnapshot'
            )
            self.volume_snapshot_mo = response.get().to_dict()['items']
            self.log.k8s(
                'get',
                'volume_snapshot',
                True,
                int(time.time() * 1000) - start_time
            )

        except BaseException:
            self.log.error('k8s.get_volume_snapshot_mo', traceback.format_exc())
            self.log.k8s(
                'get',
                'volume_snapshot',
                True,
                int(time.time() * 1000) - start_time
            )
            print(traceback.format_exc())
            return None

        self.log.k8s_mo(
            'volume_snapshot',
            self.volume_snapshot_mo
        )

        return self.volume_snapshot_mo

    def create_volume_snapshot(self, policy):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='snapshot.storage.k8s.io/v1', kind='VolumeSnapshot')
            success = True
            response = obj_list.create(
                body=policy,
                namespace=policy['metadata']['namespace'],
            )
        except BaseException:
            success = False
            self.log.error('ocp.create_volume_snapshot', traceback.format_exc())

        self.log.ocp(
            'create',
            'volume_snapshot',
            success,
            int(time.time() * 1000) - start_time
        )

        return success

    def delete_volume_snapshot(self, namespace, name):
        api_handler = self.get_api(cluster_type='ocp')
        if api_handler is None:
            return False

        try:
            start_time = int(time.time() * 1000)
            obj_list = api_handler.resources.get(api_version='snapshot.storage.k8s.io/v1', kind='VolumeSnapshot')
            success = True
            response = obj_list.delete(
                namespace=namespace,
                name=name
            )
        except BaseException:
            success = False
            self.log.error('ocp.delete_volume_snapshot', traceback.format_exc())

        self.log.ocp(
            'delete',
            'volume_snapshot',
            success,
            int(time.time() * 1000) - start_time
        )

        return success
