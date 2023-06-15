import sys
import json
import threading
import traceback
import click

from lib.aci import output as aci_output

from menu import validations
from menu import progress


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


class NoResultExit(Exception):
    pass


@click.command("contract")
@click.pass_obj
@click.option("--apic", "controller", default='', callback=validations.validate_apic_name, help="APIC name")
@click.option("--ip", "controller_ip", default='', callback=validations.validate_ip, help="APIC IP")
@click.option("--port", "controller_port", default=443, show_default=True, help="APIC Port")
@click.option("--username", "controller_username", default='', help="APIC Username")
@click.option("--password", "controller_password", default='', help="APIC Password")
@click.option("--name", default='', callback=validations.validate_apic_tenant_name, help="Filter by name")
@click.option("--tenant", default='', callback=validations.empty_string_to_none, help="Filter by tenant")
@click.option("--type", "contract_type", type=click.Choice(['all', 'standard', 'taboo', 'filter'], case_sensitive=False), default='all', show_default=True)
@click.option("--view", "-v", type=click.Choice(['default', 'prop', 'usage'], case_sensitive=False), multiple=False, default='default')
@click.option("--output", "-o", type=click.Choice(['default', 'json'], case_sensitive=False), default='default', show_default=True)
@click.option("--no-cache", "no_cache", is_flag=True, show_default=True, default=False, help="Disable cache")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_aci_contract_command(
        ctx,
        controller,
        controller_ip,
        controller_port,
        controller_username,
        controller_password,
        name,
        tenant,
        contract_type,
        view,
        output,
        no_cache,
        devel
        ):
    """Get aci contract"""

    # iserver get aci contract

    ctx.developer = devel
    ctx.output = output

    try:
        aci_output_handler = aci_output.ApicOutput(log_id=ctx.run_id)
        apic_handler = validations.validate_apic_controller(
            ctx,
            controller,
            controller_ip,
            controller_port,
            controller_username,
            controller_password,
            no_cache=no_cache
        )
        if apic_handler is None:
            raise ErrorExit

        if output not in ['json']:
            ctx.busy = True
            threading.Thread(target=progress.spinner_task, args=(ctx, False,)).start()

        object_filter = []

        tenant_filtered = False
        if name is not None:
            object_filter.append(
                'name:%s' % (name['name'])
            )

            if name['tenant'] is not None:
                tenant_filtered = True
                object_filter.append(
                    'tenant:%s' % (name['tenant'])
                )

        if tenant is not None:
            if tenant_filtered:
                ctx.my_output.error(
                    'Define tenant in one place'
                )
                raise ErrorExit

            object_filter.append(
                'tenant:%s' % (tenant)
            )

        if contract_type == 'all':
            contracts = apic_handler.get_contracts(
                contract_filter=object_filter
            )

            taboos = apic_handler.get_taboos(
                taboo_filter=object_filter
            )

            filters = apic_handler.get_filters(
                filter_filter=object_filter,
                usage_info=True
            )

            if contracts is None or len(contracts) == 0:
                raise NoResultExit

            if taboos is None or len(taboos) == 0:
                raise NoResultExit

            if filters is None or len(filters) == 0:
                raise NoResultExit

        if contract_type == 'standard':
            contracts = apic_handler.get_contracts(
                contract_filter=object_filter
            )

            if contracts is None or len(contracts) == 0:
                raise NoResultExit

        if contract_type == 'taboo':
            taboos = apic_handler.get_taboos(
                taboo_filter=object_filter
            )

            if taboos is None or len(taboos) == 0:
                raise NoResultExit

        if contract_type == 'filter':
            filters = apic_handler.get_filters(
                filter_filter=object_filter,
                usage_info=True
            )

            if filters is None or len(filters) == 0:
                raise NoResultExit

        ctx.busy = False

        if contract_type == 'all':
            json_output = {}
            json_output['contract'] = contracts
            json_output['taboo'] = taboos
            json_output['filter'] = filters
            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        json_output,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(json_output)

            if view in ['default', 'prop']:
                aci_output_handler.print_contracts(
                    contracts
                )

                aci_output_handler.print_taboos(
                    taboos
                )

                aci_output_handler.print_filters(
                    filters
                )

            if view in ['default', 'usage']:
                aci_output_handler.print_contracts_usage(
                    contracts
                )

                aci_output_handler.print_taboos_usage(
                    taboos
                )

                aci_output_handler.print_filters_usage(
                    filters
                )

        if contract_type == 'standard':
            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        contracts,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(contracts)

            if view in ['default', 'prop']:
                aci_output_handler.print_contracts(
                    contracts,
                    show_contract_filters=True
                )

            if view in ['default', 'usage']:
                aci_output_handler.print_contracts_usage(
                    contracts
                )

        if contract_type == 'taboo':
            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        taboos,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(taboos)

            if view in ['default', 'prop']:
                aci_output_handler.print_taboos(
                    taboos,
                    show_taboo_filters=True
                )

            if view in ['default', 'usage']:
                aci_output_handler.print_taboos_usage(
                    taboos
                )

        if contract_type == 'filter':
            if output == 'json':
                ctx.log_prompt = False
                ctx.my_output.default(
                    json.dumps(
                        filters,
                        indent=4
                    )
                )
                return

            ctx.my_output.json_output(filters)

            if view in ['default', 'prop']:
                aci_output_handler.print_filters(
                    filters
                )

            if view in ['default', 'usage']:
                aci_output_handler.print_filters_usage(
                    filters
                )

    except NoResultExit:
        ctx.busy = False
        sys.exit(666)

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
