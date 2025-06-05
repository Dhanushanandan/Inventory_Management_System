# Inventory Management System 🛠️
An AI-powered Inventory Management System designed to streamline product tracking with Augmented Reality (AR) support, sales analysis, and inventory optimization. This application leverages machine learning to provide insights into top-selling products and manage combo offers effectively.
📋 Table of Contents

Overview
Features
Technologies
Project Structure
Installation
AR Feature
Notifications
Usage
Contributing
License

🌟 Overview
The Inventory Management System is a modern ERP solution that combines real-time inventory tracking, AI-driven sales forecasting, and AR-based product visualization. Built with Flask and Angular, it integrates Firebase for data storage and authentication, offering a seamless experience for admins and customers.
✨ Features

🔐 Firebase Authentication: Secure login system for admins and users.
📦 Inventory Management: Real-time CRUD operations for products.
📈 Sales Forecasting: ML-based predictions for top-selling products and stock needs.
🤝 Combo Offers: AI-generated offers combining least- and best-selling products.
📊 Analytics Dashboard: Visualize demand trends and product performance.
📧 Supplier Alerts: Automatic notifications for low stock (≤10 units).
🧑‍💻 Admin Interface: Manage inventory, sales, and supplier data.
📱 Customer AR View: Scan AR markers (.patt files) to view product details in 3D.

🛠️ Technologies

Backend: Python, Flask
Frontend: HTML, CSS, JavaScript, AR.js, A-Frame
Machine Learning: scikit-learn, pandas
Database: Firebase
Other: Jupyter Notebook for model training

📂 Project Structure
Inventory_Management_System/
├── AR_Inventory_Viewer/         # Frontend templates and static files
├── static/                      # CSS, JS, images
├── templates/                   # HTML templates
├── uploads/                     # Uploaded files
├── model_training.ipynb         # Jupyter Notebook for ML model training
├── model_product_names.pkl      # Serialized model for product names
├── model_top_products.pkl       # Serialized model for top products
├── combo_offers.csv             # Data for combo offers
├── InventoryData.xlsx           # Inventory data in Excel format
├── app.py                       # Main Flask application
├── requirements.txt             # Python dependencies
├── firebase.json                # Firebase configuration
├── .firebaserc                  # Firebase project settings
├── serviceAccountKey.json       # Firebase service account key
└── README.md                    # Project documentation

🛠️ Installation
Follow these steps to set up the project locally:

Clone the Repository:
git clone https://github.com/Dhanushanandan/Inventory_Management_System.git
cd Inventory_Management_System


Create a Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Set Up Firebase:

Place your serviceAccountKey.json file in the project root.
Ensure firebase.json and .firebaserc are configured correctly.


Run the Application:
python app.py


Access the application at http://localhost:5000.



📱 AR Feature
The AR feature allows customers to view product details in 3D by scanning a .patt marker:

Open AR_Inventory_Viewer/index.html in a WebXR-compatible browser.
Allow camera access.
Hold the .patt marker in front of the camera.
View real-time product details (image, price, quantity) loaded from Firebase in an AR interface.

Supported Technologies:

AR.js: Lightweight AR framework.
A-Frame: Web framework for building 3D/AR experiences.

📧 Notifications

Low Stock Alerts: When a product’s quantity falls to ≤10:
An entry is added to the Notifications node in Firebase.
An email is automatically sent to suppliers via Firebase Cloud Functions.



🚀 Usage

Access Dashboard: Visit http://localhost:5000 to view inventory statistics.
Manage Products: Use the admin panel to add, update, or delete product details.
Analyze Sales: Explore the analytics section for insights on top-selling products and combo offer performance.
Upload Data: Import inventory data using the provided InventoryData.xlsx template.

