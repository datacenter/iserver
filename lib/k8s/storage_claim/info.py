from lib import filter_helper


class K8sStorageClaimInfo():
    def __init__(self):
        self.storage_claim = None

    def get_storage_claim_info(self, storage_claim_mo):
        if storage_claim_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            storage_claim_mo
        )
        info.update(metadata_info)

        info['spec'] = self.get(storage_claim_mo, 'spec')
        info['status'] = self.get(storage_claim_mo, 'status')
        return info

    def get_storage_claims_info(self, cache_enabled=True):
        if cache_enabled:
            if self.storage_claim is not None:
                return self.storage_claim

        managed_objects = self.get_storage_claim_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.storage_claim = []
        for managed_object in managed_objects:
            storage_claim_info = {}
            storage_claim_info['info'] = self.get_storage_claim_info(
                managed_object
            )
            storage_claim_info['mo'] = managed_object
            self.storage_claim.append(
                storage_claim_info
            )

        return self.storage_claim

    def match_storage_claim(self, storage_claim_info, object_filter):
        if object_filter is None or len(object_filter) == 0:
            return True

        for rule in object_filter:
            (key, value) = rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, storage_claim_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_storage_claim',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_storage_claims(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_storage_claims = self.get_storage_claims_info(cache_enabled=cache_enabled)
        if all_storage_claims is None:
            return None

        storage_claims = []

        for storage_claim_info in all_storage_claims:
            if not self.match_storage_claim(storage_claim_info['info'], object_filter):
                continue

            if return_mo:
                storage_claims.append(
                    storage_claim_info['mo']
                )
                continue

            storage_claims.append(
                storage_claim_info['info']
            )

        return storage_claims

    def is_storage_claim(self, name, cache_enabled=True):
        if self.get_storage_claim(name, cache_enabled=cache_enabled) is None:
            return False
        return True

    def get_storage_claim(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        storage_claims = self.get_storage_claims(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )
        if storage_claims is None:
            return None

        if len(storage_claims) == 1:
            return storage_claims[0]

        return None
