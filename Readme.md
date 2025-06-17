# FastAPI Social Media Backend

A robust, high-performance backend API for social media applications built with FastAPI and Python. This project provides a comprehensive set of endpoints for user management, posts, interactions, and real-time features essential for modern social media platforms.

## 🚀 Features

- **User Authentication & Authorization**: JWT-based authentication with role-based access control
- **User Management**: Registration, login, profile management, and user relationships
- **Post Management**: Create, read, update, delete posts with media support
- **Social Interactions**: Like, comment, share, and bookmark functionality
- **Follow System**: Follow/unfollow users with follower/following lists
- **Real-time Features**: WebSocket support for live notifications and messaging
- **Media Handling**: Image and video upload with cloud storage integration
- **Feed Algorithm**: Personalized timeline and discovery feeds
- **Search & Discovery**: Advanced search for users, posts, and hashtags
- **Analytics**: User engagement metrics and content analytics
- **Rate Limiting**: API rate limiting for security and performance
- **Comprehensive API Documentation**: Auto-generated OpenAPI documentation

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with bcrypt password hashing
- **File Storage**: AWS S3 / CloudStorage
- **Caching**: Redis for session management and caching
- **Documentation**: Automatic OpenAPI/Swagger documentation
- **Testing**: Pytest with comprehensive test coverage
- **Deployment**: Docker containerization ready

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL
- Redis (optional, for caching)
- pip or pipenv for package management

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/srivatsa2026/FastAPI.git
   cd FastAPI
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://username:password@localhost/socialmedia_db
   SECRET_KEY=your-secret-key-here
   JWT_SECRET=your-jwt-secret-here
   REDIS_URL=redis://localhost:6379
   AWS_ACCESS_KEY_ID=your-aws-access-key
   AWS_SECRET_ACCESS_KEY=your-aws-secret-key
   AWS_S3_BUCKET=your-s3-bucket-name
   ```

5. **Set up the database**
   ```bash
   # Create database tables
   python -m alembic upgrade head
   ```

6. **Run the application**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The API will be available at `http://localhost:8000`

## 📚 API Documentation

Once the server is running, you can access:

- **Interactive API Documentation (Swagger UI)**: http://localhost:8000/docs
- **Alternative API Documentation (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI JSON Schema**: http://localhost:8000/openapi.json

## 🌐 API Endpoints

### Authentication
- `POST /auth/register` - User registration
- `POST /auth/login` - User login
- `POST /auth/refresh` - Refresh JWT token
- `POST /auth/logout` - User logout

### Users
- `GET /users/me` - Get current user profile
- `PUT /users/me` - Update current user profile
- `GET /users/{user_id}` - Get user profile by ID
- `POST /users/{user_id}/follow` - Follow a user
- `DELETE /users/{user_id}/follow` - Unfollow a user
- `GET /users/{user_id}/followers` - Get user followers
- `GET /users/{user_id}/following` - Get users being followed

### Posts
- `GET /posts` - Get all posts (with pagination)
- `POST /posts` - Create a new post
- `GET /posts/{post_id}` - Get specific post
- `PUT /posts/{post_id}` - Update post
- `DELETE /posts/{post_id}` - Delete post
- `POST /posts/{post_id}/like` - Like a post
- `DELETE /posts/{post_id}/like` - Unlike a post
- `GET /posts/{post_id}/comments` - Get post comments
- `POST /posts/{post_id}/comments` - Add comment to post

### Feed
- `GET /feed/timeline` - Get personalized timeline
- `GET /feed/discover` - Get discover feed
- `GET /feed/trending` - Get trending posts

### Media
- `POST /media/upload` - Upload media files
- `GET /media/{media_id}` - Get media file

### Search
- `GET /search/users` - Search users
- `GET /search/posts` - Search posts
- `GET /search/hashtags` - Search hashtags

## 🐳 Docker Deployment

1. **Build the Docker image**
   ```bash
   docker build -t fastapi-social-media .
   ```

2. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

This will start the FastAPI application along with PostgreSQL and Redis services.

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_users.py
```

## 📊 Database Schema

The application uses the following main models:

- **User**: User profiles and authentication
- **Post**: User posts and content
- **Comment**: Comments on posts
- **Like**: Post and comment likes
- **Follow**: User follow relationships
- **Media**: File attachments and media
- **Notification**: User notifications

## 🔒 Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- Rate limiting on sensitive endpoints
- Input validation and sanitization
- CORS configuration
- SQL injection prevention through ORM
- XSS protection

## 🚀 Performance Optimizations

- Database query optimization with proper indexing
- Redis caching for frequently accessed data
- Asynchronous request handling
- Connection pooling
- Image compression and optimization
- Pagination for large datasets

## 📈 Monitoring & Logging

- Structured logging with Python logging
- Request/response logging
- Error tracking and monitoring
- Performance metrics collection
- Health check endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please make sure to:
- Follow the existing code style
- Add tests for new features
- Update documentation as needed
- Ensure all tests pass


## 👨‍💻 Author

**Srivatsa**
- GitHub: [@srivatsa2026](https://github.com/srivatsa2026)

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) for the amazing framework
- [SQLAlchemy](https://www.sqlalchemy.org/) for the powerful ORM
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation
- The Python community for excellent libraries and tools

## 📞 Support

If you have any questions or need help with setup, please:
1. Check the [documentation](http://localhost:8000/docs)
2. Search through existing [issues](https://github.com/srivatsa2026/FastAPI/issues)
3. Create a new issue if needed

---

⭐ If you found this project helpful, please give it a star on GitHub!