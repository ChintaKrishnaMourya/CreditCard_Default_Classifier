import datetime

def log_message(msg, log_file):
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    datestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    log_str = f"[{datestamp} {timestamp}] {msg}"

    log_file.write(log_str + "\n")
