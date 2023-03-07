import datetime

def log_message(msg, log_file_path):
    timestamp = datetime.datetime.now().strftime('%H:%M:%S')
    datestamp = datetime.datetime.now().strftime('%Y-%m-%d')
    log_str = f"[{datestamp} {timestamp}] {msg}"
    with open(log_file_path, "a") as log_file:
        log_file.write(log_str + "\n")
