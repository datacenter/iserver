import os
import json
import time
import ssl
import uuid
import threading
import websocket
import requests


class WebSocket():
    def __init__(self, nexus_ip, debug=False):
        self.ws_nexus_ip = nexus_ip
        self.ws_token = None
        self.ws_monitored_objects = []
        self.ws_handler = None
        self.ws_subscription_ids = '/tmp/ws_nexus_%s.json' % (str(uuid.uuid4()).rsplit('-', maxsplit=1)[-1])
        self.ws_debug = debug

    def ws_on_open(self, ws_obj):
        subscription_ids = []

        print('Object subscriptions:')
        for monitored_object in self.ws_monitored_objects:
            subscription_url = 'http://%s%s.json?subscription=yes' % (
                self.ws_nexus_ip,
                monitored_object
            )
            if self.ws_debug:
                print('- GET %s' % (subscription_url))

            response = requests.get(
                subscription_url,
                headers={'Cookie': 'APIC-cookie=%s' % (self.get_token(generate_if_none=True))},
                verify=False
            )

            if self.ws_debug:
                print('- Response %s' % (response.status_code))

            if response.status_code >= 300:
                print('[ERROR] object %s subscription request failed (%s)' % (monitored_object, response.status_code))
                self.ws_handler.close()
                return

            subscription_id = json.loads(response.text)['subscriptionId']
            subscription_ids.append(
                subscription_id
            )
            print('- %s with subscription ID: %s' % (
                monitored_object,
                subscription_id
            ))

        with open(self.ws_subscription_ids, 'w+', encoding='utf-8') as handle:
            json.dump(subscription_ids, handle)

        print('Press Ctrl-C to exit')

    def ws_on_message(self, ws_obj, ws_message):
        print(ws_message)

    def ws_on_error(self, ws_obj, ws_error):
        if ws_error is not None and len(str(ws_error)) > 0:
            print('[ERROR] %s' % (ws_error))

    def ws_on_close(self, ws_obj, ws_close_status_code, ws_close_msg):
        os.remove(self.ws_subscription_ids)

        if ws_close_msg is None:
            print('Socket closed')
        if ws_close_msg is not None:
            print('Socket closed (%s)' % (ws_close_msg))

    def ws_refresh(self):
        while True:
            timeout_epoch = int(time.time()) + 60
            while True:
                if not os.path.isfile(self.ws_subscription_ids):
                    print('Subscription refresh thread finished')
                    return

                time.sleep(5)
                if int(time.time()) > timeout_epoch:
                    break

            if not os.path.isfile(self.ws_subscription_ids):
                print('Subscription refresh thread finished')
                return

            with open(self.ws_subscription_ids, "r", encoding='utf-8') as handle:
                subscription_ids = json.load(handle)

            self.ws_token = self.get_token()
            if self.ws_token is None:
                print('[ERROR] Nexus token generation')
                return

            print('Subscriptions refresh:')
            for subscription_id in subscription_ids:
                subscription_url = 'https://%s/api/subscriptionRefresh.json?id=%s' % (self.ws_nexus_ip, subscription_id)
                response = requests.get(
                    subscription_url,
                    headers={'Cookie': 'nxapi_auth=%s' % (self.ws_token)},
                    verify=False
                )
                if self.ws_debug:
                    print('- GET %s' % (subscription_url))

                if json.loads(response.text)['totalCount'] != '0':
                    print('[ERROR] subscription refresh failed (%s)' % (subscription_id))
                    self.ws_handler.close()
                    return

                print('- subscription %s refreshed' % (subscription_id))

    def ws_run(self, objects):
        self.ws_monitored_objects = objects
        with open(self.ws_subscription_ids, 'w+', encoding='utf-8') as handle:
            json.dump([], handle)

        self.ws_token = self.get_token()
        if self.ws_token is None:
            print('[ERROR] Nexus authentication failed')
            return

        # refresh_thread = threading.Thread(target=self.ws_refresh)
        # refresh_thread.start()

        websocket.enableTrace(self.ws_debug)

        ws_url = 'wss://%s/socket%s' % (self.ws_nexus_ip, self.ws_token)
        self.ws_handler = websocket.WebSocketApp(
            ws_url,
            on_message=self.ws_on_message,
            on_error=self.ws_on_error,
            on_close=self.ws_on_close,
            on_open=self.ws_on_open,
            cookie=self.ws_token
        )

        self.ws_handler.run_forever(
            sslopt={
                "check_hostname": False,
                "cert_reqs": ssl.CERT_NONE
            }
        )
