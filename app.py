from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

app = Flask(__name__)
# Change this to a more secure random key in production
app.secret_key = 'your_secret_key_here_change_in_production'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', '').strip()
    
    # Validate the name
    if not name:
        # If no name provided, redirect back to home with error
        session['error'] = 'Please enter your name!'
        return redirect(url_for('index'))
    
    if len(name) > 50:
        # If name is too long, truncate it
        name = name[:50]
        session['info'] = 'Name was too long, truncated to 50 characters'
    
    # Store in session
    session['username'] = name
    return redirect(url_for('show_greeting'))

@app.route('/greeting')
def show_greeting():
    # Get name from session or use default
    name = session.get('username', 'Guest')
    
    # Get current time for time-based greeting
    now = datetime.now()
    
    # Pass both name and current time to template
    return render_template('greeting.html', name=name, now=now)

@app.route('/reset')
def reset_name():
    # Clear the name and any messages from session
    session.pop('username', None)
    session.pop('error', None)
    session.pop('info', None)
    return redirect(url_for('index'))

# Add error handler for 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)