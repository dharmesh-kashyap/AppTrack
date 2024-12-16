# Full Project: AppTrack

## How to Set Up the Project

### 1. Install Python
- Ensure version 3.8 or higher is installed.

### 2. Create a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install flask flask-sqlalchemy requests
```

### 4. Set Up Android Studio
- Install and configure an emulator via **AVD Manager**.
- Add ADB to PATH.

## How It Works

### Task 1 - Backend Development
- A Flask API provides endpoints to manage app details.
- Start the API server:
  ```bash
  python app.py
  ```

### Task 3 - Virtual Android System
- The emulator simulates an Android environment.
- Run the logger script:
  ```bash
  python android_logger.py
  ```

### Task 4 - Networking
- System information is fetched from the emulator and sent to the Flask API.
- Run the networking script:
  ```bash
  python networking_script.py
  ```

## Testing

### Test Flask API Endpoints
- Use Postman to test `/add-app`, `/get-app/{id}`, and `/delete-app/{id}`.

### Verify Emulator Connectivity
- Ensure the emulator is connected via:
  ```bash
  adb devices
  ```

### Check Data Flow
- Run the networking script and verify data is added to the database.
