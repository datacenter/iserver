from lib import filter_helper


class K8sReplicationControllerInfo():
    def __init__(self):
        self.replication_controller = None

    def get_replication_controller_info(self, replication_controller_mo):
        if replication_controller_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            replication_controller_mo
        )
        info.update(metadata_info)

        return info

    def get_replication_controllers_info(self, cache_enabled=True):
        if cache_enabled:
            if self.replication_controller is not None:
                return self.replication_controller

        managed_objects = self.get_replication_controller_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.replication_controller = []
        for managed_object in managed_objects:
            replication_controller_info = {}
            replication_controller_info['info'] = self.get_replication_controller_info(
                managed_object
            )
            replication_controller_info['mo'] = managed_object
            self.replication_controller.append(
                replication_controller_info
            )

        return self.replication_controller

    def match_replication_controller(self, replication_controller_info, replication_controller_filter):
        if replication_controller_filter is None or len(replication_controller_filter) == 0:
            return True

        for ap_rule in replication_controller_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_replication_controller',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_replication_controllers(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_replication_controllers = self.get_replication_controllers_info(cache_enabled=cache_enabled)
        if all_replication_controllers is None:
            return None

        replication_controllers = []

        for replication_controller_info in all_replication_controllers:
            if not self.match_replication_controller(replication_controller_info['info'], object_filter):
                continue

            if return_mo:
                replication_controllers.append(
                    replication_controller_info['mo']
                )
                continue

            replication_controllers.append(
                replication_controller_info['info']
            )

        return replication_controllers
