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

## API Endpoints

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