A RESTful API built with **Django REST Framework** that allows users to create and manage customized workout plans, track fitness goals, and explore predefined exercises.

---

### Core
- **User Authentication**
  - User registration, login, logout
  - JWT-based secure API access

- **Predefined Exercises**
  - Each includes description, instructions, and target muscles

- **Personalized Workout Plans**
  - Create tailored workout plans
  - Customize with repetitions, sets, duration, or distance
  - Specify workout frequency and goals

- **Tracking & Goals**
  - Track weight over time
  - Set personal fitness goals (e.g., weight or exercise achievements)

- **API Documentation**
  - Swagger/OpenAPI UI for easy testing and interaction

### Bonus
- **Docker & Docker Compose**
  - For quick setup and deployment

---

## Tech Stack
- **Backend**: Django REST Framework (Python)
- **Database**: SQLite
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **Docs**: Swagger / drf-spectacular
- **Containerization**: Docker & Docker Compose

---

### Local Development

```bash
# Clone the repo
git clone https://github.com/your-username/workout-planner-api.git
cd workout-planner-api

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver

# To Build images and start containers
docker-compose up --build

    
