from lib.md.aci.phy.details import MdAciPhyDetailsOutput
from lib.md.aci.phy.epg import MdAciPhyEpgOutput
from lib.md.aci.phy.l2 import MdAciPhyL2Output
from lib.md.aci.phy.optics import MdAciPhyOpticsOutput
from lib.md.aci.phy.policy import MdAciPhyPolicyOutput
from lib.md.aci.phy.state import MdAciPhyStateOutput
from lib.md.aci.phy.vlan import MdAciPhyVlanOutput


class MdAciPhyOutput(
        MdAciPhyDetailsOutput,
        MdAciPhyEpgOutput,
        MdAciPhyL2Output,
        MdAciPhyOpticsOutput,
        MdAciPhyPolicyOutput,
        MdAciPhyStateOutput,
        MdAciPhyVlanOutput
    ):
    def __init__(self):
        MdAciPhyDetailsOutput.__init__(self)
        MdAciPhyEpgOutput.__init__(self)
        MdAciPhyL2Output.__init__(self)
        MdAciPhyOpticsOutput.__init__(self)
        MdAciPhyPolicyOutput.__init__(self)
        MdAciPhyStateOutput.__init__(self)
        MdAciPhyVlanOutput.__init__(self)

    def add_phy_interface(self, line, info, key_id='id', key_hash='hash', up=False, last=False, add_oper=False):
        base = './'
        if up:
            base = '../'

        if add_oper:
            if 'stats' not in info or info['stats'] is None:
                state = ':x:'
            else:
                if info['stats']['operSt'] == 'up':
                    state = ':white_check_mark:'
                else:
                    state = ':x:'

            line = self.add_column(
                line,
                '[%s](%sphy/%s.md)%s' % (
                    info[key_id],
                    base,
                    info[key_hash],
                    state
                )
            )
        else:
            line = self.add_column(
                line,
                '[%s](%sphy/%s.md)' % (
                    info[key_id],
                    base,
                    info[key_hash]
                )
            )

        return line

    def add_phy_interface_oper_state(self, line, info):
        if 'stats' not in info or info['stats'] is None:
            state = ':x:'
        else:
            if info['stats']['operSt'] == 'up':
                state = ':white_check_mark:'
            else:
                state = ':x:'

        line = self.add_column(
            line,
            state
        )

        return line

    def add_phy_interface_state(self, line, info):
        if info['adminSt'] == 'up':
            state = ':white_check_mark:'
        else:
            state = ':x:'

        if info['switchingSt'] == 'enabled':
            state = '%s :white_check_mark:' % (state)
        else:
            state = '%s :x:' % (state)

        if 'stats' not in info or info['stats'] is None:
            state = '%s :x:' % (state)
        else:
            if info['stats']['operSt'] == 'up':
                state = '%s :white_check_mark:' % (state)
            else:
                state = '%s :x:' % (state)

        reason = None
        if 'stats' in info and info['stats'] is not None:
            reason = info['stats']['_reason']

        if reason is None:
            state = '%s (%s)' % (state, info['usage'])
        else:
            state = '%s (%s, %s)' % (state, info['usage'], reason)

        line = self.add_column(
            line,
            state
        )

        return line

    def add_phy_interface_pc(self, line, info):
        if 'stats' not in info or info['stats'] is None:
            line = self.add_column(line, '---')
            return line

        if len(info['stats']['bundleIndex']) == 0:
            line = self.add_column(line, '---')
        else:
            line = self.add_column(line, info['stats']['bundleIndex'])

        return line

    def add_phy_interface_cdp(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if item['cdp_hash'] is not None:
            line = self.add_column(line, '[Link](%scdp/%s.md)' % (base, item['cdp_hash']), last=False)
        else:
            line = self.add_column(line, '---', False)
        return line

    def add_phy_interface_lldp(self, line, item, up=False, last=False):
        base = './'
        if up:
            base = '../'

        if item['lldp_hash'] is not None:
            line = self.add_column(line, '[Link](%slldp/%s.md)' % (base, item['lldp_hash']), last=False)
        else:
            line = self.add_column(line, '---', last=False)
        return line

    def print_aci_node_phy(self, controller, node_name, info, aci_node_servers, servers, commands):
        self.print_aci_node_phy_state(controller, node_name, info, servers, commands)
        self.print_aci_node_phy_l2(controller, node_name, info)
        self.print_aci_node_phy_vlan(controller, node_name, info, commands)
        self.print_aci_node_phy_optics(controller, node_name, info, aci_node_servers)
        self.print_aci_node_phy_epg(controller, node_name, info, aci_node_servers)
        self.print_aci_node_phy_policy(controller, node_name, info)
