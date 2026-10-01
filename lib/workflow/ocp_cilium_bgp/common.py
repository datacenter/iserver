def get_default_params():
    params = {}
    params['title'] = 'OpenShift Workflow - Cilium BGP Control Plane'
    return params


def is_bgp_crd(params, my_output=None):
    clusters = params['k8s_handler'].get_isovalent_bgp_cluster_configs(cache_enabled=False)
    if clusters is None:
        if my_output is not None:
            my_output.default('BGP Control Plane CRDs %s' % (my_output.add_color('not found', 'Red')))
        return False
    
    my_output.default('BGP Control Plane CRDs %s' % (my_output.add_color('found', 'Green')))
    return True