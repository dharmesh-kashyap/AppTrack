# Task 1: Backend Development

## How to Set Up and Run

### 1. Set Up Python Environment
- Install Python (ensure version 3.8 or higher).
- Create and activate a virtual environment:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- Install required dependencies:
  ```bash
  pip install flask flask-sqlalchemy
  ```

### 2. Run the Flask API
- Navigate to the project directory:
  ```bash
  cd path\to\flask_app
  ```
- Start the server:
  ```bash
  python app.py
  ```

### 3. Access the API
- Base URL: `http://127.0.0.1:5000`

## How It Works

## Testing
- Use Postman to test endpoints with proper headers and payloads.


### POST `/add-app`
- Adds an app to the database.
- Example Request:
  ```json
  {
    "app_name": "SampleApp",
    "version": "1.0",
    "description": "Test app."
  }
  ```

  ![image](https://github.com/user-attachments/assets/378a469b-bd1e-4563-be93-5b2ef125fd67)


### GET `/get-app/{id}`
- Fetches details of an app by its ID.
- Example URL:
  ```bash
  http://127.0.0.1:5000/get-app/1
  ```
  
  ![image](https://github.com/user-attachments/assets/1c989cf1-d57c-4648-ad16-f92370a19b34)


### DELETE `/delete-app/{id}`
- Deletes an app by its ID.
- Example URL:
  ```bash
  http://127.0.0.1:5000/delete-app/1
  ```

  ![image](https://github.com/user-attachments/assets/e7ae2c9b-c041-4368-98cb-39dad4e64820)




---
