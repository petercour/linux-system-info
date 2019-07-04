import platform

print("Architecture: " + platform.architecture()[0])
print("Machine: " + platform.machine())
print("Node: " + platform.node())
print("System: " + platform.system())

# distribution
dist = platform.dist()
dist = " ".join(x for x in dist)
print("Distribution: " + dist)
