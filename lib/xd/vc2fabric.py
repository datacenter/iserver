import copy

from lib import ip_helper
from lib.xd import aci as aci_helper


def get_vms_macs(virtual_machines):
    macs = []
    for virtual_machine in virtual_machines:
        for nic in virtual_machine['nic']:
            macs.append(nic['macAddress'])
    return macs


def add_vms_fabric_connections(virtual_machines, log_id=None):
    endpoints = aci_helper.get_aci_endpoints(
        log_id=log_id,
        macs=get_vms_macs(virtual_machines)
    )

    if endpoints is not None:
        for virtual_machine in virtual_machines:
            expanded_nics = []
            for nic in virtual_machine['nic']:
                expanded_nic = copy.deepcopy(nic)
                expanded_nic['fabric'] = ''
                expanded_nic['node'] = ''
                expanded_nic['port'] = ''

                added = False
                for endpoint in endpoints:
                    if ip_helper.is_mac_equal(nic['macAddress'], endpoint['mac']):
                        if len(endpoint['fabric']) == 0:
                            expanded_nic['fabric'] = endpoint['apic']
                            expanded_nics.append(expanded_nic)
                            added = True
                            break

                        for fabric_path in endpoint['fabric']:
                            expanded_nic['fabric'] = endpoint['apic']
                            expanded_nic['node'] = fabric_path['node_id']
                            expanded_nic['port'] = fabric_path['ep']
                            expanded_nics.append(expanded_nic)

                        added = True
                        break

                if not added:
                    expanded_nics.append(expanded_nic)

            virtual_machine['nic'] = copy.deepcopy(expanded_nics)

    return virtual_machines
