﻿# project3 Cookbook

## Background information
Cookbook is a simple web application that allows users to browse and contribute recipes. The website organizes recipes into categories, making it easy for users to find and share their favorite dishes. Users can view, edit and delete both categories and recipes without logging in.They also can purchase kitchen tools by clicking a link on the home page which direct them to Amazon. 

### Goals
- External user’s goal: Find and share recipes.
- Site owner's goal: to promote a brand of cooking tools.

### User stories
- First Time Visitor Goals
  1. As a First Time Visitor, I want to easily understand the main purpose of the site.
  2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find information.
- Returning Visitor Goals
  1. Search for recipes according to categories, view relevant information about ingredients and instructions.
  2. Share recipes according to categories, write relevant information about ingredients and instructions.
  3. Buy kitchen tools from Amazon which is directed by this website.
- Frequent Visitor Goals
  1. Search for recipes according to categories, view relevant information about ingredients and instructions.
  2. Share recipes according to categories, write relevant information about ingredients and instructions.
  3. Buy kitchen tools from Amazon which is directed by this website.


## Features

### Homepage
- A clean and simple layout without a hero section.
- Recipes are listed in collapsible cards. Users can edit or delete recipes, once the full recipe is shown up.
- A promotional section for cooking tools, linking to Amazon.

### Categories Page 
- Users can create recipe categories (e.g., Italian, Vegan, Desserts) by clicking 'Add Category'.
- Recipes are organized under these categories.
- Users can view, edit and delete categories by clicking corresponding buttons.

### Share Recipe Pages
- Each recipe page includes:
  - Title
  - Ingredients
  - instructions
- By filling the form and clicking 'ADD' button, users share their recipe.

### Search Functionality
- Users can search for recipes by category.


### User Interaction
- All users can browse recipes without signing in.
- Any user can edit or delete recipes or categories.

## Technologies Used
- **Flask** – Web framework for backend development
- **HTML, CSS, JavaScript** – Frontend languages for structure, styling, and interactivity
- **PostgreSQL** – Database for storing recipes and user data
- **Materialize** – CSS framework for responsive design
- **Python** – Backend language
- **VS Code** – Development environment used for coding
- **GitHub** – Source code hosting and version control
- **Canva** - Design wireframe


## Design

### Color Scheme
The color scheme for this website is designed to be clean, simple and represent healthy eating, with a focus on readability.

