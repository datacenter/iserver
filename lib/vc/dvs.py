import json
import time
import sys


# pylint: disable=no-name-in-module
from pyVmomi import vim


class VcDvs():
    def __init__(self):
        self.dvs_objects = None
        self.dvs = None

    def get_dvs_objects(self):
        if self.dvs_objects is not None:
            return self.dvs_objects

        if not self.vc_connect():
            return None

        start_time = int(time.time() * 1000)

        content = self.vc_service_instance.RetrieveContent()
        networks_object_view = content.viewManager.CreateContainerView(
            content.rootFolder,
            [vim.DistributedVirtualSwitch],
            True
        )

        self.dvs_objects = []
        for network_obj in networks_object_view.view:
            self.dvs_objects.append(network_obj)

        networks_object_view.Destroy()

        duration = int(time.time() * 1000) - start_time
        self.log.vcenter(
            'get',
            'vim.dvs',
            True,
            duration
        )

        return self.dvs_objects

    def get_dvs_pg_info(self, pg_obj):
        info = {}
        info['configStatus'] = pg_obj.configStatus

        info['declaredAlarmState'] = str(pg_obj.declaredAlarmState)
        info['effectiveRole'] = str(pg_obj.effectiveRole)
        info['host'] = []
        for item in pg_obj.host:
            info['host'].append(
                item.name
            )

        info['key'] = pg_obj.key
        info['name'] = pg_obj.name
        info['overallStatus'] = pg_obj.overallStatus
        info['portKeys'] = pg_obj.portKeys
        info['network_type'] = 'standard'
        if isinstance(pg_obj.summary.network, vim.dvs.DistributedVirtualPortgroup):
            info['network_type'] = 'dvs'
            info['network_name'] = pg_obj.summary.network.name

        info['vm'] = []
        for item in pg_obj.vm:
            info['vm'].append(
                item.name
            )

        return info

    def get_dvs_port_info(self, port_obj):
        info = {}

        info['key'] = port_obj.key
        info['name'] = port_obj.config.name
        info['scope'] = []
        for obj in port_obj.config.scope:
            info['scope'].append(
                obj.name
            )
        vlan_info = port_obj.config.setting.vlan
        vlan_spec = vim.dvs.VmwareDistributedVirtualSwitch.TrunkVlanSpec

        if isinstance(vlan_info, vlan_spec):
            info['trunk'] = True
            info['vlans'] = []
            for item in vlan_info.vlanId:
                if item.start == item.end:
                    info['vlans'].append(str(item.start))
                else:
                    info['vlans'].append(str(item.start)+'-'+str(item.end))
        else:
            info['trunk'] = True
            info['vlans'] = []
            vlan_id = getattr(vlan_info, 'vlanId', None)
            if vlan_id is not None:
                info['vlans'].append(
                    str(vlan_id)
                )

        info['portgroupKey'] = port_obj.portgroupKey
        info['peerType'] = None
        info['peerName'] = None
        info['peerNic'] = None
        if port_obj.connectee is not None:
            info['peerType'] = port_obj.connectee.type
            info['peerName'] = port_obj.connectee.connectedEntity.name
            info['peerNic'] = port_obj.connectee.nicKey

        info['linkUp'] = None
        info['trunk'] = None
        if port_obj.state is not None and port_obj.state.runtimeInfo is not None:
            info['linkUp'] = port_obj.state.runtimeInfo.linkUp
            info['trunk'] = port_obj.state.runtimeInfo.trunkingMode

        keys = [
            'packetsInMulticast',
            'packetsOutMulticast',
            'bytesInMulticast',
            'bytesOutMulticast',
            'packetsInUnicast',
            'packetsOutUnicast',
            'bytesInUnicast',
            'bytesOutUnicast',
            'packetsInBroadcast',
            'packetsOutBroadcast',
            'bytesInBroadcast',
            'bytesOutBroadcast',
            'packetsInDropped',
            'packetsOutDropped',
            'packetsInException',
            'packetsOutException',
            'bytesInFromPnic',
            'bytesOutToPnic'
        ]
        info['stats'] = None
        if port_obj.state is not None and port_obj.state.stats is not None:
            info['stats'] = {}
            for key in keys:
                info['stats'][key] = getattr(port_obj.state.stats, key)

        return info

    def get_dvs_info(self, dvs_obj):
        info = {}

        info['name'] = dvs_obj.name
        info['overallStatus'] = dvs_obj.overallStatus

        info['portgroup'] = []
        for item in dvs_obj.portgroup:
            info['portgroup'].append(
                self.get_dvs_pg_info(
                    item
                )
            )

        info['runtime'] = {}
        info['runtime']['capacity'] = dvs_obj.runtime.resourceRuntimeInfo.capacity
        info['runtime']['usage'] = dvs_obj.runtime.resourceRuntimeInfo.usage
        info['runtime']['available'] = dvs_obj.runtime.resourceRuntimeInfo.available

        info['numPorts'] = dvs_obj.summary.numPorts
        info['numHosts'] = dvs_obj.summary.numHosts
        info['vendor'] = dvs_obj.summary.productInfo.vendor
        info['version'] = dvs_obj.summary.productInfo.version

        info['port'] = []
        port_objs = dvs_obj.FetchDVPorts()
        for port_obj in port_objs:
            info['port'].append(
                self.get_dvs_port_info(
                    port_obj
                )
            )

        return info

    def get_dvs(self):
        if self.dvs is not None:
            return self.dvs

        dvs_objs = self.get_dvs_objects()
        if dvs_objs is None:
            return None

        self.dvs = []
        for dvs_obj in dvs_objs:
            self.dvs.append(
                self.get_dvs_info(
                    dvs_obj
                )
            )

        self.dvs = sorted(
            self.dvs,
            key=lambda i: i['name']
        )

        return self.dvs
