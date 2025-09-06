# Healthcare Backend System

A comprehensive healthcare management backend system built with Django REST Framework, featuring patient management, doctor records, and secure JWT authentication.

## Features

- **User Authentication**: JWT-based secure authentication system
- **Patient Management**: Complete CRUD operations for patient records
- **Doctor Management**: Manage doctor profiles and information
- **Patient-Doctor Mapping**: Assign doctors to patients
- **PostgreSQL Database**: Robust database with proper relationships
- **RESTful APIs**: Well-structured API endpoints
- **Data Validation**: Comprehensive input validation and error handling

## Technology Stack

- **Backend**: Django 4.2, Django REST Framework
- **Database**: PostgreSQL
- **Authentication**: JWT (djangorestframework-simplejwt)
- **Environment Management**: python-decouple

## Prerequisites

- Python 3.8+
- PostgreSQL 12+
- pip (Python package manager)

## Installation & Setup

### 1. Clone the Repository
\`\`\`bash
git clone https://github.com/yourusername/healthcare-backend.git
cd healthcare-backend
\`\`\`

### 2. Create Virtual Environment
\`\`\`bash
python -m venv healthcare_env
# Windows
healthcare_env\\Scripts\\activate
# Mac/Linux
source healthcare_env/bin/activate
\`\`\`

### 3. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Environment Configuration
\`\`\`bash
cp .env.example .env
# Edit .env file with your database credentials and settings
\`\`\`

### 5. Database Setup
\`\`\`bash
# Create PostgreSQL database
createdb healthcare_db

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (optional)
python manage.py createsuperuser
\`\`\`

### 6. Run Development Server
\`\`\`bash
python manage.py runserver
\`\`\`

The server will start at \`http://localhost:8000\`

##  API Documentation

### Authentication Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | \`/api/auth/register/\` | Register a new user |
| POST | \`/api/auth/login/\` | User login |

### Patient Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | \`/api/patients/\` | Get all patients |  |
| POST | \`/api/patients/\` | Create new patient | |
| GET | \`/api/patients/{id}/\` | Get specific patient |  |
| PUT | \`/api/patients/{id}/\` | Update patient |  |
| DELETE | \`/api/patients/{id}/\` | Delete patient |  |

### Doctor Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | \`/api/doctors/\` | Get all doctors |  |
| POST | \`/api/doctors/\` | Create new doctor |  |
| GET | \`/api/doctors/{id}/\` | Get specific doctor |  |
| PUT | \`/api/doctors/{id}/\` | Update doctor |  |
| DELETE | \`/api/doctors/{id}/\` | Delete doctor |  |

### Patient-Doctor Mapping Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | \`/api/mappings/\` | Get all mappings |  |
| POST | \`/api/mappings/\` | Create new mapping |  |
| GET | \`/api/mappings/{patient_id}/\` | Get patient's doctors |  |
| DELETE | \`/api/mappings/remove/{id}/\` | Remove doctor from patient |  |

##  Sample API Requests

### Register User
\`\`\`json
POST /api/auth/register/
{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "securepass123",
    "password_confirm": "securepass123"
}
\`\`\`

### Login User
\`\`\`json
POST /api/auth/login/
{
    "email": "john@example.com",
    "password": "securepass123"
}
\`\`\`

### Create Patient
\`\`\`json
POST /api/patients/
Headers: Authorization: Bearer YOUR_JWT_TOKEN
{
    "name": "Jane Smith",
    "email": "jane@example.com",
    "phone": "+1234567890",
    "date_of_birth": "1990-01-15",
    "gender": "F",
    "address": "123 Main St, City, State",
    "medical_history": "No known allergies"
}
\`\`\`

##  Security Features

- JWT token-based authentication
- Password validation and hashing
- CORS configuration
- Environment variable management
- Input validation and sanitization

##  Project Structure

\`\`\`
healthcare-backend/
├── authentication/          # User authentication app
├── patients/               # Patient management app
├── doctors/                # Doctor management app
├── mappings/               # Patient-doctor relationship app
├── healthcare_backend/     # Main project settings
└── postman_collection/     # API testing collection
\`\`\`

##  Deployment

### Environment Variables for Production
- Set \`DEBUG=False\`
- Use a secure \`SECRET_KEY\`
- Configure proper \`ALLOWED_HOSTS\`
- Use production database credentials

##  Contributing

1. Fork the repository
2. Create your feature branch (\`git checkout -b feature/AmazingFeature\`)
3. Commit your changes (\`git commit -m 'Add some AmazingFeature'\`)
4. Push to the branch (\`git push origin feature/AmazingFeature\`)
5. Open a Pull Request

##  License

This project is licensed under the MIT License.

##  Author

**Your Name**
- GitHub: [@yourusername](https://github.com/NandaniVerma75)
- Email: nandaniverma269@gmail.com

---