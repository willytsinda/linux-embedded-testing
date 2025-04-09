import os, time

for i in range(1, 51):
    print(f"Cycle {i}/50: Suspending")
    os.system("systemctl suspend")
    time.sleep(10)
    assert "active" in os.popen("systemctl is-system-running").read()
