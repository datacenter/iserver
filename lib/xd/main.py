import time
from lib import log_helper
from lib import output_helper
from lib.xd.aci.main import Aci
from lib.xd.cache import Cache
from lib.xd.cnc.main import Cnc
from lib.xd.fi.main import Fi
from lib.xd.k8s.main import K8s
from lib.xd.mac import Mac
from lib.xd.nexus.main import Nexus
from lib.xd.serial import Serial
from lib.xd.server.main import Server
from lib.xd.ucsm.main import Ucsm
from lib.xd.vc.main import Vc


class CrossDomain(
        Aci,
        Cache,
        Cnc,
        Fi,
        K8s,
        Mac,
        Nexus,
        Serial,
        Server,
        Ucsm,
        Vc
    ):
    def __init__(self, log_id=None, debug=False):
        self.log_id = log_id
        self.log = log_helper.Log(log_id=log_id)
        self.my_output = output_helper.OutputHelper(log_id=log_id)
        if debug:
            self.my_output.set_debug()

        self.domain_name = None
        self.timestamp = int(time.time())
        self.out_of_sync = []

        self.xd = {}
        self.xd['CdpHash'] = None
        self.xd['LldpHash'] = None
        self.xd['DeviceType'] = None
        self.xd['ServerMoid'] = None
        self.xd['ServerName'] = None
        self.xd['DeviceSysName'] = None
        self.xd['NexusDevice'] = None
        self.xd['AciApicName'] = None
        self.xd['AciNodeName'] = None
        self.xd['AciNodeId'] = None
        self.xd['AciNodeRef'] = None
        self.xd['FI'] = None

        Cache.__init__(self)
        Aci.__init__(self)
        Cnc.__init__(self)
        Fi.__init__(self)
        K8s.__init__(self)
        Mac.__init__(self)
        Nexus.__init__(self)
        Serial.__init__(self)
        Server.__init__(self)
        Ucsm.__init__(self)
        Vc.__init__(self)

    def set_timestamp(self, timestamp):
        if timestamp < self.timestamp:
            self.timestamp = timestamp

    def get_short_name(self, name):
        if name is None:
            return None

        # Reconsider
        return name

    def prepare(self, domain_name, ttl, allow_partial=False, prepare_modules=None, continuation=False):
        self.domain_name = domain_name
        if continuation:
            self.load_timestamp()
        else:
            self.save_timestamp()

        self.set_ttl(ttl)

        if prepare_modules is not None:
            for item in prepare_modules:
                if len(item.split(':')) == 2:
                    if item.split(':')[0] not in prepare_modules:
                        prepare_modules.append(
                            item.split(':')[0]
                        )

        if prepare_modules is None or 'k8s' in prepare_modules:
            if not self.prepare_k8s(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'cnc' in prepare_modules:
            if not self.prepare_cnc(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'ucsm' in prepare_modules:
            if not self.prepare_ucsm(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'fi' in prepare_modules:
            if not self.prepare_fi(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'nexus' in prepare_modules:
            nexus_prepare_modules = []
            if prepare_modules is not None:
                for item in prepare_modules:
                    if len(item.split(':')) == 2:
                        if item.split(':')[0] == 'nexus':
                            nexus_prepare_modules.append(
                                item.split(':')[1]
                            )

            if len(nexus_prepare_modules) == 0:
                nexus_prepare_modules = None

            if not self.prepare_nexus(allow_partial=allow_partial, prepare_modules=nexus_prepare_modules):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'aci' in prepare_modules:
            if not self.prepare_aci(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'vc' in prepare_modules:
            if not self.prepare_vc(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        if prepare_modules is None or 'server' in prepare_modules:
            if not self.prepare_server(allow_partial=allow_partial):
                if not allow_partial:
                    return False

        return True

    def load_pre(self):
        self.my_output.debug('Load data for xd')

        self.load_timestamp()

        if not self.load_pre_k8s():
            return False

        if not self.load_pre_cnc():
            return False

        if not self.load_pre_fi():
            return False

        if not self.load_pre_ucsm():
            return False

        if not self.load_pre_vc():
            return False

        if not self.load_pre_server():
            return False

        if not self.load_pre_nexus():
            return False

        if not self.load_pre_aci():
            return False

        return True

    def run(self, domain_name):
        self.domain_name = domain_name

        if not self.load_pre():
            return False

        self.my_output.debug('Run xd')

        self.my_output.debug('- cnc')
        if not self.run_cnc():
            return False

        self.my_output.debug('- ucsm')
        if not self.run_ucsm():
            return False

        self.my_output.debug('- fi')
        if not self.run_fi():
            return False

        self.my_output.debug('- server')
        if not self.run_server():
            return False

        self.my_output.debug('- nexus')
        if not self.run_nexus():
            return False

        self.my_output.debug('- aci')
        if not self.run_aci():
            return False

        self.my_output.debug('- vc')
        if not self.run_vc():
            return False

        self.my_output.debug('- k8s')
        if not self.run_k8s():
            return False

        self.my_output.debug('- serial')
        if not self.run_serial():
            return False

        self.my_output.debug('- mac')
        if not self.run_mac():
            return False

        self.my_output.debug('Save out of sync: %s' % (len(self.out_of_sync)))
        for item in self.out_of_sync:
            self.my_output.debug('- %s' % (item))

        if not self.save_out_of_sync():
            return False

        return True

    def load_post(self, domain_name):
        self.domain_name = domain_name
        self.my_output.debug('Load data for output')

        self.load_timestamp()
        self.load_out_of_sync()

        if not self.load_post_k8s():
            self.my_output.debug('K8s failed')
            return False

        if not self.load_post_cnc():
            self.my_output.debug('CNC failed')
            return False

        if not self.load_post_fi():
            self.my_output.debug('FI failed')
            return False

        if not self.load_post_ucsm():
            self.my_output.debug('UCSM failed')
            return False

        if not self.load_post_vc():
            self.my_output.debug('VC failed')
            return False

        if not self.load_post_server():
            self.my_output.debug('Server failed')
            return False

        if not self.load_post_nexus():
            self.my_output.debug('Nexus failed')
            return False

        if not self.load_post_aci():
            self.my_output.debug('ACI failed')
            return False

        if not self.load_post_serial():
            self.my_output.debug('Serial failed')
            return False

        if not self.load_post_mac():
            self.my_output.debug('MAC failed')
            return False

        self.run_post_load_server()

        return True
