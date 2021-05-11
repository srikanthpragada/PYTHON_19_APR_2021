class Time:
    pass


t = Time()
t.hours = 10
t.mins = 20
print(t.__dict__)
print(getattr(t, 'hours'))
print(getattr(t, 'secs', 0))
print(hasattr(t, 'secs'))
delattr(t, 'hours')
setattr(t, 'hours', 0)
print(t.__dict__)
