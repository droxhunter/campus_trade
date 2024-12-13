# campus_trade
A smart campus second-hand trading program
1. System Architecture
The application will have the following components:

Frontend:
Web-based interface using frameworks like Flask (for simplicity).
Backend:
Handles authentication, product management, messaging, and administrative controls.
Database:
Stores user details, product data, messages, and evaluations (SQLite for simplicity).
Payment Integration:
WeChat Pay API integration for secure transactions.
2. Functional Modules
Each feature will be developed as an independent module for scalability:

2.1. User Registration and Login
Features:
Register with details (school, student number, etc.).
Login with credentials.
Password hashing for security.
Tools: Flask-Login, SQLAlchemy.
2.2. Product Listing
Features:
Sellers upload item details (name, description, images, price, quality).
Implementation:
Use file upload capabilities in Flask.
Store image files in a directory and their paths in the database.
2.3. Product Browsing and Search
Features:
View products by category, keyword search.
Implementation:
Full-text search using SQLAlchemy or a library like Elasticsearch for advanced capabilities.
2.4. Messaging System
Features:
Real-time chat between buyers and sellers.
Implementation:
Use Flask-SocketIO for WebSocket-based real-time messaging.
2.5. Evaluation System
Features:
Buyers leave feedback after purchase.
Feedback impacts seller reputation.
Implementation:
Create a feedback table linked to transactions and products.
2.6. Payment Integration
Features:
Secure payment via WeChat Pay.
Implementation:
Use WeChat Pay SDK for Python to process payments securely.
2.7. Personal Center
Features:
Users view posted items, purchase records, and messages.
Implementation:
Queries to fetch user-specific data from the database.
2.8. Campus Circle
Features:
Forum-style posts for topics, help requests, etc.
Implementation:
Create a posts table with upvote and comment functionality.
2.9. Administrator Functions
Features:
Product moderation, handling disputes.
Implementation:
Admin panel with privileged access.
