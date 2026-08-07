**only works with v7.23**

0. close winrar
1. open main winrar executable (`C:\Program Files\WinRAR\WinRAR.exe`) in any hex editor
2. replace bytes `8a 05 9e f8 18 00 c3` with `b0 01 90 90 90 90 c3`
3. save changes
4. enjoy no banner
---
this swaps instructions
```asm
MOV AL,byte ptr [0x1402592d0]
RET
```
with
```asm
MOV AL,0x1
NOP
NOP
NOP
NOP
RET
```
