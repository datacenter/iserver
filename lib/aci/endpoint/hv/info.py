class EndpointHvInfo():
    def __init__(self):
        pass

    def get_endpoint_hv_info(self, managed_object):
        # "childAction": "",
        # "forceResolve": "yes",
        # "isBootstrapUpd": "attach",
        # "lcOwn": "local",
        # "modTs": "2022-09-22T15:10:06.162+01:00",
        # "rType": "mo",
        # "rn": "rshyper-[comp/prov-VMware/ctrlr-[EU-SPDC-CDC-22]-EU-SPDC-CDC-22/hv-host-2842]",
        # "state": "formed",
        # "stateQual": "none",
        # "status": "",
        # "tCl": "compHv",
        # "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-CDC-22]-EU-SPDC-CDC-22/hv-host-2842",
        # "tType": "mo"
        info = {}
        info['__Output'] = {}

        keys = [
            'rn',
            'state',
            'tCl',
            'tDn',
            'tType'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info
