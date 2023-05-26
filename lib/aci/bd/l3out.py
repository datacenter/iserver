from lib import log_helper


class BridgeDomainL3Out():
    def __init__(self, log_id=None):
        self.log = log_helper.Log(log_id=log_id)

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
