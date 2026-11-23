from lib import ip_helper


def get_nexus_interface_type(name):
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

def get_nexus_interface_id(name):
    interface_type = get_nexus_interface_type(name)
    if interface_type is None:
        return None

    name = name.lower()

    if interface_type == 'mgmt':
        return name.split('mgmt')[1]

    if interface_type == 'eth':
        if len(name.split('ethernet')) == 2:
            return name.split('ethernet')[1]

        return name.split('eth')[1]

    if interface_type == 'pc':
        if len(name.split('port-channel')) == 2:
            return name.split('port-channel')[1]

        return name.split('po')[1]

    if interface_type == 'vlan':
        return name.split('vlan')[1]

    if interface_type == 'loopback':
        return name.split('loopback')[1]

    return None

def get_nexus_interface_hash(device_name, interface_name):
    interface_type = get_nexus_interface_type(interface_name)
    interface_id = get_nexus_interface_id(interface_name)

    if interface_type == 'mgmt':
        return ip_helper.get_string_md5(
            '%s mgmt%s' % (
                device_name,
                interface_id
            )
        )

    if interface_type == 'eth':
        return ip_helper.get_string_md5(
            '%s Ethernet%s' % (
                device_name,
                interface_id
            )
        )

    if interface_type == 'pc':
        return ip_helper.get_string_md5(
            '%s port-channel%s' % (
                device_name,
                interface_id
            )
        )

    if interface_type == 'vlan':
        return ip_helper.get_string_md5(
            '%s Vlan%s' % (
                device_name,
                interface_id
            )
        )

    if interface_type == 'loopback':
        return ip_helper.get_string_md5(
            '%s loopback%s' % (
                device_name,
                interface_id
            )
        )

    return None

def is_nexus_interface_equal(inta, intb):
    if intb is None or inta is None:
        return False

    inta_type = get_nexus_interface_type(inta)
    intb_type = get_nexus_interface_type(intb)
    if inta_type is None or intb_type is None:
        return False

    if inta_type != intb_type:
        return False

    inta_id = get_nexus_interface_id(inta)
    intb_id = get_nexus_interface_id(intb)
    if inta_id is None or intb_id is None:
        return False

    if inta_id != intb_id:
        return False

    return True

def get_config_interface_ethernet_ids(configuration):
    ids = []

    for line in configuration['configuration'].split('\n'):
        if len(line.split('interface Ethernet')) == 2:
            ids.append(
                line.split('interface Ethernet')[1]
            )

    return ids

def get_config_interface_pc_ids(configuration):
    ids = []

    for line in configuration['configuration'].split('\n'):
        if len(line.split('interface port-channel')) == 2:
            ids.append(
                line.split('interface port-channel')[1]
            )

    return ids

def get_config_interface_pc(configuration, interface_id):
    output = []
    start = False
    for line in configuration['configuration'].split('\n'):
        if line == 'interface port-channel%s' % (interface_id):
            start = True
            output.append(line)
            continue

        if len(line.split('interface port-channel')) == 2:
            start = False
            continue

        if len(line.strip()) == 0:
            continue

        if line[0] != ' ':
            start = False
            continue

        if start:
            output.append(line)

    return '\n'.join(output)

def get_config_interface_vlan_ids(configuration):
    ids = []

    for line in configuration['configuration'].split('\n'):
        if len(line.split('interface Vlan')) == 2:
            ids.append(
                line.split('interface Vlan')[1]
            )

    return ids

def get_config_interface_vlan(configuration, interface_id):
    output = []

    start = False
    for line in configuration['configuration'].split('\n'):
        if line == 'vlan %s' % (interface_id):
            start = True
            output.append(line)
            continue

        if len(line.split('vlan')) == 2:
            start = False
            continue

        if len(line.strip()) == 0:
            continue

        if line[0] != ' ':
            start = False
            continue

        if start:
            output.append(line)

    output.append('')

    start = False
    for line in configuration['configuration'].split('\n'):
        if line == 'interface Vlan%s' % (interface_id):
            start = True
            output.append(line)
            continue

        if len(line.split('interface Vlan')) == 2:
            start = False
            continue

        if len(line.strip()) == 0:
            continue

        if line[0] != ' ':
            start = False
            continue

        if start:
            output.append(line)

    return '\n'.join(output)

def get_config_vpc_domain(configuration):
    output = []
    start = False
    for line in configuration['configuration'].split('\n'):
        if len(line.split('vpc domain')) == 2:
            start = True
            output.append(line)
            continue

        if len(line.strip()) == 0:
            continue

        if line[0] != ' ':
            start = False
            continue

        if start:
            output.append(line)

    return '\n'.join(output)

def get_config_interface_mgmt(configuration):
    output = []
    start = False
    for line in configuration['configuration'].split('\n'):
        if line == 'interface mgmt0':
            start = True
            output.append(line)
            continue

        if len(line.split('interface Vlan')) == 2:
            start = False
            continue

        if len(line.strip()) == 0:
            continue

        if line[0] != ' ':
            start = False
            continue

        if start:
            output.append(line)

    return '\n'.join(output)

def get_config_interface_ethernet(configuration, interface_id):
    output = []
    start = False
    for line in configuration['configuration'].split('\n'):
        if line == 'interface Ethernet%s' % (interface_id):
            start = True
            output.append(line)
            continue

        if len(line.split('interface Ethernet')) == 2:
            start = False
            continue

        if len(line.strip()) == 0:
            continue

        if line[0] != ' ':
            start = False
            continue

        if start:
            output.append(line)

    return '\n'.join(output)
