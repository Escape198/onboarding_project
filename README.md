# Onboarding Funnel

This project implements a simplified onboarding funnel with a landing page, a three-step onboarding process, and a basic analytics dashboard. It is built using **FastAPI** for the backend and a clean HTML/CSS/JavaScript frontend.

---

## Features

- **Landing Page**: A welcoming page with a "Get Started" button to initiate the onboarding process.
- **Three-Step Onboarding Process**:
  - Step 1: Introduction.
  - Step 2: Embedded video (autoplay, no controls).
  - Step 3: Completion message.
- **Analytics Dashboard**: Track the number of users who completed the onboarding process.
- **REST API**: Backend services for handling onboarding logic.

---

## Tech Stack

- **Backend**: FastAPI (Python 3.10)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Containerization**: Docker

---

## Setup Instructions

### Prerequisites

- Docker and Docker Compose installed on your system.

### 1. Clone the Repository

```bash
git clone <repository-url>
cd onboarding_project
```

### 2. Build and Run with Docker Compose

```bash
docker-compose up --build
```

### 3. Access the Application

- **Frontend**: Open your browser and navigate to `http://0.0.0.0:8080`.
- **Backend**: API documentation available at `http://0.0.0.0:8000/docs`.

---

## API Endpoints

### 1. Start Onboarding

- **URL**: `POST /onboarding/start`
- **Request Body**:
  ```json
  {
    "user_name": "Ruslan"
  }
  ```
- **Response**:
  ```json
  {
    "message": "User Ruslan started onboarding!",
    "user_id": 1
  }
  ```

### 2. Complete Step

- **URL**: `POST /onboarding/complete-step`
- **Request Body**:
  ```json
  {
    "user_id": 1,
    "step": "step-1"
  }
  ```
- **Response**:
  ```json
  {
    "message": "Step step-1 completed for user 1!"
  }
  ```

### 3. Get Analytics

- **URL**: `GET /analytics/completed-users`
- **Response**:
  ```json
  {
    "completed_users": 5
  }
  ```

---

## File Structure

```
onboarding_project/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models.py
│   │   ├── database.py
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   ├── onboarding.py
│   │   │   ├── analytics.py
│   ├── Dockerfile
│   ├── requirements.txt
├── frontend/
│   ├── index.html
│   ├── onboarding/
│   │   ├── step1.html
│   │   ├── step2.html
│   │   ├── step3.html
│   ├── css/
│   │   ├── styles.css
│   ├── js/
│   │   ├── app.js
│   ├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## Frontend Flow

1. **Landing Page**:
   - Prompt the user to enter their name and start onboarding.
   - User ID is stored in `localStorage`.

2. **Onboarding Steps**:
   - Each step triggers an API request to save progress.
   - Navigation to the next step occurs automatically upon success.

3. **Completion**:
   - Final step marks the user as completed in the database.

---

## Future Improvements

- Add user authentication.
- Enhance analytics with charts.
- Make the application mobile-friendly.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
