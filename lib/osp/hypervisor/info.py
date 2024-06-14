from lib import ip_helper
from lib import filter_helper


class OspHypervisorInfo():
    def __init__(self):
        self.hypervisor = None

    def get_hypervisor_info(self, hypervisor_mo):
        if hypervisor_mo is None:
            return None

        info = hypervisor_mo.to_dict()
        info['__Output'] = {}

        if info['state'] == 'up':
            info['__Output']['state'] = 'Green'
        else:
            info['__Output']['state'] = 'Red'

        if info['status'] == 'enabled':
            info['__Output']['status'] = 'Green'
        else:
            info['__Output']['status'] = 'Red'

        info['cpu_summary'] = '%s/%s' % (
            info['vcpus_used'],
            info['vcpus']
        )

        memory_usage_pct = int(info['memory_mb_used'] * 100 / info['memory_mb'])
        info['memory_summary'] = '%s/%s [MB] (%s%%)' % (
            self.format_value_dotted(info['memory_mb_used']),
            self.format_value_dotted(info['memory_mb']),
            memory_usage_pct
        )

        disk_usage_pct = int(info['local_gb_used'] * 100 / info['local_gb'])
        info['disk_summary'] = '%s/%s [GB] (%s%%)' % (
            self.format_value_dotted(info['local_gb_used']),
            self.format_value_dotted(info['local_gb']),
            disk_usage_pct
        )

        return info

    def get_hypervisors_info(self, cache_enabled=True):
        if cache_enabled:
            if self.hypervisor is not None:
                return self.hypervisor

        managed_objects = self.get_hypervisor_mo(cache_enabled=cache_enabled)
        if managed_objects is None:
            return None

        self.hypervisor = []
        for managed_object in managed_objects:
            hypervisor_info = self.get_hypervisor_info(
                managed_object
            )
            self.hypervisor.append(
                hypervisor_info
            )

        self.log.osp_mo(
            'hypervisors',
            self.hypervisor
        )

        return self.hypervisor

    def match_hypervisor(self, hypervisor_info, hypervisor_filter):
        if hypervisor_filter is None or len(hypervisor_filter) == 0:
            return True

        for ap_rule in hypervisor_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            key_found = False

            if key == 'name':
                key_found = True
                if not filter_helper.match_string(value, hypervisor_info['hypervisor_hostname']):
                    return False

            if key == 'address':
                key_found = True
                if ip_helper.is_valid_ipv4_address(value):
                    if not filter_helper.match_string(value, hypervisor_info['host_ip']):
                        return False

                if ip_helper.is_valid_ipv4_cidr(value):
                    if not ip_helper.is_ipv4_in_cidr(hypervisor_info['host_ip'], value):
                        return False

            if key == 'vm':
                key_found = True
                if 'vm_info' in hypervisor_info:
                    found = False
                    for vm_info in hypervisor_info['vm_info']:
                        if filter_helper.match_tenant_name(value, vm_info['tenant_name']):
                            found = True
                            break

                    if not found:
                        return False

            if not key_found:
                self.log.error(
                    'match_hypervisor',
                    'Unsupported key: %s' % (key)
                )

        return True

    def get_hypervisors(self, object_filter=None, vm_info=False, cache_enabled=True):
        all_hypervisors = self.get_hypervisors_info(cache_enabled=cache_enabled)
        if all_hypervisors is None:
            return None

        hypervisors = []

        for hypervisor_info in all_hypervisors:
            if not self.match_hypervisor(hypervisor_info, object_filter):
                continue

            if vm_info:
                hypervisor_vms = self.get_virtual_machines(
                    object_filter=[
                        'hypervisor:%s' % (hypervisor_info['hypervisor_hostname'])
                    ],
                    tenant_info=True,
                    flavor_info=True
                )
                hypervisor_info['vm_info'] = []
                if hypervisor_vms is None:
                    self.log.error(
                        'get_hypervisors',
                        'Failed to get virtual machine info: %s' % (
                            hypervisor_info['name']
                        )
                    )
                else:
                    for hypervisor_vm in hypervisor_vms:
                        hypervisor_vm_info = {}
                        hypervisor_vm_info['__Output'] = hypervisor_vm['__Output']
                        hypervisor_vm_info['tenant'] = hypervisor_vm['tenant_name']
                        hypervisor_vm_info['name'] = hypervisor_vm['name']
                        hypervisor_vm_info['tenant_name'] = '%s/%s' % (
                            hypervisor_vm_info['tenant'],
                            hypervisor_vm_info['name']
                        )
                        hypervisor_vm_info['status'] = hypervisor_vm['status']
                        hypervisor_vm_info['vcpus'] = hypervisor_vm['flavor_info']['vcpus']
                        hypervisor_vm_info['ram'] = hypervisor_vm['flavor_info']['ram']
                        hypervisor_vm_info['disk'] = hypervisor_vm['flavor_info']['disk']

                        hypervisor_info['vm_info'].append(
                            hypervisor_vm_info
                        )

                if not self.match_hypervisor(hypervisor_info, object_filter):
                    continue

            hypervisors.append(
                hypervisor_info
            )

        hypervisors = sorted(
            hypervisors,
            key=lambda i: i['hypervisor_hostname'].lower()
        )

        return hypervisors

    def get_hypervisor(self, name, vm_info=False, cache_enabled=True):
        object_filter = []
        object_filter.append(
            'name:%s' % (name)
        )
        hypervisors_info = self.get_hypervisors(
            object_filter=object_filter,
            vm_info=vm_info,
            cache_enabled=cache_enabled
        )
        if hypervisors_info is None:
            self.log.error(
                'get_hypervisor',
                'Failed to get hypervisors'
            )
            return None

        if len(hypervisors_info) == 0:
            self.log.error(
                'get_hypervisor',
                'No hypervisors found'
            )
            return None

        if len(hypervisors_info) > 1:
            self.log.error(
                'get_hypervisor',
                'Multiple hypervisors found: %s' % (name)
            )
            return None

        return hypervisors_info[0]
