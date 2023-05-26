from lib import filter_helper


class ApplicationProfileInfo():
    def __init__(self):
        pass

    def get_application_profile_count(self, tenant_name=None):
        application_profile_filter = None
        if tenant_name is not None:
            application_profile_filter = ['tenant:%s' % (tenant_name)]

        application_profiles = self.get_application_profiles(
            application_profile_filter=application_profile_filter
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

        epg_filter = []
        epg_filter.append(
            'tenant:%s' % (info['tenant'])
        )
        epg_filter.append(
            'profile:%s' % (info['name'])
        )
        info['epgs'] = self.get_epgs(
            epg_filter=epg_filter
        )

        return info

    def match_application_profile(self, application_profile_info, application_profile_filter):
        if application_profile_filter is None or len(application_profile_filter) == 0:
            return True

        for ap_rule in application_profile_filter:
            (key, value) = ap_rule.split(':')
            if key == 'name':
                if not filter_helper.match_string(value, application_profile_info['name']):
                    return False

            if key == 'dn':
                if not filter_helper.match_string(value, application_profile_info['dn']):
                    return False

            if key == 'tenant':
                if not filter_helper.match_string(value, application_profile_info['tenant']):
                    return False

            if key == 'epg':
                found = False
                for epg_info in application_profile_info['epgs']:
                    if filter_helper.match_string(value, epg_info['name']):
                        found = True
                        break

                if not found:
                    return False

        return True

    def get_application_profiles(self, application_profile_filter=None):
        application_profiles = []

        if not self.initialize_application_profile():
            self.log.error(
                'get_application_profiles',
                'Application profile initialization failed'
            )
            return application_profiles

        for managed_object in self.mo_application_profile:
            application_profile_info = self.get_application_profile_info(
                managed_object
            )

            if not self.match_application_profile(application_profile_info, application_profile_filter):
                continue

            application_profiles.append(application_profile_info)

        application_profiles = sorted(
            application_profiles,
            key=lambda i: i['nameTenant'].lower()
        )

        self.log.apic_mo(
            'fvAp.info',
            application_profiles
        )

        return application_profiles
