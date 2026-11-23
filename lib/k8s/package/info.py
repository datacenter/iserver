from lib import filter_helper


class K8sPackageInfo():
    def __init__(self):
        self.package = None

    def get_package_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['catalog'] = filter_helper.get_attr(managed_object, 'metadata:labels:catalog')
        info['channel'] = filter_helper.get_attr(managed_object, 'status:defaultChannel')
        info['version'] = None
        info['description'] = None
        if info['channel'] is not None:
            channels = filter_helper.get_attr(managed_object, 'status:channels')
            if channels is not None:
                for channel in channels:
                    if channel['name'] == info['channel']:
                        info['version'] = filter_helper.get_attr(channel, 'currentCSV')
                        info['description'] = filter_helper.get_attr(channel, 'currentCSVDesc:annotations:description')

        return info

    def get_packages(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'package', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos  

    def is_package(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_package(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_package_catalog(self, name, catalog, namespace=None, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append('name:%s' % (name))
        object_filter.append('catalog:%s' % (catalog))
        infos = self.get_infos(
            'package', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        if infos is None or len(infos) != 1:
            return None
        return infos[0]

    def get_package(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'package',
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )