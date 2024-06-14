from lib import filter_helper


class K8sSecretInfo():
    def __init__(self):
        self.secret = None

    def get_secret_info(self, secret_mo):
        if secret_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            secret_mo
        )
        info.update(metadata_info)

        return info

    def get_secrets_info(self, cache_enabled=True):
        if cache_enabled:
            if self.secret is not None:
                return self.secret

        managed_objects = self.get_secret_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.secret = []
        for managed_object in managed_objects:
            secret_info = {}
            secret_info['info'] = self.get_secret_info(
                managed_object
            )
            secret_info['mo'] = managed_object
            self.secret.append(
                secret_info
            )

        return self.secret

    def match_secret(self, secret_info, secret_filter):
        if secret_filter is None or len(secret_filter) == 0:
            return True

        for ap_rule in secret_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if not key_found:
                self.log.error(
                    'match_secret',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_secrets(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_secrets = self.get_secrets_info(cache_enabled=cache_enabled)
        if all_secrets is None:
            return None

        secrets = []

        for secret_info in all_secrets:
            if not self.match_secret(secret_info['info'], object_filter):
                continue

            if return_mo:
                secrets.append(
                    secret_info['mo']
                )
                continue

            secrets.append(
                secret_info['info']
            )

        return secrets
