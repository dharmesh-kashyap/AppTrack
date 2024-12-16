# Task 4: Networking

## How to Set Up

### 1. Ensure Flask API is Running
- Navigate to the project directory where `app.py` is located.
- Start the Flask server:
  ```bash
  python app.py
  ```

### 2. Ensure Android Emulator is Running
- Start the emulator via AVD Manager or using the following command:
  ```bash
  adb devices
  ```

### 3. Install Required Dependencies
- Install the `requests` library:
  ```bash
  pip install requests
  ```

## How It Works

The networking script fetches system information from the emulator using ADB and sends the mock data to the Flask API.

## Commands

Run the networking script:
```bash
python Script_network.py
```

![image](https://github.com/user-attachments/assets/e7c4d8b7-502f-49ce-bd63-c4fecb90307e)


## Test the Data Flow

- Check if data is added to the Flask API:
  - Use GET `/get-app/{id}` in Postman.

- Verify the server response for POST `/add-app`.

---
