# 🩺 Diabetes Prediction System

> An AI-powered web application that predicts diabetes risk based on real medical data — built with Django and Machine Learning.

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![Django](https://img.shields.io/badge/Django-6.0.3-green.svg)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.8.0-orange.svg)
![Status](https://img.shields.io/badge/Status-Live-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)

---

## 🧠 What Is This Project?

Diabetes is one of the most common chronic diseases worldwide — and early detection can be life-saving.

This web application takes **8 basic health measurements** as input (like glucose level, BMI, and age) and uses a **trained Machine Learning model** to instantly predict whether a person is at risk of diabetes.

It was built as an academic project to demonstrate how data science and web development can work together to solve real-world health problems.

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🤖 ML-Powered Prediction | Trained Scikit-Learn model analyzes 8 health metrics to assess diabetes risk |
| 🎨 Glassmorphism UI | Modern frosted-glass design with a clean two-column form layout |
| 📱 Fully Responsive | Works seamlessly on desktop, tablet, and mobile |
| 💡 Beginner-Friendly Form | Each medical term includes a plain-English description so anyone can use it |
| ⚡ Instant Results | Color-coded risk feedback displayed immediately after submission |

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Backend** | Django (Python) | Handles routing, logic, and ML model integration |
| **Frontend** | HTML5, CSS3, Bootstrap | Builds the responsive, styled user interface |
| **Machine Learning** | Scikit-Learn, Pandas, NumPy | Trains and runs the diabetes prediction model |
| **Deployment** | Render + GitHub | Hosts the live application |

---

## 📸 Interface Preview

<img width="1919" height="911" alt="image" src="https://github.com/user-attachments/assets/128a85c8-92ea-45a5-83dc-a425cb5cbcf3" />
<img width="1919" height="910" alt="image" src="https://github.com/user-attachments/assets/7f6621b5-f7e4-4f19-b3a3-bee3844a77ec" />



---

## 📋 How the Prediction Works

The ML model was trained on the **Pima Indians Diabetes Dataset** and evaluates risk based on these 8 medical inputs:

| # | Input Field | What It Means |
|---|-------------|---------------|
| 1 | **Pregnancies** | How many times the patient has been pregnant |
| 2 | **Glucose** | Blood sugar level measured 2 hours after a glucose test |
| 3 | **Blood Pressure** | Diastolic (resting) blood pressure in mm Hg |
| 4 | **Skin Thickness** | Fat layer thickness measured at the tricep in mm |
| 5 | **Insulin** | Amount of insulin in blood 2 hours after the glucose test |
| 6 | **BMI** | Body Mass Index — a ratio of weight to height squared |
| 7 | **Diabetes Pedigree Function** | A score that reflects genetic/family history of diabetes |
| 8 | **Age** | Patient's age in years |

> **How it works under the hood:** The values are passed to a pre-trained classification model (e.g. Random Forest / Logistic Regression), which outputs either **Diabetic** or **Non-Diabetic** along with a confidence level.

---

## ⚙️ Local Setup — Step by Step

Follow these steps to run the project on your own machine.

### Prerequisites
- Python 3.10 or higher installed
- `pip` package manager
- Git

---

### Step 1 — Clone the Repository
```bash
git clone https://github.com/faysalmahmudprem/Diabetes-Prediction.git
cd Diabetes-Prediction
```

### Step 2 — Create a Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.
```bash
python -m venv venv
```

Then activate it:
```bash
# On Windows
.\venv\Scripts\activate

# On macOS / Linux
source venv/bin/activate
```

> ✅ You'll know it's active when you see `(venv)` at the start of your terminal line.

### Step 3 — Install Dependencies
```bash
pip install -r requirements.txt
```

This installs Django, Scikit-Learn, Pandas, and all other required packages at once.

### Step 4 — Apply Database Migrations
```bash
python manage.py migrate
```

This sets up the local SQLite database Django needs to function.

### Step 5 — Run the Development Server
```bash
python manage.py runserver
```

Now open your browser and go to:
```
http://127.0.0.1:8000/
```

You should see the prediction form ready to use. 🎉

---

## 📁 Project Structure
```
Diabetes-Prediction/
│
├── predictor/              # Core Django app
│   ├── views.py            # Handles form input and prediction logic
│   ├── models.py           # Django data models
│   └── templates/          # HTML templates for the UI
│
├── ml_model/               # Trained ML model file (.pkl)
├── static/                 # CSS, JS, and image assets
├── requirements.txt        # All Python dependencies
└── manage.py               # Django project entry point
```

> ⚠️ *Folder names may vary slightly — update this section to match your actual structure.*

---

## 🔮 Future Plans

The current version is a working proof of concept. Here's what's planned for future iterations:

### 🧬 Model Improvements
- [ ] Experiment with ensemble methods (XGBoost, Random Forest tuning) to push accuracy above 85%
- [ ] Add confidence percentage to results (e.g. "72% likelihood of diabetes")
- [ ] Display which input factors contributed most to the prediction (feature importance)
- [ ] Retrain on larger, more diverse datasets to reduce bias

### 🌐 Feature Additions
- [ ] User authentication — save and track prediction history over time
- [ ] PDF report generation — download a summary of your health inputs and result
- [ ] Multi-disease support — extend to heart disease and hypertension prediction
- [ ] Doctor referral suggestions based on risk level

### 🎨 UI/UX Enhancements
- [ ] Dark mode toggle
- [ ] Interactive input sliders instead of plain text fields
- [ ] Animated result reveal with risk gauge visualization
- [ ] Bangla language support for wider accessibility in Bangladesh

### ☁️ DevOps & Deployment
- [ ] Dockerize the application for easier deployment
- [ ] Set up CI/CD pipeline via GitHub Actions
- [ ] Migrate from SQLite to PostgreSQL for production

---

## 🤝 Contributing

Contributions, suggestions, and feedback are always welcome — whether you're a developer, data scientist, or just someone passionate about healthcare tech.

### How to Contribute

**1. Fork the repository**

Click the `Fork` button at the top right of this page.

**2. Clone your fork**
```bash
git clone https://github.com/YOUR_USERNAME/Diabetes-Prediction.git
cd Diabetes-Prediction
```

**3. Create a new branch**
```bash
git checkout -b feature/your-feature-name
```

> Use descriptive branch names like `feature/add-dark-mode` or `fix/form-validation-bug`

**4. Make your changes and commit**
```bash
git add .
git commit -m "feat: add dark mode toggle to UI"
```

**5. Push and open a Pull Request**
```bash
git push origin feature/your-feature-name
```

Then go to GitHub and open a Pull Request against the `main` branch. Describe what you changed and why.

---

### 💡 Ideas for Contribution

- Improve model accuracy or try a different algorithm
- Add unit tests for the prediction logic
- Translate the UI into Bengali
- Write a blog post or tutorial about this project
- Report bugs or suggest features via [GitHub Issues](https://github.com/faysalmahmudprem/Diabetes-Prediction/issues)

---

### Code Style Guidelines

- Follow **PEP 8** for Python code
- Keep commits small and focused — one change per commit
- Write clear commit messages using the format: `type: short description`
  - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`

---

## 📄 License

This project is licensed under the **MIT License** — meaning you're free to use, modify, and distribute it, as long as you include the original license.

See the [LICENSE](./LICENSE) file for full details.

---

## 🛡️ Disclaimer

This tool is built **strictly for educational and demonstration purposes.**

It is **not** a medical device and should **never** be used to replace professional diagnosis. If you have concerns about diabetes or any health condition, please consult a licensed healthcare provider.

---

## 👤 Author

**Faysal Mahmud Prem**
(CSE Graduate | Software Engineer | ML Enthusiast)

- 🌐 Portfolio: [faysalmahmudprem.com](https://faysalmahmudprem.netlify.com)
- 💻 GitHub: [@faysalmahmudprem](https://github.com/faysalmahmudprem)
---

*Developed with ❤️ as part of a CSE academic project — combining healthcare awareness with modern web technology.*
