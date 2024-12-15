**Issue: Users Not Persisting Across Sessions**

**Problem Description**

**Unexpected Behavior**: User accounts were not being saved after the application was restarted or when the browser was refreshed. Users had to re-register every time the application was restarted.

**Expected Behavior**: User accounts should persist even after restarting the application, allowing users to log in without needing to re-register.

**Discovery**: This issue was discovered during initial testing. After registering a user and restarting the application, attempts to log in with the registered user failed because the user data was no longer available.

**Root Cause Analysis**
**Underlying Cause**: The application was using Python dictionaries (users and recipes) for storing user and recipe data. This storage is in-memory, meaning it is lost when the application restarts.

**Incorrect Assumptions**: It was initially assumed that in-memory storage would suffice for handling user data, but this approach does not support data persistence.

**Dependencies**: This issue was tied to the use of Python dictionaries for data storage instead of a database or another form of persistent storage.
Resolution

**Fix**: The application was updated to use a database (e.g., SQLite) to store user accounts and recipes. The Flask application was modified to interact with the database instead of Python dictionaries. I also found out that i did install cyptography before running the program.

**Changes Made:**

installed cryptography 
Created a User model to represent user accounts in the database.
Updated the home() and dashboard() functions to perform database queries instead of accessing in-memory dictionaries.
Migrated existing logic to work with the database 


**Prevention**

**Prevention Steps:**

Use a database for storing critical application data in all future projects requiring persistence.
Evaluate the requirements for data persistence early in the project lifecycle to avoid temporary solutions that cannot scale.

**Lessons Learned:**
In-memory storage is useful for prototyping but unsuitable for production scenarios where data persistence is required.
Testing with realistic use cases (e.g., application restarts) is crucial for uncovering such issues early.

**Warning Signs:**
Frequent loss of data during testing.
Manual workarounds to re-register users after restarting the application.
