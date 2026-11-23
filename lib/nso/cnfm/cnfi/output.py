class NsoCnfmCnfiOutput():
    def __init__(self):
        pass

    def print_cnfm_cnfis(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'cnfd_version',
            'device_cluster',
            'readyTick',
            'aliveTick',
            'onboardTick',
            'deviceTick',
            'deviceSyncTick'
        ]

        headers = [
            'CNF Instance',
            'CNFD',
            'Cluster',
            'Plan',
            'Result',
            'Onboard',
            'Device',
            'Sync'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True
        )

    def print_cnfm_cnfis_ready(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Instance - Ready (tailf-ncs:ready) [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'ready.type',
            'ready.name',
            'ready.status',
            'ready.age'
        ]

        headers = [
            'CNF Instance',
            'Type',
            'Name',
            'Status',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['ready']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_plan(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Instance - Plan [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        new_info = []
        for item in info:
            for plan_info in item['plan']:
                new_item = {}
                new_item['namespace_name'] = item['namespace_name']
                for key in plan_info:
                    new_item[key] = plan_info[key]
                new_info.append(
                    new_item
                )

        order = [
            'namespace_name',
            'type',
            'name',
            'state.name',
            'state.status',
            'state.age'
        ]

        headers = [
            'CNF Instance',
            'Plan Type',
            'Plane Name',
            'State',
            'Status',
            'Age'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                new_info,
                order,
                ['state']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_device(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Instance - Device Onboarding [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if 'onboardDevice' not in item:
                keys = [
                    'name',
                    'address_port',
                    'authgroup',
                    'device_type',
                    'ned',
                    'state',
                    'syncTick'
                ]
                item['onboardDevice'] = {}
                for key in keys:
                    item['onboardDevice'][key] = '--'

        order = [
            'namespace_name',
            'onboardTick',
            'onboardDevice.name',
            'onboardDevice.address_port',
            'onboardDevice.authgroup',
            'onboardDevice.device_type',
            'onboardDevice.ned',
            'onboardDevice.state',
            'onboardDevice.syncTick'
        ]

        headers = [
            'CNF Instance',
            'Onboard',
            'Device Name',
            'Address',
            'Auth',
            'Type',
            'NED',
            'State',
            'In-Sync'
        ]

        self.my_output.my_table(
            info,
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=False,
            table=True,
            merge=True
        )

    def print_cnfm_cnfis_result(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Result Summary [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        order = [
            'namespace_name',
            'aliveTick',
            'k8s.kind',
            'k8s.summary'
        ]

        headers = [
            'CNF Instance',
            'Result',
            'Kind',
            'Summary'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['k8s']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_rs(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Result - ReplicaSet [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['replicaset']) == 0:
                new_item = {}
                for key in ['namespace_name', 'replicas', 'readyTick']:
                    new_item[key] = '--'
                item['replicaset'].append(
                    new_item
                )

        order = [
            'namespace_name',
            'replicaset.namespace_name',
            'replicaset.replicas',
            'replicaset.readyTick'
        ]

        headers = [
            'CNF Instance',
            'Replica Set',
            'Replicas',
            'Ready'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['replicaset']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_dep(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Result - Deployment [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['deployment']) == 0:
                new_item = {}
                for key in ['namespace_name', 'summary', 'readyTick']:
                    new_item[key] = '--'
                item['deployment'].append(
                    new_item
                )

        order = [
            'namespace_name',
            'deployment.namespace_name',
            'deployment.summary',
            'deployment.readyTick'
        ]

        headers = [
            'CNF Instance',
            'Deployment',
            'Replicas',
            'Ready'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['deployment']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_pod(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Result - Pod [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['pod']) == 0:
                new_item = {}
                for key in ['namespace_name', 'node-name', 'readyTick']:
                    new_item[key] = '--'
                item['pod'].append(
                    new_item
                )

        order = [
            'namespace_name',
            'pod.namespace_name',
            'pod.node-name',
            'pod.readyTick'
        ]

        headers = [
            'CNF Instance',
            'Pod',
            'Host',
            'Ready'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['pod']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_vmi(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Result - Virtual Machine Instance [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['vmi']) == 0:
                new_item = {}
                for key in ['namespace_name', 'readyTick']:
                    new_item[key] = '--'
                item['vmi'].append(
                    new_item
                )

        order = [
            'namespace_name',
            'vmi.namespace_name',
            'vmi.readyTick'
        ]

        headers = [
            'CNF Instance',
            'Virtual Machine Instance',
            'Ready'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['vmi']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )

    def print_cnfm_cnfis_svc(self, info, title=False):
        if title:
            self.my_output.default(
                'CNFM - CNF Result - Service [#%s]' % (len(info)),
                underline=True,
                before_newline=True
            )

        if len(info) == 0:
            self.my_output.default('None')
            return

        for item in info:
            if len(item['service']) == 0:
                new_item = {}
                for key in ['namespace_name', 'service-type', 'cluster-ip', 'ports', 'readyTick']:
                    new_item[key] = '--'
                item['service'].append(
                    new_item
                )

        order = [
            'namespace_name',
            'service.namespace_name',
            'service.service-type',
            'service.cluster-ip',
            'service.ports',
            'service.readyTick'
        ]

        headers = [
            'CNF Instance',
            'Service',
            'Type',
            'Cluster IP',
            'Port',
            'Ready'
        ]

        self.my_output.my_table(
            self.my_output.expand_lists(
                info,
                order,
                ['service']
            ),
            order=order,
            headers=headers,
            allow_order_subkeys=True,
            underline=True,
            row_separator=True,
            table=True
        )
