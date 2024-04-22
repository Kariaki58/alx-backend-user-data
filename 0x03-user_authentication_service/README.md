# User Authentication Service

## Description

This project implements a user authentication service using Flask and SQLAlchemy. It includes functionality for user registration, login, session management, password reset, and user profile access.

## Requirements

- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All files should end with a new line
- The first line of all files should be `#!/usr/bin/env python3`
- Use SQLAlchemy 1.3.x
- Use `pycodestyle` style (version 2.5)
- All modules, classes, and functions should have proper documentation
- All functions should be type annotated
- Use `bcrypt` for password hashing
- Your code should be organized into modules as described in the tasks
- Set up a basic Flask app with routes as specified in the tasks
- Implement endpoints for user registration, login, session management, password reset, and user profile access

## Tasks

1. User model
   - Define the SQLAlchemy model for the User table.

2. Create user
   - Implement the method to add a user to the database.

3. Find user
   - Implement the method to find a user by email.

4. Update user
   - Implement the method to update a user's attributes.

5. Hash password
   - Implement a function to hash passwords using bcrypt.

6. Basic Flask app
   - Set up a basic Flask app with a single route.

7. Register user
   - Implement the endpoint to register a user.

8. Credentials validation
   - Implement a method to validate user login credentials.

9. Generate UUIDs
   - Implement a function to generate UUIDs for session IDs.

10. Get session ID
    - Implement a method to create a session for a user and return the session ID.

11. Log in
    - Implement the endpoint for user login.

12. Find user by session ID
    - Implement a method to find a user by session ID.

13. Destroy session
    - Implement a method to destroy a user's session.

14. Log out
    - Implement the endpoint for user logout.

15. User profile
    - Implement the endpoint to retrieve user profile information.

16. Generate reset password token
    - Implement a method to generate a reset password token for a user.

17. Get reset password token
    - Implement the endpoint to get a reset password token for a user.

18. Update password
    - Implement a method to update a user's password using a reset token.

19. Update password end-point
    - Implement the endpoint to update a user's password using a reset token.

## Usage

1. Clone the repository:

```
git clone <repository-url>
cd 0x03-user_authentication_service
```

