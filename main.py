import sys

try:
    import parser_log as pl
except ImportError as e:
    print(f"Error importing module: {e}")
    sys.exit(1)

def main():
    log_file_path = "sample.log"
    lines = pl.parser_line(log_file_path)
    for date, hour, level, message in lines:
        print(f"Date: {date}, Hour: {hour}, Level: {level}, Message: {message}")
    events = pl.count_events(log_file_path)
    for level, total in events.most_common():
        print(f"Level: {level}, Count: {total}")


if __name__ == "__main__":
    main()
