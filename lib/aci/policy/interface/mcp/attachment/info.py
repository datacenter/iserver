from lib import filter_helper


class PolicyInterfaceMcpAttachmentInfo():
    def __init__(self):
        self.policy_interface_mcp_attachment = None

    def get_policy_interface_mcp_attachment_info(self, managed_object):
        # "childAction": "",
        # "dn": "topology/pod-1/node-2101/sys/phys-[eth1/33]/rsmcpIfPolCons",
        # "forceResolve": "yes",
        # "lcOwn": "local",
        # "modTs": "2023-03-02T20:36:22.878+02:00",
        # "parentSKey": "eth1/33",
        # "rType": "mo",
        # "selectorType": "none",
        # "sourceRelStateQual": "none",
        # "state": "formed",
        # "stateQual": "none",
        # "status": "",
        # "tCl": "mcpIfPol",
        # "tDn": "uni/infra/mcpIfP-default",
        # "tType": "mo"
        info = {}
        info['podId'] = managed_object['dn'].split('/')[1].split('-')[1]
        info['nodeId'] = managed_object['dn'].split('/')[2].split('-')[1]
        info['nodeName'] = self.get_node_name(
            info['nodeId'],
            pod_id=info['podId']
        )
        info['apic'] = self.apic_name
        info['pod_node_name'] = 'pod-%s/%s' % (
            info['podId'],
            info['nodeName']
        )

        info['interfaceId'] = managed_object['parentSKey']
        info['policyType'] = managed_object['tCl']
        info['policyDn'] = managed_object['tDn']
        info['policyName'] = managed_object['tDn'].split('/')[2][7:]

        return info

    def get_policy_interface_mcp_attachments_info(self):
        if self.policy_interface_mcp_attachment is not None:
            return self.policy_interface_mcp_attachment

        managed_objects = self.get_policy_interface_mcp_attachment_mo()
        if managed_objects is not None:
            self.policy_interface_mcp_attachment = []
            for managed_object in managed_objects:
                self.policy_interface_mcp_attachment.append(
                    self.get_policy_interface_mcp_attachment_info(
                        managed_object
                    )
                )

        return self.policy_interface_mcp_attachment

    def match_policy_interface_mcp_attachment(self, attachment_info, attachment_filter):
        if attachment_filter is None or len(attachment_filter) == 0:
            return True

        for ap_rule in attachment_filter:
            key = ap_rule.split(':')[0]
            value = ':'.join(ap_rule.split(':')[1:])

            if key == 'policy_dn':
                if not filter_helper.match_string(value, attachment_info['policyDn']):
                    return False

            if key == 'policy_name':
                if not filter_helper.match_string(value, attachment_info['policyName']):
                    return False

            if key == 'pod':
                if not filter_helper.match_string(value, attachment_info['podId']):
                    return False

            if key == 'node':
                if not filter_helper.match_string(value, attachment_info['nodeName']):
                    return False

        return True

    def get_policy_interface_mcp_attachments(self, attachment_filter=None):
        all_attachments = self.get_policy_interface_mcp_attachments_info()
        if all_attachments is None:
            return None

        attachments = []

        for attachment_info in all_attachments:
            if not self.match_policy_interface_mcp_attachment(attachment_info, attachment_filter):
                continue

            attachments.append(
                attachment_info
            )

        attachments = sorted(
            attachments,
            key=lambda i: (
                i['podId'],
                int(i['nodeId']),
                i['interfaceId']
            )
        )

        return attachments

    def get_policy_interface_mcp_attachments_node_summary(self, attachments):
        nodes = {}
        for attachment in attachments:
            if attachment['pod_node_name'] not in nodes:
                nodes[attachment['pod_node_name']] = 0

        for attachment in attachments:
            nodes[attachment['pod_node_name']] = nodes[attachment['pod_node_name']] + 1

        summary = []
        for node in nodes:
            item = {}
            item['pod_node_name'] = node
            item['interfaces'] = nodes[node]
            summary.append(item)

        summary = sorted(
            summary,
            key=lambda i: i['pod_node_name']
        )
        return summary
