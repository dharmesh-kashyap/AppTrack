import requests
import subprocess

def get_system_info():
    try:
        # Get Android OS version
        os_version = subprocess.check_output(['adb', 'shell', 'getprop', 'ro.build.version.release']).decode().strip()

        # Get device model
        device_model = subprocess.check_output(['adb', 'shell', 'getprop', 'ro.product.model']).decode().strip()

        # Return mock data
        return {
            "device_id": "emulator-5554",  # Replace with actual device ID if needed
            "os_version": os_version,
            "device_model": device_model
        }
    except subprocess.CalledProcessError as e:
        print(f"Error fetching system info: {e}")
        return {}

def send_data_to_server(data):
    try:
        # Flask API endpoint
        url = "http://127.0.0.1:5000/add-app"

        # Mock app details to send
        payload = {
            "app_name": f"Device-{data.get('device_model')}",
            "version": data.get("os_version"),
            "description": f"Device ID: {data.get('device_id')}"
        }

        # Send POST request
        response = requests.post(url, json=payload)

        # Log server response
        print(f"Server Response: {response.status_code}")
        print(response.json())
    except requests.RequestException as e:
        print(f"Error sending data to server: {e}")

if __name__ == '__main__':
    print("Fetching system information...")
    system_info = get_system_info()
    if system_info:
        print("Sending data to Flask API...")
        send_data_to_server(system_info)
