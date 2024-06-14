from lib import filter_helper


class DomainVmmControllerInfo():
    def __init__(self):
        self.domain_vmm_controller = None

    def get_domain_vmm_controller_hv_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'countUplink',
            'guid',
            'mgmtIp',
            'name',
            'oid',
            'rn',
            'state',
            'type'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['state'] == 'poweredOn':
            info['powerTick'] = '\u2713'
            info['__Output']['powerTick'] = 'Green'
        else:
            info['powerTick'] = '\u2717'
            info['__Output']['powerTick'] = 'Red'

        return info

    def get_domain_vmm_controller_vm_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'cfgdOs',
            'guid',
            'name',
            'oid',
            'os',
            'rn',
            'state',
            'template',
            'type',
            'uuid'
        ]

        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['state'] == 'poweredOn':
            info['powerTick'] = '\u2713'
            info['__Output']['powerTick'] = 'Green'
        else:
            info['powerTick'] = '\u2717'
            info['__Output']['powerTick'] = 'Red'

        return info

    def get_domain_vmm_controller_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        keys = [
            'accessMode',
            'apiVer',
            'aveSwitchingActive',
            'aveTimeOut',
            'ctrlKnob',
            'ctrlrPKey',
            'dn',
            'domName',
            'dvsVersion',
            'enableAVE',
            'enableTag',
            'enableVmFolder',
            'epRetTime',
            'hostOrIp',
            'id',
            'key',
            'lagPolicyName',
            'lastEventCollectorId',
            'maxWorkerQSize',
            'mode',
            'model',
            'name',
            'operSt',
            'port',
            'rev',
            'rootContName',
            'scope',
            'ser',
            'usr',
            'vendor',
            'vspherePHA',
            'vsphereTag',
            'vxlanDeplPref'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if info['operSt'] == 'online':
            info['operStTick'] = '\u2713'
            info['__Output']['operStTick'] = 'Green'
        else:
            info['operStTick'] = '\u2717'
            info['__Output']['operStTick'] = 'Red'

        info['serialShort'] = info['ser'].split('-')[0]

        info['compHv'] = []
        if managed_object['compHv'] is not None:
            for hv_mo in managed_object['compHv']:
                info['compHv'].append(
                    self.get_domain_vmm_controller_hv_info(
                        hv_mo
                    )
                )

        info['compHv'] = sorted(
            info['compHv'],
            key=lambda i: i['name']
        )
        info['hvCount'] = len(
            info['compHv']
        )

        info['compVm'] = []
        if managed_object['compVm'] is not None:
            for vm_mo in managed_object['compVm']:
                info['compVm'].append(
                    self.get_domain_vmm_controller_vm_info(
                        vm_mo
                    )
                )

        info['compVm'] = sorted(
            info['compVm'],
            key=lambda i: i['name']
        )
        info['vmCount'] = len(
            info['compVm']
        )

        (info['__Output']['faults'], info['faults']) = self.get_faults_info(
            managed_object['faultCounts']
        )

        info['isAnyFault'] = self.is_any_fault(
            managed_object['faultCounts']
        )

        return info

    def get_domain_vmm_controller_infos(self):
        if self.domain_vmm_controller is not None:
            return self.domain_vmm_controller

        managed_objects = self.get_domain_vmm_controller_mo()
        if managed_objects is None:
            return None

        self.domain_vmm_controller = []
        for managed_object in managed_objects:
            self.domain_vmm_controller.append(
                self.get_domain_vmm_controller_info(
                    managed_object
                )
            )

        self.log.apic_mo(
            'compCtrlr.info',
            self.domain_vmm_controller
        )

        return self.domain_vmm_controller

    def match_domain_vmm_controller(self, domain_vmm_controller_info, domain_vmm_controller_filter):
        if domain_vmm_controller_filter is None or len(domain_vmm_controller_filter) == 0:
            return True

        for aepg_rule in domain_vmm_controller_filter:
            (key, value) = aepg_rule.split(':')
            if key == 'domain':
                if not filter_helper.match_string(value, domain_vmm_controller_info['domName']):
                    return False

        return True

    def get_domain_vmm_controllers(self, domain_vmm_controller_filter=None):
        all_controllers = self.get_domain_vmm_controller_infos()
        if all_controllers is None:
            return None

        controllers = []

        for domain_vmm_controller_info in all_controllers:
            if not self.match_domain_vmm_controller(domain_vmm_controller_info, domain_vmm_controller_filter):
                continue

            controllers.append(domain_vmm_controller_info)

        controllers = sorted(
            controllers,
            key=lambda i: i['name']
        )

        return controllers
