from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import joblib
import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor  # or your model type
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import csv

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Required for sessions
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Initially load models
model_line, product_line_columns = joblib.load("model_top_products.pkl")
model_product, product_name_columns = joblib.load("model_product_names.pkl")

# Load combo offers CSV if available
try:
    combo_df = pd.read_csv("combo_offers.csv")
except FileNotFoundError:
    combo_df = pd.DataFrame(columns=['antecedents', 'consequents'])

combo_offers = []
def parse_set_string(s):
    return set(item.strip().strip("'\"") for item in s.strip('{}').split(',')) if pd.notna(s) else set()

for _, row in combo_df.iterrows():
    antecedents = parse_set_string(row['antecedents']) if isinstance(row['antecedents'], str) else set()
    consequents = parse_set_string(row['consequents']) if isinstance(row['consequents'], str) else set()
    combo_offers.append({
        'antecedents': list(antecedents),
        'consequents': list(consequents)
    })

def generate_combo_offers(df):
    # If InvoiceNo not present, group by Month as a basket
    if 'InvoiceNo' not in df.columns:
        df = df.copy()
        df['InvoiceNo'] = df['Month'].astype(str)

    basket = (df.groupby(['InvoiceNo', 'ProductName'])['QuantitySold']
                .sum().unstack().reset_index().fillna(0).set_index('InvoiceNo'))
    basket = basket.applymap(lambda x: 1 if x > 0 else 0)
    frequent_itemsets = apriori(basket, min_support=0.05, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
    combos = rules[['antecedents', 'consequents']].dropna()
    combos.to_csv("combo_offers.csv", index=False)
    print(f"Combo offers generated: {len(combos)}")
    return combos

def retrain_models(filepath):
    global model_line, product_line_columns, model_product, product_name_columns, combo_offers

    df = pd.read_csv(filepath)

    # --- Fix Month column ---
    if df['Month'].dtype == object:
        df['Month'] = df['Month'].astype(str).str.replace("-", "")
    df['Month'] = df['Month'].astype(int)
    # ------------------------

    # --- Standardize column names ---
    rename_map = {}
    if 'Product line' in df.columns:
        rename_map['Product line'] = 'ProductLine'
    if 'Quantity' in df.columns:
        rename_map['Quantity'] = 'QuantitySold'
    df = df.rename(columns=rename_map)
    # ----------------------------------------------------

    # === Preprocessing and pivot table for product lines ===
    # Aggregate product line sales by month
    line_pivot = df.pivot_table(index='Month', columns='ProductLine', values='QuantitySold', aggfunc='sum', fill_value=0)

    # Prepare training data
    X_line = line_pivot.index.values.reshape(-1, 1)  # Month as feature
    y_line = line_pivot.values

    # Train model for product lines
    model_line = RandomForestRegressor(n_estimators=100, random_state=42)
    model_line.fit(X_line, y_line)
    product_line_columns = list(line_pivot.columns)

    # === Preprocessing and pivot table for product names ===
    # Aggregate product name sales by month
    product_pivot = df.pivot_table(index='Month', columns='ProductName', values='QuantitySold', aggfunc='sum', fill_value=0)

    X_product = product_pivot.index.values.reshape(-1, 1)
    y_product = product_pivot.values

    # Train model for individual products
    model_product = RandomForestRegressor(n_estimators=100, random_state=42)
    model_product.fit(X_product, y_product)
    product_name_columns = list(product_pivot.columns)

    # Save updated models
    joblib.dump((model_line, product_line_columns), "model_top_products.pkl")
    joblib.dump((model_product, product_name_columns), "model_product_names.pkl")

    # Generate and save new combo offers
    try:
        generate_combo_offers(df)
    except Exception as e:
        print("Combo offer generation failed:", e)

    # Reload combo_offers for the /combo endpoint
    try:
        combo_df = pd.read_csv("combo_offers.csv")
    except FileNotFoundError:
        combo_df = pd.DataFrame(columns=['antecedents', 'consequents'])

    combo_offers = []
    def parse_set_string(s):
        return set(item.strip().strip("'\"") for item in s.strip('{}').split(',')) if pd.notna(s) else set()
    for _, row in combo_df.iterrows():
        antecedents = parse_set_string(row['antecedents']) if isinstance(row['antecedents'], str) else set()
        consequents = parse_set_string(row['consequents']) if isinstance(row['consequents'], str) else set()
        combo_offers.append({
            'antecedents': list(antecedents),
            'consequents': list(consequents)
        })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('About.html')

@app.route('/features')
def features():
    return render_template('Features.html')

@app.route('/contact')
def contact():
    return render_template('Contact.html')

@app.route('/login')
def login():
    return render_template('Login.html')

@app.route('/customerdashboard')
def customerdashboard():
    return render_template('customerdashboard.html')

@app.route('/dashboard')
def dashboard():
    email = session.get("loginemail")
    if not email:
        return redirect(url_for('login'))
    combo_offer = None
    with open('combo_offers.csv', newline='', encoding='utf-8') as csvfile:
        reader = list(csv.DictReader(csvfile))
        if reader:
            last = reader[-1]
            combo_offer = {
                'antecedents': last['antecedents'].strip("{}'"),
                'consequents': last['consequents'].strip("{}'")
            }
    return render_template('dashboard.html', combo_offer=combo_offer, user_email=email)

@app.route('/report')
def report():
    return render_template('Report.html')

@app.route('/suppliers')
def suppliers():
    return render_template('Suppliers.html')

@app.route('/analytics')
def analytics():
    return render_template('Analytics.html')

@app.route('/notifi')
def notifi():
    return render_template('Notifi.html')

@app.route('/products')
def products():
    return render_template('Products.html')

@app.route('/customerproduct')
def customerproduct():
    return render_template('customerproduct.html')

from flask import session, render_template, redirect, url_for

@app.route('/profile')
def profile():
    email = session.get("loginemail")
    if not email:
        return redirect(url_for('login'))
    # Example: Fetch user details from your database or Firebase
    # Replace this with your actual data fetching logic
    user_details = {
        "email": email,
        "name": "John Doe",  # Replace with actual name from DB
        "about": "Welcome to your profile page!"
    }
    return render_template('Profile.html', user=user_details)

@app.route('/order')
def order():
    return render_template('Order.html')

@app.route("/predict", methods=["POST"])
def predict():
    global model_line, product_line_columns, model_product, product_name_columns
    # Always reload models from disk to get the latest after retrain
    model_line, product_line_columns = joblib.load("model_top_products.pkl")
    model_product, product_name_columns = joblib.load("model_product_names.pkl")

    data = request.get_json()
    year = int(data["year"])
    month = int(data["month"])

    # Combine year and month to match training format (e.g., 202401 for Jan 2024)
    if month < 10:
        month_str = f"0{month}"
    else:
        month_str = str(month)
    month_feature = int(f"{year}{month_str}")

    pred_line = model_line.predict([[month_feature]])[0]
    pred_product = model_product.predict([[month_feature]])[0]

    product_line_preds = {col: int(val) for col, val in zip(product_line_columns, pred_line)}
    product_name_preds = {col: int(val) for col, val in zip(product_name_columns, pred_product)}

    return jsonify({
        "product_lines": product_line_preds,
        "product_names": product_name_preds
    })


@app.route("/upload_dataset", methods=["POST"])
def upload_dataset():
    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400
    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        retrain_models(filepath)
    except Exception as e:
        return jsonify({"error": f"Retrain failed: {str(e)}"}), 500

    return jsonify({"message": "Dataset uploaded and models retrained successfully."})

@app.route("/combo")
def combo():
    # Always reload the latest combo offers from CSV
    try:
        combo_df = pd.read_csv("combo_offers.csv")
    except FileNotFoundError:
        combo_df = pd.DataFrame(columns=['antecedents', 'consequents'])

    def parse_set_string(s):
        return set(item.strip().strip("'\"") for item in s.strip('{}').split(',')) if pd.notna(s) else set()

    combo_offers = []
    for _, row in combo_df.iterrows():
        antecedents = parse_set_string(row['antecedents']) if isinstance(row['antecedents'], str) else set()
        consequents = parse_set_string(row['consequents']) if isinstance(row['consequents'], str) else set()
        combo_offers.append({
            'antecedents': list(antecedents),
            'consequents': list(consequents)
        })
    return jsonify(combo_offers)

@app.route("/set_session", methods=["POST"])
def set_session():
    data = request.get_json()
    email = data.get("email")
    if email:
        session["loginemail"] = email
        return jsonify({"success": True})
    return jsonify({"success": False}), 400

if __name__ == "__main__":
    app.run(debug=True)
