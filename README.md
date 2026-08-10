# 🚨 Network Intrusion Detection System (NIDS)

A Machine Learning-based Network Intrusion Detection System with an interactive Streamlit cybersecurity dashboard.

## 📌 Project Overview

This project is designed to detect potentially malicious network traffic using a machine learning model.

The system allows a user to upload network traffic data in CSV format and analyzes the traffic to classify records as either:

- 🚨 **Attack**
- ✅ **Normal**

The results are displayed through an interactive cybersecurity dashboard built with Streamlit.

## ✨ Features

- 📂 Upload network traffic data in CSV format
- 🤖 Machine learning-based intrusion detection
- 🎚️ Adjustable detection sensitivity threshold
- 📊 Live traffic monitoring visualization
- 🚨 Attack count tracking
- ✅ Normal traffic count tracking
- 💻 Live activity feed
- 📈 Interactive charts using Plotly
- 🖥️ Cybersecurity-themed Streamlit dashboard

## 🛠️ Technologies Used

- **Python**
- **Pandas**
- **Scikit-learn**
- **Joblib**
- **Streamlit**
- **Plotly**
- **Jupyter Notebook**

## 📂 Project Structure

```text
NIDS_PROJECT/
│
├── notebooks/
│   └── Project notebooks and experimentation
│
├── app.py
│   └── Streamlit dashboard
│
├── nids_pipeline.py
│   └── NIDS machine learning pipeline
│
├── model.pkl
│   └── Trained machine learning model
│
├── .gitignore
│
└── README.md
```

## ⚙️ How It Works

The system follows the following workflow:

```text
Network Traffic CSV
        │
        ▼
   Data Upload
        │
        ▼
 Feature Selection
        │
        ▼
 Machine Learning Model
        │
        ▼
 Threat Probability
        │
        ▼
 Detection Threshold
        │
        ├───────────────┐
        ▼               ▼
     NORMAL           ATTACK
        │               │
        └───────┬───────┘
                ▼
       Streamlit Dashboard
```

The application loads the trained model and its required features, processes the uploaded network traffic data, and calculates a threat probability for each record.

A configurable detection threshold is then used to determine whether the traffic should be classified as normal or an attack.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/raopriyanshu90/NIDS_PROJECT.git
```

Move into the project directory:

```bash
cd NIDS_PROJECT
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install streamlit pandas joblib plotly scikit-learn
```

## ▶️ Running the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

Upload a network traffic CSV file through the dashboard to begin the analysis.

## 🎚️ Detection Sensitivity

The dashboard provides a **Detection Sensitivity** slider.

The threshold determines how the model's predicted probability is interpreted.

A lower threshold makes the detector more sensitive to potential attacks, while a higher threshold requires stronger model confidence before classifying traffic as an attack.

## 📊 Dashboard

The dashboard provides:

- Attack count
- Normal traffic count
- Live traffic monitoring graph
- Network traffic data preview
- Live activity feed
- Threat scores for detected attacks

## 🤖 Machine Learning Model

The application uses a trained machine learning model stored in `model.pkl`.

The model file contains:

- The trained model
- The feature list required by the model

The application loads these components using Joblib before performing predictions.

## 📁 Dataset

The application expects network traffic data in CSV format.

The uploaded dataset must contain the features required by the trained machine learning model.

## 🔮 Future Improvements

Possible future improvements include:

- Real-time packet capture
- Support for additional attack types
- Improved model accuracy
- Model performance evaluation
- Confusion matrix and classification reports
- Automated model retraining
- Real-time network monitoring
- Database integration
- User authentication
- Deployment to a cloud platform

## 👨‍💻 Author

**Priyanshu Kumar**

GitHub: [@raopriyanshu90](https://github.com/raopriyanshu90)

---

⭐ If you find this project useful, consider giving the repository a star.
