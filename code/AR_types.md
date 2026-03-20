To help you understand how these technologies actually "see" the world and what tools you need to build them, let's break down the mechanics and the technical layers for each.

---

## 1. AR.js (Marker-Based)
This is the "classic" WebAR. It relies on **Image Recognition** to find a specific, high-contrast pattern (like the Hiro marker) in the video feed.

* **How it Works:** The library uses **Computer Vision** to detect the four corners of the black square. By calculating how those corners are distorted (perspective), it determines the exact position ($x, y, z$) and rotation of your camera relative to the paper.
    
* **Tech Stack:**
    * **A-Frame / Three.js:** For rendering the 3D model.
    * **jsartoolkit5:** The underlying engine that handles the heavy math of marker tracking.
    * **WebRTC:** To access your laptop/phone webcam.

---

## 2. Google Model-Viewer (Slam-Based)
This uses **WebXR** and **SLAM** (Simultaneous Localization and Mapping). It doesn't need a marker because it "reads" the features of your floor.

* **How it Works:** It looks for "feature points" (dots, shadows, or textures) on your floor. As you move the phone, it tracks how those points move to build a virtual map of your room. It then places the Iris model on that virtual floor.
    
* **Tech Stack:**
    * **WebXR Device API:** The browser standard for AR/VR.
    * **ARCore (Android) / ARKit (iOS):** The deep system-level sensors that handle the motion tracking.
    * **Three.js:** Used internally by Google to render the GLB model with realistic lighting.

---

## 3. MediaPipe (ML-Based Tracking)
This is the most "AI-heavy" approach. Instead of tracking the floor, it tracks **Human Landmarks**.

* **How it Works:** A pre-trained **Deep Learning model** (Neural Network) analyzes every frame of your video to find 21 specific points on your hand. It then "parents" your 3D Iris model to one of those points (like your palm).
    
* **Tech Stack:**
    * **TensorFlow.js:** To run the Machine Learning model directly in the browser.
    * **MediaPipe Solutions:** The specific library for hand/face/pose detection.
    * **Three.js / Canvas:** To draw the 3D model on top of the hand coordinates.

---

## 4. 8th Wall (SLAM for the Web)
8th Wall is unique because it brought high-end "Markerless AR" to browsers that didn't support WebXR yet (like older iPhones).

* **How it Works:** They wrote their own highly optimized **Computer Vision engine in JavaScript and WebAssembly (Wasm)**. It performs the same SLAM tracking as Google's version but does all the math inside the browser's engine rather than relying on the phone's OS.
* **Tech Stack:**
    * **WebAssembly (Wasm):** For near-native execution speed of tracking algorithms.
    * **8th Wall Engine:** A proprietary tracking library.
    * **React / Vue / A-Frame:** Usually used as the frontend framework.

---

### Summary Table of Tech Requirements

| Method | Main Engine | Programming Language | Data Source |
| :--- | :--- | :--- | :--- |
| **AR.js** | jsartoolkit5 | JavaScript | Camera + Square Marker |
| **Model-Viewer** | WebXR | HTML / JavaScript | Camera + Accelerometer |
| **MediaPipe** | TensorFlow.js | JavaScript / Python | Camera + Neural Network |
| **8th Wall** | 8th Wall (Wasm) | JavaScript | Camera + Feature Points |
