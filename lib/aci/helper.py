from lib import ip_helper


def get_aci_interface_type(name):
    if name is None:
        return None

    name = name.lower()

    if len(name.split('eth')) == 2:
        return 'eth'

    if len(name.split('mgmt')) == 2:
        return 'mgmt'

    if len(name.split('port-channel')) == 2:
        return 'pc'

    if len(name.split('po')) == 2:
        return 'pc'

    if len(name.split('vlan')) == 2:
        return 'vlan'

    if len(name.split('loopback')) == 2:
        return 'loopback'

    return None

def get_aci_interface_id(name):
    interface_type = get_aci_interface_type(name)
    if interface_type is None:
        return None

    name = name.lower()

    if interface_type == 'mgmt':
        return int(name.split('mgmt')[1])

    if interface_type == 'eth':
        if len(name.split('ethernet')) == 2:
            interface_index = name.split('ethernet')[1]
        else:
            interface_index = name.split('eth')[1]

        if len(interface_index.split('/')) == 1:
            return int(interface_index)

        if len(interface_index.split('/')) == 2:
            index = int(interface_index.split('/')[0]) * 200
            index += int(interface_index.split('/')[1].split('.')[0])
            if len(interface_index.split('/')[1].split('.')) == 2:
                index += int(interface_index.split('/')[1].split('.')[1])
            return index

        if len(interface_index.split('/')) == 3:
            return int(interface_index.split('/')[0]) * 1000 + int(interface_index.split('/')[1]) * 200 + int(interface_index.split('/')[2])

        return -1

    if interface_type == 'pc':
        if len(name.split('port-channel')) == 2:
            interface_index = name.split('port-channel')[1]
        else:
            interface_index = name.split('po')[1]

        return int(interface_index)

    if interface_type == 'vlan':
        return name.split('vlan')[1]

    if interface_type == 'loopback':
        return name.split('loopback')[1]

    return None

def get_aci_interface_hash(controller_name, device_name, interface_name):
    interface_type = get_aci_interface_type(interface_name)
    interface_id = get_aci_interface_id(interface_name)

    if interface_type == 'mgmt':
        return ip_helper.get_string_md5(
            '%s %s mgmt%s' % (
                controller_name,
                device_name,
                interface_id
            )
        )

    if interface_type == 'eth':
        return ip_helper.get_string_md5(
            '%s %s Ethernet%s' % (
                controller_name,
                device_name,
                interface_id
            )
        )

    if interface_type == 'pc':
        return ip_helper.get_string_md5(
            '%s %s port-channel%s' % (
                controller_name,
                device_name,
                interface_id
            )
        )

    if interface_type == 'vlan':
        return ip_helper.get_string_md5(
            '%s %s Vlan%s' % (
                controller_name,
                device_name,
                interface_id
            )
        )

    if interface_type == 'loopback':
        return ip_helper.get_string_md5(
            '% %s loopback%s' % (
                controller_name,
                device_name,
                interface_id
            )
        )

    return None

def get_aci_object_hash(controller_name, mo=None, name_ap_tenant=None, name_tenant=None, name=None, extra=''):
    if mo is not None:
        if 'nameApTenant' in mo:
            return ip_helper.get_string_md5(
                '%s %s%s' % (
                    controller_name,
                    mo['nameApTenant'],
                    extra
                )
            )

        if 'nameTenant' in mo:
            return ip_helper.get_string_md5(
                '%s %s%s' % (
                    controller_name,
                    mo['nameTenant'],
                    extra
                )
            )

        return ip_helper.get_string_md5(
            '%s %s%s' % (
                controller_name,
                mo['name'],
                extra
            )
        )

    if name_ap_tenant is not None:
        return ip_helper.get_string_md5(
            '%s %s%s' % (
                controller_name,
                name_ap_tenant,
                extra
            )
        )

    if name_tenant is not None:
        return ip_helper.get_string_md5(
            '%s %s%s' % (
                controller_name,
                name_tenant,
                extra
            )
        )

    if name is not None:
        return ip_helper.get_string_md5(
            '%s %s%s' % (
                controller_name,
                name,
                extra
            )
        )

    return None

def is_aci_interface_equal(inta, intb):
    if intb is None or inta is None:
        return False

    inta_type = get_aci_interface_type(inta)
    intb_type = get_aci_interface_type(intb)
    if inta_type is None or intb_type is None:
        return False

    if inta_type != intb_type:
        return False

    inta_id = get_aci_interface_id(inta)
    intb_id = get_aci_interface_id(intb)
    if inta_id is None or intb_id is None:
        return False

    if inta_id != intb_id:
        return False

    return True

def get_policy_type_from_tcl(policy_type):
    mapping = {}
    mapping['infraInfra'] = 'Access Infra'
    mapping['infraAccNodePGrp'] = 'Access Switch'
    mapping['infraSpineAccNodePGrp'] = 'Spine Switch'
    mapping['infraSpAccPortGrp'] = 'Spine Access Port'
    mapping['infraAccPortGrp'] = 'Leaf Access Port'
    mapping['infraAccBndlGrp'] = 'PC/VPC Interface'
    mapping['infraBrkoutPortGrp'] = 'Breakout'
    mapping['vmmDomP'] = 'VMM Domain'
    mapping['vmmVSwitchPolicyCont'] = 'VMM Virtual Switch'

    if policy_type in mapping:
        return mapping[policy_type]

    return policy_type

def resolve_ep_flags(flags):
    resolved = []

    mapping = {}
    mapping['s'] = 'arp'
    mapping['R'] = 'peer-attached-r1'
    mapping['D'] = 'bounce-to-proxy'
    mapping['H'] = 'VTEP'
    mapping['B'] = 'bounce'
    mapping['O'] = 'peer attached'
    mapping['V'] = 'VPC-attached'
    mapping['S'] = 'static'
    mapping['a'] = 'local-arped'
    mapping['p'] = 'peer-aged'
    mapping['M'] = 'span'
    mapping['L'] = 'local'

    for flag in flags:
        if flag in mapping:
            resolved.append(
                '%s (%s)' % (
                    mapping[flag],
                    flag
                )
            )
            continue

        resolved.append(flag)

    return resolved
