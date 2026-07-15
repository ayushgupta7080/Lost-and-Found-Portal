# Lost & Found Portal

The **Lost & Found Portal** is a web-based application built to help users report, search, and recover lost or found items efficiently. The platform enables users to post item details with images, browse and filter listings, and connect with others to return belongings to their rightful owners.

This project focuses on **backend-driven web development** using Flask, while also implementing clean UI templates and basic authentication. It is designed as a **real-world CRUD-based system** and is under active improvement.

---

## 🔍 Key Features

- **User Authentication**
  - User registration and login system
  - Session-based authentication

- **Lost & Found Item Reporting**
  - Create posts for lost or found items
  - Add item details such as title, description, category, location, date, and images

- **Search & Filtering**
  - Search items using keywords
  - Filter results based on category and status

- **Image Upload Support**
  - Upload images to help identify items easily

- **Item Status Tracking**
  - Track item lifecycle (Lost → Found → Returned)

- **User Dashboard**
  - View and manage items posted by the logged-in user

- **Contact & Matching Flow**
  - Enables communication between users to recover items

- **Error Handling Pages**
  - Custom 403, 404, and 500 error pages for better UX

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **Templating Engine:** Jinja2  
- **Database:** SQLite (can be extended to MySQL/PostgreSQL)  
- **Authentication:** Flask session management, Werkzeug security utilities  

---

## 📁 Project Structure

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


---

## 🚀 How to Run Locally

1. **Clone the repository**

git clone https://github.com/ayushgupta7080/Lost-and-Found-Portal.git
cd Lost-and-Found-Portal

2. **Create and activate a virtual environment**
   
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac

3. Install dependencies
   
pip install -r requirements.txt

4. Set environment variables
   
  Copy .env.example to .env

  Update values if required

5. Run the application
flask run

Open your browser at:
👉 http://127.0.0.1:5000

📌 Project Status

🚧 Under Active Development

Core functionality is implemented. Planned improvements include bug fixes, feature enhancements, and deployment-ready configuration.

🔮 Planned Enhancements

Email notifications for matched lost/found items

Location-based search using maps

Admin panel for moderation

Improved matching logic between lost and found items

Deployment on a cloud platform (Render / PythonAnywhere)

👨‍💻 Author

Ayush Gupta
B.Sc. IT | Backend & Full-Stack Development Enthusiast

This project was developed to demonstrate practical skills in Flask backend development, database handling, authentication, and real-world web application design.


---

## ✅ Why this README works for recruiters

- Honest (no overclaiming)
- Clear backend focus
- Real-world problem statement
- Shows learning & iteration mindset
- Professional structure
- Easy to run locally
- Signals readiness for deployment

If you want, next I can:
- 🔹 Optimize this for **deployment README**
- 🔹 Add **screenshots section text**
- 🔹 Prepare a **2-minute interview explanation**
- 🔹 Help you deploy it live

Just tell me what you want to do next 👍
