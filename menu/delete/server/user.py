import sys
import threading
import traceback
import click

from lib.imc import endpoint as imc_endpoint
from lib.redfish import endpoint as redfish_endpoint
from lib.redfish import output as redfish_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("user")
@click.pass_obj
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--admin", "admin_password", default='', help="Admin password")
@click.option("--username", default='', help="Username")
@click.option("--no-confirm", "no_confirm", is_flag=True, show_default=True, default=False, help="No confirmation mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def delete_server_user_command(ctx, endpoint_ip, admin_password, username, no_confirm, devel):
    """Delete server user account"""

    ctx.developer = devel

    try:
        if len(admin_password) == 0:
            ctx.my_output.error(
                'Define admin password'
            )
            raise ErrorExit

        if len(username) == 0:
            ctx.my_output.error(
                'Define username to be deleted'
            )
            raise ErrorExit

        redfish_output_handler = redfish_output.RedfishOutput(log_id=ctx.run_id)
        redfish_handler = redfish_endpoint.RedfishEndpoint(
            'ucsc',
            endpoint_ip,
            443,
            'admin',
            admin_password,
            get_timeout=120,
            auto_connect=True,
            ssl_verify=False,
            log_id=ctx.run_id
        )

        if username == '__NOT_ADMIN__':
            usernames = redfish_handler.endpoint_handler.get_non_admin_role_usernames()
            if usernames is None:
                ctx.my_output.error(
                    'Failed to get non-admin accounts'
                )
                raise ErrorExit

            if len(usernames) == 0:
                ctx.my_output.error(
                    'No non-admin accounts'
                )
                return

        if username != '__NOT_ADMIN__':
            usernames = [username]

        to_be_deleted = []
        for candidate in usernames:
            if not redfish_handler.endpoint_handler.is_account_username(candidate):
                ctx.my_output.default(
                    'Username %s is already not defined' % (candidate)
                )
                continue

            to_be_deleted.append(candidate)

        if len(to_be_deleted) > 0:
            imc_handler = imc_endpoint.ImcEndpoint(
                endpoint_ip,
                22,
                'admin',
                admin_password,
                log_id=ctx.run_id
            )

            for item in to_be_deleted:
                account = redfish_handler.endpoint_handler.get_account_by_username(item)
                redfish_output_handler.print_ucsc_properties(
                    'account',
                    [account],
                    title=False
                )

                if not no_confirm:
                    value = input('Confirm (Y/N) ')
                    if value.lower() != 'y':
                        ctx.my_output.default(
                            'No action taken'
                        )
                        return

                ctx.my_output.default(
                    'Deleting user %s...' % (item)
                )

                success = imc_handler.delete_user(
                    account['id']
                )
                if not success:
                    ctx.my_output.error(
                        'User %s delete failed' % (item)
                    )
                    raise ErrorExit

                ctx.my_output.default(
                    'User %s deleted' % (item)
                )

            ctx.busy = False

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
