# project3 Cookbook

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
- **Frontend:** HTML, CSS (Materialize Framework)
- **Backend:** Flask (Python)
- **Database:** PostgreSQL
- **Deployment:** [Add if applicable]

## Installation
1. Clone the repository:
   ```sh
   git clone <repository-url>
