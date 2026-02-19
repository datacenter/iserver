from lib import filter_helper


class K8sPackageInfo():
    def __init__(self):
        self.package = None

    def get_package_info(self, package_mo):
        if package_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            package_mo
        )
        info.update(metadata_info)

        info['status'] = package_mo['status']
        info['catalog'] = filter_helper.get_attr(package_mo, 'metadata:labels:catalog')

        info['info'] = {}
        info['info']['channel'] = filter_helper.get_attr(package_mo, 'status:defaultChannel')
        info['info']['version'] = None
        info['info']['description'] = None
        if info['info']['channel'] is not None:
            channels = filter_helper.get_attr(package_mo, 'status:channels')
            if channels is not None:
                for channel in channels:
                    if channel['name'] == info['info']['channel']:
                        info['info']['version'] = filter_helper.get_attr(channel, 'currentCSV')
                        info['info']['description'] = filter_helper.get_attr(channel, 'currentCSVDesc:annotations:description')

        return info

    def get_packages_info(self, cache_enabled=True):
        if cache_enabled:
            if self.package is not None:
                return self.package

        managed_objects = self.get_package_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.package = []
        for managed_object in managed_objects:
            package_info = {}
            package_info['info'] = self.get_package_info(
                managed_object
            )
            package_info['mo'] = managed_object
            self.package.append(
                package_info
            )

        return self.package

    def match_package(self, package_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, package_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (package_info['namespace'], package_info['name'])):
                    return False

            if key == 'catalog':
                key_found = True
                if not filter_helper.match_string(value, package_info['catalog']):
                    return False

            if key == 'installed':
                key_found = True
                if 'installed' not in package_info['info']:
                    return False

                if value == 'true' and not package_info['info']['installed']:
                    return False

                if value == 'false' and package_info['info']['installed']:
                    return False

            if not key_found:
                self.log.error(
                    'match_package',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_packages(self, object_filter=None, return_mo=False, cache_enabled=True, subscription_info=False):
        all_packages = self.get_packages_info(cache_enabled=cache_enabled)
        if all_packages is None:
            return None

        packages = []

        for package_info in all_packages:
            if subscription_info:
                package_info['info']['info']['installed'] = self.is_subscription_by_package(
                    package_info['info']['name']
                )

            if not self.match_package(package_info['info'], object_filter):
                continue

            if return_mo:
                packages.append(
                    package_info['mo']
                )
                continue

            packages.append(
                package_info['info']
            )

        if not return_mo:
            packages = sorted(
                packages,
                key=lambda i: (
                    i['namespace'],
                    i['name']
                )
            )

        return packages

    def is_package(self, namespace, name, cache_enabled=True):
        if self.get_package(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_package(self, name, namespace=None, catalog=None, return_mo=False, cache_enabled=True):
        object_filter = []
        if namespace is not None:
            object_filter.append(
                'namespace:%s' % (namespace)
            )

        if catalog is not None:
            object_filter.append(
                'catalog:%s' % (catalog)
            )

        object_filter.append(
            'name:%s' % (name)
        )
        packages = self.get_packages(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if packages is None:
            return None

        if len(packages) == 1:
            return packages[0]

        return None

    def get_package_channel(self, package_name, channel_name):
        try:
            package_info = self.get_package(package_name)
            for channel in package_info['status']['channels']:
                if channel['name'] == channel_name:
                    return channel
        except BaseException:
            pass

        return None
