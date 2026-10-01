from lib import ip_helper


class K8sClusterIssuerInfo():
    def __init__(self):
        self.cluster_issuer = None
        self.cluster_issuer_namespace = 'cert-manager'

    def get_cluster_issuer_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['secret'] = self.get(managed_object, 'spec:ca:secretName')
        info['secretT'] = self.get(managed_object, 'spec:ca:secretName')
        info = self.add_tick(
            info, 
            'Ready', 
            'True', 
            'readyT', 
            bool_attribute='ready',
            condition=True
        )
        return info

    def get_cluster_issuers(self, object_filter=None, secret_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'cluster_issuer', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )

        if infos is None:
            return None
        
        if not secret_info:
            return infos
        
        for info in infos:
            info['crt'] = None
            info['crtT'] = None
            secret_mo = self.get_secret(
                self.cluster_issuer_namespace,
                self.get(info, 'spec:ca:secretName'),
                return_mo=True
            )
            if secret_mo is None:
                info['secretT'] = '\u2717 %s' % (info['secretT'])
            else:
                info['secretT'] = '\u2713 %s' % (info['secretT'])
                info['crt'] = ip_helper.get_cert_info(
                    ip_helper.decode_text_64(self.get(secret_mo, 'data:tls.crt')).encode('utf-8')
                )
                info['crtT'] = self.get(info, 'crt', on_error={}, on_none={}, cast='json2txt').split('\n')

        return infos

    def is_cluster_issuer(self, name, cache_enabled=True, optimized=True):
        if self.get_cluster_issuer(name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def get_cluster_issuer(self, name, secret_info=False, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'cluster_issuer', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized,
            secret_info=secret_info
        )