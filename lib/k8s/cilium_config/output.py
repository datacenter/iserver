import json
import yaml
from lib import filter_helper


class K8sCiliumConfigOutput():
    def __init__(self):
        pass

    def print_cilium_config(self, info):
        self.my_output.default(
            yaml.safe_dump(info['spec']), 
            before_newline=True, 
            wrap='~~~'
        )

    def print_cilium_config_state(self, info):
        self.my_output.default('Cilium config state', underline=False, before_newline=True)
        if info['processing_error']:
            self.my_output.default(
                '- processing error: %s [reason:%s]' % (
                    self.my_output.add_color(info['processing_error'], 'Red'),
                    info['info']['processing_error_reason']
                )
            )
            self.my_output.default(
                info['info']['processing_error_message'],
                wrap='~~~'
            )
        else:
            self.my_output.default(
                '- processing error: %s' % (
                    self.my_output.add_color(info['processing_error'], 'Green')
                )
            )
            
        if info['values_error']:
            self.my_output.default(
                '- values error: %s [reason:%s]' % (
                    self.my_output.add_color(info['values_error'], 'Red'),
                    info['info']['values_error_reason']
                )
            )
            self.my_output.default(
                info['info']['values_error_message'],
                wrap='~~~'
            )
        else:
            self.my_output.default(
                '- values error: %s' % (
                    self.my_output.add_color(info['values_error'], 'Green')
                )
            )

    def print_cilium_mesh_status(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Cluster Name', 'cluster_name'],
                ['Cluster ID', 'cluster_id'],
                ['Cluster IP', 'ips'],
                ['Cluster Port', 'port'],
                ['Summary', 'agent_summary'],
                ['Cilium Agent', 'agent.metadata.pod'],
                ['Node', 'agent.metadata.node'],
                ['Node IP', 'agent.metadata.ip'],
                ['Ready', 'agent.readyTick']
            ]
        )

    def print_cilium_private_network_state(self, info, before_newline=True):
        if before_newline:
            self.my_output.default('')

        if info['enabled']:
            self.my_output.default('Private network %s' % (self.my_output.add_color('enabled', 'Green')))
            self.my_output.default('Cilium configuration', before_newline=True)
            self.my_output.default(yaml.dump(info['configuration']), wrap='~~~')
            self.print_cilium_private_network_webhook(info)
        else:
            self.my_output.default('Private network %s' % (self.my_output.add_color('disabled', 'Red')))

    def print_cilium_private_network_webhook(self, info):
        self.my_output.default('Private network webhook', before_newline=True)
        if info['webhook']['enabled']:
            self.my_output.default('- %s' % (self.my_output.add_color('enabled', 'Green')))
            if info['webhook']['configured']:
                self.my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], self.my_output.add_color('found', 'Green')))
            else:
                self.my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], self.my_output.add_color('not found', 'Red')))

            if info['webhook']['service_found']:
                self.my_output.default('- service %s %s' % (info['webhook']['service_name'], self.my_output.add_color('found', 'Green')))
            else:
                self.my_output.default('- service %s %s' % (info['webhook']['service_name'], self.my_output.add_color('not found', 'Red')))

            if len(info['webhook']['service_endpoints']) > 0:
                self.my_output.default('- service endpoints: %s' % (', '.join(info['webhook']['service_endpoints'])))
            else:
                self.my_output.default('- service endpoints %s' % (self.my_output.add_color('not found', 'Red')))
        else:
            self.my_output.default('- %s' % (self.my_output.add_color('disabled', 'Red')))
            if info['webhook']['configured']:
                self.my_output.default('- mutating webhook %s %s' % (info['webhook']['name'], self.my_output.add_color('found', 'Red')))
            if info['webhook']['service_found']:
                self.my_output.default('- service %s %s' % (info['webhook']['service_name'], self.my_output.add_color('found', 'Red')))

    def print_cilium_agent_private_networks_state(self, info):
        for item in info:
            item['subnetT'] = json.dumps(item['Subnets'], indent=2).split('\n')

        self.my_output.default('Cilium Agent DB: private-networks', up_and_down='~', before_newline=True)
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network', 'Name'],
                ['ID', 'ID'],
                ['VNI', 'VNI'],
                ['Subnet', 'subnetT']
            ]
        )

    def print_cilium_agent_privnet_endpoints_state(self, info):
        self.my_output.default('Cilium Agent DB: privnet-endpoints', up_and_down='~', before_newline=True)
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network', 'network.name'],
                ['Subnet', 'Subnet'],
                ['Namespace', 'source.namespace'],
                ['Name', 'name'],
                ['IP', 'network.ip'],
                ['MAC', 'network.mac'],
                ['POD IP', 'ip'],
                ['Node', 'nodeName'],
                ['External', 'flags.external']
            ]
        )

    def print_cilium_agent_privnet_routes_state(self, info):
        for item in info:
            item['peerT'] = json.dumps(item['Peer'], indent=2).split('\n')

        self.my_output.default('Cilium Agent DB: privnet-routes', up_and_down='~', before_newline=True)
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network', 'Network'],
                ['Subnet', 'Subnet'],
                ['Destination', 'Destination'],
                ['Gateway', 'Gateway'],
                ['EVPN', 'EVPNGateway'],
                ['Peer', 'peerT']
            ]
        )

    def print_cilium_agent_privnet_node_attachments_state(self, info):
        for item in info:
            item['interfaceT'] = '%s [%s]' % (
                filter_helper.get(item, 'Interface:Name'),
                filter_helper.get(item, 'Interface:Index')
            )
            error = filter_helper.get(item, 'Interface:Error', on_error='', on_none='')
            if len(error) > 0:
                item['interfaceT'] = [item['interfaceT'], error]

            item['conflictT'] = filter_helper.get(item, 'Conflict', on_error='', on_none='')
            if item['conflictT'] == 'none':
                item['conflictT'] = None

        self.my_output.default('Cilium Agent DB: privnet-node-attachments', up_and_down='~', before_newline=True)
        self.my_output.my_table_ng(
            info,
            [
                ['Name', 'Resource.Name'],
                ['Network', 'Network'],
                ['Type', 'Type'],
                ['Interface', 'interfaceT'],
                ['Conflict', 'conflictT'],
                ['Status', 'OpsStatus.kind']
            ]
        )

    def print_cilium_agent_privnet_inbs_state(self, info):
        self.my_output.default('Cilium Agent DB: privnet-inbs', up_and_down='~', before_newline=True)
        self.my_output.default(json.dumps(info, indent=4))

    def print_cilium_agent_privnet_mapentries_state(self, info):
        for item in info:
            item['networkT'] = '%s [%s]' % (
                filter_helper.get(item, 'Target:NetworkName'),
                filter_helper.get(item, 'Target:ID:Network')
            )
            item['subnetT'] = '%s [%s]' % (
                filter_helper.get(item, 'Target:SubnetName'),
                filter_helper.get(item, 'Target:ID:Subnet')
            )
                
        self.my_output.default('Cilium Agent DB: privnet-mapentries', up_and_down='~', before_newline=True)
        self.my_output.my_table_ng(
            info,
            [
                ['Type', 'Type'],
                ['Network', 'networkT'],
                ['Subnet', 'subnetT'],
                ['CIDR', 'Target.CIDR'],
                ['MAC', 'Target.MAC'],
                ['NH', 'Routing.NextHop'],
                ['IfIndex', 'Routing.EgressIfIndex'],
                ['VNI', 'Routing.VNI'],
                ['L2 Announce', 'Routing.L2Announce'],
                ['Status', 'Status.kind'],
                ['Gneigh', 'GneighStatus.kind']
            ]
        )

    def print_cilium_agent_privnet_subnets_state(self, info):
        for item in info:
            item['networkT'] = '%s [%s]' % (
                filter_helper.get(item, 'Network'),
                filter_helper.get(item, 'NetworkID')
            )
            item['subnetT'] = '%s [%s]' % (
                filter_helper.get(item, 'Name'),
                filter_helper.get(item, 'ID')
            )
            item['egressT'] = '%s [%s]' % (
                filter_helper.get(item, 'EgressIfName'),
                filter_helper.get(item, 'EgressIfIndex')
            )
            item['routeT'] = json.dumps(item['Routes'], indent=2).split('\n')

        self.my_output.default('Cilium Agent DB: privnet-subnets', up_and_down='~', before_newline=True)
        self.my_output.my_table_ng(
            info,
            [
                ['Private Network', 'networkT'],
                ['Subnet', 'subnetT'],
                ['DHCP', 'DHCP.mode'],
                ['CIDRv4', 'CIDRv4'],
                ['CIDRv6', 'CIDRv6'],
                ['VNI', 'VNI'],
                ['Route', 'routeT']
            ]
        )