import click

from lib.imc import settings


def validate_cache_ttl(user_cache_ttl, log_id=None):
    endpoint_settings_handler = settings.ImcEndpointSettings(log_id=log_id)
    endpoint_settings = endpoint_settings_handler.get_imc_settings()
    if endpoint_settings['CacheEnabled']:
        cache_ttl = endpoint_settings['CacheTtl']
    else:
        cache_ttl = -1

    if user_cache_ttl is not None:
        try:
            cache_ttl = int(user_cache_ttl)
        except BaseException:
            pass

    return cache_ttl


def get_imc_cli_endpoints(ctx, endpoint_ips, username, password, update_settings=True):
    endpoint_settings_handler = settings.ImcEndpointSettings(log_id=ctx.run_id)
    endpoints = []

    for endpoint_ip in endpoint_ips:
        endpoint_settings = endpoint_settings_handler.get_cli_endpoint(endpoint_ip)
        if endpoint_settings is None:
            if len(username) == 0 or len(password) == 0:
                ctx.my_output.error('Define username and password for endpoint: %s' % (endpoint_ip))
                return None

            endpoint_settings = {}
            endpoint_settings['ip'] = endpoint_ip
            endpoint_settings['port'] = 22
            endpoint_settings['username'] = username
            endpoint_settings['password'] = password

            if update_settings:
                endpoint_settings_handler.set_imc_ssh_access(
                    endpoint_ip,
                    username=username,
                    password=password
                )

        endpoints.append(
            endpoint_settings
        )

    return endpoints

def validate_boot_order(ctx, param, values):
    if len(values) == 0:
        raise click.BadParameter('Define at least one boot order parameter')

    allowed = ['hdd', 'pxe', 'fdd', 'efi', 'cdrom']
    for value in values:
        if value not in allowed:
            raise click.BadParameter('Allowed boot order parameter: %s' % (','.join(allowed)))

    return values

def validate_boot_device_type(ctx, param, value):
    if len(value) == 0:
        raise click.BadParameter('Define at boot device type')

    allowed = [
        'PXE',
        'ISCSI',
        'LOCALHDD',
        'SAN',
        'USB',
        'VMEDIA',
        'PCHSTORAGE',
        'UEFISHELL',
        'NVME',
        'LOCALCDD',
        'HTTP',
        'EMBEDDEDSTORAGE'
    ]
    if value not in allowed:
        raise click.BadParameter('Allowed boot device type: %s' % (','.join(allowed)))

    return value
