class BridgeDomainL3OutInfo():
    def __init__(self):
        pass

    def get_bridge_domain_l3out_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['tenant'] = managed_object['tDn'].split('/')[1].split('tn-')[1]
        info['name'] = managed_object['tnL3extOutName']
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            managed_object['tnL3extOutName']
        )

        return info
