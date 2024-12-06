from models.user import User

def create_personal_user():
    # Create a new personal user
    new_user = User("PersonalUser", "personal@test.com", "password123", "personal")
    new_user.save_to_db()
    print("Personal user created successfully!")

if __name__ == "__main__":
    create_personal_user()
