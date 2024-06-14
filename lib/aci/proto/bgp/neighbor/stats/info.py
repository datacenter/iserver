class ProtocolBgpNeighborStatsInfo():
    def __init__(self):
        pass

    def get_protocol_bgp_neighbor_stats_info(self, managed_object):
        info = {}
        info['__Output'] = {}

        # "byteInRecvQ":"0",
        # "byteInSendQ":"0",
        # "byteRcvd":"16116741",
        # "byteSent":"13610230",
        # "capRcvd":"0",
        # "capSent":"0",
        # "childAction":"",
        # "connectRetryTs":"1970-01-01T01:00:00.000+01:00",
        # "dn":"topology/pod-1/node-201/sys/bgp/inst/dom-common:smi5Gc-cvim4-N3-N4_VRF/peer-[<ip>/32]/ent-[<ip>]/peerstats",
        # "kaRcvd":"848117",
        # "kaSent":"710369",
        # "kaTs":"2023-01-16T15:23:37.122+01:00",
        # "modTs":"never",
        # "monPolDn":"",
        # "msgRcvd":"848179",
        # "msgSent":"712365",
        # "notifRcvd":"0",
        # "notifSent":"17",
        # "openRcvd":"18",
        # "openSent":"19",
        # "routeRefreshRcvd":"0",
        # "routeRefreshSent":"26",
        # "status":"",
        # "updateRcvd":"44",
        # "updateSent":"1934"

        for key in managed_object:
            info[key] = managed_object[key]

        return info

    def get_protocol_bgp_neighbor_stats(self, pod_id, node_id, bgp_domain_name, bgp_peer_addr, bgp_state_addr):
        managed_object = self.get_protocol_bgp_neighbor_stats_mo(
            pod_id,
            node_id,
            bgp_domain_name,
            bgp_peer_addr,
            bgp_state_addr
        )
        if managed_object is None or len(managed_object) == 0:
            return None

        return self.get_protocol_bgp_neighbor_stats_info(managed_object)
