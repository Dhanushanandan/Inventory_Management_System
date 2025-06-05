Inventory Management System
An AI-powered Inventory Management System designed to streamline product tracking with Augmented Reality (AR) support, sales analysis, and inventory optimization. This application leverages machine learning models to provide insights into top-selling products and manage combo offers effectively.

🚀 Features
🔐 Firebase Authentication – Secure login system.

📦 Inventory Management – Add, update, delete products in real-time.

📈 Sales Forecasting – ML-based predictions for top-selling products and stock quantity needs.

🤝 Combo Offers – AI-generated offers using least- and best-selling product data.

📊 Analytics Dashboard – Visualize demand trends and product performance.

📧 Supplier Alerts – Low stock notifications and email alerts.

🧑‍💻 Admin Interface – Manage inventory, sales, and supplier data.

📱 Customer AR View – Scan AR marker (.patt file) to view product details in 3D AR

🔍 AR Feature for Customers
Customers can scan a special .patt marker using their mobile devices to view product details through Augmented Reality.

How it Works
Customer scans marker (.patt file) using their device camera.

AR interface loads the product data from Firebase in real time.

Product details are displayed in 3D, including image, price, and quantity.

AR Supported Tech:

AR.js

A-Frame



Technologies Used
Backend: Python, Flask

Frontend: HTML, CSS, JavaScript

Machine Learning: scikit-learn, pandas

Database: Firebase

Others: Jupyter Notebook for model training

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Dhanushanandan/Inventory_Management_System.git
cd Inventory_Management_System
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Set up Firebase:

Place your serviceAccountKey.json file in the project root.

Ensure firebase.json and .firebaserc are configured correctly.

Run the application:

bash
Copy
Edit
python app.py
Access the application at http://localhost:5000.

Project Structure
plaintext
Copy
Edit
Inventory_Management_System/
├── AR_Inventory_Viewer/         # Frontend templates and static files
├── static/                      # Static assets (CSS, JS, images)
├── templates/                   # HTML templates
├── uploads/                     # Uploaded files
├── model_training.ipynb         # Jupyter Notebook for training ML models
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

🧪 Setup Instructions
Clone the Repo

bash
Copy
Edit
git clone https://github.com/Dhanushanandan/Inventory_Management_System.git
cd Inventory_Management_System
Install Backend Dependencies

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # or venv\Scripts\activate (Windows)
pip install -r requirements.txt
Add Firebase Credentials

Place serviceAccountKey.json in the root directory.

Run the Flask App

bash
Copy
Edit
python app.py
Visit http://localhost:5000

📸 Using the AR Feature
Open AR_Inventory_Viewer/index.html in a WebXR-compatible browser.

Allow camera access.

Hold the .patt marker in front of your camera.

Product information will appear in AR.

📧 Notifications
When product quantity ≤ 10:

Entry is added to Notifications node in Firebase.

Supplier email is automatically triggered via Firebase Cloud Functions.



Usage
Access Dashboard: Navigate to the homepage to view inventory statistics.

Manage Products: Add or update product details through the admin panel.

Analyze Sales: Use the analytics section to view top-selling products and combo offer performance.

Upload Data: Import inventory data using the provided Excel template.
