**only works with v4.32 64-bit**

will work if the sha-256 hash of `wiztree64.exe` is `6bffb6b63d96ff19824641e8ced04e5e0f648696073d82a508f1bb1a21e7eb46`

0. close wiztree
1. open main wiztree executable (`C:\Program Files\WizTree\WizTree64.exe`) in any hex editor
2. replace bytes `0f 84 4a 08 00 00` with `90 90 90 90 90 90` (bypass key check)
3. replace bytes `1b 00 01 74 18` with `1b 00 01 eb 18` (bypass integrity check)
4. save changes
5. enjoy no donate button
---
bypassing key check swaps instruction
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
bypassing integrity check swaps instruction
```asm
JZ 00ba24a3
```
with
```asm
JMP 00ba24a3
```
---
**to undo**

repeat, but replace `b0 01 90 90 90 90 c3` with `8a 05 9e f8 18 00 c3`
