from lib import filter_helper


class NsoCnfmResultInfo():
    def __init__(self):
        self.cnfm_result = None

    def get_cnfm_result_vmi_info(self, info, cnfm_result_mo):
        vmis_mo = self.get(
            cnfm_result_mo,
            'virtualmachineinstance',
            on_error=[],
            on_none=[]
        )

        info['vmi'] = []
        vmi_ready = 0
        for vmi_mo in vmis_mo:
            vmi_info = {}
            vmi_info['__Output'] = {}
            vmi_info['namespace'] = vmi_mo['namespace']
            vmi_info['name'] = vmi_mo['name']
            vmi_info['namespace_name'] = '%s/%s' % (
                vmi_info['namespace'],
                vmi_info['name']
            )
            vmi_info['status'] = vmi_mo['status']
            vmi_info['labels'] = vmi_mo['labels']
            vmi_info['selector'] = vmi_mo['selector']
            for key in ['replicas']:
                vmi_info[key] = vmi_mo[key]

            if vmi_info['status'] == 'alive':
                vmi_info['ready'] = True
                vmi_info['readyTick'] = '\u2713'
                vmi_info['__Output']['readyTick'] = 'Green'
                vmi_ready = vmi_ready + 1
            else:
                vmi_info['ready'] = False
                vmi_info['readyTick'] = '\u2717'
                vmi_info['__Output']['readyTick'] = 'Red'

            info['vmi'].append(
                vmi_info
            )

        found = False
        for k8s_info in info['k8s']:
            if k8s_info['kind'] == 'VirtualMachineInstance':
                found = True
                if len(info['vmi']) != k8s_info['desired']:
                    self.log.error(
                        'get_cnfm_result_info',
                        'Unexpected vmi desired value'
                    )

        if not found:
            k8s_info = {}
            k8s_info['__Output'] = {}
            k8s_info['kind'] = 'VirtualMachineInstance'
            k8s_info['desired'] = len(info['vmi'])
            k8s_info['available'] = vmi_ready
            if k8s_info['desired'] == 0:
                k8s_info['summary'] = '--'
            else:
                k8s_info['summary'] = '%s/%s' % (
                    k8s_info['desired'],
                    k8s_info['available']
                )

                if k8s_info['desired'] == k8s_info['available']:
                    k8s_info['__Output']['summary'] = 'Green'
                else:
                    k8s_info['__Output']['summary'] = 'Red'

            info['k8s'].append(
                k8s_info
            )

        return info

    def get_cnfm_result_pod_info(self, info, cnfm_result_mo):
        pods_mo = self.get(
            cnfm_result_mo,
            'pod',
            on_error=[],
            on_none=[]
        )

        info['pod'] = []
        pod_ready = 0
        for pod_mo in pods_mo:
            pod_info = {}
            pod_info['__Output'] = {}
            pod_info['namespace'] = pod_mo['namespace']
            pod_info['name'] = pod_mo['name']
            pod_info['namespace_name'] = '%s/%s' % (
                pod_info['namespace'],
                pod_info['name']
            )
            pod_info['status'] = pod_mo['status']
            pod_info['labels'] = pod_mo['labels']
            for key in ['ip', 'host-ip', 'node-name', 'deployment', 'replica', 'container', 'selector']:
                pod_info[key] = None
                if key in pod_mo:
                    pod_info[key] = pod_mo[key]

            if pod_info['status'] == 'alive':
                pod_info['ready'] = True
                pod_info['readyTick'] = '\u2713'
                pod_info['__Output']['readyTick'] = 'Green'
                pod_ready = pod_ready + 1
            else:
                pod_info['ready'] = False
                pod_info['readyTick'] = '\u2717'
                pod_info['__Output']['readyTick'] = 'Red'

            info['pod'].append(
                pod_info
            )

        found = False
        for k8s_info in info['k8s']:
            if k8s_info['kind'] == 'Pod':
                found = True
                if len(info['pod']) != k8s_info['desired']:
                    self.log.error(
                        'get_cnfm_result_info',
                        'Unexpected pod desired value'
                    )

        if not found:
            k8s_info = {}
            k8s_info['__Output'] = {}
            k8s_info['kind'] = 'Pod'
            k8s_info['desired'] = len(info['pod'])
            k8s_info['available'] = pod_ready
            if k8s_info['desired'] == 0:
                k8s_info['summary'] = '--'
            else:
                k8s_info['summary'] = '%s/%s' % (
                    k8s_info['desired'],
                    k8s_info['available']
                )

                if k8s_info['desired'] == k8s_info['available']:
                    k8s_info['__Output']['summary'] = 'Green'
                else:
                    k8s_info['__Output']['summary'] = 'Red'

            info['k8s'].append(
                k8s_info
            )

        return info

    def get_cnfm_result_replicaset_info(self, info, cnfm_result_mo):
        replicasets_mo = self.get(
            cnfm_result_mo,
            'replicaset',
            on_error=[],
            on_none=[]
        )

        info['replicaset'] = []
        replicaset_ready = 0
        for replicaset_mo in replicasets_mo:
            replicaset_info = {}
            replicaset_info['__Output'] = {}
            replicaset_info['namespace'] = replicaset_mo['namespace']
            replicaset_info['name'] = replicaset_mo['name']
            replicaset_info['namespace_name'] = '%s/%s' % (
                replicaset_info['namespace'],
                replicaset_info['name']
            )
            replicaset_info['status'] = replicaset_mo['status']
            replicaset_info['labels'] = replicaset_mo['labels']
            replicaset_info['selector'] = replicaset_mo['selector']
            for key in ['replicas']:
                replicaset_info[key] = replicaset_mo[key]

            if replicaset_info['status'] == 'alive':
                replicaset_info['ready'] = True
                replicaset_info['readyTick'] = '\u2713'
                replicaset_info['__Output']['readyTick'] = 'Green'
                replicaset_ready = replicaset_ready + 1
            else:
                replicaset_info['ready'] = False
                replicaset_info['readyTick'] = '\u2717'
                replicaset_info['__Output']['readyTick'] = 'Red'

            info['replicaset'].append(
                replicaset_info
            )

        found = False
        for k8s_info in info['k8s']:
            if k8s_info['kind'] == 'ReplicaSet':
                found = True
                if len(info['replicaset']) != k8s_info['desired']:
                    self.log.error(
                        'get_cnfm_result_info',
                        'Unexpected replicaset desired value'
                    )

        if not found:
            k8s_info = {}
            k8s_info['__Output'] = {}
            k8s_info['kind'] = 'ReplicaSet'
            k8s_info['desired'] = len(info['replicaset'])
            k8s_info['available'] = replicaset_ready
            if k8s_info['desired'] == 0:
                k8s_info['summary'] = '--'
            else:
                k8s_info['summary'] = '%s/%s' % (
                    k8s_info['desired'],
                    k8s_info['available']
                )

                if k8s_info['desired'] == k8s_info['available']:
                    k8s_info['__Output']['summary'] = 'Green'
                else:
                    k8s_info['__Output']['summary'] = 'Red'

            info['k8s'].append(
                k8s_info
            )

        return info

    def get_cnfm_result_deployment_info(self, info, cnfm_result_mo):
        deployments_mo = self.get(
            cnfm_result_mo,
            'deployment',
            on_error=[],
            on_none=[]
        )

        info['deployment'] = []
        deployment_ready = 0
        for deployment_mo in deployments_mo:
            deployment_info = {}
            deployment_info['__Output'] = {}
            deployment_info['namespace'] = deployment_mo['namespace']
            deployment_info['name'] = deployment_mo['name']
            deployment_info['namespace_name'] = '%s/%s' % (
                deployment_info['namespace'],
                deployment_info['name']
            )
            deployment_info['status'] = deployment_mo['status']
            deployment_info['labels'] = deployment_mo['labels']
            deployment_info['selector'] = deployment_mo['selector']
            for key in ['replicas', 'updated-replicas', 'available-replicas', 'ready-replicas', 'unavailable-replicas']:
                deployment_info[key] = deployment_mo[key]

            deployment_info['summary'] = '%s/%s' % (
                deployment_info['replicas'],
                deployment_info['ready-replicas']
            )
            if deployment_info['replicas'] == deployment_info['ready-replicas']:
                deployment_info['ready'] = True
                deployment_info['readyTick'] = '\u2713'
                deployment_info['__Output']['readyTick'] = 'Green'
                deployment_info['__Output']['summary'] = 'Green'
                deployment_ready = deployment_ready + 1
            else:
                deployment_info['ready'] = False
                deployment_info['readyTick'] = '\u2717'
                deployment_info['__Output']['readyTick'] = 'Red'
                deployment_info['__Output']['summary'] = 'Red'

            info['deployment'].append(
                deployment_info
            )

        found = False
        for k8s_info in info['k8s']:
            if k8s_info['kind'] == 'Deployment':
                found = True
                if len(info['deployment']) != k8s_info['desired']:
                    self.log.error(
                        'get_cnfm_result_info',
                        'Unexpected deployment desired value'
                    )

        if not found:
            k8s_info = {}
            k8s_info['__Output'] = {}
            k8s_info['kind'] = 'Deployment'
            k8s_info['desired'] = len(info['deployment'])
            k8s_info['available'] = deployment_ready
            if k8s_info['desired'] == 0:
                k8s_info['summary'] = '--'
            else:
                k8s_info['summary'] = '%s/%s' % (
                    k8s_info['desired'],
                    k8s_info['available']
                )

                if k8s_info['desired'] == k8s_info['available']:
                    k8s_info['__Output']['summary'] = 'Green'
                else:
                    k8s_info['__Output']['summary'] = 'Red'

            info['k8s'].append(
                k8s_info
            )

        return info

    def get_cnfm_result_service_info(self, info, cnfm_result_mo):
        services_mo = self.get(
            cnfm_result_mo,
            'service',
            on_error=[],
            on_none=[]
        )

        info['service'] = []
        service_ready = 0
        for service_mo in services_mo:
            service_info = {}
            service_info['__Output'] = {}
            service_info['namespace'] = service_mo['namespace']
            service_info['name'] = service_mo['name']
            service_info['namespace_name'] = '%s/%s' % (
                service_info['namespace'],
                service_info['name']
            )
            service_info['status'] = service_mo['status']
            service_info['labels'] = service_mo['labels']
            service_info['selector'] = service_mo['selector']
            for key in ['service-type', 'cluster-ip', 'port']:
                service_info[key] = service_mo[key]

            port_descriptions = []
            for port in service_info['port']:
                if service_info['service-type'] == 'NodePort':
                    port['description'] = '%s:%s/%s' % (
                        port['port'],
                        port['node-port'],
                        port['protocol']
                    )
                    if 'name' in port:
                        port['description'] = '%s (%s)' % (
                            port['description'],
                            port['name']
                        )

                if service_info['service-type'] != 'NodePort':
                    port['description'] = '%s/%s' % (
                        port['port'],
                        port['protocol']
                    )
                    if 'name' in port:
                        port['description'] = '%s (%s)' % (
                            port['description'],
                            port['name']
                        )

                port_descriptions.append(
                    port['description']
                )

            service_info['ports'] = ','.join(port_descriptions)

            if service_info['status'] == 'alive':
                service_info['ready'] = True
                service_info['readyTick'] = '\u2713'
                service_info['__Output']['readyTick'] = 'Green'
                service_ready = service_ready + 1
            else:
                service_info['ready'] = False
                service_info['readyTick'] = '\u2717'
                service_info['__Output']['readyTick'] = 'Red'

            info['service'].append(
                service_info
            )

        found = False
        for k8s_info in info['k8s']:
            if k8s_info['kind'] == 'Service':
                found = True
                if len(info['service']) != k8s_info['desired']:
                    self.log.error(
                        'get_cnfm_result_info',
                        'Unexpected service desired value'
                    )

        if not found:
            k8s_info = {}
            k8s_info['__Output'] = {}
            k8s_info['kind'] = 'Service'
            k8s_info['desired'] = len(info['service'])
            k8s_info['available'] = service_ready
            if k8s_info['desired'] == 0:
                k8s_info['summary'] = '--'
            else:
                k8s_info['summary'] = '%s/%s' % (
                    k8s_info['desired'],
                    k8s_info['available']
                )

                if k8s_info['desired'] == k8s_info['available']:
                    k8s_info['__Output']['summary'] = 'Green'
                else:
                    k8s_info['__Output']['summary'] = 'Red'

            info['k8s'].append(
                k8s_info
            )

        return info

    def get_cnfm_result_k8s_info(self, info, cnfm_result_mo):
        info['k8s'] = []

        objects_mo = self.get(
            cnfm_result_mo,
            'k8s-objects:kind',
            on_error=[],
            on_none=[]
        )
        for object_mo in objects_mo:
            k8s_info = {}
            k8s_info['__Output'] = {}
            k8s_info['kind'] = object_mo['name']
            k8s_info['desired'] = object_mo['desired-count']
            k8s_info['available'] = object_mo['available-count']
            if k8s_info['desired'] == 0:
                k8s_info['summary'] = '--'
            else:
                k8s_info['summary'] = '%s/%s' % (
                    k8s_info['desired'],
                    k8s_info['available']
                )

                if k8s_info['desired'] == k8s_info['available']:
                    k8s_info['__Output']['summary'] = 'Green'
                else:
                    k8s_info['__Output']['summary'] = 'Red'

            info['k8s'].append(
                k8s_info
            )

        info = self.get_cnfm_result_vmi_info(
            info,
            cnfm_result_mo
        )

        info = self.get_cnfm_result_pod_info(
            info,
            cnfm_result_mo
        )

        info = self.get_cnfm_result_replicaset_info(
            info,
            cnfm_result_mo
        )

        info = self.get_cnfm_result_deployment_info(
            info,
            cnfm_result_mo
        )

        info = self.get_cnfm_result_service_info(
            info,
            cnfm_result_mo
        )

        info['k8s'] = sorted(
            info['k8s'],
            key=lambda i: i['kind']
        )

        return info

    def get_cnfm_result_info(self, cnfm_result_mo):
        if cnfm_result_mo is None:
            return None

        info = {}
        info['__Output'] = {}

        info['name'] = self.get(
            cnfm_result_mo,
            'name'
        )

        info['alive'] = self.get(
            cnfm_result_mo,
            'state:status'
        )
        if info['alive'] == 'alive':
            info['aliveTick'] = '\u2713'
            info['__Output']['aliveTick'] = 'Green'
        else:
            info['aliveTick'] = '\u2717'
            info['__Output']['aliveTick'] = 'Red'

        info = self.get_cnfm_result_k8s_info(
            info,
            cnfm_result_mo
        )

        return info

    def get_cnfm_results_info(self, cache_enabled=True):
        if cache_enabled:
            if self.cnfm_result is not None:
                return self.cnfm_result

        managed_objects = self.get_cnfm_result_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.cnfm_result = []
        for managed_object in managed_objects:
            cnfm_result_info = self.get_cnfm_result_info(
                managed_object
            )
            self.cnfm_result.append(
                cnfm_result_info
            )

        return self.cnfm_result

    def match_cnfm_result(self, cnfm_result_info, cnfm_result_filter):
        if cnfm_result_info is None or len(cnfm_result_filter) == 0:
            return True

        for ap_rule in cnfm_result_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, cnfm_result_info['name']):
                    return False

            if not key_found:
                self.log.error(
                    'match_cnfm_result',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_cnfm_results(self, object_filter=None, cache_enabled=True):
        all_cnfm_results = self.get_cnfm_results_info(cache_enabled=cache_enabled)
        if all_cnfm_results is None:
            return None

        cnfm_results = []

        for cnfm_result_info in all_cnfm_results:
            if not self.match_cnfm_result(cnfm_result_info, object_filter):
                continue

            cnfm_results.append(
                cnfm_result_info
            )

        return cnfm_results

    def get_cnfm_result(self, cnfm_cnfi_name, cache_enabled=True):
        cnfm_results = self.get_cnfm_results(
            object_filter=[
                'name:%s' % (cnfm_cnfi_name),
            ],
            cache_enabled=cache_enabled
        )
        if cnfm_results is None or len(cnfm_results) != 1:
            return None

        return cnfm_results[0]
