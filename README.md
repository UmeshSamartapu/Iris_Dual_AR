# DUAL Iris AR 🌸

```markdown
An interactive Augmented Reality application built with **Django** that visualizes the famous Iris Dataset in 3D space. This project bridges the gap between data science and immersive technology by allowing users to explore botanical data through their camera.

## 🚀 Features

- **Dual-Mode AR:** Support for both Markerless (Mobile) and Marker-based (Laptop) tracking.
- **Data-Driven Scaling:** The model is scaled precisely according to the Iris species dimensions (X: Virginica, Y: Setosa, Z: Versicolor).
- **Cross-Platform:** Works on Android/iOS via WebXR and on Desktop via AR.js.
- **Interactive UI:** A unified landing page to guide users based on their hardware.

## 🛠️ Tech Stack

- **Backend:** Django (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **AR Engines:** - [Google Model-Viewer](https://modelviewer.dev/) (Mobile SLAM)
  - [AR.js](https://ar-js-org.github.io/AR.js-Docs/) (Laptop Marker-tracking)
- **3D Framework:** A-Frame / Three.js

## 📦 Project Structure

```text
iris_ar_project/
├── templates/
│   ├── landing.html     # Selection page
│   ├── index.html       # Mobile AR (WebXR)
│   └── laptop_ar.html   # Laptop AR (AR.js)
├── static/
│   └── models/
│       └── Iris.glb     # 3D Iris Model
├── viewer/              # Django App
└── manage.py
```

## 🏃 Setup Instructions

1. **Clone the project** and navigate to the directory.
2. **Install Django:**
   ```bash
   pip install django
   ```
3. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
4. **Access the Application:**
   - **On Laptop:** Go to `http://127.0.0.1:8000/` and choose "Laptop AR".
   - **On Mobile:** Use `ngrok` to create an HTTPS tunnel:
     ```bash
     ngrok http 8000
     ```
     Open the `https` link provided by ngrok on your mobile browser.

## 📸 How to Use

### Laptop Mode
1. Click **"Download Hiro Marker"** on the Laptop AR page.
2. Open the marker image on your phone or print it.
3. Show the marker to your laptop's webcam to see the Iris model bloom!

### Mobile Mode
1. Tap **"Activate AR Camera"**.
2. Scan a flat surface (floor or table).
3. Tap the screen to place the model in your real-world environment.

## 📊 Data Mapping
The model scaling represents the relationship between Iris species:
- **X-Axis:** Virginica
- **Y-Axis:** Setosa
- **Z-Axis:** Versicolor

---
Developed with ❤️ by umeshsamartapu
```
"# Iris_Dual_AR" 
