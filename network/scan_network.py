import subprocess
import platform
import locale


def get_connected_devices():
    system = platform.system()

    if system == "Windows":
        cmd = ["arp", "-a"]
        encoding = locale.getpreferredencoding()
    else:
        cmd = ["ip", "neigh"]
        encoding = "utf-8"

    try:
        result = subprocess.check_output(cmd, text=True, encoding=encoding)

        print("======= Found devices =======")

        for line in result.splitlines():
            if system == "Windows":
                if "dynamic" in line.lower():
                    print(line)
            else:
                if "lladdr" in line:
                    print(line)

    except Exception as e:
        print("Error:", e)


get_connected_devices()

"""Network Device Discovery Script

This Python script scans the local network and displays a list of connected devices by retrieving entries from the 
system’s ARP (Address Resolution Protocol) table. It works on both Windows and Unix-based operating systems (Linux/macOS).

How It Works

Detects the operating system
The script uses the platform module to determine whether it is running on Windows or a Unix-based system.

Executes the appropriate system command

On Windows, it runs the arp -a command.

On Linux/macOS, it runs the ip neigh command.

Handles system encoding

On Windows, it automatically detects the system’s preferred encoding using the locale module.

On Unix-based systems, it uses UTF-8 encoding.

Parses and filters results

On Windows, it prints only entries marked as "dynamic" (active devices).

On Unix-based systems, it prints lines containing "lladdr" (devices with MAC addresses).

Error handling
Any execution errors (for example, missing system commands or permission issues) are caught and displayed.

Output

The script prints a header:

======= Found devices =======

Followed by a filtered list of currently connected devices detected on the local network.

Purpose

This script provides a simple cross-platform way to inspect active devices on a local network without requiring external
libraries."""