from lib.aci import settings as aci_settings
from lib.xd.aci.aae import AciAae
from lib.xd.aci.accportprof import AciAccessPortProfile
from lib.xd.aci.ap import AciAp
from lib.xd.aci.bd import AciBd
from lib.xd.aci.bgp import AciBgp
from lib.xd.aci.cdp import AciCdp
from lib.xd.aci.contract.main import AciContract
from lib.xd.aci.domain.main import AciDomain
from lib.xd.aci.ep import AciEp
from lib.xd.aci.epg import AciEpg
from lib.xd.aci.l2out import AciL2Out
from lib.xd.aci.l3out import AciL3Out
from lib.xd.aci.lacp import AciLacp
from lib.xd.aci.lldp import AciLldp
from lib.xd.aci.mac import AciMac
from lib.xd.aci.mo import AciMo
from lib.xd.aci.node import AciNode
from lib.xd.aci.phy import AciPhy
from lib.xd.aci.pool.main import AciPool
from lib.xd.aci.server import AciServer
from lib.xd.aci.svi import AciSvi
from lib.xd.aci.tenant import AciTenant
from lib.xd.aci.vrf import AciVrf


class Aci(
        AciAae,
        AciAccessPortProfile,
        AciAp,
        AciBd,
        AciBgp,
        AciCdp,
        AciContract,
        AciDomain,
        AciEp,
        AciEpg,
        AciL2Out,
        AciL3Out,
        AciLacp,
        AciLldp,
        AciMac,
        AciMo,
        AciNode,
        AciPhy,
        AciSvi,
        AciPool,
        AciServer,
        AciTenant,
        AciVrf
    ):
    def __init__(self):
        AciAae.__init__(self)
        AciAccessPortProfile.__init__(self)
        AciAp.__init__(self)
        AciBd.__init__(self)
        AciBgp.__init__(self)
        AciCdp.__init__(self)
        AciContract.__init__(self)
        AciDomain.__init__(self)
        AciEp.__init__(self)
        AciEpg.__init__(self)
        AciL2Out.__init__(self)
        AciL3Out.__init__(self)
        AciLacp.__init__(self)
        AciLldp.__init__(self)
        AciMac.__init__(self)
        AciMo.__init__(self)
        AciNode.__init__(self)
        AciPhy.__init__(self)
        AciPool.__init__(self)
        AciServer.__init__(self)
        AciSvi.__init__(self)
        AciTenant.__init__(self)
        AciVrf.__init__(self)

    def load_pre_aci(self):
        if not self.load_pre_aci_aae():
            self.my_output.error('ACI aae load failed')
            return False

        if not self.load_pre_aci_app():
            self.my_output.error('ACI app load failed')
            return False

        if not self.load_pre_aci_ap():
            self.my_output.error('ACI ap load failed')
            return False

        if not self.load_pre_aci_bd():
            self.my_output.error('ACI bd load failed')
            return False

        if not self.load_pre_aci_bgp():
            self.my_output.error('ACI bgp load failed')
            return False

        if not self.load_pre_aci_cdp():
            self.my_output.error('ACI cdp load failed')
            return False

        if not self.load_pre_aci_contract():
            self.my_output.error('ACI contract load failed')
            return False

        if not self.load_pre_aci_domain():
            self.my_output.error('ACI domain load failed')
            return False

        if not self.load_pre_aci_ep():
            self.my_output.error('ACI ep load failed')
            return False

        if not self.load_pre_aci_epg():
            self.my_output.error('ACI epg load failed')
            return False

        if not self.load_pre_aci_l2out():
            self.my_output.error('ACI l2out load failed')
            return False

        if not self.load_pre_aci_l3out():
            self.my_output.error('ACI l3out load failed')
            return False

        if not self.load_pre_aci_lacp():
            self.my_output.error('ACI lacp load failed')
            return False

        if not self.load_pre_aci_lldp():
            self.my_output.error('ACI lldp load failed')
            return False

        if not self.load_pre_aci_mo():
            self.my_output.error('ACI mo load failed')
            return False

        if not self.load_pre_aci_node():
            self.my_output.error('ACI node load failed')
            return False

        if not self.load_pre_aci_node_cmd():
            self.my_output.error('ACI node cmd load failed')
            return False

        if not self.load_pre_aci_phy():
            self.my_output.error('ACI phy load failed')
            return False

        if not self.load_pre_aci_pool():
            self.my_output.error('ACI pool load failed')
            return False

        if not self.load_pre_aci_svi():
            self.my_output.error('ACI svi load failed')
            return False

        if not self.load_pre_aci_tenant():
            self.my_output.error('ACI tenant load failed')
            return False

        if not self.load_pre_aci_vrf():
            self.my_output.error('ACI vrf load failed')
            return False

        return True

    def get_aci_names(self):
        names = []
        for key in self.aci_ep:
            names.append(key)
        return names

    def get_aci_handlers(self):
        aci_settings_handler = aci_settings.ApicSettings(log_id=self.log_id)
        aci_controllers = aci_settings_handler.get_apic_domain_controllers(self.domain_name)
        return aci_controllers

    def prepare_aci(self, allow_partial=False):
        success = True
        self.my_output.debug('Get aci nodes...')
        if not self.prepare_aci_nodes():
            self.my_output.error('Get aci nodes failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci ep...')
        if not self.prepare_aci_ep():
            self.my_output.error('Get aci ep failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci lacp...')
        if not self.prepare_aci_lacp():
            self.my_output.error('Get aci lacp failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci cdp...')
        if not self.prepare_aci_cdp():
            self.my_output.error('Get aci cdp failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci lldp...')
        if not self.prepare_aci_lldp():
            self.my_output.error('Get aci lldp failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci bgp...')
        if not self.prepare_aci_bgp():
            self.my_output.error('Get aci bgp failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci tenant...')
        if not self.prepare_aci_tenant():
            self.my_output.error('Get aci tenant failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci ap...')
        if not self.prepare_aci_ap():
            self.my_output.error('Get aci ap failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci bd...')
        if not self.prepare_aci_bd():
            self.my_output.error('Get aci bd failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci epg...')
        if not self.prepare_aci_epg():
            self.my_output.error('Get aci epg failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci vrf...')
        if not self.prepare_aci_vrf():
            self.my_output.error('Get aci vrf failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci phy...')
        if not self.prepare_aci_phy():
            self.my_output.error('Get aci phy failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci phy...')
        if not self.prepare_aci_svi():
            self.my_output.error('Get aci svi failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci l2out...')
        if not self.prepare_aci_l2out():
            self.my_output.error('Get aci l2out failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci l3out...')
        if not self.prepare_aci_l3out():
            self.my_output.error('Get aci l3out failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci domain...')
        if not self.prepare_aci_domain():
            self.my_output.error('Get aci domain failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci aae...')
        if not self.prepare_aci_aae():
            self.my_output.error('Get aci aae failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci contract...')
        if not self.prepare_aci_contract():
            self.my_output.error('Get aci contract failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci pool...')
        if not self.prepare_aci_pool():
            self.my_output.error('Get aci pool failed')
            success = False
            if not allow_partial:
                return False

        self.my_output.debug('Get aci access port profiles...')
        if not self.prepare_aci_accportprof():
            self.my_output.error('Get aci access port profile failed')
            success = False
            if not allow_partial:
                return False

        mos = []
        mo = {}
        mo['key'] = 'fvStPathAtt'
        mo['type'] = 'class'
        mo['name'] = 'fvStPathAtt'
        mo['query'] = None
        mo['node'] = False
        mos.append(mo)

        mo = {}
        mo['key'] = 'fvDyPathAtt'
        mo['type'] = 'class'
        mo['name'] = 'fvDyPathAtt'
        mo['query'] = None
        mo['node'] = False
        mos.append(mo)

        mo = {}
        mo['key'] = 'l3extInstP'
        mo['type'] = 'class'
        mo['name'] = 'l3extInstP'
        mo['query'] = None
        mo['node'] = False
        mos.append(mo)

        self.my_output.debug('Get aci mo...')
        if not self.prepare_aci_mo(mos, ):
            self.my_output.error('Get aci mo failed')
            success = False
            if not allow_partial:
                return False

        return success

    def run_aci(self):
        # Order matters
        self.my_output.debug('\t- mo')
        if not self.run_aci_mo():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- server')
        if not self.run_aci_server():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- app')
        if not self.run_aci_accportprof():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- cdp')
        if not self.run_aci_cdp():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- lldp')
        if not self.run_aci_lldp():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- svi')
        if not self.run_aci_svi():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- phy')
        if not self.run_aci_phy():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- ap')
        if not self.run_aci_ap():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- ep')
        if not self.run_aci_ep():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- tenant')
        if not self.run_aci_tenant():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- epg')
        if not self.run_aci_epg():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- bd')
        if not self.run_aci_bd():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- vrf')
        if not self.run_aci_vrf():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- bgp')
        if not self.run_aci_bgp():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- lacp')
        if not self.run_aci_lacp():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- node')
        if not self.run_aci_node():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- l2out')
        if not self.run_aci_l2out():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- l3out')
        if not self.run_aci_l3out():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- aae')
        if not self.run_aci_aae():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- domain')
        if not self.run_aci_domain():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- contract')
        if not self.run_aci_contract():
            self.my_output.error('Failed')
            return False

        self.my_output.debug('\t- pool')
        if not self.run_aci_pool():
            self.my_output.error('Failed')
            return False

        return True

    def run_aci_serial(self):
        if not self.run_aci_node_serial():
            return False

        return True

    def run_aci_mac(self):
        return True

    def load_post_aci(self):
        if not self.load_post_aci_aae():
            self.my_output.error('ACI aae load failed')
            return False

        if not self.load_post_aci_app():
            self.my_output.error('ACI app load failed')
            return False

        if not self.load_post_aci_ap():
            self.my_output.error('ACI ap load failed')
            return False

        if not self.load_post_aci_bd():
            self.my_output.error('ACI bd load failed')
            return False

        if not self.load_post_aci_bgp():
            self.my_output.error('ACI bgp load failed')
            return False

        if not self.load_post_aci_cdp():
            self.my_output.error('ACI cdp load failed')
            return False

        if not self.load_post_aci_contract():
            self.my_output.error('ACI contract load failed')
            return False

        if not self.load_post_aci_domain():
            self.my_output.error('ACI domain load failed')
            return False

        if not self.load_post_aci_ep():
            self.my_output.error('ACI ep load failed')
            return False

        if not self.load_post_aci_epg():
            self.my_output.error('ACI epg load failed')
            return False

        if not self.load_post_aci_l2out():
            self.my_output.error('ACI l2out load failed')
            return False

        if not self.load_post_aci_l3out():
            self.my_output.error('ACI l3out load failed')
            return False

        if not self.load_post_aci_lacp():
            self.my_output.error('ACI lacp load failed')
            return False

        if not self.load_post_aci_lldp():
            self.my_output.error('ACI lldp load failed')
            return False

        if not self.load_post_aci_mo():
            self.my_output.error('ACI mo load failed')
            return False

        if not self.load_post_aci_node():
            self.my_output.error('ACI node load failed')
            return False

        if not self.load_post_aci_node_cmd():
            self.my_output.error('ACI node cmd load failed')
            return False

        if not self.load_post_aci_phy():
            self.my_output.error('ACI phy load failed')
            return False

        if not self.load_post_aci_pool():
            self.my_output.error('ACI pool load failed')
            return False

        if not self.load_post_aci_svi():
            self.my_output.error('ACI svi load failed')
            return False

        if not self.load_post_aci_tenant():
            self.my_output.error('ACI tenant load failed')
            return False

        if not self.load_post_aci_vrf():
            self.my_output.error('ACI vrf load failed')
            return False

        if not self.load_post_aci_node_servers():
            self.my_output.error('ACI node servers load failed')
            return False

        if not self.load_post_aci_node_intfs():
            self.my_output.error('ACI node servers load intfs')
            return False

        return True
