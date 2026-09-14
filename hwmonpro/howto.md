**only works with v1.59.0**

will work if the sha-256 hash of `hwmonitorpro.exe` is `8e79862b98668ed27b1aeb14baaa59c539a7bd035f9c0e7ccc23404ba89cc6be`

0. close hwmonnitor
1. open main hwmonitor executable (`C:\Program Files\CPUID\HWMonitorPro\HWMonitorPro.exe`) in any hex editor
2. replace bytes `80 d4 1d 40 01 00 00 00` with `b0 de 1d 40 01 00 00 00`
3. save changes
4. enjoy all values
---
**note:**
this will only disable `[TRIAL]` values 

if there are other trial version restrictions (that i have not been able to find), 
this patch will not work

---
**to undo**

replace `b0 de 1d 40 01 00 00 00 60` with `80 d4 1d 40 01 00 00 00 60`
