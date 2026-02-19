import yaml
from lib.k8s import output as k8s_output
from lib import output_helper
from lib.workflow.ocp_cilium_pnet import common as local_common
from lib.workflow import ocp_common as global_common
from lib.workflow.ocp_cilium_cni import common as cilium_common
from menu.common import get_confirmation


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'test-namespace' not in params:
        params['test-namespace'] = 'test-pnet'

    if 'test-network-a' not in params:
        params['test-network-a'] = {}
        params['test-network-a']['name'] = 'test-network-a'
        params['test-network-a']['cidr4'] = '192.168.250.0/24'
        params['test-network-a']['cidr6'] = 'fd10:0:250::0/64'
        params['test-network-a']['pod1'] = 'pod-a1'
        params['test-network-a']['pod1v4'] = '192.168.250.33'
        params['test-network-a']['pod1v6'] = 'fd10:0:250::33'
        params['test-network-a']['pod1mac'] = 'd6:3a:9e:72:bf:21'
        params['test-network-a']['pod2'] = 'pod-a2'
        params['test-network-a']['pod2v4'] = '192.168.250.34'
        params['test-network-a']['pod2v6'] = 'fd10:0:250::34'
        params['test-network-a']['pod2mac'] = 'd6:3a:9e:72:bf:22'

    if 'test-network-b' not in params:
        params['test-network-b'] = {}
        params['test-network-b']['name'] = 'test-network-b'
        params['test-network-b']['cidr4'] = '192.168.250.0/24'
        params['test-network-b']['cidr6'] = 'fd10:0:250::0/64'
        params['test-network-b']['pod1'] = 'pod-b1'
        params['test-network-b']['pod1v4'] = '192.168.250.33'
        params['test-network-b']['pod1v6'] = 'fd10:0:250::33'
        params['test-network-b']['pod1mac'] = 'd6:3a:9e:72:bf:23'
        params['test-network-b']['pod2'] = 'pod-b2'
        params['test-network-b']['pod2v4'] = '192.168.250.35'
        params['test-network-b']['pod2v6'] = 'fd10:0:250::35'
        params['test-network-b']['pod2mac'] = 'd6:3a:9e:72:bf:24'

    if 'cleanup' not in params:
        params['cleanup'] = True

    if not isinstance(params['cleanup'], bool):
        return None, 'cleanup params must be true or false'

    if 'cleanup-on-error' not in params:
        params['cleanup-on-error'] = False

    if not isinstance(params['cleanup-on-error'], bool):
        return None, 'cleanup-on-error params must be true or false'

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
        'test-namespace',
        'test-network-a',
        'test-network-b',
        'cleanup',
        'cleanup-on-error',
        'confirmation',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def prepare(params, my_output):
    if not global_common.prepare_namespace(params['k8s_handler'], params['test-namespace'], my_output):
        return False
    
    success = params['k8s_handler'].create_clusterwide_private_network(
        params['test-network-a']['name'],
        cidrv4=params['test-network-a']['cidr4'],
        cidrv6=params['test-network-a']['cidr6'],
        my_output=my_output,
        confirmation=params['confirmation'],
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].create_clusterwide_private_network(
        params['test-network-b']['name'],
        cidrv4=params['test-network-b']['cidr4'],
        cidrv6=params['test-network-b']['cidr6'],
        my_output=my_output,
        confirmation=params['confirmation'],
        wait=True
    )
    if not success:
        return False

    my_output.default('Create pods')    

    body = params['k8s_handler'].get_clusterwide_private_network_pod_body(
        params['test-namespace'], 
        params['test-network-a']['pod1'],
        params['test-network-a']['name'], 
        params['test-network-a']['pod1v4'], 
        params['test-network-a']['pod1v6'], 
        params['test-network-a']['pod1mac']
    )
    my_output.default(yaml.dump(body))    
    if params['confirmation']:
        if not get_confirmation():
            return False

    if not params['k8s_handler'].create_resource(body):
        my_output.error('Pod create failed')
        return False

    body = params['k8s_handler'].get_clusterwide_private_network_pod_body(
        params['test-namespace'], 
        params['test-network-a']['pod2'],
        params['test-network-a']['name'], 
        params['test-network-a']['pod2v4'], 
        params['test-network-a']['pod2v6'], 
        params['test-network-a']['pod2mac']
    )
    my_output.default(yaml.dump(body))    
    if params['confirmation']:
        if not get_confirmation():
            return False

    if not params['k8s_handler'].create_resource(body):
        my_output.error('Pod create failed')
        return False

    body = params['k8s_handler'].get_clusterwide_private_network_pod_body(
        params['test-namespace'], 
        params['test-network-b']['pod1'],
        params['test-network-b']['name'], 
        params['test-network-b']['pod1v4'], 
        params['test-network-b']['pod1v6'], 
        params['test-network-b']['pod1mac']
    )
    my_output.default(yaml.dump(body))    
    if params['confirmation']:
        if not get_confirmation():
            return False

    if not params['k8s_handler'].create_resource(body):
        my_output.error('Pod create failed')
        return False

    body = params['k8s_handler'].get_clusterwide_private_network_pod_body(
        params['test-namespace'], 
        params['test-network-b']['pod2'],
        params['test-network-b']['name'], 
        params['test-network-b']['pod2v4'], 
        params['test-network-b']['pod2v6'], 
        params['test-network-b']['pod2mac']
    )
    my_output.default(yaml.dump(body))    
    if params['confirmation']:
        if not get_confirmation():
            return False

    if not params['k8s_handler'].create_resource(body):
        my_output.error('Pod create failed')
        return False

    my_output.default('Wait for pods')
    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-a']['pod1']))
    if not params['k8s_handler'].wait_pod_phase(params['test-namespace'], params['test-network-a']['pod1'], ['Running'], max_time=600):
        my_output.error('Pod has not reached desired state')
        return False

    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-a']['pod2']))
    if not params['k8s_handler'].wait_pod_phase(params['test-namespace'], params['test-network-a']['pod2'], ['Running'], max_time=600):
        my_output.error('Pod has not reached desired state')
        return False
        
    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-b']['pod1']))
    if not params['k8s_handler'].wait_pod_phase(params['test-namespace'], params['test-network-b']['pod1'], ['Running'], max_time=600):
        my_output.error('Pod has not reached desired state')
        return False

    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-b']['pod2']))
    if not params['k8s_handler'].wait_pod_phase(params['test-namespace'], params['test-network-b']['pod2'], ['Running'], max_time=600):
        my_output.error('Pod has not reached desired state')
        return False

    return True


