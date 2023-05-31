class PolicySnoopMld():
    def __init__(self):
        pass

    def get_policy_snoop_mld_mo(self, tenant, name):
        distinguished_name = 'uni/tn-%s/mldsnoopPol-%s' % (
            tenant,
            name
        )

        managed_objects = self.get_managed_object(
            distinguished_name
        )
        if managed_objects is None:
            return None

        if managed_objects['totalCount'] != '1':
            return None

        self.log.apic_mo(
            'mldSnoopPol',
            managed_objects['imdata'][0]
        )

        return managed_objects['imdata'][0]['mldSnoopPol']['attributes']

    def get_policy_snoop_mld_info(self, managed_object):
        # "adminSt": "disabled",
        # "annotation": "",
        # "childAction": "",
        # "ctrl": "",
        # "descr": "",
        # "dn": "uni/tn-k8s/mldsnoopPol-Test",
        # "extMngdBy": "",
        # "lastMbrIntvl": "1",
        # "lcOwn": "local",
        # "modTs": "2023-01-20T07:23:26.975+01:00",
        # "name": "Test",
        # "nameAlias": "",
        # "ownerKey": "",
        # "ownerTag": "",
        # "queryIntvl": "125",
        # "rspIntvl": "10",
        # "startQueryCnt": "2",
        # "startQueryIntvl": "31",
        # "status": "",
        # "uid": "15374",
        # "userdom": ":all:common:",
        # "ver": "v2"
        keys = [
            'adminSt',
            'dn',
            'lastMbrIntvl',
            'name',
            'queryIntvl',
            'rspIntvl',
            'startQueryCnt',
            'startQueryIntvl',
            'ver'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        # "dn": "uni/tn-k8s/mldsnoopPol-Test"
        info['tenant'] = managed_object['dn'].split('/')[1][3:]
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        if info['adminSt'] == 'enabled':
            info['__Output']['adminSt'] = 'Green'
        else:
            info['__Output']['adminSt'] = 'Red'

        return info

    def get_policy_snoop_mld(self, tenant, name):
        managed_object = self.get_policy_snoop_mld_mo(tenant, name)
        if managed_object is None:
            return None
        return self.get_policy_snoop_mld_info(managed_object)
