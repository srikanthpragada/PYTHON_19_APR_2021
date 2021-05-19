import json


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"


t = Time(10, 20, 30)
json_string = json.dumps(t.__dict__)
print(json_string)
time_dict = json.loads(json_string)
# Convert dict to Time object
