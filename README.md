# DEEPMED VISION

DEEPMED VISION is a web-based platform designed for the secure and efficient handling of medical images for various diagnostic tasks. The platform enables healthcare professionals to upload, analyze, and manage medical images (MRI, CT, ECG, etc.) and associate them with patient information. DEEPMED VISION streamlines medical imaging processes and enhances the workflow for doctors, radiologists, and healthcare providers.

## Features

- **User Authentication:** Login and signup system for secure access to medical image analysis and patient information.
- **Image Upload and Analysis:** Drag-and-drop image upload functionality with options to select the medical image modality (MRI, CT, etc.) and tasks (classification, segmentation).
- **Patient Management:** Track and manage patient data and medical history, with quick access to previous scans and analysis results.
- **Dynamic User Experience:** Real-time updates with AJAX for image upload and analysis without page reloads.
- **Security and Privacy:** Built on Django, ensuring encrypted session management, CSRF protection, and user-based access control.
- **Optimized Inference with Intelipex:** Utilization of Intelipex optimization techniques to enhance model performance for faster inference times.

## Screenshots

### Login Page
![Login](https://github.com/shravan-18/DeepMed-Vision/blob/main/DeepMedVision/DeepMedApp/static/images/Login.png)

### Main Homepage
![Main Homepage](https://github.com/shravan-18/DeepMed-Vision/blob/main/DeepMedVision/DeepMedApp/static/images/mainhomepage.png)

### Image Upload Page
![Image Upload](https://github.com/shravan-18/DeepMed-Vision/blob/main/DeepMedVision/DeepMedApp/static/images/imageupload.png)

### Patient Details Page
![Patient Details](https://github.com/shravan-18/DeepMed-Vision/blob/main/DeepMedVision/DeepMedApp/static/images/Patient%20Details%202.png)

### Patient History Page
![Patient History](https://github.com/shravan-18/DeepMed-Vision/blob/main/DeepMedVision/DeepMedApp/static/images/Patient%20History.png)

### Scan Page
![Scan](https://github.com/shravan-18/DeepMed-Vision/blob/main/DeepMedVision/DeepMedApp/static/images/scan.png)

## User Flow

1. **Login or Signup:** Users must sign up for an account or log in using their credentials.
2. **Upload Medical Images:** Users can drag and drop medical images to upload them for analysis.
3. **Select Modality and Task:** After uploading, users choose the medical image modality (MRI, CT, etc.) and the task (e.g., classification or segmentation) from dropdown menus.
4. **Analysis and Results:** The uploaded image is sent to the server for analysis, and results are displayed in a text-based format.
5. **Patient History:** Users can view and manage patient details, upload new scans, and track the diagnostic history of each patient.

## Components

### Scanner
This is where users can upload medical images. After uploading, the system lets users select:
- **Medical Image Modality** (e.g., MRI, CT)
- **Analysis Task** (e.g., Classification, Segmentation)

The results of the analysis are dynamically returned and displayed to the user.

### Patient History
This section lists all patients, along with their details, medical history, and diagnostic results. Users can easily manage patient records and associate new images with specific patients.

## Intelipex Optimization

DEEPMED VISION leverages **Intelipex Optimization** to enhance the performance of our machine learning models, ensuring faster inference times without sacrificing accuracy. 

### Key Benefits of Intelipex Optimization:
- **Model Acceleration:** By applying Intelipex techniques, we optimize the model architecture and inference engine, significantly reducing the time taken for predictions. This is particularly important in a medical setting where timely analysis can be critical for patient care.
- **Efficient Resource Utilization:** Intelipex helps in maximizing the use of available computational resources, leading to a more efficient deployment of deep learning models.
- **Improved Scalability:** With the optimization techniques, the system can handle a larger number of simultaneous users and requests, making it suitable for a high-demand medical environment.
- **Enhanced Throughput:** The overall system throughput is improved, allowing multiple images to be processed concurrently and enabling quicker results for healthcare professionals.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/username/deepmed-vision.git
    ```

2. Navigate to the project directory:
    ```bash
    cd deepmed-vision
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

5. Open the application in a browser at `http://127.0.0.1:8000/`.

## Usage

1. **Login/Signup:** Navigate to the login/signup page, create an account, or log in with your credentials.
2. **Upload Medical Images:** Use the **Scanner** section to upload medical images by dragging and dropping them into the designated area. Choose the image modality and analysis task from the dropdown menus, then click "Submit."
3. **View Analysis Results:** Once the analysis is complete, the results will be displayed in a text format.
4. **Manage Patients:** In the **Patient History** section, view and manage patient details, add new scans, and track diagnostic results.

## Explanation of DEEPMED VISION

DEEPMED VISION is designed to simplify and accelerate medical image analysis for healthcare professionals. With an emphasis on user experience, the platform provides a clear and intuitive interface that allows doctors, radiologists, and other medical personnel to upload, analyze, and manage patient images quickly and securely.

### User Authentication

The login and signup system ensures that only authorized users can access sensitive patient data. By leveraging Django's built-in authentication framework, we offer a robust yet simple way for healthcare providers to maintain the confidentiality and integrity of medical information.

### Image Upload and Analysis

The **Scanner** section is the core of DEEPMED VISION. Medical images from different modalities such as MRI, CT, and ECG can be uploaded by dragging and dropping them into the designated area. After uploading, users can select the appropriate modality and task from dropdown menus, further refining the system's ability to deliver the most accurate results.

The analysis tasks are processed by the server, which can interface with advanced deep learning models for classification or segmentation. The results are displayed back to the user in a text format, providing quick and actionable insights.

### Patient Management

The **Patient History** section helps healthcare providers manage patient information. Each patient profile includes vital details and their medical history of uploaded scans. Doctors can initiate a scan for a particular patient by clicking on **Scan Now**, ensuring new images are linked to the correct patient record.

### Dynamic User Experience

By implementing AJAX functionality, DEEPMED VISION ensures a dynamic and responsive user experience. The **drag-and-drop** functionality reduces the need for file input fields, streamlining the image upload process. No page reload is required after submitting a scan request, providing a seamless user interaction.

### Security and Privacy

Security is a core component of DEEPMED VISION. The application ensures secure data handling, encrypted session management, and protection against vulnerabilities like SQL Injection, XSS, and CSRF. Access to patient data and imaging results is restricted based on user authentication.

### Extensibility and Future Plans

DEEPMED VISION is designed with scalability in mind. Future versions could include features such as:
- Real-time image enhancement and anomaly detection using advanced deep learning models.
- Integration with hospital management systems (HMS) to streamline patient data flow.
- Collaboration features for multiple doctors to review the same image scan.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

