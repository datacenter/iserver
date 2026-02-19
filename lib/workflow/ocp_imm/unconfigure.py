import json
from lib import ip_helper
from lib import iaccount_helper
from lib import output_helper
from lib.k8s import output as k8s_output
from lib.intersight import helper as intersight_helper
from lib.workflow.ocp_imm import common as local_common


def validate(params):
    if 'cluster' not in params or params['cluster'] is None:
        return None, 'Cluster name required'

    if 'iaccount' not in params or params['iaccount'] is None or len(params['iaccount']) == 0:
        params['iaccount'] = None

    if 'verbose' not in params:
        params['verbose'] = False

    if not isinstance(params['verbose'], bool):
        return None, 'verbose param must be true or false'
    
    if 'check-verbose' not in params:
        params['check-verbose'] = params['verbose']

    if not isinstance(params['check-verbose'], bool):
        return None, 'check-verbose param must be true or false'
    
    params['iaccout_key'] = None
    if params['iaccount'] is not None:
        iaccount_handler = iaccount_helper.IntersightAccount()
        iaccount_configuration = iaccount_handler.get_iaccount_configuration(params['iaccount'])
        if iaccount_configuration is None:
            return None, 'Intersight account not found'

        params['iaccount_key'] = iaccount_configuration['keyid']
    
    allowed_keys = [
        'cluster',
        'iaccount',
        'iaccount_key',
        'verbose',
        'check-verbose'
    ]
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Intersight Hardware - Unconfigure', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False
    
    nodes = params['k8s_handler'].get_nodes()
    if nodes is None:
        my_output.error('Failed to get nodes')
        return False
    
    for node in nodes:
        my_output.default('Node [%s]' % (node['name']))

        is_other_intersight_annotation = False
        annotation_key = None
        annotation_dev_key = None
        if params['iaccount_key'] is not None:
            annotation_key = 'intersight-%s' % (ip_helper.get_string_md5(params['iaccount_key']))
            annotation_key = 'intersight-dev-%s' % (ip_helper.get_string_md5(params['iaccount_key']))

        for annotation in node['annotations']:
            if annotation_key is not None and annotation == annotation_key:
                my_output.default('- delete annotation: %s' % (annotation_key))
                if not params['k8s_handler'].delete_node_annotation(node['name'], annotation_key):
                    my_output.error('rest api failed')
                    return False

            if annotation_dev_key is not None and annotation == annotation_dev_key:
                my_output.default('- delete annotation: %s' % (annotation_dev_key))
                if not params['k8s_handler'].delete_node_annotation(node['name'], annotation_dev_key):
                    my_output.error('rest api failed')
                    return False
                
            if annotation_key is None and annotation.startswith('intersight-'):
                is_other_intersight_annotation = True
                my_output.default('- delete annotation: %s' % (annotation))
                if not params['k8s_handler'].delete_node_annotation(node['name'], annotation_key):
                    my_output.error('rest api failed')
                    return False

        if params['iaccount_key'] is None or not is_other_intersight_annotation:
            for annotation in node['annotations']:
                if annotation.startswith('server-'):
                    my_output.default('- delete annotation: %s' % (annotation))
                    if not params['k8s_handler'].delete_node_annotation(node['name'], annotation_key):
                        my_output.error('rest api failed')
                        return False

    return True
