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

        if log_record.get('FuncName'):
            log_record['FuncName'] = log_record['FuncName'].upper()
        else:
            log_record['FuncName'] = record.funcName
