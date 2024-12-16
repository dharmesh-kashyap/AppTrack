import subprocess

def get_system_info():
    try:
        # Get Android OS version
        os_version = subprocess.check_output(['adb', 'shell', 'getprop', 'ro.build.version.release']).decode().strip()
        print(f"Android OS Version: {os_version}")

        # Get device model
        device_model = subprocess.check_output(['adb', 'shell', 'getprop', 'ro.product.model']).decode().strip()
        print(f"Device Model: {device_model}")

        # Get available memory
        mem_info = subprocess.check_output(['adb', 'shell', 'cat', '/proc/meminfo']).decode()
        print(f"Memory Info:\n{mem_info}")

    except subprocess.CalledProcessError as e:
        print(f"Error executing ADB command: {e}")

if __name__ == '__main__':
    print("Fetching system information...")
    get_system_info()
