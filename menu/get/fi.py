import json
import sys
import csv
import traceback
import click

from lib.intersight import settings as intersight_settings
from lib.intersight import fi
from lib.intersight import fi_output

from menu import defaults
from menu import validations

from progress.bar import Bar


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("fi")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--name", "name_filter", multiple=True, help="Select by name")
@click.option("--serial", "serial_filter", multiple=True, help="Select by serial")
@click.option("--model", "model_filter", multiple=True, help="Select by model")
@click.option("--ttl", "user_cache_ttl", default=None, help="Cache TTL")
@click.option("--view", "-v", default=['state|eth|pc|fc|fpc|all'], help="[state]", show_default=True, multiple=True)
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'yaml'], case_sensitive=False), default='default', show_default=True)
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_fi_command(
        ctx,
        iaccount,
        name_filter,
        serial_filter,
        model_filter,
        user_cache_ttl,
        view,
        output,
        devel
        ):
    """Get fi details"""

    ctx.developer = devel
    ctx.output = output
    if ctx.output == 'default':
        ctx.my_output.set_debug()

    view = validations.validate_view(
        ctx,
        view,
        'state|eth|pc|fc|fpc|all',
        'state',
        []
    )
    if view is None:
        sys.exit(1)

    try:
        settings_handler = intersight_settings.IntersightSettings(
            log_id=ctx.run_id
        )
        cache_ttl = settings_handler.get_intersight_cache_ttl()
        if user_cache_ttl is not None:
            try:
                cache_ttl = int(user_cache_ttl)
            except BaseException:
                cache_ttl = -1

            if cache_ttl < 0:
                ctx.my_output.error('Cache TTL must be gt 0')
                raise ErrorExit

        if output not in ['json', 'yaml']:
            if cache_ttl is None:
                ctx.my_output.default('iaccount %s (cache: off)' % (iaccount))
            else:
                if cache_ttl == 0:
                    ctx.my_output.default('iaccount %s (cache: any)' % (iaccount))
                if cache_ttl > 0:
                    ctx.my_output.default('iaccount %s (cache: %s seconds)' % (iaccount, cache_ttl))

            ctx.my_output.default('Select fi...')

        fi_handler = fi.Fi(iaccount, log_id=ctx.run_id)

        match_rules = fi_handler.get_mo_match_rules(
            name_filter=name_filter,
            serial_filter=serial_filter,
            model_filter=model_filter
        )

        fis_mo = fi_handler.get_mo(
            match_rules=match_rules,
            cache_ttl=cache_ttl
        )

        if output not in ['json']:
            ctx.my_output.default('Selected fi: %s' % (len(fis_mo)))

        # Collect FI information

        settings = {}
        settings['summary'] = True

        settings['eth'] = False
        if 'eth' in view or 'pc' in view:
            settings['eth'] = True

        settings['pc'] = False
        if 'pc' in view:
            settings['pc'] = True

        settings['fc'] = False
        if 'fc' in view:
            settings['fc'] = True

        settings['fpc'] = False
        if 'fpc' in view:
            settings['fpc'] = True

        if output not in ['json']:
            ctx.my_output.default('Collect fi api objects...')

        fi_handler.set_cache(
            fis_mo,
            settings,
            cache_ttl,
            ctx=ctx
        )

        bar_handler = None
        if output == 'default':
            bar_handler = Bar('Collect fi information', max=len(fis_mo))
            bar_handler.goto(0)

        fis_info = fi_handler.get_info(
            fis_mo,
            settings,
            match_rules,
            cache_ttl,
            prepare_cache=False,
            bar_handler=bar_handler
        )

        if output == 'default':
            bar_handler.finish()

        # Output section

        fi_output_handler = fi_output.FiOutput(log_id=ctx.run_id)

        ctx.my_output.json_output(fis_info)
        if output == 'json':
            ctx.my_output.default(json.dumps(fis_info, indent=4))
            ctx.log_prompt = False
            return

        if 'state' in view:
            fi_output_handler.print_state(
                fis_info,
                title=True
            )

        if 'eth' in view:
            for fi_info in fis_info:
                fi_output_handler.print_eth(
                    fi_info,
                    title=True
                )

        if 'eth' in view:
            for fi_info in fis_info:
                fi_output_handler.print_eth(
                    fi_info,
                    title=True
                )

        if 'pc' in view:
            for fi_info in fis_info:
                fi_output_handler.print_pc(
                    fi_info,
                    title=True
                )

        if 'fc' in view:
            for fi_info in fis_info:
                fi_output_handler.print_fc(
                    fi_info,
                    title=True
                )

        if 'fpc' in view:
            for fi_info in fis_info:
                fi_output_handler.print_fpc(
                    fi_info,
                    title=True
                )

        ctx.my_output.default('Filter: name, serial, model', before_newline=True)
        ctx.my_output.default('View:   state (def), etc, pc, fc, fpc, all')

    except ErrorExit:
        ctx.busy = False
        sys.exit(1)

    except BaseException:
        ctx.busy = False
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
