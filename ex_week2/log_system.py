loggers = []
def log(massage, timestamp = None,level = None, date=None,events=None):
    logger = {'msg':massage}
    if timestamp:
        logger['time'] = timestamp
    if timestamp and level:
        logger['level'] = level
    if events and date:
        logger["events"] = events
        logger['date'] = date
    loggers.append(logger)
    return logger

def processing_logs(filter_type,start = None,end = None):
    match filter_type:
        case 'no_date_no_time':
            res = date_time_filter()
        case 'timestamp_range':
            res = timestamp_filter(start,end)
        case 'short_msg':
            res = short_msg_filter()
    return res


def date_time_filter():
    res = loggers.copy()
    for log in loggers:
        if log.get('date') or log.get('time'):
            res.remove(log)
    return res

def timestamp_filter(start = None,end = None):
    res = []
    for log in loggers:
        if log.get('time'):
            if log.get('time') >= start and log.get('time') <= end:
                res.append(log)
    return res

def short_msg_filter():
    res = []
    for log in loggers:
        if len(log.get('msg').split()) <= 10:
            res.append(log)
    return res

import time
log('hi how are you',time.time())
log('Hello world',level=6)
log('i am good thank you for asking, what do you doing? ',time.time(),date='25/2/2024')
print(loggers)

print(processing_logs('short_msg'))
print(processing_logs('no_date_no_time'))
print(processing_logs('timestamp_range',start = 100000, end = 2708859699))