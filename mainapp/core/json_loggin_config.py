from datetime import datetime
from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)

        if not log_record.get('timestamp'):
            log_record['timestamp'] = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()

        else:
            log_record['level'] = record.levelname

        if log_record.get('pathname'):
            log_record['pathname'] = log_record['pathname'].upper()
        else:
            log_record['pathname'] = record.pathname

        if log_record.get('filename'):
            log_record['filename'] = log_record['filename'].upper()
        else:
            log_record['filename'] = record.filename

        if log_record.get('funcName'):
            log_record['funcName'] = log_record['funcName'].upper()
        else:
            log_record['funcName'] = record.funcName

        if log_record.get('lineno'):
            log_record['lineno'] = log_record['lineno'].upper()
        else:
            log_record['lineno'] = record.lineno