def check(params, my_output):
    my_output.default('Validate IP address assingment', underline=True, before_newline=True)

    my_output.default('Pod %s/%s' % (params['test-namespace'], params['test-network-a']['pod1']))
    output = params['k8s_handler'].get_pod_addresses(params['test-namespace'], params['test-network-a']['pod1'])
    if output is None:
        my_output.error('Failed to get ip address')
        return False    
    my_output.default(output, wrap='~~~')
    if params['test-network-a']['pod1v4'] not in output:
        my_output.error('IP address mismatch')
        return False
    my_output.default('IP address match', color='Green')
    if params['test-network-a']['pod1mac'] not in output:
        my_output.error('MAC address mismatch')
        return False
    my_output.default('MAC address match', color='Green')

    my_output.default('Pod %s/%s' % (params['test-namespace'], params['test-network-a']['pod2']), before_newline=True)
    output = params['k8s_handler'].get_pod_addresses(params['test-namespace'], params['test-network-a']['pod2'])
    if output is None:
        my_output.error('Failed to get ip address')
        return False    
    my_output.default(output, wrap='~~~')
    if params['test-network-a']['pod2v4'] not in output:
        my_output.error('IP address mismatch')
        return False
    my_output.default('IP address match', color='Green')
    if params['test-network-a']['pod2mac'] not in output:
        my_output.error('MAC address mismatch')
        return False
    my_output.default('MAC address match', color='Green')

    my_output.default('Pod %s/%s' % (params['test-namespace'], params['test-network-b']['pod1']), before_newline=True)
    output = params['k8s_handler'].get_pod_addresses(params['test-namespace'], params['test-network-b']['pod1'])
    if output is None:
        my_output.error('Failed to get ip address')
        return False    
    my_output.default(output, wrap='~~~')
    if params['test-network-b']['pod1v4'] not in output:
        my_output.error('IP address mismatch')
        return False
    my_output.default('IP address match', color='Green')
    if params['test-network-b']['pod1mac'] not in output:
        my_output.error('MAC address mismatch')
        return False
    my_output.default('MAC address match', color='Green')

    my_output.default('Pod %s/%s' % (params['test-namespace'], params['test-network-b']['pod2']), before_newline=True)
    output = params['k8s_handler'].get_pod_addresses(params['test-namespace'], params['test-network-b']['pod2'])
    if output is None:
        my_output.error('Failed to get ip address')
        return False    
    my_output.default(output, wrap='~~~')
    if params['test-network-b']['pod2v4'] not in output:
        my_output.error('IP address mismatch')
        return False
    my_output.default('IP address match', color='Green')
    if params['test-network-b']['pod2mac'] not in output:
        my_output.error('MAC address mismatch')
        return False
    my_output.default('MAC address match', color='Green')

    my_output.default('Validate connectivity within the network', underline=True, before_newline=True)

    my_output.default('Network: %s' % (params['test-network-a']['name']))

    output = params['k8s_handler'].get_pod_ping(params['test-namespace'], params['test-network-a']['pod1'], params['test-network-a']['pod2v4'])
    if output is None:
        my_output.error('Failed to run ping in test-network-a')
        return False
    
    my_output.default(output, wrap='~~~')
    if '100% packet loss' in output:
        my_output.error('Unexpected failure')
        return False
    
    my_output.default('Ping successful', color='Green')

    my_output.default('Network: %s' % (params['test-network-b']['name']), before_newline=True)

    output = params['k8s_handler'].get_pod_ping(params['test-namespace'], params['test-network-b']['pod1'], params['test-network-b']['pod2v4'])
    if output is None:
        my_output.error('Failed to run ping in test-network-b')
        return False
    
    my_output.default(output, wrap='~~~')
    if '100% packet loss' in output:
        my_output.error('Unexpected failure')
        return False

    my_output.default('Ping successful', color='Green')

    my_output.default('Validate connectivity across the network', underline=True, before_newline=True)

    my_output.default('Network: %s' % (params['test-network-a']['name']))

    output = params['k8s_handler'].get_pod_ping(params['test-namespace'], params['test-network-a']['pod1'], params['test-network-b']['pod2v4'])
    if output is None:
        my_output.error('Failed to run ping in test-network-a')
        return False
    
    my_output.default(output, wrap='~~~')
    if ' 0% packet loss' in output:
        my_output.error('Unexpected success')
        return False

    my_output.default('Ping unsuccessful', color='Green')

    return True


