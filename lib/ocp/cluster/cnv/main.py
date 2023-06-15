class OcpClusterCnv():
    def __init__(self):
        self.ocp_cnv_namespace_name = 'openshift-cnv'
        self.ocp_cnv_operator_group_name = 'kubevirt-hyperconverged-group'
        self.ocp_cnv_subscription_name = 'hco-operatorhub'
        self.ocp_cnv_csv_name = 'kubevirt-hyperconverged'

    def get_ocp_cnv_state(self):
        info = {}
        info['__Output'] = {}

        info['installed'] = False
        info['namespace'] = {}
        info['namespace']['name'] = self.ocp_cnv_namespace_name
        info['namespace']['exists'] = self.is_namespace_name(self.ocp_cnv_namespace_name)
        if info['namespace']['exists']:
            info['__Output']['namespace.name'] = 'Green'
        else:
            info['__Output']['namespace.name'] = 'Red'

        info['operator'] = {}
        info['operator']['name'] = self.ocp_cnv_operator_group_name
        info['operator']['exists'] = False
        info['__Output']['operator.name'] = 'Red'
        if info['namespace']['exists']:
            info['operator']['exists'] = self.is_ocp_operator_group(
                info['operator']['name'],
                info['namespace']['name']
            )
            if info['operator']['exists']:
                info['__Output']['operator.name'] = 'Green'

        info['subscription'] = {}
        info['subscription']['name'] = self.ocp_cnv_subscription_name
        info['subscription']['exists'] = False
        info['subscription']['ready'] = False
        info['subscription']['state'] = 'Not installed'
        info['__Output']['subscription.name'] = 'Red'
        info['__Output']['subscription.state'] = 'Red'
        if info['namespace']['exists']:
            subscription_info = self.get_ocp_subscription(
                info['subscription']['name'],
                info['namespace']['name']
            )
            if subscription_info is not None:
                info['subscription']['exists'] = True
                info['subscription']['state'] = subscription_info['state']
                info['subscription']['spec'] = subscription_info['spec']
                if info['subscription']['exists'] and info['subscription']['state'] == 'AtLatestKnown':
                    info['__Output']['subscription.name'] = 'Green'
                    info['__Output']['subscription.state'] = 'Green'
                    info['subscription']['ready'] = True

        info['csv'] = {}
        info['csv']['name'] = self.ocp_cnv_csv_name
        info['csv']['phase'] = 'Not installed'
        info['csv']['exists'] = False
        info['csv']['ready'] = False
        info['__Output']['csv.name'] = 'Red'
        info['__Output']['csv.phase'] = 'Red'
        if info['subscription']['ready']:
            info['csv']['name'] = subscription_info['spec']['startingCSV']
            csv_info = self.get_ocp_csv(
                info['csv']['name'],
                info['namespace']['name']
            )
            if csv_info is not None:
                info['csv']['exists'] = True
                info['csv']['phase'] = csv_info['phase']
                if info['csv']['exists'] and info['csv']['phase'] == 'Succeeded':
                    info['__Output']['csv.name'] = 'Green'
                    info['__Output']['csv.phase'] = 'Green'
                    info['csv']['ready'] = True
                    info['installed'] = True

        return info
