from lib import ip_helper
from lib import filter_helper
from lib import output_helper
from lib.workflow.ocp_intersight_operator import common as local_common
from lib.workflow import ocp_common


def validate(params):
    rules = [
        ['cluster', False, None, 'str', None, None, None, None],
        ['client-id', False, None, 'str', None, None, None, None],
        ['client-secret', False, None, 'str', None, None, None, None],
        ['location', False, None, 'str', None, None, ['us', 'eu', 'va'], None]
    ]
    success, params, allowed_keys = ocp_common.check_parameters(params, rules)
    if not success:
        return None, params

    return ocp_common.sanitize_params(params, allowed_keys, defaults=local_common.get_default_params()), None

    
def run(params, log_id=None):
    my_output = output_helper.OutputHelper(log_id=log_id)
    my_output.default('OpenShift Workflow - Cisco Intersight Operator - Register Account', before_newline=True, after_newline=True, double_underline=True)

    params, error = validate(params)
    if error is not None:
        my_output.error(error)
        return False

    if params['initialize']:
        params = ocp_common.workflow_init(params, my_output, log_id)
        if params is None:
            return False

    subscription = ocp_common.get_subscription(
        params['k8s_handler'],
        params['__default__']['name'],
        my_output=my_output,
        brief=True
    )
    if subscription is None:
        return True
    
    if not params['k8s_handler'].is_any_intersight(cache_enabled=False):
        my_output.error('Create CiscoIntersight instance first')
        return False

    data = {}
    data['ClientId'] = ip_helper.encode_text_64(params['client-id'])
    data['ClientSecret'] = ip_helper.encode_text_64(params['client-secret'])
    data['ApplianceHostNames'] = ip_helper.encode_text_64('[]')
    if params['location'] == 'us':
        data['CloudHostName'] = ip_helper.encode_text_64('https://us-east-1.intersight.com')
        data['Location'] = ip_helper.encode_text_64('us-east-1')

    if params['location'] == 'eu':
        data['CloudHostName'] = ip_helper.encode_text_64('https://eu-central-1.intersight.com')
        data['Location'] = ip_helper.encode_text_64('eu-central-1')

    if params['location'] == 'va':
        my_output.error('Virtual appliance not supported yet')
        return False
    
    data['ProxyHostIp'] = ''
    data['ProxyPort'] = ''
    data['ProxyUsername'] = ''
    data['ProxyPassword'] = ''

    proxy = params['k8s_handler'].get_proxy('cluster')
    if proxy is not None:
        proxy_https = filter_helper.get(proxy, 'https_proxy')
        if proxy_https is not None:
            parsed = ip_helper.get_url_parse(proxy_https)
            if parsed is not None:
                data['ProxyHostIp'] = ip_helper.encode_text_64(parsed['hostname'])
                data['ProxyPort'] = ip_helper.encode_text_64(str(parsed['port']))

    success = params['k8s_handler'].create_or_update_secret_kv(
        params['__default__']['namespace'],
        params['__default__']['secret'],
        data, 
        secret_type='Opaque',
        replace=True,
        confirmation=params['confirmation'], 
        my_output=my_output, 
        wait=True
    )
    if not success:
        return False
    
    my_output.default('')
    my_output.default('Completed tasks')
    my_output.default('- Cisco intersight account registered')
    return True
