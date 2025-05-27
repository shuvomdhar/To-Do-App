# To-Do App

A simple yet powerful task management application that allows multiple users to create accounts, manage their personal to-do lists, and stay organized. Built with Python Flask and SQLite database.

## Features

- **User Authentication**: Secure user registration and login system
- **Personal Task Management**: Each user has their own private to-do list
- **Task Operations**: Create, read, update, and delete tasks
- **Task Status**: Mark tasks as completed or pending
- **User-Friendly Interface**: Clean and intuitive web interface
- **Data Persistence**: All data stored securely in SQLite database

## Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Flask sessions
- **Password Security**: Werkzeug password hashing

## This is how it will work
![To-Do App]("D:\To-Do Recording.gif")


## Prerequisites


Before running the application, make sure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/shuvomdhar/To-Do-App.git
```

```bash
cd To-Do App
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv To-Do_env

# Activate virtual environment
# On Windows:
To-Do_env\Scripts\activate

# On macOS/Linux:
source To-Do_env/bin/activate
```

### 3. Install Required Dependencies

```bash
pip install flask flask-sqlalchemy werkzeug
```

### 4. Database Setup

The application uses SQLite database. You need to create the database tables before running the app.

#### Option 1: Using Python Interactive Shell

```bash
python
```

Then run the following commands:

```python
from run import app, db
with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
exit()
```

#### Option 2: Using a Setup Script

Create a file named `setup_db.py` with the following content:

```python
from run import app, db

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")
```

Then run:

```bash
python setup_db.py
```

### 5. Run the Application

```bash
python run.py
```

The application will start running on `http://127.0.0.1:5000` or `http://localhost:5000`

## Usage

### Getting Started

1. **Open your web browser** and navigate to `http://localhost:5000`

2. **Create an Account**:
   - Click on "Register" or "Sign Up"
   - Enter your username, email, and password
   - Submit the registration form

3. **Login**:
   - Use your credentials to log into your account
   - You'll be redirected to your personal dashboard

4. **Manage Tasks**:
   - **Add Task**: Click "Add New Task" and enter task details
   - **View Tasks**: See all your tasks in an organized list
   - **Mark Complete**: Check off completed tasks
   - **Edit Task**: Modify existing task details
   - **Delete Task**: Remove tasks you no longer need

5. **Logout**: Use the logout option to securely end your session

## Project Structure

```
todo-app/
│
├── run.py                 # Main application file
├── models.py             # Database models (User, Task)
├── templates/            # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
├── static/               # CSS, JS, and image files
│   ├── css/
│   ├── js/
│   └── images/
├── instance/             # SQLite database file (created automatically)
│   └── todo.db
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Database Schema

### Users Table
- `id`: Primary key
- `username`: Unique username
- `email`: User's email address
- `password_hash`: Hashed password for security
- `created_at`: Account creation timestamp

### Tasks Table
- `id`: Primary key
- `title`: Task title
- `description`: Task description (optional)
- `completed`: Boolean status (True/False)
- `created_at`: Task creation timestamp
- `updated_at`: Last modification timestamp
- `user_id`: Foreign key linking to Users table

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page |
| GET/POST | `/register` | User registration |
| GET/POST | `/login` | User login |
| GET | `/dashboard` | User dashboard with tasks |
| POST | `/add_task` | Add new task |
| PUT | `/update_task/<id>` | Update existing task |
| DELETE | `/delete_task/<id>` | Delete task |
| POST | `/logout` | User logout |

## Configuration

### Environment Variables (Optional)

You can set the following environment variables for additional configuration:

```bash
export FLASK_ENV=development    # For development mode
export FLASK_DEBUG=1           # Enable debug mode
export SECRET_KEY=your-secret-key-here
```

### Database Configuration

By default, the app uses SQLite database stored in `instance/todo.db`. To use a different database, modify the database URI in `run.py`:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database_name.db'
```

## Troubleshooting

### Common Issues

1. **Database Errors**:
   - Make sure you've created the database tables using the setup instructions
   - Check if the `instance` folder has proper write permissions

2. **Import Errors**:
   - Ensure all required packages are installed: `pip install flask flask-sqlalchemy werkzeug`
   - Make sure you're in the correct directory and virtual environment is activated

3. **Port Already in Use**:
   - If port 5000 is busy, specify a different port: `python run.py --port 5001`

4. **Template Not Found Errors**:
   - Ensure the `templates` folder exists in the same directory as `run.py`
   - Check that all template files are present

### Getting Help

If you encounter any issues:

1. Check the console output for error messages
2. Ensure all dependencies are properly installed
3. Verify the database has been created successfully
4. Make sure you're running the app from the correct directory

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Security Notes

- Passwords are hashed using Werkzeug's security utilities
- User sessions are managed securely
- Each user can only access their own tasks
- Input validation is implemented to prevent common vulnerabilities

## Future Enhancements

- Task categories and tags
- Due dates and reminders
- Task sharing between users
- Mobile app development
- Email notifications
- Task priority levels
- Search and filter functionality

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Quick Start Commands

Here's a quick copy-paste guide to get started:

```bash
# 1. Install dependencies
pip install flask flask-sqlalchemy werkzeug

# 2. Set up database
python -c "from run import app, db; app.app_context().push(); db.create_all(); print('Database created!')"

# 3. Run the application
python run.py
```

Then open your browser and go to `http://localhost:5000`

---

**Happy Task Managing! **
