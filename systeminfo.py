# Cailan White 2025
# Simple system information script

import platform

def print_system_info():
    print("System:", platform.system())
    print("Host name:", platform.node())
    print("OS version:", platform.release())
    print("Machine type:", platform.machine())

def get_system_info_lines():
    system_info_lines = []
    system_info_lines.append("System:", platform.system())
    system_info_lines.append("Host name:", platform.node())
    system_info_lines.append("OS version:", platform.release())
    system_info_lines.append("Machine type:", platform.machine())
    return system_info_lines

def main():
    print_system_info()

if __name__ == '__main__':
    main()