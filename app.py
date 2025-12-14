from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
# Secret key for session management (in production, use a secure random key)
app.secret_key = 'your_secret_key_here_change_in_production'

# Homepage route - shows the name input form
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and show greeting
@app.route('/greet', methods=['POST'])
def greet():
    # Get the name from the form
    name = request.form.get('name', '').strip()
    
    # Store name in session for persistence
    if name:
        session['username'] = name
    
    # Redirect to greeting page
    return redirect(url_for('show_greeting'))

# Route to display the greeting
@app.route('/greeting')
def show_greeting():
    # Get name from session, or use default
    name = session.get('username', 'Guest')
    return render_template('greeting.html', name=name)

# Route to reset/change the name
@app.route('/reset')
def reset_name():
    # Clear the name from session
    session.pop('username', None)
    # Redirect back to homepage
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)