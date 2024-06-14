class EndpointIpInfo():
    def __init__(self):
        pass

    def get_endpoint_ip_info(self, managed_object):
        # "addr": "<ip>",
        # "annotation": "",
        # "baseEpgDn": "",
        # "bdDn": "",
        # "childAction": "",
        # "createTs": "2022-09-14T22:56:47.772+01:00",
        # "debugMACMessage": "",
        # "esgUsegDn": "",
        # "extMngdBy": "",
        # "fabricPathDn": "topology/pod-1/paths-2205/pathep-[eth1/25]",
        # "flags": "",
        # "lcOwn": "local",
        # "modTs": "2022-09-14T22:57:01.829+01:00",
        # "monPolDn": "uni/tn-common/monepg-default",
        # "rn": "ip-[<ip>]",
        # "status": "",
        # "uid": "0",
        # "userdom": "all",
        # "vrfDn": "uni/tn-common/ctx-Infra_VRF"
        info = {}
        info['__Output'] = {}

        keys = [
            'addr',
            'baseEpgDn',
            'vrfDn'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info
