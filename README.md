# SocialSite Django Project

This is a Django project named SocialSite that implements various API endpoints for a social networking platform.

![image](https://github.com/Chityanj/ssocialsite/assets/20499500/487dc7ec-6556-4155-8fe0-5d3e92b1cc03)

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

- Python 3.9 or later
- pip
- Docker (optional, for running with Docker)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/socialsite.git
   cd socialsite

2. Create and activate a virtual environment (recommended):

```
python -m venv venv
source venv/bin/activate
```

3. Install project dependencies:

```
pip install -r requirements.txt
```


5. Apply database migrations:

```
python manage.py makemigrations
python manage.py migrate
```

## Run Locally
1. Start the development server:

```
python manage.py runserver
```

Access the API endpoints at http://localhost:8000/api/

## Run with Docker
1. Build the Docker image:

```
docker build -t socialsite .
```

2. Run the Docker container:

```
docker run -p 8000:8000 -d socialsite
```
Access the API endpoints at http://localhost:8000/api/

## Run Tests
Run the Django test cases:

```
python manage.py test
```

## API Endpoints and Curls

1. Get User Profile:
```bash

curl -X GET http://localhost:8000/api/user/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
2. Follow User:
```bash
curl -X POST http://localhost:8000/api/follow/<USER_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```


3. Unfollow User:
```bash

curl -X POST http://localhost:8000/api/unfollow/<USER_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
4. Create Post:
```bash

curl -X POST http://localhost:8000/api/posts/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>" -d "title=New Post&description=This is a new post."
```
5. Delete Post:
```bash
curl -X DELETE http://localhost:8000/api/posts/<POST_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
6. Authenticate
```bash
curl -X POST http://localhost:8000/api/authenticate/ -d "email=user@example.com&password=yourpassword"

```

7. Like Post:
```bash

curl -X POST http://localhost:8000/api/like/<POST_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
8. Unlike Post:
```bash

curl -X POST http://localhost:8000/api/unlike/<POST_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
9. Add Comment to Post:

```bash

curl -X POST http://localhost:8000/api/comment/<POST_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>" -d "comment=This is a comment."
```
10. Get Single Post with Likes and Comments:
```bash

curl -X GET http://localhost:8000/api/posts/<POST_ID>/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
11. Get All Posts:
```bash

curl -X GET http://localhost:8000/api/all_posts/ -H "Authorization: Bearer <YOUR_JWT_TOKEN>"
```
Remember to replace <YOUR_JWT_TOKEN> with a valid JWT token and <USER_ID

```
POST /api/authenticate: User authentication and JWT token generation.
POST /api/follow/{id}: Follow a user by authenticated user.
POST /api/unfollow/{id}: Unfollow a user by authenticated user.
GET /api/user: Get user profile details by authenticated user.
POST /api/posts/: Add a new post by authenticated user.
DELETE /api/posts/{id}: Delete a post by authenticated user.
POST /api/like/{id}: Like a post by authenticated user.
POST /api/unlike/{id}: Unlike a post by authenticated user.
POST /api/comment/{id}: Add a comment for a post by authenticated user.
GET /api/posts/{id}: Get details of a single post with likes and comments.
GET /api/all_posts: Get all posts by authenticated user sorted by post time.
```