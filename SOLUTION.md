# Solution Steps

1. 1. Define a SQLAlchemy User model in app/models.py with a unique constraint on the email field.

2. 2. Create Pydantic schemas for user input (UserCreate) and output (UserOut) in app/schemas.py.

3. 3. Set up the database connection (to PostgreSQL) and session dependency in app/database.py.

4. 4. In app/main.py, set up the FastAPI app. Implement a /register endpoint that:

5.     a. Checks at the application level if a user with the given email already exists.

6.     b. Attempts to add the new user to the database.

7.     c. Handles IntegrityError exceptions to catch duplicate emails at the database level.

8.     d. Returns a clear 400 error message when a duplicate is found.

9. 5. Create requirements.txt with FastAPI, SQLAlchemy, psycopg2-binary, and uvicorn.

10. 6. Add a Dockerfile to containerize the FastAPI application.

11. 7. Write a docker-compose.yml file to orchestrate the API and a PostgreSQL service together.

12. 8. Use Alembic or 'Base.metadata.create_all' at startup to create the users table if it does not exist.

13. 9. Test registration with new and duplicate emails to confirm correct error handling.

