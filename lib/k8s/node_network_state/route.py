class K8sNodeNetworkStateRouteInfo():
    def __init__(self):
        pass

    def get_node_network_state_route_info(self, managed_object):
        info = []
        routes_mo = self.get(
            managed_object,
            'status:currentState:routes:running'
        )
        for route_mo in routes_mo:
            route_info = {}
            for key in route_mo:
                route_info[key] = route_mo[key]
            info.append(
                route_info
            )

        info = sorted(
            info,
            key=lambda i: (
                i['table-id'],
                i['destination']
            )
        )
        return info