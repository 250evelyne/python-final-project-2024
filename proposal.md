# Recipe Manager and Meal Planner

## Project Description

The Recipe Manager and Meal Planner is a web application designed to help users store, manage, and plan their meals efficiently. The application allows users to save their favorite recipes, categorize them by type (e.g., breakfast, lunch, dinner), and generate meal plans on a weekly or daily basis. The app also includes a feature for automatically generating shopping lists based on the meal plan, and it can calculate nutritional information for each recipe, making meal planning both convenient and health-conscious.

## Main Idea

The core functionality of the Recipe Manager and Meal Planner revolves around helping users streamline their cooking and meal planning. Key features include:

- **Recipe Storage**: Users can store recipes with ingredients, instructions, and categories for easy access.
- **Meal Calendar**: A meal planning tool where users can assign recipes to specific days, ensuring meals are planned ahead of time.
- **Automatic Shopping List**: The application generates a shopping list based on the ingredients needed for planned meals, saving time and ensuring nothing is forgotten.
- **Nutritional Information**: Using a nutritional API, the app can calculate and display nutritional details (calories, macronutrients, etc.) for each recipe.
- **Recipe Scaling**: Users can adjust serving sizes, and the app will automatically scale ingredient quantities accordingly.

This application simplifies both the planning and execution of meals, making it a valuable tool for anyone trying to stay organized in the kitchen, maintain a healthy diet, or reduce the stress of grocery shopping.

## Technologies

To build the Recipe Manager and Meal Planner, the following technologies will be used:

- **Flask**: A lightweight web framework that will be used to build the application’s backend.
- **SQLite**: A simple, yet powerful database to store user recipes, meal plans, and shopping lists.
- **Jinja2**: For templating the front-end views in the Flask application.
- **HTML/CSS/JavaScript**: For building the front-end interface, allowing users to interact with the app.
- **jQuery**: To handle client-side operations, such as form validation and dynamic updates to the page.
- **Nutritional Information API** (e.g., **Edamam** or **Spoonacular**): To fetch nutritional data for recipes, enabling the app to calculate the nutritional value of each meal.
- **Python**: For handling the application’s core logic, including recipe management, meal planning, and shopping list generation.

## Project Timeline

Here’s the proposed timeline for the development of the Recipe Manager and Meal Planner:

- **Week 4**: Project initialization and setup
  - Create the GitHub repository
  - Set up the project structure with basic files (README, proposal, initial Flask setup)
  - Install Flask, SQLite, and other required libraries
  
- **Week 5**: First meaningful commit beyond initial setup
  - Implement recipe storage functionality
  - Design a basic UI for adding and displaying recipes
  - Set up the SQLite database for storing recipe data
  
- **Week 7**: Project week – focused development time in class
  - Implement the meal planning feature (meal calendar)
  - Allow users to assign recipes to specific days on the calendar
  
- **Weeks 8-12**: Continued development with regular commits
  - **Week 8**: Automatic shopping list generation based on meal plans
  - **Week 9**: Integrate the Nutritional Information API to calculate nutritional values for recipes
  - **Week 10**: Add recipe scaling functionality to adjust servings and ingredients
  - **Week 11**: Finalize the user interface and polish front-end elements (styling, interactivity)
  - **Week 12**: Testing and bug fixes
  
- **Week 13**: Project week – focused development time in class
  - Conduct final testing and integrate feedback from peers or the instructor
  - Prepare for project presentation
  
- **Week 14**: Final project presentation
  - Present the Recipe Manager and Meal Planner to classmates and instructor, showcasing the main features (recipe storage, meal planner, shopping list generator, etc.)
