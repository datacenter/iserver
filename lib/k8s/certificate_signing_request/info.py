from lib import ip_helper


class K8sCsrInfo():
    def __init__(self):
        self.csr = None

    def get_csr_info(self, managed_object):
        if managed_object is None:
            return None
        
        info = self.get_base_info(
            managed_object,
            condition_table=True
        )

        info['csr'] = self.get(managed_object, 'spec:request')
        info['csr_info'] = ip_helper.get_csr_info(ip_helper.decode_text_64(info['csr']).encode('utf-8'))
        info['signer'] = self.get(managed_object, 'spec:signerName')
        info['username'] = self.get(managed_object, 'spec:username')
        info['usage'] = self.get(managed_object, 'spec:usages', on_error=[], on_none=[])
        info['usageT'] = ','.join(info['usage'])
        info['group'] = self.get(managed_object, 'spec:groups', on_error=[], on_none=[])
        info['groupT'] = ','.join(info['group'])

        info['pending'] = True
        info['approved'] = False
        info['issued'] = False
        info['flag'] = []

        for condition in info['condition']:
            if condition['type'] == 'Approved':
                info['approved'] = True
                info['pending'] = False
                info['flag'].append('Approved')

        info['certificate'] = self.get(managed_object, 'status:certificate')
        info['certificate_info'] = None
        if info['certificate'] is not None:
            info['certificate_info'] = ip_helper.get_cert_info(ip_helper.decode_text_64(info['certificate']).encode('utf-8'))
            info['issued'] = True
            info['pending'] = False
            info['flag'].append('Issued')

        if not info['approved']:
            info['flag'].append('Pending')

        info['flagT'] = ','.join(info['flag'])

        return info

    def get_csrs(self, object_filter=None, return_mo=False, cache_enabled=True):
        infos = self.get_infos(
            'csr', 
            object_filter=object_filter, 
            return_mo=return_mo, 
            cache_enabled=cache_enabled
        )
        return infos

    def get_csr(self, name, return_mo=False, cache_enabled=True, optimized=True):
        return self.get_info(
            'csr', 
            name,
            return_mo=return_mo, 
            cache_enabled=cache_enabled,
            optimized=optimized
        )

    def is_csr(self, name, return_mo=False, cache_enabled=True, optimized=True):
        if self.get_csr(name, return_mo=return_mo, cache_enabled=cache_enabled, optimized=optimized) is None:
            return False
        return True