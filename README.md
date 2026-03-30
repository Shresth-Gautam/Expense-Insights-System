# 💰 Expense Tracking System

A full-stack Expense Tracking System built using **FastAPI**, **MySQL**, and **Streamlit** that allows users to manage daily expenses and visualize spending patterns.

---

## 🚀 Features

* 📅 Add and update daily expenses
* 📊 View analytics and category-wise breakdown
* 💾 Persistent storage using MySQL
* ⚡ Fast backend powered by FastAPI
* 🎨 Interactive frontend using Streamlit

---

## 🏗️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** MySQL
* **Language:** Python

---

## 📂 Project Structure

```
5_project_two_expense_management/
│
├── backend/
│   ├── server.py
│   ├── db_helper.py
│   └── logging_setup.py
│
├── frontend/
│   ├── app.py
│   ├── add_update_ui.py
│   └── analytics_ui.py
│
├── tests/
│   └── backend/
│       └── test_db_helper.py
│
├── expense_db_creation.sql
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

---

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn streamlit mysql-connector-python pandas requests
```

---

### 4️⃣ Setup Database

* Open MySQL
* Run the SQL file:

```sql
expense_db_creation.sql
```

---

### 5️⃣ Run Backend Server

```bash
uvicorn backend.server:app --reload
```

👉 API will be available at:

```
http://localhost:8000
```

👉 Swagger Docs:

```
http://localhost:8000/docs
```

---

### 6️⃣ Run Frontend

```bash
streamlit run frontend/app.py
```

👉 App will open at:

```
http://localhost:8501
```

---

## 📊 API Endpoints

| Method | Endpoint         | Description               |
| ------ | ---------------- | ------------------------- |
| GET    | /expenses/{date} | Fetch expenses for a date |
| POST   | /expenses/{date} | Add/Update expenses       |
| POST   | /analytics/      | Get expense summary       |

---

## 🧪 Running Tests

```bash
pytest tests
```

---

## 📌 Sample Output

* Add/Update expenses via UI
* Visual analytics using bar charts
* Category-wise percentage breakdown

---

## 🔮 Future Enhancements

* 🔐 User authentication
* ☁️ Cloud deployment (AWS/Render)
* 📱 Mobile-friendly UI
* 📈 Advanced analytics dashboard

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📧 Contact

**Shresth Gautam**
Aspiring Data Analyst | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
