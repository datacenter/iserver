class PolicyMonitoring():
    def __init__(self):
        pass

    def get_policy_monitoring_info(self, managed_object):
        # "annotation": "",
        # "childAction": "",
        # "extMngdBy": "",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2021-05-19T18:26:53.317+01:00",
        # "monPolDn": "uni/fabric/monfab-default",
        # "rType": "mo",
        # "rn": "rsmonIfInfraPol",
        # "state": "formed",
        # "stateQual": "default-target",
        # "status": "",
        # "tCl": "monInfraPol",
        # "tContextDn": "",
        # "tDn": "uni/infra/moninfra-default",
        # "tRn": "moninfra-default",
        # "tType": "name",
        # "tnMonInfraPolName": "",
        # "uid": "0",
        # "userdom": "all"
        keys = [
            'state',
            'tDn',
            'tRn',
            'tnMonInfraPolName'
        ]
        info = {}
        info['__Output'] = {}

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['name'] = info['tRn'].split('moninfra-')[1]

        return info
