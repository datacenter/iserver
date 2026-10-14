def is_interface_name_phys(name):
    if name == 'lo':
        return False

    if 'bond' in name:
        return False

    return True


def analyze_ip_link_show_output(output, phys_only=False):
    interfaces = []

    info = None
    for line in output.split('\n'):
        if ' mtu ' in line:
            if info is not None:
                if info['netns'] is not None:
                    info['phys'] = False
                else:
                    info['phys'] = is_interface_name_phys(info['name'])

                if not phys_only or info['phys']:
                    interfaces.append(
                        info
                    )

            info = {}
            info['index'] = line.split(':')[0]
            info['name'] = line.split(':')[1].strip()
            info['flags'] = line.split('<')[1].split('>')[0]
            info['mtu'] = line.split(' mtu ')[1].split(' ')[0]
            info['state'] = line.split(' state ')[1].split(' ')[0]
            info['up'] = False
            if info['state'] == 'UP':
                info['up'] = True
            info['mac'] = ''
            info['netns'] = None
            info['vf'] = []

        if ' vf ' in line:
            vf_info = {}
            vf_info['index'] = line.split(' vf ')[1].split(' ')[0]
            vf_info['mac'] = line.split(' link/ether ')[1].split(' ')[0]
            if len(line.split(' link-netns ')) > 1:
                info['netns'] = line.split(' link-netns ')[1].split(' ')[0]

            vf_info['vlan'] = None
            if ' vlan ' in line:
                vf_info['vlan'] = line.split(' vlan ')[1].split(' ')[0].rstrip(',')
            vf_info['spoof'] = line.split(' spoof checking ')[1].split(' ')[0].rstrip(',')
            vf_info['link'] = line.split(' link-state ')[1].split(' ')[0].rstrip(',')
            vf_info['trust'] = line.split(' trust ')[1].split(' ')[0].rstrip(',')
            info['vf'].append(
                vf_info
            )

        if ' vf ' not in line and ' link/ether ' in line:
            info['mac'] = line.split(' link/ether ')[1].split(' ')[0]
            if len(line.split(' link-netns ')) > 1:
                info['netns'] = line.split(' link-netns ')[1].split(' ')[0]

    if info is not None:
        if info['netns'] is not None:
            info['phys'] = False
        else:
            info['phys'] = is_interface_name_phys(info['name'])

        if not phys_only or info['phys']:
            interfaces.append(
                info
            )

    return interfaces