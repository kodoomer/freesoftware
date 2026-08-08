# loads the whole executable into ram but it works
winrar = r"C:\Program Files\WinRAR\WinRAR.exe"
with open(winrar, 'rb') as file:
    content = file.read()
content = content.replace(b'\x8a\x05\x9e\xf8\x18\x00\xc3', b'\xb0\x01\x90\x90\x90\x90\xc3')
with open(winrar, 'wb') as file:
    file.write(content)
print("Done!")
