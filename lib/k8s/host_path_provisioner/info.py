from lib import filter_helper


class K8sHostPathProvisionerInfo():
    def __init__(self):
        self.host_path_provisioner = None

    def get_host_path_provisioner_info(self, host_path_provisioner_mo):
        if host_path_provisioner_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            host_path_provisioner_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(host_path_provisioner_mo, 'spec')
        info['status'] = self.get(host_path_provisioner_mo, 'status')
        return info

    def get_host_path_provisioners_info(self, cache_enabled=True):
        if cache_enabled:
            if self.host_path_provisioner is not None:
                return self.host_path_provisioner

        managed_objects = self.get_host_path_provisioner_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.host_path_provisioner = []
        for managed_object in managed_objects:
            host_path_provisioner_info = {}
            host_path_provisioner_info['info'] = self.get_host_path_provisioner_info(
                managed_object
            )
            host_path_provisioner_info['mo'] = managed_object
            self.host_path_provisioner.append(
                host_path_provisioner_info
            )

        return self.host_path_provisioner

    def match_host_path_provisioner(self, host_path_provisioner_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, host_path_provisioner_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_host_path_provisioner',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_host_path_provisioners(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_host_path_provisioners = self.get_host_path_provisioners_info(cache_enabled=cache_enabled)
        if all_host_path_provisioners is None:
            return None

        host_path_provisioners = []

        for host_path_provisioner_info in all_host_path_provisioners:
            if not self.match_host_path_provisioner(host_path_provisioner_info['info'], object_filter):
                continue

            if return_mo:
                host_path_provisioners.append(
                    host_path_provisioner_info['mo']
                )
                continue

            host_path_provisioners.append(
                host_path_provisioner_info['info']
            )

        return host_path_provisioners

    def is_host_path_provisioner(self, name, cache_enabled=True):
        if self.get_host_path_provisioner(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_host_path_provisioner(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        host_path_provisioners = self.get_host_path_provisioners(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if host_path_provisioners is None:
            return None

        if len(host_path_provisioners) == 1:
            return host_path_provisioners[0]

        return None
