class K8sBgpSessionStateOutput():
    def __init__(self):
        pass

    def print_bgp_session_states_state(self, info):
        self.my_output.my_table_ng(
            info,
            [
                ['Node', 'status.node'],
                ['Pod', 'owner_name'],
                ['Peer', 'status.peer'],
                ['Status', 'status.bgpStatus'],
                ['BFD', 'status.bfdStatus']
            ]
        )