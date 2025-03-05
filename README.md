# Attendance Mask Detection System

This project is a computer vision application that **detects faces**, **recognizes known individuals**, and **checks for face masks** in real-time using a webcam. It also logs attendance for recognized faces. If someone is detected without a mask, the system captures a snapshot of the violation.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Future Improvements](#future-improvements)
- [License](#license)
---

## Overview

The **Attendance Mask Detection System** combines face recognition and mask detection. It stores attendance in a CSV file, marking the entry time when a person is detected, and the exit time when the program ends (or on next detection, depending on your logic). The system can also generate plots and an output CSV summarizing who was present, absent, wearing masks, etc.

---

## Features

1. **Face Detection**: Uses the OpenCV DNN face detector to locate faces in the video stream.
2. **Face Recognition**: Utilizes the `face_recognition` library to match detected faces against known encodings in `ImagesAttendance/`.
3. **Mask Detection**: Uses a pre-trained MobileNetV2-based mask detector to classify each face as Mask or No Mask.
4. **Attendance Tracking**: Logs each recognized person’s entry and exit times in `Attendance.csv`.
5. **Violation Logging**: Captures a snapshot (`violation_*.png`) if a person is detected without a mask.
6. **Reporting**: Generates basic CSV and graphical reports (`output.csv`, plots) indicating attendance and mask usage.

---

## Project Structure

```bash
Facial Recognition and Mask Detection Integration with Attendance Management System/
├── face_detector/
│   ├── deploy.prototxt
│   └── res10_300x300_ssd_iter_140000.caffemodel
├── ImagesAttendance/
│   └── # Directory for storing student images
├── violations/
│   └── # Directory for storing mask violation images
├── Attendance.csv
├── students.csv
├── output.csv
├── Face_Recognition_Mask_Detection.ipynb
├── train_mask_detection_model.ipynb
├── clear_files.ipynb
├── README.md
└── requirements.txt
```
---

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/jagrit-sharma/MaskVision.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd "Facial Recognition and Mask Detection Integration with Attendance Management System"
   ```

3. **Install Required Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Make sure you have Python 3.7 or higher installed.

4. **Verify Directory Structure**

   Ensure that the following folders and files exist:
   ```bash
   Facial Recognition and Mask Detection Integration with Attendance Management System/
    ├── face_detector/
    │   ├── deploy.prototxt
    │   └── res10_300x300_ssd_iter_140000.caffemodel
    ├── ImagesAttendance/
    │   └── # Directory for storing student images
    ├── violations/
    │   └── # Directory for storing mask violation images
    ├── Attendance.csv
    ├── students.csv
    ├── output.csv
    ├── Face_Recognition_Mask_Detection.ipynb
    ├── train_mask_detection_model.ipynb
    ├── clear_files.ipynb
    ├── README.md
    └── requirements.txt
   ```

5. **(Optional) Clear Existing Attendance Files**

   If you want a fresh start, open and run `clear_files.ipynb` to reset `Attendance.csv` and `output.csv` before running the main script.

6. **Run the Application**

   - Open `Face_Recognition_Mask_Detection.ipynb` in a Jupyter environment (or compatible IDE).
   - Run all cells to start the webcam-based detection, attendance logging, and mask detection.

7. **Check Logs and Reports**

   - `Attendance.csv` will contain detailed logs (Name, Entry Time, Exit Time).
   - `output.csv` will contain a summary of Present/Absent statuses based on `students.csv`.
   - Additional plots and images may be saved (e.g., mask violation snapshots in `violations/`).

8. **Shut Down**

   - Press **Esc** or close the notebook cell to stop the video stream.
   - Review and save any generated reports or figures before exiting.
  ---
  ## Future Improvements

1. **User Interface (UI) Enhancements**  
   - Integrate a Streamlit or Flask web application to provide a more intuitive interface for viewing real-time video, attendance logs, and mask violation alerts.

2. **Database Integration**  
   - Store attendance records in a relational or NoSQL database (e.g., MySQL, PostgreSQL, MongoDB) for enhanced scalability and querying capabilities.

3. **Notifications**  
   - Implement an email or SMS alert system for immediate notification when a mask violation is detected or when an unknown person is recognized.

4. **Automated Scheduling**  
   - Use tools like `cron` (Linux) or Task Scheduler (Windows) to automate script execution at specific intervals, and/or auto-generate daily/weekly attendance reports.

5. **Improved Face Recognition Models**  
   - Consider adding or switching to more advanced face recognition methods (e.g., ArcFace, FaceNet) for better accuracy in various lighting conditions.

6. **Mask Detector Optimization**  
   - If performance is slow, explore TensorRT or OpenVINO optimizations for faster inference on GPUs or other specialized hardware.

7. **Mobile or Edge Deployment**  
   - Port the system to low-power devices like Raspberry Pi or NVIDIA Jetson Nano for onsite, edge-based mask and attendance detection.

8. **Additional Features**  
   - Detect and track multiple individuals simultaneously, maintain historical logs, or integrate multi-camera setups for large-scale environments.
  ---
  ## License

This project is licensed under the [MIT License](https://github.com/jagrit-sharma/MaskVision/blob/main/LICENSE).

