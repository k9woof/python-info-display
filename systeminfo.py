# Cailan White 2025
# Simple system information script

import platform

# print basic system info
def print_system_info():
    print("System:", platform.system())
    print("Host name:", platform.node())
    print("OS version:", platform.release())
    print("Machine type:", platform.machine())

# get basic system info as lines
def get_system_info_lines():
    system_info_lines = []
    system_info_lines.append(f"System: {platform.system()}")
    system_info_lines.append(f"Host name: {platform.node()}")
    system_info_lines.append(f"OS version: {platform.release()}")
    system_info_lines.append(f"Machine type: {platform.machine()}")
    return system_info_lines

def main():
    print_system_info()

if __name__ == '__main__':
    main()