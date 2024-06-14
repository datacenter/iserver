import json
import sys
import traceback
import click
from webexteamssdk import WebexTeamsAPI

from lib.intersight.cond_alarm import main as cond_alarm
from lib.intersight import compute_output
from lib.intersight import bot_output
from lib import log_helper

from menu import defaults
from menu import validations


class Failure(Exception):
    pass


class ErrorExit(Exception):
    pass


@click.command("alarm")
@click.pass_obj
@click.option("--iaccount", is_flag=False, show_default=True, cls=defaults.default_from_context('iaccount'), callback=validations.validate_iaccount, type=click.STRING, help="Intersight account")
@click.option("--code", "alarm_code", default='', callback=validations.empty_string_to_none, help="Filter by code")
@click.option("--sev", "severity", type=click.Choice(['any', 'crit', 'warn', 'info'], case_sensitive=False), default='any', show_default=True, help="Filter by severity")
@click.option("--when", "alarm_when", default='1y', show_default=True, callback=validations.validate_timestamp_filter, help="Filter faults by timestamp")
@click.option("--new", "only_new", is_flag=True, show_default=True, default=False, help="Only new from last new run")
@click.option("--cleared", "include_cleared", is_flag=True, show_default=True, default=False, help="Show cleared alarms")
@click.option("--limit", default=-1, help="Limit alarms")
@click.option("--output", "-o", type=click.Choice(['default', 'json', 'bot'], case_sensitive=False), default='default', show_default=True)
@click.option("--bot", default='', callback=validations.validate_bot, help="Send result to bot")
@click.option("--devel", is_flag=True, show_default=True, default=False, help="Developer output")
def get_intersight_alarm_command(
        ctx,
        iaccount,
        alarm_code,
        severity,
        alarm_when,
        only_new,
        include_cleared,
        limit,
        output,
        bot,
        devel
        ):
    """Get alarm"""

    # iserver get is alarm

    ctx.developer = devel

    try:
        if output == 'default':
            ctx.my_output.default('Get alarms...')

        if output == 'bot' and bot is None:
            ctx.my_output.error('Define --bot')
            raise ErrorExit

        cond_alarm_handler = cond_alarm.CondAlarm(iaccount, log_id=ctx.run_id)

        cond_alarm_filter = []

        cond_alarm_filter.append(
            'timestamp:%s' % (alarm_when)
        )

        cond_alarm_filter.append(
            'new:%s' % (only_new)
        )

        cond_alarm_filter.append(
            'cleared:%s' % (include_cleared)
        )

        if alarm_code is not None:
            cond_alarm_filter.append(
                'code:%s' % (alarm_code)
            )

        if severity is not None:
            cond_alarm_filter.append(
                'severity:%s' % (severity)
            )

        alarms = cond_alarm_handler.get_cond_alarms(
            cond_alarm_filter=cond_alarm_filter,
            update_moid_cache=only_new
        )

        if alarms is None:
            ctx.my_output.error('Failed to get alarms')
            raise ErrorExit

        if limit > 0:
            alarms = alarms[:limit]

        if output == 'json':
            ctx.my_output.default(json.dumps(alarms, indent=4))
            ctx.log_prompt = False
            return

        if output == 'default':
            compute_output_handler = compute_output.ComputeOutput(log_id=ctx.run_id)
            compute_output_handler.print_alarm(alarms)

        if bot is not None and len(alarms) > 0:
            bot_output_handler = bot_output.ComputeBotOutput(log_id=ctx.run_id)
            output, html_output = bot_output_handler.print_alarm(alarms)

            users = validations.validate_bot_group(bot['users'], 'intersight.alarm')
            if len(users) == 0:
                ctx.my_output.error('No bot user found')
                raise ErrorExit

            if len(bot['proxies']) == 0:
                webex_api_handler = WebexTeamsAPI(
                    access_token=bot['token']
                )
            else:
                webex_api_handler = WebexTeamsAPI(
                    access_token=bot['token'],
                    proxies=bot['proxies']
                )

            log_handler = log_helper.Log(log_id=ctx.run_id)

            files = None
            filename = log_handler.bot_output(output, log_id=ctx.run_id)
            if filename is not None:
                files = [filename]

            output = bot_output_handler.my_output.sanitize_bot_output(
                output,
                None
            )

            rooms = webex_api_handler.rooms.list()
            for room in rooms:
                for user in users:
                    if getattr(room, 'title') == user['title']:
                        webex_api_handler.messages.create(
                            roomId=getattr(room, 'id'),
                            markdown=output,
                            files=files
                        )

    except ErrorExit:
        sys.exit(1)

    except BaseException:
        ctx.my_output.traceback(traceback.format_exc())
        sys.exit(1)
