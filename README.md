Lost & Found Portal

The Lost & Found Portal is a web-based application designed to help users report, search, and recover lost or found items efficiently. The platform allows users to post detailed item information with images, browse and filter listings, and connect with others to return belongings to their rightful owners. This project focuses on practical backend-driven web development using Flask, along with clean UI templates and structured database handling. It is built as a real-world CRUD-based system and is under active development.

Key Features

User authentication with registration and login using session-based security

Reporting lost and found items with title, description, category, location, date, and images

Search and filter functionality to quickly find relevant items

Image upload support for better item identification

Item status tracking (Lost → Found → Returned)

User dashboard to view and manage posted items

Contact flow between users to facilitate item recovery

Custom error handling pages (403, 404, 500) for improved user experience

Tech Stack

Backend: Python, Flask

Frontend: HTML5, CSS3, Bootstrap

Templating Engine: Jinja2

Database: SQLite (extendable to MySQL/PostgreSQL)

Authentication: Flask session management, Werkzeug security utilities

Project Structure

Lost-and-Found-Portal/
│
├── static/ # CSS, JavaScript, images, uploads
├── templates/ # HTML templates (auth, dashboard, items, errors)
├── instance/ # SQLite database (local)
├── app.py # Main Flask application
├── app_routes.py # Route definitions
├── models.py # Database models
├── forms.py # Form handling logic
├── utils.py # Utility/helper functions
├── requirements.txt # Project dependencies
├── .env.example # Environment variable template
└── README.md # Project documentation

How to Run Locally

Clone the repository
git clone https://github.com/ayushgupta7080/Lost-and-Found-Portal.git

cd Lost-and-Found-Portal

Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate (Windows)
source venv/bin/activate (Linux/Mac)

Install dependencies
pip install -r requirements.txt

Configure environment variables
Copy .env.example to .env and update values if required

Run the application
flask run

Open your browser at http://127.0.0.1:5000

Project Status

Under active development. Core functionality is implemented, and the project is being improved with bug fixes, feature enhancements, and deployment-ready configuration.

Planned Enhancements

Email notifications for matched lost and found items

Location-based search and map integration

Admin panel for moderation and management

Improved matching logic between lost and found items

Cloud deployment and live demo

Author

Ayush Gupta
B.Sc. IT | Backend & Full-Stack Development Enthusiast

This project was developed to demonstrate practical skills in Flask backend development, database integration, authentication, and real-world web application design.
