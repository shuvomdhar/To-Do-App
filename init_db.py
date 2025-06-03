from app import create_app, db
from app.models import User, Task

app = create_app()

with app.app_context():
    # Drop all tables to recreate with new structure
    db.drop_all()
    
    # Create all tables
    db.create_all()
    
    print("Database and tables created successfully.")
    print("Note: All existing data has been cleared due to schema changes.")
    print("You can now register new users and create tasks!")