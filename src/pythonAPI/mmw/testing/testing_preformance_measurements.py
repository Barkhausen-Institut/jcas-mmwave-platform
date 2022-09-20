import os, sys, time
# Import mmw_helpers module from parent path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir  = os.path.abspath(os.path.join(current_dir, os.pardir))
#print(parent_dir)
sys.path.append(parent_dir)
import mmw_helpers as h

p = h.performance()
#p = h.performance()

p.reset("test1")
p.reset("test2")

time.sleep(2)
p.record("test1","after 2 sec sleep")
time.sleep(1)
p.record("test1", "after 3 sec sleep")
p.record("test2", "after 3 sec sleep")

print(p.read("test1"))
print(p.read("test2"))
print(p.read_all())



