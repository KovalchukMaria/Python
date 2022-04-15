import re

with open(r'task_5_6.txt', encoding='utf-8') as f_lessons:
    line_txt = []
    for line in f_lessons:
        line = line.replace('-', '0')
        line_txt.append(line)
    print(line_txt)
    line_re = []
    for el in line_txt:
        el = re.sub(r'\(.+?\)', r' ', el)
        line_re.append(el)
    lines_end = []
    for el in line_re:
        el_2 = el.split()
        lines_end.append(el_2)
    for el in lines_end:
        s = int(el[1]) + int(el[2]) + int(el[3])
        el.pop(1)
        el.pop(1)
        el.pop(1)
        el.append(s)
        print(el)