- **Background Color**: The background is set to **white** (#FFFFFF) to provide a clean, minimalistic look, ensuring that the content remains the focal point.
- **Primary Color**: The main accents of the website are in **green** and **light green**. They are used for navigation bar and footer, giving out a healthy eating vibe and guiding the user’s attention.
- **Text Color**: The primary font color is **black** (#000000) for optimal contrast against the white background, ensuring readability across all devices and environments.

This simple color scheme enhances the user experience by focusing on clarity, ease of navigation, and visual comfort.

### Typography:

In this project, I used the default **Materialize** font stack for the app's typography. The Materialize framework uses a set of system fonts to ensure excellent performance, wide compatibility, and consistent readability across various devices and platforms.

- The font stack is made up of:
  - `-apple-system` (for Apple devices)
  - `BlinkMacSystemFont` (for browsers on macOS)
  - `Segoe UI` (for Windows devices)
  - `Roboto` (commonly used for Android and modern browsers)
  - `Ubuntu`, `Cantarell`, `Helvetica Neue`, `sans-serif` (additional fallback options)

By relying on system fonts, Materialize avoids loading external fonts, which improves the performance and speed of the app. The result is a clean, readable experience across desktop and mobile devices.

### Wireframe

Below is the wireframe for this project:

- **Home page**
![Homepage](images_readme/wireframe_home.PNG)
- **Recipe Form**
![RecipeForm](images_readme/recipeform.png)
- **Category page**
![Categorypage](images_readme/wireframe_category.png)

## Testing

### Homepage

This test ensures that all key elements on the homepage work correctly, including navigation, promotions, and recipe listings

- **Expected Results**
1. Navigation links should direct users to the correct pages (Share Recipe, Categories).
2. The promotional picture should load properly.
3. Clicking the "Shop Now" button should open the Amazon page.
4. Recipes should be displayed inside collapsible cards.
5. Clicking a recipe card should expand/collapse the details.
6. Edit and Delete buttons should appear on each recipe card and function correctly.

- **Actual Results**
![Homepage](images_readme/homepage.PNG)
1. Navigation links are working correctly.
2. The promotional image loads properly.
3. Recipes display correctly inside collapsible cards.
4. Clicking a card expands/collapses the recipe details as expected.
![Recipecard](images_readme/collapsible_card.PNG)
5. Edit and Delete buttons appear on each recipe card and function correctly.
![editdelete](images_readme/collapsible_card2.PNG)
![Editrecipe](images_readme/edit_recipe.PNG)
6. The "Shop Now" button redirects to Amazon as expected.
![PromotionPage](images_readme/shopnow_page.PNG)

### Categories Page

- **Expected Result**
1. Categories should be displayed inside cards.
2. Each category card should have View, Edit, and Delete buttons.
3. View button should open a page showing recipes in collapsible cards in that category.
4. Edit button should navigate to the Edit Category page where the category name can be changed.
5. Delete button should remove the category from the list immediately.
- **Actual Result:** 
1. Categories display correctly in card format.
![CategoriesPage](images_readme/categories_page.PNG)
2. View button works → Clicking it correctly shows recipes in that category and the collapsible card works.
![ViewCategories](images_readme/category_page2.PNG)
![ViewCategories](images_readme/category_page3.PNG)
3. Edit button works → Clicking it navigates to the Edit Category page, where the category name can be updated.
![EditCategories](images_readme/edit_category.PNG)
4. Delete button works → Clicking it immediately removes the category from the page. No confirmation prompt appears.
![DeleteCategoriesPage](images_readme/delete_category.PNG)

### Share Recipe Page

- **Expected Result**
1. The page should display a form with the following fields:
Title (text input)
Ingredients (textarea)
Instructions (textarea)
2. A Submit button should be present to share the recipe.
3. After submitting, the new recipe should be saved and visible in the relevant category..
 
- **Actual Result:** 
1. The form loads correctly with all required fields.
![ShareRecipe](images_readme/share_recipe_page.PNG)
2. The Submit button works → Clicking it successfully saves the recipe.
3. The newly added recipe appears in the correct category after submission.

### Report Issues
- **Contact:** Email [wendytanvalencia@gmail.com].

## Bug

### Issue: Broken Navigation Links

- **Problem**: 
Some navigation links (like from the Categories page to the Recipe View page) weren’t working, leading to 404 errors.
- **Solution**: 
Checked the routes in Flask and found that some URLs were incorrectly linked. Corrected the route paths in the run.py file and tested the navigation again.
- **Fix**: 
After the correction, all links now lead to the correct pages.

### Category Deletion Without Confirmation

- **Problem**: The Delete button on the Categories page removed a category immediately without any confirmation, which could lead to accidental deletions.
- **Solution**:
I decided to proceed without the confirmation for now for simplicity but awared that it could be added in the future for improved user experience.
- **Fix**: 
The deletion function works.

### Changing Database

- **Problem**: 
The initial idea was to include a user model but found it difficult for me to handle, so I decided to substitute it with a category model. However, when reseting the database after some initial setup, the system can't  remove the User model and introduce a Category model. The existing tables and database structure were causing conflicts.
- **Solution**:
1.Dropping the old tables (including the User table).
2.Creating new migrations after defining the new Category model.
3.Applying the new migration to reset the database to match the new models.
- **Fix**: 
After running the migrations and updating the models, the database was successfully reset, and the new Category model was in place without errors.

### Promotion card Image Not Showing

- **Problem**: 
The image for the promotion card was not displaying correctly in the final output despite being referenced in the code.
- **Solution**: 
I checked the image path and found that there was a mismatch between the image folder location and the path used in the HTML file.
- **Fix**: 
After correcting the path to the correct image folder, the image displayed correctly within the collapsible cards.


## Version Control
This project uses Git for version control. 
- **Repository**: The project is maintained in a Git repository, which helps track changes and manage the project’s history.
- **Commits**: Changes are committed with descriptive messages to keep track of modifications and updates.
- **Commit Messages**: Descriptive commit messages are used to explain the purpose of each change.
- **Main Branch**: The `main` branch represents the latest stable version of the project. All final changes are merged into this branch.

## Deployment
This application is hosted on Heroku.

You can access it directly by visiting the following URL:https://cookbook2025-5f9129fdca8f.herokuapp.com/

![image](https://github.com/user-attachments/assets/333364fe-70f6-4a9f-86fa-e5ab4393e00d)

## Credits

- The images used on this website are sourced from various platforms. Below are the appropriate credits for each image:

**kitchen_tools** - Image source:[UNL Food](https://food.unl.edu/article/cooks-tools-30-time-saving-kitchen-tools/)

- Much of the database setup and management structure for this project was inspired by the Database Management Systems walkthrough provided by [Code Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DIWADRDB+5/courseware/c0c31790fcf540539fd2bd3678b12406/6e44128b0b37416ab40c1a87ef2cb32a/) . 

- Used Materialize CSS For providing a responsive framework for the frontend design.
