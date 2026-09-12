# loads the whole executable into ram but it works
filepath = r"C:\Program Files\WizTree\WizTree64.exe"
with open(filepath, 'rb') as file:
    content = file.read()
content = content.replace(b'\x0f\x84\x4a\x08\x00\x00', b'\x90\x90\x90\x90\x90\x90')
content = content.replace(b'\x1b\x00\x01\x74\x18', b'\x1b\x00\x01\xeb\x18')
with open(filepath, 'wb') as file:
    file.write(content)
print("Done!")
