# 🐾 Veterinary Clinic Website with Appointment Reservation System  
**CS50: Introduction to Computer Science – Final Project**

---

## 📍 Live Demo  
👉 [Visit the website](https://veterinary-clinic-app.onrender.com/)

---

## 📋 Description

This project is a full-stack, web-based application written in **Python**, with **JavaScript** and **SQL** (via the CS50 library). It also includes an additional standalone Python program.

The web application is built for a general veterinary clinic. It provides essential information for clients—services, contact details, and clinic background—along with an **online appointment reservation system**.

The main layout and styling are implemented using the **Bootstrap** framework. Some components are customized using the `custom.css` file, which overrides default Bootstrap styles such as colors.

---

## 📦 Dependencies  

All dependencies are listed in **`requirements.txt`**.

---

## ⚙️ app.py  

The main application file containing the core logic and route definitions.  
It features **9 main routes**:

- `/` – Index (homepage)  
- `/services`  
- `/pricing`  
- `/appointments`  
- `/map`  
- `/admin` – Login (default: `admin` / `admin`)  
- `/logout`  
- `/console`  
- `/clear`  

### Key Functionality:

- Public-facing pages provide general information about the clinic.  
- **`/appointments`** allows users to submit appointment requests without needing to create an account.  
- **`/admin`** enables veterinary staff to log in and manage requests.  
- **`/console`** is an internal dashboard to accept/reject appointments.  
- **`/logout`** ends the session for staff users.

---

## 📁 functions.py  

Utility functions used in the app:

- `apology()` – Displays error messages  
- `current_time()` – Returns current date/time for validations  
- `login_required()` – Restricts access to certain views (used by staff)  
- `email_prototype()` – Simulates email notifications (prints to console)

---

## 👨‍⚕️ admin_manager.py  

A simple script to manage staff accounts.  
Enables creation of new admin users, whose credentials are stored in **`all.db`** (hashed passwords included).

---

## 🗃️ all.db  

This SQLite database includes two primary tables:

1. **`admins`** – Stores usernames, IDs, and hashed passwords  
2. **`appointments`** – Stores appointment data (ID, client info, date, time, status, etc.)

---

## 🎨 /static/custom.css  

Overrides default Bootstrap styles, such as colors and buttons.

---

## 🖼️ /static/images  

Contains all website images and a `.txt` file listing image credits.

---

## 📁 /templates  

Houses all HTML templates rendered by the app.  
The base file **`layout.html`** is extended by other templates using **Jinja**.  
It includes:

- Navbar  
- Footer  
- Custom buttons  
- Bootstrap components  

---

### 🔍 Template Highlights:

#### `/templates/index.html`  

- Homepage with a Bootstrap carousel and featurettes  
- Introductory page for visitors

#### `/templates/appointments.html`  

- Online appointment form  
- Fields: name, email, date, time, reason  
- **Client-side validation:**  
  - Valid email format  
  - Date must be today or within 90 days  
  - Time must be during working hours  
- **Server-side validation (in `app.py`):**  
  - Prevents double-bookings  
  - Blocks past appointments

#### `/templates/console.html`  

- Dashboard for staff (requires login)  
- Accessed after login or via a "Manage Appointments" button  
- Displays **three tables**:  
  1. Pending appointments  
  2. Accepted appointments  
  3. Rejected appointments  
- Admins can accept/reject pending requests  
- Includes a "Clear Old Appointments" button

---

## 🧠 Final Thoughts  

This website gives pet owners a user-friendly way to find clinic info and book appointments—no need to call or email. It streamlines communication while helping staff manage requests efficiently.

---

## 🙏 Acknowledgments  

1. [Freepik](https://www.freepik.com/) – Image resources  
2. [TextMagic Code Formatter](https://freetools.textmagic.com/source-code-formatter) – Code formatting  
3. [ChatGPT](https://chat.openai.com/) – guidance, suggestions, and grammar correction
4. [Bootstrap](https://getbootstrap.com/) – UI framework  
5. [Stack Overflow](https://stackoverflow.com/) – Troubleshooting  
6. [W3Schools](https://www.w3schools.com/) – Web dev tutorials  
7. [CS50](https://pll.harvard.edu/course/cs50-introduction-computer-science) – Project inspiration & utility functions  
8. Additional sources listed in **`references.txt`**
