import os
import sys
import traceback
import click

from lib.ocp import settings

from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("virtctl")
@click.pass_obj
@click.option("--cluster", "cluster_name", callback=validations.empty_string_to_none, help="OCP cluster name")
@click.option("--ip", "linux_ip", default='', callback=validations.empty_string_to_none, help="IP/FQDN")
@click.option("--username", default='', callback=validations.empty_string_to_none, help="Username")
@click.option("--password", default='', callback=validations.empty_string_to_none, help="Password")
@click.option("--key", default='', callback=validations.validate_optional_file, help="SSH public key")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def set_ocp_virtctl(
        ctx,
        cluster_name,
        linux_ip,
        username,
        password,
        key,
        devel
        ):
    """Set ocp cluster virtctl"""

    # iserver set ocp virtctl

    ctx.developer = devel

    try:
        settings_handler = settings.OcpSettings(log_id=ctx.run_id)

        if cluster_name is None:
            cluster_name = settings_handler.get_default_cluster()
            if cluster_name is None:
                ctx.my_output.error('Define OCP cluster name')
            raise ErrorExit

        if linux_ip is None:
            ctx.my_output.error('Define linux server ip address')
            raise ErrorExit

        if username is None:
            ctx.my_output.error('Define username')
            raise ErrorExit

        if password is None and key is None:
            ctx.my_output.error('Define password or public key')
            raise ErrorExit

        if password is not None and key is not None:
            ctx.my_output.error('Define password or public key')
            raise ErrorExit

        cluster_settings = settings_handler.get_ocp_cluster(cluster_name, strict_match=False)
        if cluster_settings is None:
            ctx.my_output.error('Cluster not found')
            raise ErrorExit

        cluster_settings['virtctl'] = {}
        cluster_settings['virtctl']['ip'] = linux_ip
        cluster_settings['virtctl']['username'] = username
        cluster_settings['virtctl']['password'] = password
        cluster_settings['virtctl']['key_filename'] = key

        success = settings_handler.set_ocp_cluster(
            cluster_settings
        )
        if not success:
            ctx.my_output.error('Failed to update ocp cluster kubeconfig')
            raise ErrorExit

        ctx.my_output.default('OCP cluster virtctl set: %s' % (cluster_name))

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
