import copy
from lib import ip_helper
from lib.vc import vcenter


class VcDvs():
    def __init__(self):
        self.vc_dvs = None

    def load_pre_vc_dvs(self):
        self.vc_dvs = self.get_pre_cache('vcenter', 'dvs')
        if self.vc_dvs is None:
            return False

        return True

    def set_post_vc_dvs(self):
        return self.set_post_cache('vcenter-dvs', self.vc_dvs)

    def load_post_vc_dvs(self):
        self.vc_dvs = self.get_post_cache('vcenter-dvs')
        if self.vc_dvs is None:
            return False

        return True

    def get_vc_dvs(self, vc):
        if vc in self.vc_dvs:
            info = copy.deepcopy(self.vc_dvs[vc])
            return info

        return None

    def prepare_vc_dvs(self, cache_enabled=True):
        vc_instances = self.get_vc_handlers()
        if vc_instances is None or len(vc_instances) == 0:
            return False

        self.vc_dvs = {}

        for vc_instance in vc_instances:
            self.my_output.debug('Vcenter dvs: %s' % (vc_instance['name']))

            if cache_enabled and self.cache_ttl is not None:
                # L2-cache
                if vc_instance['name'] in self.vc_dvs:
                    self.my_output.debug('L2 Cache hit')
                    continue

                # L3-cache
                cache = self.get_cache('vcenter-%s-dvs' % (vc_instance['name']))
                if cache is not None:
                    self.my_output.debug('L3 Cache hit network')
                    self.vc_dvs[vc_instance['name']] = cache
                    continue

            self.my_output.debug('Cache miss')

            vc_handler = vcenter.Vcenter(
                vc_instance['ip'],
                vc_instance['username'],
                vc_instance['password'],
                port=vc_instance['port'],
                log_id=self.log_id
            )

            self.vc_dvs[vc_instance['name']] = vc_handler.get_dvs()
            if self.vc_dvs[vc_instance['name']] is None:
                return False

            self.set_cache(
                'vcenter-%s-dvs' % (vc_instance['name']),
                self.vc_dvs[vc_instance['name']]
            )

        return True

    def run_vc_dvs_pg(self, vc, dvs, pg):
        pg['up'] = False
        if pg['overallStatus'] == 'green':
            pg['up'] = True

        if len(pg['name'].split('-DVUplinks-')) == 2:
            pg['uplink'] = True
        else:
            pg['uplink'] = False

        pg['trunk'] = False
        pg['vlans'] = None
        for network in self.vc_network[vc]:
            if network['portGroupKey'] == pg['key']:
                pg['trunk'] = network['trunk']
                pg['vlans'] = network['vlans']

        pg['numVms'] = len(pg['vm'])
        pg['numVmsUp'] = 0
        for pvm in pg['vm']:
            for vm in self.vc_vm[vc]:
                if vm['name'] == pvm:
                    if vm['up']:
                        pg['numVmsUp'] += 1

        pg['numPorts'] = len(pg['portKeys'])
        pg['numPortsUp'] = 0
        for port in dvs['port']:
            if pg['key'] == port['portgroupKey']:
                port_up = False
                if port['linkUp'] is not None:
                    port_up = port['linkUp']
                if port_up:
                    pg['numPortsUp'] += 1

        return pg

    def run_vc_dvs_port(self, vc, dvs, port):
        port['host'] = None
        port['_host'] = None
        port['host_hash'] = None
        port['host_nic_hash'] = None
        port['vm_hash'] = None

        port['up'] = False
        if port['linkUp'] is not None:
            port['up'] = port['linkUp']

        if port['peerType'] is not None and port['peerType'] == 'vmVnic':
            port['vm_hash'] = ip_helper.get_string_md5(
                '%s %s' % (
                    vc,
                    port['peerName']
                )
            )

        if port['peerType'] is not None and port['peerType'] == 'pnic':
            port['host'] = port['peerName']
            port['_host'] = self.get_vc_host_name_short(port['host'])
            port['host_hash'] = ip_helper.get_string_md5(
                '%s %s' % (
                    vc,
                    port['host']
                )
            )
            port['host_nic_hash'] = ip_helper.get_string_md5(
                '%s %s %s' % (
                    vc,
                    port['host'],
                    port['peerNic']
                )
            )

        port['portgroupName'] = None
        port['vlans'] = None
        port['uplink'] = None

        for pg in dvs['portgroup']:
            if pg['key'] == port['portgroupKey']:
                port['portgroupName'] = pg['name']
                port['vlans'] = pg['vlans']
                port['uplink'] = pg['uplink']

        return port

    def _run_vc_dvs(self, vc, dvs):
        dvs['_name'] = dvs['name']
        dvs['vcenter'] = vc

        dvs['up'] = False
        if dvs['overallStatus'] == 'green':
            dvs['up'] = True

        dvs['hash'] = ip_helper.get_string_md5(
            '%s %s' % (
                vc,
                dvs['name']
            )
        )

        for pg in dvs['portgroup']:
            pg = self.run_vc_dvs_pg(vc, dvs, pg)

        for port in dvs['port']:
            pg = self.run_vc_dvs_port(vc, dvs, port)

        # Augment Port Group
        dvs['vm'] = []
        dvs['host'] = []
        dvs['numHostsUp'] = 0
        dvs['numDpg'] = 0
        dvs['numDpgUp'] = 0
        dvs['numUpg'] = 0
        dvs['numUpgUp'] = 0
        dvs['numVms'] = 0
        dvs['numVmsUp'] = 0
        for pg in dvs['portgroup']:
            for pvm in pg['vm']:
                if pvm not in dvs['vm']:
                    dvs['vm'].append(
                        pvm
                    )
                    dvs['numVms'] += 1
                    for vm in self.vc_vm[vc]:
                        if vm['name'] == pvm:
                            if vm['up']:
                                pg['numVmsUp'] += 1

            for phost in pg['host']:
                if phost not in dvs['host']:
                    dvs['host'].append(
                        phost
                    )
                    for host in self.vc_host[vc]:
                        if host['name'] == phost:
                            if self.is_vc_host_up(host):
                                dvs['numHostsUp'] += 1

            if pg['uplink']:
                dvs['numUpg'] += 1
                if pg['up']:
                    dvs['numUpgUp'] += 1

            if not pg['uplink']:
                dvs['numDpg'] += 1
                if pg['up']:
                    dvs['numDpgUp'] += 1

        # Augment port
        dvs['numPortsUp'] = 0
        dvs['numDownlink'] = 0
        dvs['numDownlinkUp'] = 0
        dvs['numUplink'] = 0
        dvs['numUplinkUp'] = 0
        for port in dvs['port']:
            if port['up']:
                dvs['numPortsUp'] += 1

            if port['uplink']:
                dvs['numUplink'] += 1
                if port['up']:
                    dvs['numUplinkUp'] += 1

            if not port['uplink']:
                dvs['numDownlink'] += 1
                if port['up']:
                    dvs['numDownlinkUp'] += 1

        # Augment adapters
        dvs['numAdapter'] = 0
        dvs['numAdapterUp'] = 0
        dvs['adapter'] = {}
        for host in self.vc_host[vc]:
            if host['name'] not in dvs['host']:
                continue

            dvs['adapter'][host['name']] = {}
            dvs['adapter'][host['name']]['numAdapter'] = 0
            dvs['adapter'][host['name']]['numAdapterUp'] = 0

            if host['pnet'] is None:
                continue

            for hdvs in host['pnet']['dvswitch']:
                if hdvs['name'] == dvs['name']:
                    dvs['numAdapter'] += hdvs['numUplinks']
                    dvs['numAdapterUp'] += hdvs['numUplinksUp']
                    dvs['adapter'][host['name']]['numAdapter'] = hdvs['numUplinks']
                    dvs['adapter'][host['name']]['numAdapterUp'] = hdvs['numUplinksUp']

        # Sort
        dvs['host'] = sorted(dvs['host'])
        dvs['vm'] = sorted(dvs['vm'])
        dvs['port'] = sorted(
            dvs['port'],
            key=lambda i: (int(i['key']))
        )

        return dvs

    def run_vc_dvs(self):
        for vc in self.vc_instance:
            if vc not in self.vc_dvs:
                self.vc_dvs[vc] = []

            for dvs in self.vc_dvs[vc]:
                dvs = self._run_vc_dvs(vc, dvs)

        if not self.set_post_vc_dvs():
            return False

        return True
