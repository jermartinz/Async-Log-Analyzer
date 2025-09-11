def parser_line(line):
    sections = line.strip().split(' ', 3)
    if len(sections) >= 4:
        date = sections[0]
        hour = sections[1]
        level = sections[2]
        message = sections[3]
        return date, hour, level, message
    return None

def count_events(path_file):
    counters = {"INFO": 0, "WARN": 0, "ERROR": 0, "DEBUG": 0}

    with open(path_file, 'r') as file:
        for line in file:
            result = parser_line(line)
            if result:
                _, _, level, _ = result
                if level in counters:
                    counters[level] += 1
    return counters

result = parser_line("2025-09-10 20:23:59 ERROR Test Log_439")
counts = count_events("sample.log")

if __name__ == "__main__":
    test_line = "2025-09-10 20:23:59 ERROR Test Log_439"
    print(parser_line(test_line))


