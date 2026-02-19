from progress.bar import Bar

from lib import iaccount_helper
from lib import output_helper

from lib.intersight import compute
from lib.intersight import fi


def get_iaccount_domain(iaccount):
    iaccount_handler = iaccount_helper.IntersightAccount()
    iaccount_metadata = iaccount_handler.get_iaccount_description(iaccount)
    if iaccount_metadata is None or 'domain' not in iaccount_metadata or iaccount_metadata['domain'] is None:
        return None
    return iaccount_metadata['domain']


def get_all_servers_hw(iaccount, cache_ttl, log_id=None, silent=False):
    my_output = output_helper.OutputHelper(log_id=log_id)
    if not silent:
        my_output.default('Select servers...')

    compute_handler = compute.Compute(iaccount, log_id=log_id)
    servers_mo = compute_handler.get_mo(
        match_rules=compute_handler.get_mo_match_rules(),
        include_rack=True,
        rack_expand=['PciDevices', 'Psus', 'Fanmodules', 'RegisteredDevice'],
        include_blade=True,
        blade_expand=['PciDevices', 'PciNodes', 'RegisteredDevice'],
        cache_ttl=None
    )

    if not silent:
        my_output.default('Collect server api objects...')

    settings = {}
    settings['board'] = True
    settings['connector'] = True
    settings['cpu'] = True
    settings['fan'] = True
    settings['gpu'] = True
    settings['locator'] = True
    settings['memory'] = True
    settings['net'] = True
    settings['pci'] = True
    settings['psu'] = True
    settings['state'] = True
    settings['storage'] = True
    settings['tpm'] = True
    settings['workflow'] = None
    compute_handler.set_cache(
        servers_mo,
        settings,
        cache_ttl
    )

    bar_handler = None
    if not silent:
        bar_handler = Bar('Collect server information', max=len(servers_mo))
        bar_handler.goto(0)

    match_rules = {}
    servers_info = compute_handler.get_info(
        servers_mo,
        settings,
        match_rules,
        cache_ttl,
        prepare_cache=False,
        bar_handler=bar_handler
    )

    if not silent:
        bar_handler.finish()
        my_output.default('Selected servers: %s' % (len(servers_mo)))

    return servers_info


def get_all_servers(iaccount, cache_ttl, log_id=None, silent=False):
    my_output = output_helper.OutputHelper(log_id=log_id)

    if not silent:
        my_output.default('Select servers...')

    compute_handler = compute.Compute(iaccount, log_id=log_id)
    servers_mo = compute_handler.get_mo(
        match_rules=compute_handler.get_mo_match_rules(),
        include_rack=True,
        include_blade=True,
        cache_ttl=None
    )

    if not silent:
        my_output.default('Collect server api objects [%s]...' % (len(servers_mo)))

    settings = {}
    compute_handler.set_cache(
        servers_mo,
        settings,
        cache_ttl
    )

    bar_handler = None
    if not silent:
        bar_handler = Bar('Collect server information', max=len(servers_mo))
        bar_handler.goto(0)

    match_rules = {}
    servers_info = compute_handler.get_info(
        servers_mo,
        settings,
        match_rules,
        cache_ttl,
        prepare_cache=False,
        bar_handler=bar_handler
    )

    if not silent:
        bar_handler.finish()
        my_output.default('Selected servers: %s' % (len(servers_mo)))

    return servers_info


def get_all_servers_net(iaccount, cache_ttl, log_id=None, silent=False):
    my_output = output_helper.OutputHelper(log_id=log_id)
    if not silent:
        my_output.default('Select servers...')

    compute_handler = compute.Compute(iaccount, log_id=log_id)
    servers_mo = compute_handler.get_mo(
        match_rules=compute_handler.get_mo_match_rules(),
        include_rack=True,
        rack_expand=['PciDevices'],
        include_blade=True,
        blade_expand=['PciDevices'],
        cache_ttl=None
    )

    if not silent:
        my_output.default('Collect server api objects [%s]...' % (len(servers_mo)))

    settings = {}
    settings['net'] = True
    settings['pci'] = True
    compute_handler.set_cache(
        servers_mo,
        settings,
        cache_ttl
    )

    bar_handler = None
    if not silent:
        bar_handler = Bar('Collect server information', max=len(servers_mo))
        bar_handler.goto(0)

    match_rules = {}
    servers_info = compute_handler.get_info(
        servers_mo,
        settings,
        match_rules,
        cache_ttl,
        prepare_cache=False,
        bar_handler=bar_handler
    )

    if not silent:
        bar_handler.finish()
        my_output.default('Selected servers: %s' % (len(servers_mo)))

    return servers_info


def get_all_fis(iaccount, cache_ttl, log_id=None, silent=False):
    my_output = output_helper.OutputHelper(log_id=log_id)
    if not silent:
        my_output.default('Select fis...')

    fi_handler = fi.Fi(iaccount, log_id=log_id)
    fis_mo = fi_handler.get_mo(
        cache_ttl=None
    )
    settings = {}
    settings['summary'] = True
    settings['eth'] = True
    settings['pc'] = True

    fi_handler.set_cache(
        fis_mo,
        settings,
        cache_ttl
    )

    bar_handler = None
    if not silent:
        bar_handler = Bar('Collect fi information', max=len(fis_mo))
        bar_handler.goto(0)

    match_rules = {}
    fis_info = fi_handler.get_info(
        fis_mo,
        settings,
        match_rules,
        cache_ttl,
        prepare_cache=False,
        bar_handler=bar_handler
    )

    if not silent:
        bar_handler.finish()
        my_output.default('Selected servers: %s' % (len(fis_mo)))

    return fis_info
