from lib import ip_helper


class K8sCertificateInfo():
    def __init__(self):
        self.certificate = None

    def get_certificate_info(self, managed_object):
        if managed_object is None:
            return None

        info = self.get_base_info(managed_object)
        info['secret'] = self.get(info, 'spec:secretName')
        info['secretT'] = self.get(managed_object, 'spec:secretName')
        info['issuerT'] = self.get(managed_object, 'spec:issuerRef', on_error={}, on_none={}, cast='json2txt').split('\n')
        info['timerT'] = []
        info['timerT'].append('Not before: %s' % (self.get(managed_object, 'status:notBefore')))
        info['timerT'].append('Not after : %s' % (self.get(managed_object, 'status:notAfter')))
        info['timerT'].append('Renewal   : %s' % (self.get(managed_object, 'status:renewalTime')))
        info = self.add_tick(
            info, 
            'Ready', 
            'True', 
            'readyT', 
            bool_attribute='ready',
            condition=True
        )
        return info
    
    def get_certificates(self, object_filter=None, secret_info=False, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'certificate', 
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
                info['namespace'],
                self.get(info, 'spec:secretName'),
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

    def get_certificate(self, namespace, name, secret_info=False, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'certificate', 
            name,
            namespace=namespace,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized,
            secret_info=secret_info
        )

    def is_certificate(self, namespace, name, cache_enabled=True, optimized=True):
        if self.get_certificate(namespace, name, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True

    def is_any_certificate(self, cache_enabled=True):
        infos = self.get_certificates(cache_enabled=cache_enabled)
        if infos is None or len(infos) == 0:
            return False
        return True