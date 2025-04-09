# Kernel Panic Test Procedure

```bash
# Trigger panic
echo c > /proc/sysrq-trigger

# Verify recovery:
dmesg | grep -i "crash\|panic"
fsck -nv /dev/sda1
```