def cleanup(params, my_output):
    my_output.default('Delete pods')
    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-a']['pod1']))
    if params['k8s_handler'].is_pod(params['test-namespace'], params['test-network-a']['pod1']):
        if not params['k8s_handler'].delete_pod_mo(params['test-namespace'], params['test-network-a']['pod1']):
            my_output.error('rest api failed')
            return False
    
        if not params['k8s_handler'].wait_no_pod(params['test-namespace'], params['test-network-a']['pod1']):
            my_output.error('Pod is not gone')
            return False

    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-a']['pod2']))
    if params['k8s_handler'].is_pod(params['test-namespace'], params['test-network-a']['pod2']):
        if not params['k8s_handler'].delete_pod_mo(params['test-namespace'], params['test-network-a']['pod2']):
            my_output.error('rest api failed')
            return False
        
        if not params['k8s_handler'].wait_no_pod(params['test-namespace'], params['test-network-a']['pod2']):
            my_output.error('Pod is not gone')
            return False

    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-b']['pod1']))
    if params['k8s_handler'].is_pod(params['test-namespace'], params['test-network-b']['pod1']):
        if not params['k8s_handler'].delete_pod_mo(params['test-namespace'], params['test-network-b']['pod1']):
            my_output.error('rest api failed')
            return False
        
        if not params['k8s_handler'].wait_no_pod(params['test-namespace'], params['test-network-b']['pod1']):
            my_output.error('Pod is not gone')
            return False

    my_output.default('- %s/%s' % (params['test-namespace'], params['test-network-b']['pod2']))
    if params['k8s_handler'].is_pod(params['test-namespace'], params['test-network-b']['pod2']):
        if not params['k8s_handler'].delete_pod_mo(params['test-namespace'], params['test-network-b']['pod2']):
            my_output.error('rest api failed')
            return False
        
        if not params['k8s_handler'].wait_no_pod(params['test-namespace'], params['test-network-b']['pod2']):
            my_output.error('Pod is not gone')
            return False

    success = params['k8s_handler'].delete_clusterwide_private_network(
        params['test-network-a']['name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False

    success = params['k8s_handler'].delete_clusterwide_private_network(
        params['test-network-b']['name'],
        my_output=my_output,
        wait=True
    )
    if not success:
        return False
    
    if not global_common.cleanup_namespace(params['k8s_handler'], params['test-namespace'], my_output):
        return False
    
    return True


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cilium - Private Network Functional Test', before_newline=True, after_newline=True, double_underline=True) 

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    if not local_common.is_pnet_ready(params, my_output):
        return False     

    success = prepare(params, my_output)
    if not success:
        my_output.error('Test preparation failed')
    else:
        success = check(params, my_output)
        if not success:
            my_output.error('Check failed')

    if params['cleanup']:
        if not success and not params['cleanup-on-error']:
            if params['confirmation']:
                if not get_confirmation(title='Delete resources?'):
                    return False
            
        if not cleanup(params, my_output):
            my_output.error('Test cleanup failed')
            success = False

    if success:
        my_output.default('Test completed successfully', before_newline=True)
        
    return success
