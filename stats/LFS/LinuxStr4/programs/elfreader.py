#!/bin/python3
import lief

binary = lief.parse("simple")
header = binary.header

print("Entry point: %08x" % header.entrypoint)
print("Architecture: ", header.machine_type)

for section in binary.sections:
    print("Section %s - size: %s bytes" % (section.name, section.size)
