import json
import time
import traceback
import requests

from progress.bar import Bar


class Api():
    def __init__(self, apic_ip, apic_port, username, password):
        self.apic_ip = apic_ip
        self.apic_port = apic_port
        self.apic_username = username
        self.apic_password = password

        self.session_connected = False
        self.token = None
        self.request_info = {}

        self.api_fault_limit = 1000
        self.api_event_limit = 1000
        self.api_audit_limit = 1000

    def get_apic_ip(self):
        return self.apic_ip

    def get_request_info(self):
        return self.request_info

    def get_token(self, generate_if_none=False):
        if generate_if_none and self.token is None:
            self.generate_token()
        return self.token

    def generate_token(self):
        url = "https://%s:%s/api/aaaLogin.json" % (
            self.apic_ip,
            self.apic_port
        )

        payload = {
            "aaaUser": {
                "attributes": {
                    "name": self.apic_username,
                    "pwd": self.apic_password
                }
            }
        }

        headers = {
            "Content-Type": "application/json"
        }

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        try:
            response = requests.post(
                url,
                data=json.dumps(
                    payload
                ),
                headers=headers,
                verify=False
            ).json()
            self.token = response['imdata'][0]['aaaLogin']['attributes']['token']
            self.session_connected = True
        except BaseException:
            self.log.error(
                'apic.connect',
                traceback.format_exc()
            )
            self.session_connected = False
            self.my_output.error(
                'Failed to connect: %s:%s' % (
                    self.apic_ip,
                    self.apic_port
                )
            )

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.log.apic(
            'connect %s:%s' % (
                self.apic_ip,
                self.apic_port
            ),
            self.session_connected,
            duration_ms
        )

    def is_connected(self):
        if self.apic_settings is not None and not self.apic_settings['online']:
            return False

        if self.token is None:
            self.generate_token()
            if self.token is None:
                return False

        return True

    def get_mo_children_attributes(self, mo_name, managed_object, child_name, include_grandchildren=False):
        attributes = []
        if 'children' in managed_object[mo_name]:
            for child in managed_object[mo_name]['children']:
                for key in child:
                    if key == child_name:
                        child_attributes = child[child_name]['attributes']
                        if include_grandchildren:
                            if 'children' in child[child_name]:
                                for grandchild in child[child_name]['children']:
                                    for grandkey in grandchild:
                                        child_attributes[grandkey] = grandchild[grandkey]['attributes']

                        attributes.append(
                            child_attributes
                        )

        return attributes

    def get_mo_child_attributes(self, mo_name, managed_object, child_name, include_grandchildren=False):
        if 'children' in managed_object[mo_name]:
            for child in managed_object[mo_name]['children']:
                for key in child:
                    if key == child_name:
                        child_attributes = child[child_name]['attributes']
                        if include_grandchildren:
                            if 'children' in child[child_name]:
                                for grandchild in child[child_name]['children']:
                                    for grandkey in grandchild:
                                        child_attributes[grandkey] = grandchild[grandkey]['attributes']

                        return child_attributes

        return None

    def get_mo_node_resource_ctx(self, mo_name, managed_object):
        resources = []
        if 'children' in managed_object[mo_name]:
            for child in managed_object[mo_name]['children']:
                for key in child:
                    if key == 'pconsNodeDeployCtx':
                        if 'children' in child[key]:
                            for item in child[key]['children']:
                                for ckey in item:
                                    if ckey == 'pconsResourceCtx':
                                        resource = {}
                                        resource['deployStatus'] = child[key]['attributes']['deployStatus']
                                        resource['nodeId'] = child[key]['attributes']['nodeId']
                                        resource['ctxClass'] = item[ckey]['attributes']['ctxClass']
                                        resource['ctxDn'] = item[ckey]['attributes']['ctxDn']
                                        resources.append(
                                            resource
                                        )
        return resources

    def get_class(self, class_name, response_format='json', query_target_filter=None, query=None, node_class=False):
        self.request_info = {}
        self.request_info['url'] = '--'
        self.request_info['status_code'] = '--'
        self.request_info['duration'] = '--'
        self.request_info['error'] = None
        self.request_info['connected'] = True

        if not self.is_connected():
            self.request_info['connected'] = False
            return None

        if node_class:
            url = "https://%s:%s/api/node/class/%s.%s" % (
                self.apic_ip,
                self.apic_port,
                class_name,
                response_format
            )
        else:
            url = "https://%s:%s/api/class/%s.%s" % (
                self.apic_ip,
                self.apic_port,
                class_name,
                response_format
            )

        # if query is None:
        #     query = 'page=0&page-size=10000'
        # else:
        #     query = '%s&page=0&page-size=10000' % (query)

        if query is not None:
            url = '%s?%s' % (
                url,
                query
            )

        if query_target_filter is not None:
            url = '%s?query-target-filter=%s' % (
                url,
                query_target_filter
            )

        headers = {
            "Cookie": "APIC-Cookie=%s" % (self.token),
        }

        requests.packages.urllib3.disable_warnings()
        start_time = int(time.time() * 1000)
        success = True
        item_count = '-'
        try:
            self.request_info['url'] = url
            response = requests.get(
                url,
                headers=headers,
                verify=False
            )
            self.request_info['status_code'] = response.status_code
            if response.status_code >= 300:
                self.log.error(
                    'apic.get_class',
                    'Url %s response code %s' % (
                        url,
                        response.status_code
                    )
                )

                self.log.error(
                    'apic.get_class',
                    'Url %s response %s' % (
                        url,
                        response.content
                    )
                )

                self.request_info['error'] = response.content.decode('utf-8')
                success = False
                response = None

            if response is not None:
                if response_format == 'json':
                    response = response.json()
                    item_count = len(response['imdata'])
                else:
                    response = response.content

        except BaseException:
            self.log.error(
                'apic.get_class',
                traceback.format_exc()
            )
            response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.request_info['duration'] = duration_ms

        log_info = '%s:%s class %s' % (
            self.apic_ip,
            self.apic_port,
            class_name
        )
        if query_target_filter is not None:
            log_info = '%s filter %s' % (
                log_info,
                query_target_filter
            )
        if query is not None:
            log_info = '%s query %s' % (
                log_info,
                query
            )

        self.log.apic(
            log_info,
            success,
            duration_ms,
            item_count=item_count
        )

        return response

    def get_managed_object(self, distinguished_name, response_format='json', query_target_filter=None, query=None, node_mo=False):
        self.request_info = {}
        self.request_info['url'] = '--'
        self.request_info['status_code'] = '--'
        self.request_info['duration'] = '--'
        self.request_info['error'] = None
        self.request_info['connected'] = True

        if not self.is_connected():
            self.request_info['connected'] = False
            return None

        if node_mo:
            url = "https://%s:%s/api/node/mo/%s.%s" % (
                self.apic_ip,
                self.apic_port,
                distinguished_name,
                response_format
            )
        else:
            url = "https://%s:%s/api/mo/%s.%s" % (
                self.apic_ip,
                self.apic_port,
                distinguished_name,
                response_format
            )

        if query is not None:
            url = '%s?%s' % (
                url,
                query
            )

        if query_target_filter is not None:
            url = '%s?query-target=%s' % (
                url,
                query_target_filter
            )

        headers = {
            "Cookie": "APIC-Cookie=%s" % (self.token),
        }

        start_time = int(time.time() * 1000)
        requests.packages.urllib3.disable_warnings()
        success = True
        item_count = None
        try:
            self.request_info['url'] = url
            response = requests.get(
                url,
                headers=headers,
                verify=False
            )
            self.request_info['status_code'] = response.status_code
            if response.status_code >= 300:
                self.log.error(
                    'apic.get_managed_object',
                    'Url %s response code %s' % (
                        url,
                        response.status_code
                    )
                )

                self.log.error(
                    'apic.get_managed_object',
                    'Url %s response %s' % (
                        url,
                        response.content
                    )
                )

                self.request_info['error'] = response.content.decode('utf-8')
                success = False
                response = None

            if response is not None:
                if response_format == 'json':
                    response = response.json()
                    item_count = len(response['imdata'])
                else:
                    response = response.content

        except BaseException:
            self.log.error(
                'apic.get_managed_object',
                traceback.format_exc()
            )
            response = None
            success = False

        end_time = int(time.time() * 1000)
        duration_ms = end_time - start_time
        self.request_info['duration'] = duration_ms

        log_info = '%s:%s mo %s' % (
            self.apic_ip,
            self.apic_port,
            distinguished_name
        )
        if query_target_filter is not None:
            log_info = '%s filter %s' % (
                log_info,
                query_target_filter
            )
        if query is not None:
            log_info = '%s query %s' % (
                log_info,
                query
            )

        self.log.apic(
            log_info,
            success,
            duration_ms,
            item_count=item_count
        )

        return response

    def get_mos(self, bar_enabled=False):
        if bar_enabled:
            bar_handler = Bar('Global Objects', max=79)
            bar_handler.goto(0)

        self.get_application_profile_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_bridge_domains_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_contracts_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_filters_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_subjects_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_taboos_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_taboo_subjects_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_domain_aaa_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_domain_l2_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_domain_l3_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_domain_phy_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_domain_vmm_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_domain_vmm_epg_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_endpoints_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_endpoint_vmm_vnic_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_endpoint_vmm_vm_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_endpoint_vmm_hv_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_epgs_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_epg_locale_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_l2out_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_l3out_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_l3out_logical_node_profile_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_node_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_node_power_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_node_psu_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_node_sensor_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_node_system_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_node_temp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_fabric_path_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_group_access_interface_breakout_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_group_access_interface_port_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_group_access_interface_vpc_node_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_group_access_interface_vpc_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_global_aae_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_auth_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_auth_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_cdp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_cdp_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_copp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_copp_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_copp_protocol_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_dpp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_dpp_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_fc_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_fc_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_l2_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_l2_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_link_flap_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_link_flap_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_link_level_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_link_level_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_link_level_fc_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_link_level_fc_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_lldp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_lldp_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_mcp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_mcp_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_pfc_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_pfc_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_port_channel_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policies_interface_port_channel_info()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_port_channel_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_port_channel_member_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_port_channel_member_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_port_security_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_port_security_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_slow_drain_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_slow_drain_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_storm_control_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_storm_control_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_stp_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_stp_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_synce_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_synce_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_transceiver_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_policy_interface_transceiver_attachment_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_pool_vlan_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_tenant_mo()
        if bar_enabled:
            bar_handler.next()

        self.get_vrfs_mo()
        if bar_enabled:
            bar_handler.next()

        if bar_enabled:
            bar_handler.finish()

        nodes = self.get_nodes()
        for node in nodes:
            if bar_enabled:
                bar_handler = Bar('Node Objects: %s' % (node['id']), max=59)

            self.get_adjacency_cdp_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_adjacency_lacp_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_adjacency_lldp_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_cloudsec_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_encap_routed_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_fc_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_fcpc_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_node_address_ipv4_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_node_interface_ipv4_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_node_address_ipv6_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_node_interface_ipv6_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interfaces_lacp_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_lacp_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_loopback_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_macsec_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_management_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_management_state_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_management_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_cap_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_eee_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_load_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_pc_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_rmon_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_ether_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_fc_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_phy_qos_stats_mo(
                node['podId'],
                node['id'],
                cache_enabled=False
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_port_channels_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_svi_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_tunnel_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interface_vfc_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_interfaces_virtual_port_channel_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_vlan_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_node_interface_policy_profile_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_arp_domains_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_arp_adjacencies_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_bfd_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_bfd_interfaces_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_bfd_sessions_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_bgp_domains_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_bgp_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_bgp_neighbors_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_cdp_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_cdp_interfaces_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_cdp_neighbors_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_hsrp_domains_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_hsrp_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_hsrp_interfaces_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_ipv4_domains_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_ipv6_domains_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_isis_domains_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_isis_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_lacp_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_lldp_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_lldp_stats_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_nd_domain_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_nd_instance_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_nd_interface_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            self.get_protocol_nd_neighbor_mo(
                node['podId'],
                node['id']
            )
            if bar_enabled:
                bar_handler.next()

            if bar_enabled:
                bar_handler.finish()

        # get_interface_fault_counts_mo(self, pod_id, node_id, interface_type, interface_id)

        # get_interface_macsec_castats_mo(self, pod_id, node_id, interface_id)
        # get_interface_macsec_rx_mo(self, pod_id, node_id, interface_id)
        # get_interface_macsec_stats_mo(self, pod_id, node_id, interface_id)
        # get_interface_macsec_tx_mo(self, pod_id, node_id, interface_id)

        # get_interface_phy_epg_stats_mo(self, pod_id, node_id, interface_id)

        # get_interface_policy_profile_mo(self, profile_name)
        # get_interface_port_channel_relations_mo(self, pod_id, node_id, port_channel_id)
        # get_policy_group_access_interface_vpc_port_mo(self, policy_group_name, node_id)
        # get_policy_snoop_igmp_mo(self, tenant, name)
        # get_policy_snoop_mld_mo(self, tenant, name)
        # get_protocol_bfd_session_peer_mo(self, pod_id, node_id, session_id)
        # get_protocol_bfd_session_stats_mo(self, pod_id, node_id, session_id)
        # get_protocol_bgp_neighbor_stats_mo(self, pod_id, node_id, bgp_domain_name, bgp_peer_addr, bgp_state_addr)
        # get_protocol_ipv4_routes_mo(self, pod_id, node_id, ipv4_domain_name)
        # get_protocol_ipv6_routes_mo(self, pod_id, node_id, ipv6_domain_name)
        # get_protocol_isis_domain_interfaces_mo(self, pod_id, node_id, instance_name, domain_name)
        # get_protocol_isis_domain_lsps_mo(self, pod_id, node_id, instance_name, domain_name)
        # get_protocol_isis_domain_neighbors_mo(self, pod_id, node_id, instance_name, domain_name)
        # get_protocol_isis_domain_routes_mo(self, pod_id, node_id, instance_name, domain_name)
        # get_protocol_isis_domain_trees_mo(self, pod_id, node_id, instance_name, domain_name)
        # get_protocol_isis_domain_tunnels_mo(self, pod_id, node_id, instance_name, domain_name)
        # get_vrf_ipv4_mo(self, tenant, name)
        # get_vrf_ipv6_mo(self, tenant, name)
