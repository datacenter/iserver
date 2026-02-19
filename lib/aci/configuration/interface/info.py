class ConfigurationInterfaceInfo():
    def __init__(self):
        pass

    def get_configuration_interface_infra_port_breakout_info(self, managed_object):
        info = {}

        info['policyName'] = managed_object['assocGrp'].split('/brkoutportgrp-')[1]
        if managed_object['assocGrpExist'] == 'yes' and managed_object['assocGrpOverrideExist'] == 'no':
            info['policyApplied'] = True
        else:
            info['policyApplied'] = False

        keys = [
            'assocGrpExist',
            'assocGrpOverride',
            'assocGrpOverrideExist',
            'brkoutMap',
            'description',
            'mode',
            'pod',
            'node',
            'nodeSelectorDn',
            'portSelectorDn',
            'portTypeRole',
            'shutdown'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        info['interfaceId'] = '%s/%s' % (managed_object['card'], managed_object['port'])
        return info

    def get_configuration_interface_infra_port_group_info(self, managed_object):
        info = {}

        info['policyName'] = managed_object['assocGrp'].split('/accportgrp-')[1]
        if managed_object['assocGrpExist'] == 'yes' and managed_object['assocGrpOverrideExist'] == 'no':
            info['policyApplied'] = True
        else:
            info['policyApplied'] = False

        keys = [
            'assocGrpExist',
            'assocGrpOverride',
            'assocGrpOverrideExist',
            'description',
            'mode',
            'pod',
            'node',
            'nodeSelectorDn',
            'portSelectorDn',
            'portTypeRole',
            'shutdown'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if managed_object['subPort'] == "0":
            info['interfaceId'] = '%s/%s' % (managed_object['card'], managed_object['port'])
        else:
            info['interfaceId'] = '%s/%s/%s' % (managed_object['card'], managed_object['port'], managed_object['subPort'])
        return info

    def get_configuration_interface_infra_port_bundle_info(self, managed_object):
        info = {}

        info['policyName'] = managed_object['assocGrp'].split('/accbundle-')[1]
        if managed_object['assocGrpExist'] == 'yes' and managed_object['assocGrpOverrideExist'] == 'no':
            info['policyApplied'] = True
        else:
            info['policyApplied'] = False

        keys = [
            'assocGrpExist',
            'assocGrpOverride',
            'assocGrpOverrideExist',
            'description',
            'mode',
            'pod',
            'node',
            'nodeSelectorDn',
            'pcDescription',
            'pcPortDn',
            'portSelectorDn',
            'portTypeRole',
            'shutdown'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        if managed_object['subPort'] == "0":
            info['interfaceId'] = '%s/%s' % (managed_object['card'], managed_object['port'])
        else:
            info['interfaceId'] = '%s/%s/%s' % (managed_object['card'], managed_object['port'], managed_object['subPort'])
        return info

    def get_configuration_interface_infra_port_info(self, managed_object):
        if len(managed_object['assocGrp'].split('/brkoutportgrp-')) == 2:
            return self.get_configuration_interface_infra_port_breakout_info(managed_object)

        if len(managed_object['assocGrp'].split('/accportgrp-')) == 2:
            return self.get_configuration_interface_infra_port_group_info(managed_object)

        if len(managed_object['assocGrp'].split('/accbundle-')) == 2:
            return self.get_configuration_interface_infra_port_bundle_info(managed_object)

        self.log.error(
            'get_configuration_interface_infra_port_info',
            'Unsupported assocGrp: %s' % (managed_object['assocGrp'])
        )

        return None

    def get_configuration_interface_fabric_port_info(self, managed_object):
        info = {}
        for key in managed_object:
            info[key] = managed_object[key]
        return info

    def get_configuration_interface_infra_bundle_info(self, managed_object):
        info = {}

        if len(managed_object['assocGrp'].split('/accbundle-')) != 2:
            self.log.error(
                'get_configuration_interface_infra_bundle_info',
                'Unsupported assocGrp: %s' % (managed_object['assocGrp'])
            )
            return None

        info['policyName'] = managed_object['assocGrp'].split('/accbundle-')[1]
        if managed_object['assocGrpExist'] == 'yes' and managed_object['assocGrpOverrideExist'] == 'no':
            info['policyApplied'] = True
        else:
            info['policyApplied'] = False

        keys = [
            'assocGrpExist',
            'assocGrpOverride',
            'assocGrpOverrideExist',
            'description',
            'mode',
            'nodeA',
            'nodeB',
            'podA',
            'podB',
            'pcShutdown',
            'pcPortDn'
        ]
        for key in keys:
            info[key] = None
            if key in managed_object:
                info[key] = managed_object[key]

        return info

    def get_configuration_interface_info(self, interface_type, configuration):
        if interface_type == 'infraPortSummary':
            return self.get_configuration_interface_infra_port_info(configuration)

        if interface_type == 'fabricPortSummary':
            return self.get_configuration_interface_fabric_port_info(configuration)

        if interface_type == 'infraBundleSummary':
            return self.get_configuration_interface_infra_bundle_info(configuration)

        self.log.error(
            'get_configuration_interface_info',
            'Unsupported mo: [%s] %s' % (interface_type, configuration)
        )
        return None

    def get_configuration_interfaces(self, cache_enabled=True):
        if not cache_enabled:
            self.init_configuration_interface_mo()

        configurations = self.get_configuration_interface_mo(cache_enabled=cache_enabled)
        if configurations is None:
            return None

        info = {}
        for key in self.configuration_interface_types:
            info[key] = []

            for configuration in configurations[key]:
                if len(configuration['assocGrp']) == 0:
                    continue

                configuration_info = self.get_configuration_interface_info(key, configuration)
                if configuration_info is not None:
                    info[key].append(
                        configuration_info
                    )
                    continue

                self.log.error(
                    'get_configuration_interfaces',
                    'Failed to get info: %s' % (configuration)
                )

        for bundle in info['infraBundleSummary']:
            bundle['interfaces'] = []
            for port in info['infraPortSummary']:
                if port['mode'] != 'vpc':
                    continue

                if port['policyName'] == bundle['policyName']:
                    bundle['interfaces'].append(
                        dict(
                            pod=port['pod'],
                            node=port['node'],
                            interfaceId=port['interfaceId']
                        )
                    )

        return info

    def get_configuration_vpc(self, policy_name, cache_enabled=True):
        configurations = self.get_configuration_interfaces(cache_enabled=cache_enabled)
        if configurations is None:
            return None

        for bundle in configurations['infraBundleSummary']:
            if bundle['policyName'] == policy_name:
                return bundle

        return None

    def get_configuration_interface(self, pod, node, interface_id, cache_enabled=True):
        configurations = self.get_configuration_interfaces(cache_enabled=cache_enabled)
        if configurations is None:
            return None

        interface_configurations = []

        for port in configurations['infraPortSummary']:
            if port['pod'] != pod:
                continue

            if port['node'] != node:
                continue

            if port['interfaceId'] != interface_id:
                continue

            interface_configurations.append(
                port
            )

        return interface_configurations
