**only works with v4.32 64-bit**

will work if the sha-256 hash of `wiztree64.exe` is `6bffb6b63d96ff19824641e8ced04e5e0f648696073d82a508f1bb1a21e7eb46`

0. close wiztree
1. open main wiztree executable (`C:\Program Files\WizTree\WizTree64.exe`) in any hex editor
2. replace bytes `0f 84 4a 08 00 00` with `90 90 90 90 90 90`
3. save changes
4. enjoy no donate button
---
this swaps instructions
```asm
JZ 00b95e5e
```
with
```asm
NOP
NOP
NOP
NOP
NOP
NOP
```
---
**to undo**

repeat, but replace `b0 01 90 90 90 90 c3` with `8a 05 9e f8 18 00 c3`
