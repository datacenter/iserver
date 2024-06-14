import sys
import copy
import traceback
import click

from progress.bar import IncrementalBar

from lib import file_helper
from lib import filter_helper
from lib.imc import endpoint as imc_endpoint
from lib.redfish import endpoint as redfish_endpoint
from lib.redfish import endpoint_settings as redfish_endpoint_settings
from lib.redfish import output as redfish_output
from lib.intersight.lcm import tag as lcm_server_tag
from lib.intersight import validations as intersight_validations

from menu import defaults
from menu import common
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("users")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--ip", "ip_filter", multiple=True, help="Select by IP or subnet")
@click.option("--name", "name_filter", multiple=True, callback=intersight_validations.name_filter, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, callback=intersight_validations.serial_filter, help="Select by serial")
@click.option("--group", "group_filter", default='', callback=validations.validate_group_serials, help="Group name")
@click.option("--file", "input_filename", is_flag=False, show_default=False, default='', type=click.STRING, help="Accounts Definition JSON")
@click.option("--verify", is_flag=True, show_default=True, default=False, help="Verify")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_redfish_users_command(
        ctx,
        iaccount,
        group_filter,
        serial_filter,
        name_filter,
        ip_filter,
        input_filename,
        verify,
        devel
    ):
    """Set redfish users accounts (batch)"""

    ctx.developer = devel

    try:
        redfish_output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)
        content = file_helper.get_file_json(input_filename)
        if content is None:
            ctx.my_output.error(
                'Failed to read the file: %s' % (input_filename)
            )
            raise ErrorExit

        ctx.my_output.default('Select target servers...')

        all_servers_mo = common.get_servers_mo(
            ctx,
            iaccount,
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=intersight_validations.add_group_filter(serial_filter, group_filter),
            include_rack=True,
            include_blade=False,
            show_progress=False
        )
        if all_servers_mo is None or len(all_servers_mo) == 0:
            ctx.my_output.error(
                'No servers matching search criteria'
            )
            raise ErrorExit

        selected_servers_mo = []
        for server_mo in all_servers_mo:
            exclude_server = False

            for exclude_tag in content['exclude']['tag']:
                for server_tag in server_mo['Tags']:
                    if server_tag['Key'] == exclude_tag.split(':')[0]:
                        if server_tag['Value'] == exclude_tag.split(':')[1]:
                            exclude_server = True

            for exclude_name in content['exclude']['name']:
                if filter_helper.match_string(exclude_name, server_mo['Name']):
                    exclude_server = True

            if not exclude_server:
                selected_servers_mo.append(
                    server_mo
                )

        if len(selected_servers_mo) == 0:
            ctx.my_output.error(
                'No servers matching search criteria'
            )
            raise ErrorExit

        common.print_servers_mo_info(
            ctx,
            iaccount,
            selected_servers_mo,
            show_progress=True,
            cache=False
        )

        if not common.get_confirmation():
            return

        if verify:
            verified_mo = []

            bar_handler = IncrementalBar('Verify users', max=len(selected_servers_mo))
            bar_handler.goto(0)
            for server_mo in selected_servers_mo:
                verified = True
                accounts = []

                if content['create_accounts']:
                    for account in content['account']:
                        accounts.append(account)

                if content['new_admin_password'] is None:
                    admin_account = {}
                    admin_account['username'] = content['admin_username']
                    admin_account['password'] = content['admin_account']
                    accounts.append(admin_account)

                if content['new_admin_password'] is not None:
                    admin_account = {}
                    admin_account['username'] = content['admin_username']
                    admin_account['password'] = content['new_admin_password']
                    accounts.append(admin_account)

                for account in accounts:
                    ctx.my_output.default(
                        'Verify user %s on %s' % (
                            account['username'],
                            server_mo['ManagementIp']
                        )
                    )

                    redfish_handler = redfish_endpoint.RedfishEndpoint(
                        'ucsc',
                        server_mo['ManagementIp'],
                        443,
                        account['username'],
                        account['password'],
                        get_timeout=30,
                        auto_connect=True,
                        ssl_verify=False,
                        log_id=ctx.run_id
                    )

                    if not redfish_handler.is_connected():
                        verified = False

                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler

                    if not verified:
                        break

                if verified:
                    verified_mo.append(
                        server_mo
                    )

                bar_handler.next()

            bar_handler.finish()

            if len(verified_mo) == 0:
                ctx.my_output.default(
                    'No servers verified'
                )
                return

            common.print_servers_mo_info(
                ctx,
                iaccount,
                verified_mo,
                show_progress=True,
                cache=False
            )

            if content['tag'] is not None:
                if not common.get_confirmation():
                    return

                ctx.my_output.default(
                    'Update server tags in Intersight'
                )

                lcm_server_tag_handler = lcm_server_tag.LcmServerTag(
                    iaccount,
                    dry_run=False,
                    wait=True,
                    silent=False,
                    verbose=False,
                    debug=False,
                    log_id=ctx.run_id
                )
                if not lcm_server_tag_handler.add(verified_mo, [content['tag']]):
                    raise ErrorExit

            return

        failed_servers_mo = []

        for server_mo in selected_servers_mo:
            servers_mo = [server_mo]
            common.print_servers_mo_info(
                ctx,
                iaccount,
                servers_mo,
                show_progress=True,
                cache=False,
                title=False
            )

            if len(content['admin_passwords']) == 1:
                server_admin_password = content['admin_passwords'][0]
            else:
                server_admin_password = None

                ctx.my_output.default('Verify current admin password...')
                imc_handler = imc_endpoint.ImcEndpoint(
                    server_mo['ManagementIp'],
                    22,
                    content['admin_username'],
                    content['admin_passwords'][0],
                    log_id=ctx.run_id
                )
                version = imc_handler.get_version()
                del imc_handler

                if version is not None:
                    server_admin_password = content['admin_passwords'][0]
                    ctx.my_output.default('Current admin password: %s' % (server_admin_password))

                if version is None:
                    imc_handler = imc_endpoint.ImcEndpoint(
                        server_mo['ManagementIp'],
                        22,
                        content['admin_username'],
                        content['admin_passwords'][1],
                        log_id=ctx.run_id
                    )
                    version = imc_handler.get_version()
                    del imc_handler

                    if version is not None:
                        server_admin_password = content['admin_passwords'][1]
                        ctx.my_output.default('Current admin password: %s' % (server_admin_password))

                if server_admin_password is None:
                    ctx.my_output.error(
                        'Admin password verification failed'
                    )
                    failed_servers_mo.append(server_mo)
                    continue

            ctx.my_output.default('Enable redfish access...')
            imc_handler = imc_endpoint.ImcEndpoint(
                server_mo['ManagementIp'],
                22,
                content['admin_username'],
                server_admin_password,
                log_id=ctx.run_id
            )
            success = imc_handler.enable_redfish()
            del imc_handler

            if not success:
                ctx.my_output.error(
                    'Failed to enable redfish on %s' % (
                        server_mo['ManagementIp']
                    )
                )
                failed_servers_mo.append(server_mo)
                continue

            ctx.my_output.default('Verify admin access via RedFish...')
            if server_mo['ManagementIp'] is None:
                ctx.my_output.error(
                    'No management IP of server %s' % (
                        server_mo['Moid']
                    )
                )
                failed_servers_mo.append(server_mo)
                continue

            redfish_handler = redfish_endpoint.RedfishEndpoint(
                'ucsc',
                server_mo['ManagementIp'],
                443,
                content['admin_username'],
                server_admin_password,
                get_timeout=120,
                auto_connect=True,
                ssl_verify=False,
                log_id=ctx.run_id
            )
            account = redfish_handler.endpoint_handler.get_account_by_username(content['admin_username'], cache_enabled=False)
            redfish_handler.endpoint_handler.disconnect()
            del redfish_handler

            if account is None:
                ctx.my_output.error(
                    'Failed to get username %s from %s' % (
                        content['admin_username'],
                        server_mo['ManagementIp']
                    )
                )
                failed_servers_mo.append(server_mo)
                continue

            ctx.my_output.default('Update RedFish access settings...')
            redfish_handler = redfish_endpoint.RedfishEndpoint(
                'ucsc',
                server_mo['ManagementIp'],
                443,
                content['admin_username'],
                server_admin_password,
                get_timeout=30,
                ssl_verify=False,
                log_id=ctx.run_id
            )
            identity = redfish_handler.endpoint_handler.get_template_identity_properties()

            if identity is None:
                ctx.my_output.error(
                    'Failed to collect identity from %s' % (
                        server_mo['ManagementIp']
                    )
                )
                redfish_handler.endpoint_handler.disconnect()
                del redfish_handler
                failed_servers_mo.append(server_mo)
                continue

            endpoint_settings_handler = redfish_endpoint_settings.RedfishEndpointSettings(
                log_id=ctx.run_id
            )
            success = endpoint_settings_handler.set_redfish_endpoint_settings(
                redfish_handler.endpoint_handler.get_endpoint_configuration(),
                identity
            )

            redfish_handler.endpoint_handler.disconnect()
            del redfish_handler
            del endpoint_settings_handler

            if not success:
                ctx.my_output.error(
                    'Failed to save endpoint identity from %s' % (
                        server_mo['ManagementIp']
                    )
                )
                failed_servers_mo.append(server_mo)
                continue

            if content['delete_non_admin_role']:
                ctx.my_output.default('Delete non-admin role users')

                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    content['admin_username'],
                    server_admin_password,
                    get_timeout=30,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )

                imc_handler = imc_endpoint.ImcEndpoint(
                    server_mo['ManagementIp'],
                    22,
                    content['admin_username'],
                    server_admin_password,
                    log_id=ctx.run_id
                )

                allowed_usernames = []
                for account in content['account']:
                    allowed_usernames.append(
                        account['username']
                    )

                usernames = redfish_handler.endpoint_handler.get_non_admin_role_usernames(allowed_usernames=allowed_usernames)
                if usernames is None:
                    ctx.my_output.error(
                        'Failed to get accounts from %s' % (
                            server_mo['ManagementIp']
                        )
                    )
                    failed_servers_mo.append(server_mo)
                    continue

                if len(usernames) == 0:
                    ctx.my_output.default(
                        'No non-admin users found'
                    )

                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    del imc_handler

                if len(usernames) > 0:
                    user_delete_success = True
                    for username in usernames:
                        account = redfish_handler.endpoint_handler.get_account_by_username(username, cache_enabled=False)
                        if account is None:
                            ctx.my_output.error(
                                'Failed to get account %s from %s' % (
                                    username,
                                    server_mo['ManagementIp']
                                )
                            )
                            user_delete_success = False
                            break

                        success = imc_handler.delete_user(
                            account['id']
                        )
                        if not success:
                            ctx.my_output.error(
                                'Failed to delete account %s from %s' % (
                                    username,
                                    server_mo['ManagementIp']
                                )
                            )
                            user_delete_success = False
                            break

                        ctx.my_output.default(
                            'User %s deleted' % (username)
                        )

                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    del imc_handler

                    if not user_delete_success:
                        failed_servers_mo.append(server_mo)
                        continue

                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    content['admin_username'],
                    server_admin_password,
                    get_timeout=30,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )
                accounts = redfish_handler.endpoint_handler.get_template_properties('account', cache_enabled=False)
                redfish_handler.endpoint_handler.disconnect()
                del redfish_handler

                if accounts is None:
                    ctx.my_output.error(
                        'Failed to get existing accounts from server: %s' % (
                            server_mo['ManagementIp']
                        )
                    )
                    failed_servers_mo.append(server_mo)
                    continue

                redfish_output_handler.print_ucsc_properties(
                    'account',
                    accounts,
                    title=False
                )

            if content['create_accounts']:
                ctx.my_output.default('Create users')
                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    content['admin_username'],
                    server_admin_password,
                    get_timeout=30,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )

                imc_handler = imc_endpoint.ImcEndpoint(
                    server_mo['ManagementIp'],
                    22,
                    content['admin_username'],
                    server_admin_password,
                    log_id=ctx.run_id
                )

                ctx.my_output.default('Get unused account ids')
                account_ids = redfish_handler.endpoint_handler.get_account_empty_ids(cache_enabled=False)
                if account_ids is None:
                    ctx.my_output.error(
                        'Failed to get empty account ids on server %s' % (
                            server_mo['ManagementIp']
                        )
                    )

                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    del imc_handler
                    failed_servers_mo.append(server_mo)
                    continue

                if len(account_ids) < len(content['account']):
                    ctx.my_output.error(
                        'Failed to get enough account ids on server %s' % (
                            server_mo['ManagementIp']
                        )
                    )
                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    del imc_handler
                    failed_servers_mo.append(server_mo)
                    continue

                index = 0
                create_user_success = True
                for account in content['account']:
                    ctx.my_output.default('Create: %s' % (account))
                    if redfish_handler.endpoint_handler.is_account_username(account['username']):
                        ctx.my_output.error(
                            'Username %s is already defined on server %s' % (
                                account['username'],
                                server_mo['ManagementIp']
                            )
                        )
                        create_user_success = False
                        break

                    if 'id' in account:
                        account_id = account['id']
                    else:
                        account_id = account_ids[index]

                    success = imc_handler.add_user(
                        account_id,
                        account['username'],
                        account['password'],
                        account['role']
                    )
                    if not success:
                        ctx.my_output.error(
                            'Failed to create new account on server %s' % (
                                server_mo['ManagementIp']
                            )
                        )
                        create_user_success = False
                        break

                    ctx.my_output.default(
                        'User %s with id %s created on %s' % (
                            account['username'],
                            account_id,
                            server_mo['ManagementIp']
                        )
                    )

                    index = index + 1

                redfish_handler.endpoint_handler.disconnect()
                del redfish_handler
                del imc_handler

                if not create_user_success:
                    failed_servers_mo.append(server_mo)
                    continue

                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    content['admin_username'],
                    server_admin_password,
                    get_timeout=30,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )
                accounts = redfish_handler.endpoint_handler.get_template_properties('account', cache_enabled=False)
                redfish_handler.endpoint_handler.disconnect()
                del redfish_handler

                if accounts is None:
                    ctx.my_output.error(
                        'Failed to get existing accounts from server: %s' % (
                            server_mo['ManagementIp']
                        )
                    )
                    failed_servers_mo.append(server_mo)
                    continue

                redfish_output_handler.print_ucsc_properties(
                    'account',
                    accounts,
                    title=False
                )

            if content['new_admin_password'] is not None and content['new_admin_password'] != server_admin_password:
                ctx.my_output.default('Change admin password')
                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    content['admin_username'],
                    server_admin_password,
                    get_timeout=30,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )

                imc_handler = imc_endpoint.ImcEndpoint(
                    server_mo['ManagementIp'],
                    22,
                    content['admin_username'],
                    server_admin_password,
                    log_id=ctx.run_id
                )

                account = redfish_handler.endpoint_handler.get_account_by_username(content['admin_username'], cache_enabled=False)
                if account is None:
                    ctx.my_output.error(
                        'Failed to get admin account %s  on server %s' % (
                            content['admin_username'],
                            server_mo['ManagementIp']
                        )
                    )
                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    del imc_handler
                    failed_servers_mo.append(server_mo)
                    continue

                success = imc_handler.set_user(
                    account['id'],
                    content['new_admin_password'],
                    'admin'
                )
                if not success:
                    ctx.my_output.error(
                        'Failed to set admin account %s password on server %s' % (
                            content['admin_username'],
                            server_mo['ManagementIp']
                        )
                    )
                    del redfish_handler
                    del imc_handler
                    failed_servers_mo.append(server_mo)
                    continue

                redfish_handler.endpoint_handler.disconnect()
                del redfish_handler
                del imc_handler

            ctx.my_output.default('Update RedFish access settings')
            accounts = copy.deepcopy(content['account'])
            if content['new_admin_password'] is not None:
                admin_account = {}
                admin_account['username'] = content['admin_username']
                admin_account['password'] = content['new_admin_password']
                admin_account['username'] = 'admin'
                accounts.append(admin_account)

            users_verified = True
            for account in accounts:
                ctx.my_output.default(
                    'Verify user %s on %s' % (
                        account['username'],
                        server_mo['ManagementIp']
                    )
                )

                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    account['username'],
                    account['password'],
                    get_timeout=30,
                    auto_connect=True,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )

                if not redfish_handler.is_connected():
                    ctx.my_output.error(
                        'Username %s not working on server %s' % (
                            account['username'],
                            server_mo['ManagementIp']
                        )
                    )
                    users_verified = False
                    break

            redfish_handler.endpoint_handler.disconnect()
            del redfish_handler

            if not users_verified:
                failed_servers_mo.append(server_mo)
                continue

            if content['new_admin_password'] is not None and content['new_admin_password'] != server_admin_password:
                ctx.my_output.default('Update RedFish access settings with new admin password')
                redfish_handler = redfish_endpoint.RedfishEndpoint(
                    'ucsc',
                    server_mo['ManagementIp'],
                    443,
                    content['admin_username'],
                    content['new_admin_password'],
                    get_timeout=30,
                    ssl_verify=False,
                    log_id=ctx.run_id
                )
                identity = redfish_handler.endpoint_handler.get_template_identity_properties()

                if identity is None:
                    ctx.my_output.error(
                        'Failed to collect identity from %s' % (
                            server_mo['ManagementIp']
                        )
                    )
                    failed_servers_mo.append(server_mo)
                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    continue

                endpoint_settings_handler = redfish_endpoint_settings.RedfishEndpointSettings(
                    log_id=ctx.run_id
                )
                success = endpoint_settings_handler.set_redfish_endpoint_settings(
                    redfish_handler.endpoint_handler.get_endpoint_configuration(),
                    identity
                )
                if not success:
                    ctx.my_output.error(
                        'Failed to save endpoint identity from %s' % (
                            server_mo['ManagementIp']
                        )
                    )
                    failed_servers_mo.append(server_mo)
                    redfish_handler.endpoint_handler.disconnect()
                    del redfish_handler
                    continue

                redfish_handler.endpoint_handler.disconnect()
                del redfish_handler

            if content['tag_success'] is not None:
                ctx.my_output.default(
                    'Update server tags in Intersight'
                )

                lcm_server_tag_handler = lcm_server_tag.LcmServerTag(
                    iaccount,
                    dry_run=False,
                    wait=True,
                    silent=False,
                    verbose=False,
                    debug=False,
                    log_id=ctx.run_id
                )
                if not lcm_server_tag_handler.add([server_mo], [content['tag_success']]):
                    ctx.my_output.error(
                        'Server tag failed'
                    )

        if len(failed_servers_mo) > 0:
            ctx.my_output.default(
                'Setting failed servers tag'
            )
            for failed_server_mo in failed_servers_mo:
                ctx.my_output.default(
                    '- %s' % (failed_server_mo['Name'])
                )

            lcm_server_tag_handler = lcm_server_tag.LcmServerTag(
                iaccount,
                dry_run=False,
                wait=True,
                silent=False,
                verbose=False,
                debug=False,
                log_id=ctx.run_id
            )
            if not lcm_server_tag_handler.add(failed_servers_mo, [content['tag_failure']]):
                ctx.my_output.error(
                    'Server tag failed'
                )

        common.print_servers_info(
            ctx,
            iaccount,
            ip_filter=ip_filter,
            name_filter=name_filter,
            serial_filter=new_serial_filter,
            include_rack=True,
            include_blade=False,
            show_progress=False
        )

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
