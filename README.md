# Communication_LTD Information System

This is an intentionally insecure web system for Communication_LTD, a fictional telecommunications company. The system consists of a Flask web frontend and a Node.js backend API with MySQL database.

## System Architecture

- **Frontend**: Flask web application (Python) - runs on port 5000
- **Backend**: Node.js API server - runs on port 3000  
- **Database**: MySQL database

## Prerequisites

Before running the system, ensure you have the following installed:

1. **Python 3.x** - [Download Python](https://www.python.org/downloads/)
2. **Node.js and npm** - [Download Node.js](https://nodejs.org/)
3. **MySQL Server** - [Download MySQL](https://dev.mysql.com/downloads/mysql/)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/adikovo/unsecuredWebsite.git
cd Communication_LTD
```

### 2. Database Setup
1. Start your MySQL server
2. Open MySQL command line or a MySQL client (like MySQL Workbench)
3. Run the contents of `database.sql` to create the database and tables:
   ```sql
   CREATE DATABASE IF NOT EXISTS communication_ltd;
   USE communication_ltd;

   CREATE TABLE IF NOT EXISTS users (
       id INT PRIMARY KEY AUTO_INCREMENT,
       username VARCHAR(255) UNIQUE NOT NULL,
       password VARCHAR(255) NOT NULL,
       email VARCHAR(255) NOT NULL
   );

   CREATE TABLE IF NOT EXISTS customers (
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(255) NOT NULL,
       email VARCHAR(255),
       address VARCHAR(255),
       package_type VARCHAR(255)
   );
   ```

### 3. Backend Setup (Node.js API)
1. Install Node.js dependencies:
   ```bash
   npm install
   ```

2. Update database connection settings in `server.js`:
   - Open `server.js`
   - Update the database connection parameters (lines 14-18):
   ```javascript
   const db = mysql.createConnection({
       host: 'localhost',
       user: 'root',                    // Your MySQL username (usually 'root')
       password: 'YOUR_MYSQL_PASSWORD', // Replace with your MySQL password
       database: 'communication_ltd'
   });
   ```

3. Start the Node.js backend server:
   ```bash
   node server.js
   ```
   The backend will run on `http://localhost:3000`

### 4. Frontend Setup (Flask Web App)
1. Open a new terminal window/tab
2. Create a Python virtual environment (recommended):
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - **Windows**: `.venv\Scripts\activate`
   - **macOS/Linux**: `source .venv/bin/activate`

4. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Start the Flask application:
   ```bash
   python app.py
   ```
   You should see:
   ```
   * Running on http://127.0.0.1:5000
   * Debug mode: on
   ```

## Quick Start Summary

For a fast setup (assuming MySQL is already running):

1. **Clone and navigate**: `git clone <repo-url> && cd Communication_LTD`
2. **Install Node.js deps**: `npm install`
3. **Update MySQL password** in `server.js` (line 16) with your own MySQL password
4. **Start backend**: `node server.js`
5. **Install Python deps**: `pip install -r requirements.txt`
6. **Start frontend**: `python app.py`
7. **Open browser**: Go to `http://localhost:5000`

## Test the System

### Sample Test Flow:
1. **Register a new user**:
   - Go to `http://localhost:5000`
   - Click "Register"
   - Create a test account (e.g., username: "testuser", password: "test123")

2. **Login and test features**:
   - Login with your test account
   - Add a customer (e.g., Name: "John Doe", Email: "john@test.com")
   - Search for the customer by name
   - View all customers

### Expected Behavior:
- ✅ Registration should show green success message
- ✅ Login should redirect to system page
- ✅ Adding customers should show success message
- ✅ Search should find exact name matches only
- ✅ "Show All Customers" displays table with all customer data

## Running the System

### Start Order (Important!)
1. **First**: Start MySQL server
2. **Second**: Start Node.js backend (`node server.js`)
3. **Third**: Start Flask frontend (`python app.py`)

### Access the Application
- Open your web browser
- Navigate to `http://localhost:5000`
- You'll be redirected to the login page

## Features

### User Management
- **Register**: Create new user accounts
- **Login**: Authenticate users
- **Change Password**: Update user passwords

### Customer Management
- **Add Customer**: Add new customers with name, email, address, and package type
- **Search Customer**: Search for customers by exact name match
- **View All Customers**: Display all customers in a table format
- **Customer Data**: View customer ID, name, email, address, and package type

## API Endpoints

### User Endpoints
- **POST** `/register` - Register new user
- **POST** `/login` - User login
- **POST** `/change-password` - Change user password

### Customer Endpoints
- **POST** `/add-customer` - Add new customer
- **GET** `/search-customers?query=name` - Search customers by name
- **GET** `/customers` - Get all customers

## File Structure
```
Communication_LTD/
├── app.py                 # Flask web application
├── server.js             # Node.js backend API
├── database.sql          # Database setup script
├── requirements.txt      # Python dependencies
├── package.json          # Node.js dependencies
├── templates/            # HTML templates
│   ├── login.html
│   ├── register.html
│   ├── system.html
│   ├── change_password.html
│   └── forgot_password.html
└── static/
    └── style.css         # CSS styling
```
