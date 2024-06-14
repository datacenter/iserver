class EndpointVmInfo():
    def __init__(self):
        pass

    def get_endpoint_vm_info(self, managed_object):
        # "childAction": "",
        # "forceResolve": "yes",
        # "isBootstrapUpd": "attach",
        # "lcOwn": "local",
        # "modTs": "2022-12-16T15:57:06.305+01:00",
        # "rType": "mo",
        # "rn": "rstoVm-[comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-12062]",
        # "state": "formed",
        # "stateQual": "none",
        # "status": "",
        # "tCl": "compVm",
        # "tDn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-12062",
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
