import sys

try:
    import parser_log as pl
except ImportError as e:
    print(f"Error importing module: {e}")
    sys.exit(1)

def main():
    log_file_path = "sample.log"
    results = pl.parser_line("2025-09-10 20:23:59 ERROR Test Log_439")
    counts = pl.count_events(log_file_path)
    print("Parsed Line Result:", results)
    print("Event Counts:")
    for level, count in counts.items():
        print(f"{level}: {count}")

if __name__ == "__main__":
    main()
