
# Task 3: Virtual Android System Simulation

## How to Set Up

### 1. Install Android Studio
- Download from [here](https://developer.android.com/studio).
- Set up an Android emulator:
  - Go to **AVD Manager**.
  - Create a new device and start the emulator.

### 2. Install ADB
- Add ADB to your PATH (found in `platform-tools` of the Android SDK).
- Verify ADB:
  ```bash
  adb version
  ```

### 3. Install Sample APK
- Download an APK file and install it:
  ```bash
  adb install sample.apk
  ```

## How It Works

- The emulator simulates an Android environment.
- Use ADB commands to:
  - Retrieve system information (e.g., OS version, device model).
  - Install and manage APK files.

## Script

Run the Python script to fetch system information:
```bash
python android_logger.py
```

![image](https://github.com/user-attachments/assets/1a6dadd3-3f8a-48ad-bd6d-3e7b2efd6df9)


The script logs:
- OS version.
- Device model.
- Memory details.

## Testing

- Verify the APK is installed on the emulator:
  ```bash
  adb shell pm list packages | grep <package_name>
  ```

---
