import time
import json


class Trace():
    def __init__(self):
        pass

    def trace_rest(self, trace_filename, method, url, headers, data, params, response_code, response_data):
        if response_data is None:
            return

        if data is not None:
            try:
                data = data.decode('utf-8')
            except BaseException:
                data = str(data)

        timestamp = int(time.time() * 1000)
        message = {
            'timestamp': timestamp,
            'message': method,
            'url': url,
            'headers': headers,
            'data': data,
            'params': params,
            'response_code': response_code,
            'response_data': response_data
        }

        if trace_filename is not None:
            self.log.adhoc(
                trace_filename,
                json.dumps(message, indent=4)
            )

        else:
            self.log.adhoc(
                'nso.trace.%s' % (timestamp),
                json.dumps(
                    message,
                    indent=4
                )
            )
