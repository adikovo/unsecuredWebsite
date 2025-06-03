from flask import Flask, render_template, request, redirect, url_for, flash, session
import requests

app = Flask(__name__)
app.secret_key = 'insecure_secret_key'  # Not secure, for demo only

# Node.js backend URL
BACKEND_URL = 'http://localhost:3000'

# Home route (redirect to login)
@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        try:
            r = requests.post(f'{BACKEND_URL}/register', json={
                'username': username,
                'email': email,
                'password': password
            })
            if r.status_code == 200:
                flash('User registered successfully! Please login.', 'success')
                return redirect(url_for('login'))
            else:
                flash(r.json().get('error', 'Registration failed.'), 'error')
        except Exception as e:
            flash('Could not connect to backend.', 'error')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            r = requests.post(f'{BACKEND_URL}/login', json={
                'username': username,
                'password': password
            })
            if r.status_code == 200:
                session['username'] = username
                return redirect(url_for('system'))
            else:
                error = r.json().get('error', 'Login failed.')
                if error == 'Incorrect username':
                    flash('user does not exist', 'error')
                else:
                    flash(error, 'error')
        except Exception as e:
            flash('Could not connect to backend.', 'error')
    return render_template('login.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # No code sent, just redirect to change password
        email = request.form['email']
        session['reset_email'] = email
        return redirect(url_for('change_password'))
    return render_template('forgot_password.html')

@app.route('/change-password', methods=['GET', 'POST'])
def change_password():
    username = session.get('username')
    if not username:
        flash('You must be logged in to change your password.', 'warning')
        return redirect(url_for('login'))
    if request.method == 'POST':
        new_password = request.form['new_password']
        try:
            r = requests.post(f'{BACKEND_URL}/change-password', json={
                'username': username,
                'currentPassword': '',  # Not used
                'newPassword': new_password
            })
            if r.status_code == 200:
                flash('Password changed successfully!', 'success')
                return redirect(url_for('system'))
            else:
                flash(r.json().get('error', 'Password change failed.'), 'error')
        except Exception as e:
            flash('Could not connect to backend.', 'error')
    return render_template('change_password.html')

@app.route('/system', methods=['GET', 'POST'])
def system():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    customer_name = None
    customers = None
    
    if request.method == 'POST':
        # Handle adding new customer
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        package_type = request.form['package_type']
        try:
            r = requests.post(f'{BACKEND_URL}/add-customer', json={
                'name': name,
                'email': email,
                'address': address,
                'package_type': package_type
            })
            if r.status_code == 200:
                customer_name = name
            else:
                flash(r.json().get('error', 'Failed to add customer.'), 'error')
        except Exception as e:
            flash('Could not connect to backend.', 'error')
    
    elif request.method == 'GET':
        # Handle search and list actions
        action = request.args.get('action')
        
        if action == 'search':
            query = request.args.get('query')
            if query:
                try:
                    r = requests.get(f'{BACKEND_URL}/search-customers', params={'query': query})
                    if r.status_code == 200:
                        customers = r.json().get('customers', [])
                        if not customers:
                            flash(f'No customers found matching "{query}".', 'info')
                    else:
                        flash('Error searching customers.', 'error')
                except Exception as e:
                    flash('Could not connect to backend.', 'error')
        
        elif action == 'list':
            try:
                r = requests.get(f'{BACKEND_URL}/customers')
                if r.status_code == 200:
                    customers = r.json().get('customers', [])
                else:
                    flash('Error fetching customers.', 'error')
            except Exception as e:
                flash('Could not connect to backend.', 'error')
    
    return render_template('system.html', customer_name=customer_name, customers=customers)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True) 