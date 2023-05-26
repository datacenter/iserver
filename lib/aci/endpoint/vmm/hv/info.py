from lib import filter_helper


class EndpointVmmHvInfo():
    def __init__(self):
        self.endpoint_vmm_hv = None

    def get_endpoint_vmm_hv_info(self, managed_object):
        # "availAdminSt": "gray",
        # "availOperSt": "gray",
        # "childAction": "",
        # "countUplink": "0",
        # "descr": "",
        # "dn": "comp/prov-VMware/ctrlr-[EU-SPDC-POD2B]-EU-SPDC-POD2B/hv-host-11004",
        # "enteringMaintenance": "no",
        # "guid": "ef308948-5457-4b43-b570-c2bd8359e739",
        # "id": "0",
        # "issues": "",
        # "lcOwn": "local",
        # "mgmtIp": "0.0.0.0",
        # "modTs": "2022-12-12T16:31:55.873+01:00",
        # "monPolDn": "uni/infra/moninfra-default",
        # "name": "esx71.emea-sp.cisco.com",
        # "nameAlias": "",
        # "oid": "host-11004",
        # "operIssues": "",
        # "os": "",
        # "state": "poweredOn",
        # "status": "",
        # "type": "hv",
        # "uuid": ""
        info = {}
        info['__Output'] = {}
        keys = [
            'availAdminSt',
            'availOperSt',
            'countUplink',
            'dn',
            'enteringMaintenance',
            'mgmtIp',
            'name',
            'oid',
            'state'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['vmm'] = info['dn'].split('[')[1].split(']')[0]

        return info

    def get_endpoints_vmm_hv_info(self):
        if self.endpoint_vmm_hv is not None:
            return self.endpoint_vmm_hv

        managed_objects = self.get_endpoint_vmm_hv_mo()
        if managed_objects is None:
            return None

        self.endpoint_vmm_hv = []
        for managed_object in managed_objects:
            self.endpoint_vmm_hv.append(
                self.get_endpoint_vmm_hv_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'compHv.info',
            self.endpoint_vmm_hv
        )

        return self.endpoint_vmm_hv

    def match_endpoint_vmm_hv(self, vm_info, vm_filter):
        if vm_filter is None or len(vm_filter) == 0:
            return True

        for rule in vm_filter:
            key = rule.split(':')[0]
            value = ':'.join(rule.split(':')[1:])

            if key == 'dn':
                if not filter_helper.match_string(value, vm_info['dn']):
                    return False

        return True

    def get_endpoint_vmm_hv(self, vm_filter=None, expected_single=False):
        all_vms = self.get_endpoints_vmm_hv_info()

        vms = []

        for vm_info in all_vms:
            if self.match_endpoint_vmm_hv(vm_info, vm_filter):
                vms.append(
                    vm_info
                )

        if expected_single:
            if len(vms) == 0:
                return None

            if len(vms) == 1:
                return vms[0]

            self.log.error(
                'get_endpoint_vmm_hv',
                'Expected single result'
            )
            return None

        return vms
