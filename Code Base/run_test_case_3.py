import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import task_manager as tm

tasks = []

print("Test Case 3: Invalid Input\n")

print("(a) Add: Pay bill, Priority: Urgent")
print("\n".join(tm.add_task(tasks, "Pay bill", "Urgent", "")))

print("\n(b) Add: Pay bill, Due: 15-10-2026")
print("\n".join(tm.add_task(tasks, "Pay bill", "", "15-10-2026")))

print("\n(c) Option 4 (Complete): T999")
print("\n".join(tm.complete_task(tasks, "T999")))