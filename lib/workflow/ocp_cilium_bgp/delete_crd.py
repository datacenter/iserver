import os
import yaml
from lib import file_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.workflow.ocp_cilium_bgp import common as local_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'filename' not in params:
        return None, 'CRD filename required'
    
    if not os.path.isfile(params['filename']):
        return None, 'CRD filename not found'
    
    content = file_helper.get_file_text(params['filename'])
    if content is None:
        return None, 'CRD file read failed'
    
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
        return None, 'No bgp crd found'

    if 'confirmation' not in params:
        params['confirmation'] = True

    if not isinstance(params['confirmation'], bool):
        return None, 'confirmation param must be true or false'
        
    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
        
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    allowed_keys = [
        'cluster',
        'filename',
        'crd',
        'confirmation',
        'check-verbose',
        'verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    k8s_output_handler = k8s_output.K8sOutput(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium BGP Control Plane - Delete configuration', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
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
