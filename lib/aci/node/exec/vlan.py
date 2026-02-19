import re


class NodeExecVlan():
    def __init__(self):
        pass

    def parse_node_vlan_extended(self, output):
        vlans = []
        column_length = []
        started = False
        vlan = None

        for line in output.split('\n'):
            leading_spaces_count = len(line) - len(line.lstrip(' '))
            line = re.sub(', ', ',', line)
            line = re.sub(' +', ' ', line)
            line = line.strip()
            words = line.split(' ')
            if len(words) == 0:
                continue

            if not started:
                if words[0] == '----':
                    for word in words:
                        column_length.append(
                            len(word)
                        )

                    started = True
                    continue

            if started:
                if len(words) < 4:
                    # continuation of vlan name
                    name_extended = False
                    if leading_spaces_count < column_length[0] + column_length[1]:
                        name_extended = True
                        vlan['name'] = '%s%s' % (
                            vlan['name'],
                            words[0]
                        )

                    index = 0
                    for word in words:
                        if name_extended and word == words[0] and index == 0:
                            index += 1
                            continue

                        index += 1
                        if len(word.split('vlan-')) > 1 or len(word.split('vxlan-')) > 1:
                            vlan['encap'] = '%s%s' % (
                                vlan['encap'],
                                word
                            )

                        if len(word.split('Eth')) > 1 or len(word.split('Po')) > 1:
                            vlan['ports'] = '%s%s' % (
                                vlan['ports'],
                                word
                            )

                if len(words) == 4:
                    if vlan is not None:
                        vlans.append(
                            vlan
                        )

                    vlan = {}
                    vlan['id'] = words[0]
                    vlan['name'] = words[1]
                    vlan['encap'] = words[2]
                    if words[3] == '--':
                        vlan['ports'] = ''
                    else:
                        vlan['ports'] = words[3]

        if started and vlan is not None:
            vlans.append(
                vlan
            )

        for vlan in vlans:
            vlan['id'] = int(vlan['id'])
            vlan['encap'] = vlan['encap'].split(',')
            vlan['ports'] = vlan['ports'].split(',')

        return vlans
