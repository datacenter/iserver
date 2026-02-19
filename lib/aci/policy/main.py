from lib.aci import helper as aci_helper
from lib.aci.policy.general.main import PolicyGeneral
from lib.aci.policy.interface.main import PolicyInterface
from lib.aci.policy.monitoring.main import PolicyMonitoring
from lib.aci.policy.snoop.main import PolicySnoop
from lib.aci.policy.switch.main import PolicySwitch
from lib.aci.policy.troubleshooting.main import PolicyTroubleshooting


class Policy(
    PolicyGeneral,
    PolicyInterface,
    PolicyMonitoring,
    PolicySnoop,
    PolicySwitch,
    PolicyTroubleshooting
    ):
    def __init__(self):
        PolicyGeneral.__init__(self)
        PolicyInterface.__init__(self)
        PolicyMonitoring.__init__(self)
        PolicySnoop.__init__(self)
        PolicySwitch.__init__(self)
        PolicyTroubleshooting.__init__(self)

    def get_policy_type_from_tcl(self, policy_type):
        return aci_helper.get_policy_type_from_tcl(policy_type)

    def get_policy_name_from_tdn(self, policy_name):
        if policy_name.startswith('uni/infra/funcprof/'):
            funcname = policy_name.split('uni/infra/funcprof/')[1]
            return '-'.join(funcname.split('-')[1:])

        if policy_name.startswith('uni/vmmp-VMware/dom-'):
            name = policy_name.split('uni/vmmp-VMware/dom-')[1]
            if name.endswith('/vswitchpolcont'):
                name = name.split('/vswitchpolcont')[0]
            return name

        if policy_name == 'uni/infra':
            return 'infra'

        return policy_name
