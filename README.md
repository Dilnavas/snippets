# Text Saving and Retrieval REST API using Django

This project is a text saving and retrieval web app developed using Django. The app allows users to save short text snippets with a title, timestamp, and created user. Each snippet is associated with a tag, which is a simple model with only a title field. The app checks whether a tag with the same title exists before creating a new one and links the snippet to the existing tag if found. JWT authentication is implemented for user authentication.

GitHub Repository: [snippets](https://github.com/Dilnavas/snippets.git)

## Authentication API
1. **Login API**: Allows users to log in and obtain an access token for authentication.
2. **Refresh API**: Provides a refreshed access token when the current access token has expired.

## CRUD APIs
1. **Overview API**: Provides the total count of snippets and lists all available snippets with hyperlinks to their respective detail APIs.
2. **Create API**: Allows users to create and save a new snippet by providing the necessary information.
3. **Detail API**: Displays the title, content, and timestamp information of a specific snippet.
4. **Update API**: Enables users to update individual snippet items. Returns the updated item detail as a response.
5. **Delete API**: Deletes selected items and returns the list of remaining items as a response.
6. **Tag List API**: Lists all available tags.
7. **Tag Detail API**: Returns snippets linked to the selected tag.

## Setup and Usage
1. Clone the repository: `git clone https://github.com/Dilnavas/snippets.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the database and run migrations: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`
5. Access the web app in your browser at `http://localhost:8000/`

Please refer to the project repository for detailed documentation, code structure, and usage examples.

## Contributors
- [Dilnavas C P](https://github.com/Dilnavas) - Project Developer