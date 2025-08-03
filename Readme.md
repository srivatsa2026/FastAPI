# FastAPI Social Media Backend

A robust, high-performance backend API for social media applications built with FastAPI and Python. This project provides a comprehensive set of endpoints for user management, posts, interactions, and real-time features essential for modern social media platforms.

## 🚀 Features

- **User Authentication & Authorization**: JWT-based authentication with role-based access control
- **User Management**: Registration, login, profile management, and user relationships
- **Post Management**: Create, read, update, delete posts with media support
- **Social Interactions**: Like, comment, share, and bookmark functionality

## 🛠️ Tech Stack

- **Framework**: FastAPI
- **Language**: Python 3.8+
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT tokens with bcrypt password hashing

## 📋 Prerequisites

Before running this application, make sure you have the following installed:

- Python 3.8 or higher
- PostgreSQL
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
   source venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   DATABASE_HOSTNAME=your_host_name
   DATABASE_PORT=your_port_number
   DATABASE_PASSWORD=your_database_password
   DATABASE_NAME=your_database_name
   DATABASE_USERNAME=your_database_username
   SECRET_KEY=your_secret_key
   ALGORITHM=your_algorithm
   ACCESS_TOKEN_EXPIRE_MINUTES=token_expiraton_in_minutes
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


### Posts
- `GET /posts` - Get all posts (with pagination)
- `POST /posts` - Create a new post
- `GET /posts/{post_id}` - Get specific post
- `PUT /posts/{post_id}` - Update post
- `DELETE /posts/{post_id}` - Delete post


## 📊 Database Schema

The application uses the following main models:

- **User**: User profiles and authentication
- **Post**: User posts and content
- **Comment**: Comments on posts
- **Like**: Post and comment likes

## 🔒 Security Features

- JWT token-based authentication
- Password hashing with bcrypt
- Rate limiting on sensitive endpoints
- Input validation and sanitization
- CORS configuration
- SQL injection prevention through ORM

## 🚀 Performance Optimizations

- Database query optimization with proper indexing
- Asynchronous request handling
- Connection pooling
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

---

⭐ If you found this project helpful, please give it a star on GitHub!