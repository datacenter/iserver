import sys
import json
import traceback
import click

from progress.bar import Bar

from lib.intersight import scu

from menu import user_inputs
from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("scu")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--file", "filename", is_flag=False, show_default=False, default='', type=click.STRING, help="Input yaml file")
@click.option("--organization", "organization_name", is_flag=False, show_default=False, default='', type=click.STRING, help="Organization Name")
@click.option("--name", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Name")
@click.option("--version", is_flag=False, show_default=False, default='', type=click.STRING, help="SCU Version")
@click.option("--type", "link_type", type=click.Choice(['url', 'nfs'], case_sensitive=False), default='url', help="Link type")
@click.option("--link", is_flag=False, show_default=False, default='', type=click.STRING, help="Link")
@click.option("--interactive", is_flag=True, show_default=True, default=False, help="Interactive mode")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def create_scu_command(ctx, iaccount, filename, organization_name, name, version, link_type, link, interactive, devel):
    """Create software configuration utilities"""

    # iserver create scu

    ctx.developer = devel

    try:
        scu_handler = scu.SoftwareConfigurationUtility(iaccount, log_id=ctx.run_id)

        if len(filename) > 0:
            ctx.my_output.default('Input file verification...')
            scus = validations.validate_yaml_file(ctx, filename)
            if scus is None:
                raise ErrorExit

        if len(filename) == 0:
            if len(name) == 0 and len(version) == 0 and len(link) == 0:
                interactive = True

            if interactive:
                ctx.my_output.default('Get scus...')
                items = scu_handler.get_all()
                scu_handler.print(items)

                ctx.my_output.default('')
                ctx.my_output.default('Define new scu', underline=True)
                ctx.my_output.default('')

                name = user_inputs.get_value(ctx, 'Name')
                version = user_inputs.get_value(ctx, 'Version')
                link_type = user_inputs.get_selection(ctx, 'Select link type', ['url', 'nfs'])
                link = user_inputs.get_value(ctx, 'Link')
                organization_name = user_inputs.get_organization_name(ctx, iaccount)

            if not interactive:
                if len(name) == 0:
                    ctx.my_output.error('Define name')
                    raise ErrorExit

                if len(version) == 0:
                    ctx.my_output.error('Define version')
                    raise ErrorExit

                if len(link) == 0:
                    ctx.my_output.error('Define link')
                    raise ErrorExit

                organization_id = validations.validate_organization(ctx, iaccount, organization_name)
                if organization_id is None:
                    raise ErrorExit

            scus = []
            item = {}
            item['Name'] = name
            item['Version'] = version
            item['Link'] = link
            item['Type'] = link_type
            item['Organization'] = organization_name
            scus.append(item)

        ctx.my_output.default('\nInput parameters verification...')
        ctx.my_output.debug(
            json.dumps(
                scus,
                indent=4
            )
        )

        for scu_definition in scus:
            success, reason = scu_handler.validate_add(scu_definition)
            if not success:
                ctx.my_output.error('Input parameters validation failed')
                ctx.my_output.default(reason)
                raise ErrorExit

        ctx.my_output.default('Input parameters verified')

        bar_handler = Bar('Progress', max=len(scus))
        bar_handler.goto(0)
        failed = []
        for item in scus:
            if not scu_handler.add(item):
                failed.append(item)
            bar_handler.next()
        bar_handler.finish()

        if len(failed) > 0:
            ctx.my_output.error('Some create tasks failed')
            for item in failed:
                ctx.my_output.default('- %s' % (item))
            raise ErrorExit

        items = scu_handler.get_all()
        scu_handler.print(items)

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
