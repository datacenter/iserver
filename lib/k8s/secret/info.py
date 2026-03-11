from lib import ip_helper


class K8sSecretInfo():
    def __init__(self):
        self.secret = None

    def get_secret_info(self, managed_object):
        info = self.get_base_info(
            managed_object
        )
        return info

    def get_secrets(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'secret', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_secret(self, namespace, name, return_mo=False, cache_enabled=True):
        return self.get_info(
            'secret', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

    def is_secret(self, namespace, name, cache_enabled=True):
        if self.get_secret(namespace, name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def generate_secret_name(self, namespace, name=None):
        if name is None:
            return ip_helper.get_short_uuid()

        if not self.is_secret(namespace, name, cache_enabled=False):
            return name
        
        return 'name-%s' % (ip_helper.get_short_uuid())
