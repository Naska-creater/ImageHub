# Project Description
ImageHub is a web application developed using Django that allows users to upload, store, and view images along with their descriptions. The application provides functionalities for user account management, image uploads, and image management, making it a comprehensive platform for image sharing.

## Technologies Used
- Programming Language: Python 3
- Web Framework: Django
- API Framework: Django REST Framework
- Database: PostgreSQL
- Containerization: Docker
- Web Server: Nginx (for serving static files)

## Installation and Running Instructions

Ensure you have Docker installed on your machine.
Make sure you have Python 3 and pip installed.

### Step-by-Step Installation
1. Clone the repository:
 - git clone https://github.com/yourusername/ImageHub.git
 - cd ImageHub

2. Build the Docker container:
 - docker-compose build

3. Run the application:
 - docker-compose up

4. Access the application:
 - Open your web browser and go to http://localhost:8000 to access the ImageHub application.

### Usage
- User Registration: Users can create an account to utilize the application.
- Login: Users can log in to access their accounts.
- Image Upload: Users can upload images and add descriptions.
- View Images: Users can browse images uploaded by others.
- Edit/Delete Images: Users can manage their uploaded images.
### API Documentation
Detailed API documentation will be provided separately, including endpoint descriptions, request/response formats, and example data.
### Functional Requirements
#### For Users:
- Account registration
- Login
- Uploading images
- Viewing images
- Adding descriptions to images
- Editing and deleting images
#### For Admin:
- User management
- Image management
#### CRUD Operations
#### User:

- Create: Register a new user.
- Read: View profile information.
- Update: Update profile information.
- Delete: Delete account.
- 
#### Categories:

- Create: Create a new category (admin only).
- Read: View categories.
- Update: Edit category name (admin only).
- Delete: Delete a category (admin only).

#### Images:

- Create: Upload a new image with a description.
- Read: View all uploaded images with descriptions.
- Update: Edit an uploaded image's description.
- Delete: Delete an image.

#### Permissions and Roles
- Ordinary User: Upload images, view all images, edit and delete their images.
- Administrator: Manage all images and descriptions.

#### Security
- Authentication: Implementing an authentication system (e.g., Token Authentication).
- Data Validation: Ensure correct input data for all operations.
#### Testing
-Unit tests will be written to verify the functionality of the application.