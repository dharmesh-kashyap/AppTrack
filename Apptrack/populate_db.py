from app import app, db, AppDetails

# Add sample data
def add_sample_data():
    sample_apps = [
        {"app_name": "TestApp1", "version": "1.0", "description": "First sample app."},
        {"app_name": "TestApp2", "version": "2.0", "description": "Second sample app."},
        {"app_name": "TestApp3", "version": "3.1", "description": "Third sample app."}
    ]

    for app in sample_apps:
        new_app = AppDetails(
            app_name=app["app_name"],
            version=app["version"],
            description=app["description"]
        )
        db.session.add(new_app)

    db.session.commit()
    print("Sample data added!")

# Run the function
if __name__ == '__main__':
    with app.app_context():  # Use the Flask app's context, not db's
        add_sample_data()
