from collections import Counter

def parser_line(path_file):
    line_logs = []
    with open(path_file, 'r', encoding='utf-8') as file:
        for line in file:
            sections = line.strip().split(' ', 3)
            if len(sections) >= 4:
                date, hour, level, message = sections
                line_logs.append((date, hour, level, message))
    return line_logs

def count_events(path_file):
    logs = parser_line(path_file)
    levels = [level for _, _, level, _ in logs]
    return Counter(levels)

if __name__ == "__main__":
    test_line = "ERROR Test Log_xxxx"
    print(parser_line(test_line))


