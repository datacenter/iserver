# https://www.kareemccie.com/2021/12/what-is-endpoint-retention-policy-in-aci.html


class BridgeDomainRetentionInfo():
    def __init__(self):
        pass

    def get_bridge_domain_retention_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        info['tenant'] = managed_object['tDn'].split('/')[1].split('tn-')[1]
        info['name'] = managed_object['tnFvEpRetPolName']
        info['nameTenant'] = '%s/%s' % (
            info['tenant'],
            info['name']
        )

        return info
