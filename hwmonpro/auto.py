# loads the whole executable into ram but it works
filepath = r"C:\Program Files\CPUID\HWMonitorPro\HWMonitorPro.exe"
with open(filepath, 'rb') as file:
    content = file.read()
content = content.replace(b'\x80\xd4\x1d\x40\x01\x00\x00\x00', b'\xb0\xde\x1d\x40\x01\x00\x00\x00')
with open(filepath, 'wb') as file:
    file.write(content)
print("Done!")
