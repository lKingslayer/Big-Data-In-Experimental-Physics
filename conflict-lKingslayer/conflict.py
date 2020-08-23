#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""THis is code is to identify the conflict between selected courses and candidates"""
import sys
import string

INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]

# We use encoding argument here for some reason,
# to finish this assignment, you need to figure it out by yourself
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    LINES = f.readlines()
    FIRST_LINE = LINES[0]
    NUM_LINES_SELECTED = list(map(int, (x for x in FIRST_LINE.split() if x.isdigit())))[0]
    NUM_LINES_CANDIDATE = list(map(int, (x for x in FIRST_LINE.split() if x.isdigit())))[1]

    COURSE_SELECTED = []
    for i in range(1, NUM_LINES_SELECTED + 1):
        line = LINES[i].split()
        key = ""
        a = {}
        key += line[1]
        key += ' '
        key += line[3]
        key += ' '
        key += line[2]
        a.setdefault(key, [])
        for j in range(4, len(line) - 3):
            a[key].append(line[j])
        COURSE_SELECTED.append(a)

    CANDIDATE = []
    for i in range(NUM_LINES_SELECTED + 1, NUM_LINES_SELECTED + NUM_LINES_CANDIDATE + 1):
        line = LINES[i].split()
        key = ""
        a = {}
        key += line[0]
        key += ' '
        key += line[1]
        key += ' '
        key += line[2]

        a.setdefault(key, [])
        for j in range(5, len(line) - 5):
            a[key].append(line[j])
        CANDIDATE.append(a)

f.close()


def get_dict_value(self):
    """This function is to get the time of courses and convert them into strings"""
    for item in self:
        return self[item][0].split(",", 2)


sys.stdout = open(OUTPUT_FILE, "w", encoding='utf-8')

for candidate in CANDIDATE:
    selected_conflict_number = []
    selected_conflict = []
    t = 0
    for selected in COURSE_SELECTED:
        is_conflict = False
        if (candidate.keys() == selected.keys()) is False:

            for candidate_date in get_dict_value(candidate):
                candidate_hour = candidate_date[0:candidate_date.find('(', 0)]
                candidate_week = candidate_date[candidate_date.find('(')
                                                + 1:candidate_date.find(')',
                                                                        candidate_date.find('(') + 1)]
                if candidate_week == "全周":
                    candidate_week = "1-16"
                elif candidate_week == "前八周":
                    candidate_week = "1-8"
                elif candidate_week == "后八周":
                    candidate_week = "9-16"
                candidate_week_start = int(candidate_week.split("-", 1)[0])
                candidate_week_end = int(candidate_week.split("-", 1)[1])

                for selected_date in get_dict_value(selected):
                    selected_hour = selected_date[0:selected_date.find('(', 0)]
                    selected_week = selected_date[selected_date.find('(')
                                                  + 1:selected_date.find(')',
                                                                         selected_date.find('(') + 1)]
                    if selected_week == "全周":
                        selected_week = "1-16"
                    elif selected_week == "前八周":
                        selected_week = "1-8"
                    elif selected_week == "后八周":
                        selected_week = "9-16"
                    selected_week_start = int(selected_week.split("-", 1)[0])
                    selected_week_end = int(selected_week.split("-", 1)[1])
                    hour_is_overlap = False

                    if candidate_hour == selected_hour:
                        hour_is_overlap = True

                    if max(selected_week_start, candidate_week_start) < min(selected_week_end, candidate_week_end) \
                            and hour_is_overlap:
                        is_conflict = True
                        t += 1
                        break

                if is_conflict:
                    break

        if is_conflict:
            if t == 1:
                print(list(candidate.keys())[0] + ":")
            selected_conflict.append(list(selected.keys())[0])
            selected_conflict_number.append(list(selected.keys())[0].split(" ", 1)[0])

    temp = {}
    for i, j in zip(selected_conflict_number, selected_conflict):
        temp[j] = i
    for number in sorted(temp):
        print("\t" + number)

sys.stdout.close()
