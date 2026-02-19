from lib.md.vc.vm.nic.ucsm_blade import MdVcVmNicUcsmBladeOutput
from lib.md.vc.vm.nic.ucsm_rack import MdVcVmNicUcsmRackOutput


class MdVcVmNicOutput(MdVcVmNicUcsmBladeOutput, MdVcVmNicUcsmRackOutput):
    def __init__(self):
        MdVcVmNicUcsmBladeOutput.__init__(self)
        MdVcVmNicUcsmRackOutput.__init__(self)

    def print_vc_vm_nic(self, vm, nic):
        self.print_page_header('vCenter - Virtual Machine - Network Connectivity')

        self.my_output.print_stream('## Virtual Machine', 'output')
        self.my_output.print_stream('- Name: %s' % (vm['name']), 'output')
        self.my_output.print_stream('- UUID: %s' % (vm['uuid']), 'output')
        self.my_output.print_stream('- Connection state: %s' % (vm['connectionState']), 'output')
        self.my_output.print_stream('- Power state: %s' % (vm['powerState']), 'output')
        if vm['up']:
            self.my_output.print_stream('- Up :white_check_mark:', 'output')
        else:
            self.my_output.print_stream('- Up :x:', 'output')

        self.my_output.print_stream('- Guest: %s' % (vm['guestFullName']), 'output')
        if vm['annotation'] is not None and len(vm['annotation']) > 0:
            self.my_output.print_stream('- Annotation: %s' % (vm['annotation']), 'output')
        self.my_output.print_stream('- VM Path: %s' % (vm['vmPathName']), 'output')

        self.my_output.print_stream('\nLocation', 'output')
        self.my_output.print_stream('- vCenter: [%s](../%s-vm.md)' % (vm['vcenter'], vm['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: [%s](./%s.md)' % (vm['clusterName'], vm['cluster_hash']), 'output')
        self.my_output.print_stream('- Host: [%s](./%s.md)' % (vm['host'], vm['host_hash']), 'output')

        if not nic['fabric']['collected']:
            self.my_output.print_stream('## Fabric Connection Summary', 'output')
            self.my_output.print_stream(':x: information not collected', 'output')
            self.my_output.print_stream('Reason - %s' % (nic['fabric']['reason']), 'output')
            self.save_output(nic['hash'], subdir='vc/nic')
            return

        if nic['fabric']['server']['management'] == 'UCSM' and nic['fabric']['server']['type'] == 'Blade':
            self.add_vc_vm_nic_ucsm_blade_summary(nic)
            self.add_vc_vm_nic_ucsm_blade_legend()
            self.add_vc_vm_nic_ucsm_blade_details(vm, nic['fabric'])

        if nic['fabric']['server']['management'] == 'UCSM' and nic['fabric']['server']['type'] == 'Rack':
            self.add_vc_vm_nic_ucsm_rack_summary(nic)

        # self.my_output.print_stream('## Debug', 'output')
        # self.my_output.print_stream('```%s```' % (json.dumps(nic, indent=4)), 'output')

        self.save_output(nic['hash'], subdir='vc/nic')
