from lib import filter_helper


class ApplicationProfileInfo():
    def __init__(self):
        self.application_profile = None

    def get_application_profile_count(self, tenant_name=None):
        application_profile_filter = None
        if tenant_name is not None:
            application_profile_filter = ['tenant:%s' % (tenant_name)]

        application_profiles = self.get_application_profiles(
            application_profile_filter=application_profile_filter,
            epg_info=False
        )
        return len(application_profiles)

    def get_application_profile_info(self, managed_object):
        keys = [
            'descr',
            'dn',
            'name',
            'prio',
            'userdom'
        ]

        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # Dn format
        # [0]: uni/tn-{name}/ap-{name}
        info['tenant'] = info['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info

    def get_application_profiles_info(self):
        if self.application_profile is not None:
            return self.application_profile

        managed_objects = self.get_application_profile_mo()
        if managed_objects is None:
            return None

        self.application_profile = []
        for managed_object in managed_objects:
            self.application_profile.append(
                self.get_application_profile_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'fvAp.info',
            self.application_profile
        )

        return self.application_profile

    def match_application_profile(self, application_profile_info, application_profile_filter):
        if application_profile_filter is None or len(application_profile_filter) == 0:
            return True

        for ap_rule in application_profile_filter:
            (key, value) = ap_rule.split(':')

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, application_profile_info['name']):
                    return False

            if key == 'dn':
                key_found = True
                if not filter_helper.match_string(value, application_profile_info['dn']):
                    return False

            if key == 'tenant':
                key_found = True
                if not filter_helper.match_string(value, application_profile_info['tenant']):
                    return False

            if key == 'epg':
                key_found = True
                if 'epgs' in application_profile_info:
                    (epg_tenant, epg_name) = filter_helper.get_tenant_name(value)

                    found = False
                    for epg_info in application_profile_info['epgs']:
                        if filter_helper.match_string(epg_name, epg_info['name']):
                            if epg_tenant is None:
                                found = True
                                break

                            if filter_helper.match_string(epg_tenant, epg_info['tenant']):
                                found = True
                                break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_application_profile',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_application_profiles(self, application_profile_filter=None, epg_info=False):
        all_profiles = self.get_application_profiles_info()
        if all_profiles is None:
            return None

        application_profiles = []

        for application_profile_info in all_profiles:
            if not self.match_application_profile(application_profile_info, application_profile_filter):
                continue

            if epg_info:
                epg_filter = []
                epg_filter.append(
                    'tenant:%s' % (application_profile_info['tenant'])
                )
                epg_filter.append(
                    'profile:%s' % (application_profile_info['name'])
                )
                application_profile_info['epgs'] = self.get_epgs(
                    epg_filter=epg_filter
                )

                if not self.match_application_profile(application_profile_info, application_profile_filter):
                    continue

            application_profiles.append(application_profile_info)

        application_profiles = sorted(
            application_profiles,
            key=lambda i: i['nameTenant'].lower()
        )

        return application_profiles
