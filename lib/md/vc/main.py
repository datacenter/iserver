import os
from lib import file_helper
from lib.md.vc.cluster import MdVcClusterOutput
from lib.md.vc.dvs import MdVcDvsOutput
from lib.md.vc.host import MdVcHostOutput
from lib.md.vc.net import MdVcNetOutput
from lib.md.vc.nic import MdVcNicOutput
from lib.md.vc.switch import MdVcSwitchOutput
from lib.md.vc.vm.main import MdVcVmOutput
from lib.md.vc.vnic import MdVcVnicOutput


class MdVcOutput(
        MdVcClusterOutput,
        MdVcDvsOutput,
        MdVcHostOutput,
        MdVcNetOutput,
        MdVcNicOutput,
        MdVcSwitchOutput,
        MdVcVmOutput,
        MdVcVnicOutput
    ):
    def __init__(self):
        MdVcClusterOutput.__init__(self)
        MdVcDvsOutput.__init__(self)
        MdVcHostOutput.__init__(self)
        MdVcNetOutput.__init__(self)
        MdVcNicOutput.__init__(self)
        MdVcSwitchOutput.__init__(self)
        MdVcVmOutput.__init__(self)
        MdVcVnicOutput.__init__(self)

    def add_vc_host(self, line, item, up=False, down=False, name='name', hname='hash'):
        base = './'
        if up:
            base = '../'
        if down:
            base = './vc/'

        line = self.add_column(
            line,
            '[%s](%shost/%s.md)' % (
                item[name],
                base,
                item[hname]
            )
        )

        return line

    def add_vc_host_link(self, line, link_type, item, up=False, down=False, name='_name', hname='hash'):
        base = './'
        if up:
            base = '../'
        if down:
            base = './vc/'

        line = self.add_column(
            line,
            '[%s](%s%s/%s.md)' % (
                item[name],
                base,
                link_type,
                item[hname]
            )
        )

        return line

    def print_vc_host_bar(self, current_host, hosts):
        line = ''
        for host in hosts:
            if host['name'] == current_host['name']:
                line = '%s%s ' % (line, host['_name'])
            else:
                if host['_ready']:
                    line = '%s[%s](./%s.md) ' % (line, host['_name'], host['hash'])

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_vc_cluster_bar(self, current_cluster, clusters):
        line = ''
        for cluster in clusters:
            if cluster['name'] == current_cluster['name']:
                line = '%s%s ' % (line, cluster['_name'])
            else:
                line = '%s[%s](./%s.md) ' % (line, cluster['_name'], cluster['hash'])

        self.my_output.print_stream(
            '\n%s\n' % (line.strip()),
            'output'
        )

    def print_vc_bar(self, vcenter, section):
        line = '\n[Back](../README.md)'
        if section == 'hosts':
            line = '%s Hosts' % (line)
        else:
            line = '%s [Hosts](./%s-hosts.md)' % (line, vcenter)

        if section == 'dvs':
            line = '%s DVS' % (line)
        else:
            line = '%s [DVS](./%s-dvs.md)' % (line, vcenter)

        if section == 'net':
            line = '%s Net' % (line)
        else:
            line = '%s [Net](./%s-net.md)' % (line, vcenter)

        if section == 'vm':
            line = '%s VM' % (line)
        else:
            line = '%s [VM](./%s-vm.md)' % (line, vcenter)

        self.my_output.print_stream(
            line,
            'output'
        )

    def print_vc_host_page_header(self, title, host, hosts):
        self.print_page_header('vCenter Host - %s' % (title))
        self.print_vc_host_bar(host, hosts)
        self.my_output.print_stream('[Back](../../README.md)', 'output')

        self.my_output.print_stream(
            '## Host\n',
            'output'
        )

        self.my_output.print_stream('- vCenter: %s' % (host['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: %s' % (host['clusterName']), 'output')
        self.my_output.print_stream('- Host: %s' % (host['name']), 'output')
        self.my_output.print_stream('', 'output')

    def print_vc_cluster_page_header(self, title, cluster, clusters):
        self.print_page_header('vCenter Cluster - %s' % (title))
        self.print_vc_cluster_bar(cluster, clusters)
        self.my_output.print_stream('[Back](../../README.md)', 'output')

        self.my_output.print_stream(
            '## Cluster\n',
            'output'
        )

        self.my_output.print_stream('- vCenter: %s' % (cluster['vcenter']), 'output')
        self.my_output.print_stream('- Cluster: %s' % (cluster['name']), 'output')
        self.my_output.print_stream('', 'output')

    def print_vc_page_header(self, vcenter, title, section):
        self.print_page_header('vCenter - %s' % (title))
        self.print_vc_bar(vcenter, section)

    def get_vc_template_dir(self):
        main_dir = file_helper.get_main_dir()
        if main_dir is None:
            return None

        directory = os.path.join(
            os.path.join(
                os.path.join(
                    main_dir,
                    'templates'
                ),
                'md'
            ),
            'vc'
        )

        return directory

    def print_vc(self, vcenter):
        self.my_output.default('vCenter: %s' % (vcenter))

        self.copy_file(
            os.path.join(self.get_compute_template_dir(), 'ucsm-blade.png'),
            'ucsm-blade.png',
            subdir='vc/nic'
        )

        self.copy_file(
            os.path.join(self.get_compute_template_dir(), 'generic-vic-connectivity.png'),
            'generic-vic-connectivity.png',
            subdir='vc/nic'
        )

        self.vc_dvs_count[vcenter]['__ALL__'] = 0
        self.vc_dvs_up_count[vcenter]['__ALL__'] = 0
        self.vc_net_count[vcenter]['__ALL__'] = 0
        self.vc_net_up_count[vcenter]['__ALL__'] = 0
        self.vc_vm_count[vcenter]['__ALL__'] = 0
        self.vc_vm_up_count[vcenter]['__ALL__'] = 0

        clusters = self.xd_handler.get_vc_cluster(vcenter)
        hosts = self.xd_handler.get_vc_host(vcenter)
        networks = self.xd_handler.get_vc_network(vcenter)
        dvs = self.xd_handler.get_vc_dvs(vcenter)
        vms = self.xd_handler.get_vc_vm(vcenter)

        self.print_vc_dvses(vcenter, dvs, vms, hosts)
        self.print_vc_nets(vcenter, networks, hosts, dvs, vms)
        self.print_vc_vms(vcenter, vms)

        for host in hosts:
            self.vc_nic_count[vcenter][host['name']] = 0
            self.vc_nic_up_count[vcenter][host['name']] = 0
            self.vc_vnic_count[vcenter][host['name']] = 0
            self.vc_vnic_up_count[vcenter][host['name']] = 0
            self.vc_switch_count[vcenter][host['name']] = 0
            self.vc_switch_up_count[vcenter][host['name']] = 0
            self.vc_dvs_count[vcenter][host['name']] = 0
            self.vc_dvs_up_count[vcenter][host['name']] = 0
            self.vc_net_count[vcenter][host['name']] = 0
            self.vc_net_up_count[vcenter][host['name']] = 0
            self.vc_vm_count[vcenter][host['name']] = 0
            self.vc_vm_up_count[vcenter][host['name']] = 0

            if 'pnet' not in host or host['pnet'] is None:
                self.my_output.error(
                    'No net info: %s %s' % (host['vcenter'], host['name'])
                )
            else:
                self.print_vc_host_nics(host, hosts)
                self.print_vc_host_vnics(host, hosts)
                self.print_vc_host_switches(host, hosts)
                self.print_vc_host_dvses(host, hosts, networks, vms)

            if 'network' not in host or host['network'] is None:
                self.my_output.error(
                    'No network info: %s %s' % (vcenter, host['name'])
                )
            else:
                self.print_vc_host_nets(host, hosts)

            if 'vm' not in host or host['vm'] is None:
                self.my_output.error(
                    'No vm info: %s %s' % (vcenter, host['name'])
                )
            else:
                self.print_vc_host_vms(host, hosts)

        for cluster in clusters:
            self.vc_vm_count[vcenter][cluster['name']] = 0
            self.vc_vm_up_count[vcenter][cluster['name']] = 0

            self.print_vc_cluster_hosts(cluster, clusters, hosts)
            self.print_vc_cluster_vms(cluster, clusters, hosts)

        self.print_vc_hosts(vcenter, hosts)
