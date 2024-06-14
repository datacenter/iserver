from lib import filter_helper


class EndpointVmmVnicInfo():
    def __init__(self):
        self.endpoint_vmm_vnic = None

    def get_endpoint_vmm_vnic_info(self, managed_object):
        # "adapterType": "Vmxnet3",
        # "addressType": "assigned",
        # "childAction": "",
        # "descr": "",
        # "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/vm-vm-12127/vnic-00:50:56:B4:16:6D",
        # "guid": "241",
        # "id": "0",
        # "ip": "<ip>",
        # "issues": "",
        # "lcOwn": "local",
        # "mac": "00:50:56:B4:16:6D",
        # "modTs": "2023-01-16T20:52:58.626+01:00",
        # "monPolDn": "uni/tn-common/monepg-default",
        # "name": "Network adapter 1",
        # "nameAlias": "",
        # "oid": "4000",
        # "operSt": "down",
        # "status": "",
        # "type": "virt",
        # "uuid": "",
        # "vmName": ""
        info = {}
        info['__Output'] = {}

        keys = [
            'dn',
            'name',
            'operSt',
            'adapterType'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['operSt'] == 'up':
            info['__Output']['operSt'] = 'Green'
        else:
            info['__Output']['operSt'] = 'Red'

        return info

    def get_endpoints_vmm_vnic_info(self):
        if self.endpoint_vmm_vnic is not None:
            return self.endpoint_vmm_vnic

        managed_objects = self.get_endpoint_vmm_vnic_mo()
        if managed_objects is None:
            return None

        self.endpoint_vmm_vnic = []
        for managed_object in managed_objects:
            self.endpoint_vmm_vnic.append(
                self.get_endpoint_vmm_vnic_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'compVNic.info',
            self.endpoint_vmm_vnic
        )

        return self.endpoint_vmm_vnic

    def match_endpoint_vmm_vnic(self, vm_info, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        for rule in vm_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            if key == 'dn':
                if not filter_helper.match_string('%s/*' % (value), vm_info['dn']):
                    return False

            if key == 'mac':
                if not filter_helper.match_string('*/vnic-%s' % (value), vm_info['dn']):
                    return False

        return True

    def get_endpoint_vmm_vnic(self, vm_filter=None, expected_single=False):
        all_vms = self.get_endpoints_vmm_vnic_info()

        vms = []

        for vm_info in all_vms:
            if self.match_endpoint_vmm_vnic(vm_info, vm_filter):
                vms.append(
                    vm_info
                )

        if expected_single:
            if len(vms) == 0:
                return None

            if len(vms) == 1:
                return vms[0]

            self.log.error(
                'get_endpoint_vmm_vnic',
                'Expected single result'
            )
            return None

        return vms
