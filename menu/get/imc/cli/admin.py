import sys
import json
import traceback
import click

from progress.bar import Bar

from lib.imc.cli import endpoint
from lib.imc.cli import output as imc_output

from menu import validations

from menu.get.imc.cli import common as imc_common
from menu.get.imc.cli import validations as imc_validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("admin")
@click.pass_obj
@click.option("--ip", "endpoint_ip", multiple=True, callback=validations.validate_ips, help="IMC IP address")
@click.option("--username", default='', help="IMC ssh username")
@click.option("--password", default='', help="IMC ssh password")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--view", "-v", default=['all'], help="[comm|fault|http|ip|ipmi|kvm|ntp|redfish|ssh|sel|smtp|snmp|sol|syslog|tls|vmedia|xml|all]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_imc_cli_admin_command(
        ctx,
        endpoint_ip,
        username,
        password,
        user_cache_ttl,
        view,
        output,
        devel
        ):
    """Get imc admin settings"""

    # iserver get imc admin

    ctx.developer = devel
    ctx.output = output
    view = validations.validate_view(
        ctx,
        view,
        'comm|fault|http|ip|ipmi|kvm|ntp|redfish|ssh|sel|smtp|snmp|sol|syslog|tls|vmedia|xml|all',
        'all',
        [
            'comm:http,ssh,tls,xml,redfish,ipmi'
        ]
    )
    if view is None:
        sys.exit(1)

    cache_ttl = imc_validations.validate_cache_ttl(user_cache_ttl, log_id=ctx.run_id)
    imc_common.print_cache_ttl(ctx, output, cache_ttl)

    try:
        endpoints = imc_validations.get_imc_cli_endpoints(
            ctx,
            endpoint_ip,
            username,
            password
        )

        if endpoints is None:
            raise ErrorExit

        if len(endpoints) == 0:
            ctx.my_output.error('Define imc endpoints')
            raise ErrorExit

        fault_info = False
        if 'fault' in view:
            fault_info = True

        http_info = False
        if 'http' in view:
            http_info = True

        ip_info = False
        if 'ip' in view:
            ip_info = True

        ipmi_info = False
        if 'ipmi' in view:
            ipmi_info = True

        kvm_info = False
        if 'kvm' in view:
            kvm_info = True

        ntp_info = False
        if 'ntp' in view:
            ntp_info = True

        redfish_info = False
        if 'redfish' in view:
            redfish_info = True

        sel_info = False
        if 'sel' in view:
            sel_info = True

        smtp_info = False
        if 'smtp' in view:
            smtp_info = True

        snmp_info = False
        if 'snmp' in view:
            snmp_info = True

        sol_info = False
        if 'sol' in view:
            sol_info = True

        ssh_info = False
        if 'ssh' in view:
            ssh_info = True

        syslog_info = False
        if 'syslog' in view:
            syslog_info = True

        tls_info = False
        if 'tls' in view:
            tls_info = True

        vmedia_info = False
        if 'vmedia' in view:
            vmedia_info = True

        xml_info = False
        if 'ipmi' in view:
            xml_info = True

        response = []

        if output != 'json':
            bar_handler = Bar('Progress', max=len(endpoints))
            bar_handler.goto(0)

        for item in endpoints:
            endpoint_handler = endpoint.ImcCliEndpoint(
                item['ip'],
                item['port'],
                item['username'],
                item['password'],
                cache_ttl=cache_ttl,
                log_id=ctx.run_id
            )

            admin = endpoint_handler.get_admin(
                fault_info=fault_info,
                http_info=http_info,
                ip_info=ip_info,
                ipmi_info=ipmi_info,
                kvm_info=kvm_info,
                ntp_info=ntp_info,
                redfish_info=redfish_info,
                sel_info=sel_info,
                smtp_info=smtp_info,
                snmp_info=snmp_info,
                sol_info=sol_info,
                syslog_info=syslog_info,
                ssh_info=ssh_info,
                tls_info=tls_info,
                vmedia_info=vmedia_info,
                xml_info=xml_info
            )
            if admin is None:
                ctx.my_output.error('Failed to get admin settings from: %s' % (item['ip']))
            else:
                response.append(
                    admin
                )

            if output != 'json':
                bar_handler.next()

        if output != 'json':
            bar_handler.finish()

        if output == 'json':
            ctx.my_output.default(
                json.dumps(
                    response,
                    indent=4
                )
            )
            return

        ctx.my_output.json_output(response)

        imc_output_handler = imc_output.ImcCliOutput(
            log_id=ctx.run_id
        )

        if output == 'default':
            imc_output_handler.print_imc_admin(response)

        ctx.my_output.default('Filter: --', before_newline=True)
        ctx.my_output.default('View:   comm, fault, http, ip, ipmi, kvm, ntp, redfish, sel, smtp, snmp, sol, ssh, syslog, tls, vmedia, xml, all')
        ctx.my_output.default('Output: default, json')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
