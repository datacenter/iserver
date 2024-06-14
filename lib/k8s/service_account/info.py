from lib import filter_helper


class K8sServiceAccountInfo():
    def __init__(self):
        self.service_account = None

    def get_service_account_info(self, service_account_mo):
        if service_account_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            service_account_mo
        )
        info.update(metadata_info)

        info['secret'] = self.get(service_account_mo, 'secrets', on_error=[], on_none=[])
        info['secretCount'] = len(info['secret'])

        return info

    def get_service_accounts_info(self, cache_enabled=True):
        if cache_enabled:
            if self.service_account is not None:
                return self.service_account

        managed_objects = self.get_service_account_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.service_account = []
        for managed_object in managed_objects:
            service_account_info = {}
            service_account_info['info'] = self.get_service_account_info(
                managed_object
            )
            service_account_info['mo'] = managed_object
            self.service_account.append(
                service_account_info
            )

        return self.service_account

    def match_service_account(self, service_account_info, service_account_filter):
        if service_account_filter is None or len(service_account_filter) == 0:
            return True

        for ap_rule in service_account_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'namespace':
                key_found = True
                if not filter_helper.match_string(value, service_account_info['namespace']):
                    return False

            if key == 'name':
                key_found = True
                if not filter_helper.match_namespace_name(value, '%s/%s' % (service_account_info['namespace'], service_account_info['name'])):
                    return False

            if not key_found:
                self.log.error(
                    'match_service_account',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_service_accounts(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_service_accounts = self.get_service_accounts_info(cache_enabled=cache_enabled)
        if all_service_accounts is None:
            return None

        service_accounts = []

        for service_account_info in all_service_accounts:
            if not self.match_service_account(service_account_info['info'], object_filter):
                continue

            if return_mo:
                service_accounts.append(
                    service_account_info['mo']
                )
                continue

            service_accounts.append(
                service_account_info['info']
            )

        return service_accounts
