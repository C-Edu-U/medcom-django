# **MedCom SaaS - Healthcare Management System**  

![MedCom Logo](static/images/logo.png)

## **Overview**  
MedCom SaaS is a **comprehensive healthcare management system** designed to streamline **patient management, appointment scheduling, medical record handling, and revenue tracking** for hospitals, private practices, and independent doctors.

This platform allows **doctors, patients, and administrators** to efficiently manage healthcare services while ensuring **security, usability, and data integrity**.

---

## **Features**  
### **🔹 Patient Management**
- Register and manage patient records.
- Secure login for patients to view and manage their appointments.
- Edit personal information and download clinical history as a PDF.

### **🔹 Doctor Management**
- Register and manage doctor profiles and specializations.
- Assign multiple specializations to doctors with graduation dates.
- Manage doctor availability through a **dynamic scheduling system**.

### **🔹 Appointment Scheduling**
- Patients can schedule appointments based on **doctor availability**.
- **Real-time time slot blocking** ensures no double bookings.
- Dynamic **doctor-service selection** before booking.

### **🔹 Clinical History Management**
- Doctors can add **medical notes** and track patient visits.
- Patients can **download their medical history** as a professionally formatted **PDF**.
- **Secure access control** ensures privacy of medical records.

### **🔹 Revenue & Accounting**
- **Detailed revenue reports** with total income, earnings per service, and monthly breakdowns.
- **Downloadable PDF revenue summary** for accounting and audits.
- **Dynamic filtering** based on selected date ranges.

### **🔹 Role-Based Access Control**
- **Patients**: Can schedule/view appointments, edit profiles, and download medical history.
- **Doctors**: Can manage appointments, view patients, and update records.
- **Administrators**: Have full control over users, financials, and reports.

---

## **🚀 Installation & Setup**  
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/medcom-saas.git
cd medcom-saas
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure Static Files**
```bash
python manage.py collectstatic
```

### **5️⃣ Apply Migrations & Create Superuser**
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
Follow the prompts to create an **admin account**.

### **6️⃣ Run the Server**
```bash
python manage.py runserver
```
Visit **`http://127.0.0.1:8000/`** in your browser.

---

## **🛠️ Technologies Used**
- **Backend**: Django, Django ORM, SQLite/MySQL
- **Frontend**: Bootstrap, HTML5, CSS3
- **Admin UI**: Django Jazzmin
- **Charts & Reporting**: Chart.js, ReportLab (for PDF generation)
- **Authentication & Security**: Django Auth, Role-Based Permissions

---

## **📂 Project Structure**
```
medcom_project/
│── medcom/               # Main Django App
│   ├── settings.py       # Project settings
│   ├── urls.py           # Main URL routing
│   ├── views.py          # Main views
│   ├── static/           # Static files (CSS, JS, images)
│   ├── templates/        # HTML Templates
│── appointments/         # Appointment Management
│── patients/             # Patient Management
│── doctors/              # Doctor & Specialization Management
│── services/             # Healthcare Services
│── reports/              # Revenue & Analytics
│── clinical_histories/   # Medical Record Management
│── templates/            # Shared frontend templates
│── static/images/        # Logo & static assets
│── db.sqlite3            # Database (if using SQLite)
│── manage.py             # Django management script
```

---

## **📊 Reports & Analytics**
### **1️⃣ Revenue Report (For Accounting)**
- **Generate revenue reports** filtered by date range.
- **PDF download available** for accountants and auditors.
- **Includes:**
  - Total revenue.
  - Monthly earnings breakdown.
  - Service-based revenue distribution.
  - Detailed **service completion history**.

### **2️⃣ Medical Record Reports**
- **Patients can download their complete medical history** as a PDF.
- **Doctors can manage and update records securely**.

### **3️⃣ Admin Dashboard**
- **Visual charts** for appointments, revenue, and doctor performance.
- **Export data in multiple formats** (coming soon).

---

## **🔒 Security & Access Control**
- **Role-based authentication** ensures secure access to sensitive data.
- **Patients can only access their own records**.
- **Doctors can only access assigned patients**.
- **Admins have full system control**.

---

## **📝 Future Enhancements**
- 🔹 **Online Payment Integration** (Stripe, PayPal)
- 🔹 **Multi-language Support**
- 🔹 **API for Mobile App Integration**
- 🔹 **AI-based Appointment Recommendations**

---

## **📝 License**
**This project is open-source and publicly available under the Public License.**  

---

## **🤝 Contributing**
We welcome contributions! To contribute:
1. **Fork the repository**.
2. **Create a feature branch**:  
   ```bash
   git checkout -b feature-name
   ```
3. **Make changes and commit**:  
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push the branch**:  
   ```bash
   git push origin feature-name
   ```
5. **Create a pull request**.

---

## **I really appreciate reviews and contributions :)**
