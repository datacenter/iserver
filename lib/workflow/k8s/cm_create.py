from lib import output_helper
from lib.workflow.k8s import common as local_common
from lib.workflow import ocp_common
from lib import file_helper
from lib import filter_helper


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['__id__', True, None, None, None, None, None, None],
        ['namespace', False, None, 'str', None, None, None, None],
        ['name', False, None, 'str', None, None, None, None],
        ['content', False, None, 'dict', None, None, None, None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules, extras=['__type__'])
    if not success:
        return None, params

    # "__type__": "config-map",
    # "name": "c8kv${__id__}-day0",
    # "content": {
    #     "iosxe_config.txt": {
    #         "file": "C:\\tmp\\c8kv-data.txt",
    #         "vars": {
    #             "HOSTNAME": "c8kv${__id__}",
    #             "ADDRESS": "15.2${__id__}.2${__id__}.2${__id__}",
    #             "MASK": "255.255.255.0"
    #         }
    #     }
    # }
    params['data'] = {}
    allowed_keys.append('data')
    for key in params['content']:
        filename = filter_helper.get(params['content'][key], 'file')
        if filename is None:
            return None, 'Config map data with file reference required'
        
        variables = {}
        if '__id__' in params and params['__id__'] is not None:
            if '__id__' not in variables:
                variables['__id__'] = params['__id__']

        cm_vars = filter_helper.get(params['content'][key], 'vars', on_error={}, on_none={})
        if not isinstance(cm_vars, dict):
            return None, 'Config map data with vars dict required'
        
        for cm_var in cm_vars:
            cm_vars[cm_var] = filter_helper.replace_attributes(cm_vars[cm_var], variables)

        params['data'][key] = file_helper.get_file_text(
            filename,
            cm_vars
        )
        if params['data'][key] is None:
            return None, 'Config map data file read failed: %s' % (filename)

        if file_helper.is_content_attributes(params['data'][key]):
            unresolved = file_helper.get_content_attributes(params['data'][key])
            return None, 'Config map data file %s has unresolved variables: %s' % (filename, ', '.join(unresolved))
        
    return local_common.sanitize_params(params, allowed_keys), None


def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('Kubernetes Workflow - Config Map - Create', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    params = local_common.initialize(params, my_output, log_id)
    if params is None:
        return False

    success = params['k8s_handler'].create_or_update_config_map(
        params['namespace'], 
        params['name'], 
        params['data'], 
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True        
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- config map created')
    return True
