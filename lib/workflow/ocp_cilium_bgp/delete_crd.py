import yaml
from lib import file_helper
from lib import output_helper
from lib.workflow.ocp_cilium_bgp import common as local_common
from menu.common import get_confirmation
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['filename', False, None, 'file-k8s', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params
        
    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    ocp_common.print_title(params, my_output, 'Delete configuration')
    params = ocp_common.workflow_init(params, my_output, log_id, cilium_required=True)
    if params is None:
        return False

    content = file_helper.get_file_text(params['filename'])
    if content is None:
        my_output.error('CRD file read failed: %s' % (params['filename']))
        return False
    
    params['crd'] = []
    for item in content.split('---'):
        try:
            yitem = yaml.safe_load(item)
        except:
            continue

        if not file_helper.is_kube_kind(yitem):
            continue

        if yitem['kind'] not in ['IsovalentBGPClusterConfig', 'IsovalentBGPPeerConfig', 'IsovalentBGPAdvertisement']:
            continue

        params['crd'].append(yitem)
    
    if len(params['crd']) == 0:
        my_output.error('No bgp crd found: %s' % (params['filename']))
        return False

    content = []
    for item in params['crd']:
        content.append(yaml.safe_dump(item))

    my_output.default(
        '---\n'.join(content),
        before_newline=True,
        wrap='~~~'
    )
    
    if params['confirmation']:
        if not get_confirmation():
            return False
    
    for crd in params['crd']:
        if crd['kind'] == 'IsovalentBGPClusterConfig':
            if params['k8s_handler'].get_isovalent_bgp_cluster_config(crd['metadata']['name']) is None:
                my_output.default('IsovalentBGPClusterConfig %s %s' % (crd['metadata']['name'], my_output.add_color('already deleted', 'Green')))
                continue

            success = params['k8s_handler'].delete_resource(crd['kind'], crd['apiVersion'], crd['metadata']['name'])
            if success:
                my_output.default('IsovalentBGPClusterConfig %s %s' % (crd['metadata']['name'], my_output.add_color('deleted', 'Green')))
            else:
                my_output.default('IsovalentBGPClusterConfig %s %s' % (crd['metadata']['name'], my_output.add_color('delete failed', 'Red')))
        
        if crd['kind'] == 'IsovalentBGPPeerConfig': 
            if params['k8s_handler'].get_isovalent_bgp_peer_config(crd['metadata']['name']) is None:
                my_output.default('IsovalentBGPPeerConfig %s %s' % (crd['metadata']['name'], my_output.add_color('already deleted', 'Green')))
                continue

            success = params['k8s_handler'].delete_resource(crd['kind'], crd['apiVersion'], crd['metadata']['name'])
            if success:
                my_output.default('IsovalentBGPPeerConfig %s %s' % (crd['metadata']['name'], my_output.add_color('deleted', 'Green')))
            else:
                my_output.default('IsovalentBGPPeerConfig %s %s' % (crd['metadata']['name'], my_output.add_color('delete failed', 'Red')))
        
        if crd['kind'] == 'IsovalentBGPAdvertisement':
            if params['k8s_handler'].get_isovalent_bgp_advertisement(crd['metadata']['name']) is None:
                my_output.default('IsovalentBGPAdvertisement %s %s' % (crd['metadata']['name'], my_output.add_color('already deleted', 'Green')))
                continue

            success = params['k8s_handler'].delete_resource(crd['kind'], crd['apiVersion'], crd['metadata']['name'])
            if success:
                my_output.default('IsovalentBGPAdvertisement %s %s' % (crd['metadata']['name'], my_output.add_color('deleted', 'Green')))
            else:
                my_output.default('IsovalentBGPAdvertisement %s %s' % (crd['metadata']['name'], my_output.add_color('delete failed', 'Red')))

    return True