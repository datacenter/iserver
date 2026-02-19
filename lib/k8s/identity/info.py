from lib import filter_helper


class K8sIdentityInfo():
    def __init__(self):
        self.identity = None

    def get_identity_info(self, identity_mo):
        if identity_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        metadata_info = self.get_metadata_info(
            identity_mo
        )
        info.update(metadata_info)

        info['groups'] = self.get(identity_mo, 'groups')
        info['identities'] = self.get(identity_mo, 'identities')
        return info

    def get_identities_info(self, cache_enabled=True):
        if cache_enabled:
            if self.identity is not None:
                return self.identity

        managed_objects = self.get_identity_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.identity = []
        for managed_object in managed_objects:
            identity_info = {}
            identity_info['info'] = self.get_identity_info(
                managed_object
            )
            identity_info['mo'] = managed_object
            self.identity.append(
                identity_info
            )

        return self.identity

    def match_identity(self, identity_info, identity_filter):
        if identity_filter is None or len(identity_filter) == 0:
            return True

        for ap_rule in identity_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, identity_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_identity',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_identities(self, object_filter=None, return_mo=False, cache_enabled=True):
        all_identities = self.get_identities_info(cache_enabled=cache_enabled)
        if all_identities is None:
            return None

        identities = []

        for identity_info in all_identities:
            if not self.match_identity(identity_info['info'], object_filter):
                continue

            if return_mo:
                identities.append(
                    identity_info['mo']
                )
                continue

            identities.append(
                identity_info['info']
            )

        return identities

    def get_identity(self, name, return_mo=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        identities = self.get_identities(
            object_filter=object_filter,
            return_mo=return_mo,
            cache_enabled=cache_enabled
        )

        if identities is None:
            return None

        if len(identities) == 1:
            return identities[0]

        return None

    def is_identity(self, name, return_mo=False, cache_enabled=True):
        if self.get_identity(name, return_mo=return_mo, cache_enabled=cache_enabled) is None:
            return False
        return True
