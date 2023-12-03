import sys
import threading
import traceback
import click

from lib.imc import endpoint as imc_endpoint
from lib.redfish import endpoint as redfish_endpoint
from lib.redfish import output as redfish_output

from menu import progress
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("user")
@click.pass_obj
@click.option("--ip", "endpoint_ip", default='', callback=validations.validate_ip, help="Management IP address")
@click.option("--admin", "admin_password", default='', help="Admin password")
@click.option("--username", default='', help="Username")
@click.option("--password", default='', help="Password")
@click.option("--role", type=click.Choice(['admin', 'user', 'readonly'], case_sensitive=False), default='readonly', help="Role")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_server_user_command(ctx, endpoint_ip, admin_password, username, password, role, devel):
    """Create server user account"""

    ctx.developer = devel

    try:
        if len(admin_password) == 0:
            ctx.my_output.error(
                'Define admin password'
            )
            raise ErrorExit

        if len(username) == 0:
            ctx.my_output.error(
                'Define username'
            )
            raise ErrorExit

        if len(password) == 0:
            ctx.my_output.error(
                'Define password'
            )
            raise ErrorExit

        if len(password) > 20:
            ctx.my_output.error(
                'Define password with maximum length of 20 characters'
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

        if redfish_handler.endpoint_handler.is_account_username(username):
            ctx.my_output.error(
                'Username %s is already defined' % (username)
            )
            raise ErrorExit

        account_id = redfish_handler.endpoint_handler.get_account_empty_id()
        if account_id is None:
            ctx.my_output.error(
                'Failed to allocate new account id'
            )
            raise ErrorExit

        ctx.busy = True
        threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        imc_handler = imc_endpoint.ImcEndpoint(
            endpoint_ip,
            22,
            'admin',
            admin_password,
            log_id=ctx.run_id
        )

        success = imc_handler.add_user(
            account_id,
            username,
            password,
            role
        )
        if not success:
            ctx.my_output.error(
                'User create failed'
            )
            raise ErrorExit

        ctx.busy = False

        ctx.my_output.default(
            'User created'
        )

        accounts = redfish_handler.endpoint_handler.get_template_properties('account', cache_enabled=False)
        if accounts is None:
            ctx.my_output.error(
                'Failed to get existing accounts'
            )
            raise ErrorExit

        redfish_output_handler.print_ucsc_properties(
            'account',
            accounts,
            title=True
        )

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
