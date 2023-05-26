class NodeInterfacePolicyProfileInfo():
    def __init__(self):
        pass

    def get_node_interface_policy_profile_info(self, managed_object):
        # "childAction": "deleteNonPresent",
        # "deplSt": "delivered",
        # "dn": "uni/infra/nodecfgcont/node-205/rsinterfacePolProfile-[uni/infra/accportprof-UCSB1-FI-A_IntProf]",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2021-12-09T23:30:56.576+02:00",
        # "monPolDn": "",
        # "rType": "mo",
        # "state": "formed",
        # "stateQual": "none",
        # "status": "",
        # "tCl": "infraAccPortP",
        # "tDn": "uni/infra/accportprof-UCSB1-FI-A_IntProf",
        # "tType": "mo"

        keys = [
            'tCl',
            'tDn'
        ]
        info = {}
        for key in keys:
            info[key] = managed_object[key]

        if info['tCl'] != 'infraAccPortP':
            self.log.error(
                'get_node_interface_policy_profile_info',
                'Unsupported profile class: %s' % (info['tCl'])
            )
            return None

        info['name'] = info['tDn'].split('/')[2][12:]

        return info

    def get_node_interface_policy_profiles(self, pod_id, node_id):
        managed_objects = self.get_node_interface_policy_profile_mo(pod_id, node_id)
        if managed_objects is None:
            return None

        profiles = []
        for managed_object in managed_objects:
            profile_info = self.get_node_interface_policy_profile_info(
                managed_object
            )

            if profile_info is not None:
                profiles.append(
                    profile_info
                )

        return profiles
