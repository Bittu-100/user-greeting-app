from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import random
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)
# Use environment variable for secret key
app.secret_key = os.getenv('SECRET_KEY', 'fallback_secret_key_for_development')

# App configuration from environment
app.config['APP_NAME'] = os.getenv('APP_NAME', 'User Greeting App')
app.config['APP_VERSION'] = os.getenv('APP_VERSION', '1.0.0')

# List of fun facts about names
NAME_FACTS = [
    "The most common name in the world is Mohammed.",
    "In many cultures, names have special meanings.",
    "Some names are palindromes (read the same forwards and backwards).",
    "The longest name in the world has 747 characters!",
    "In Iceland, names must be approved by a naming committee.",
    "Some people change their names to match their personality.",
    "Names can influence how people perceive you.",
    "In some cultures, names are chosen based on birth order.",
    "There are over 100,000 different first names in use worldwide.",
    "Some names become popular because of famous people or characters."
]

# Global visitor counter
visitor_count = 0

@app.before_request
def count_visitors():
    """Count visitors and track session visits"""
    global visitor_count
    visitor_count += 1
    
    # Track individual user visits
    if 'visit_count' not in session:
        session['visit_count'] = 1
    else:
        session['visit_count'] = session.get('visit_count', 0) + 1
    
    # Store total visits in session for display
    session['total_visits'] = visitor_count

def get_name_fact(name):
    """Get a fun fact about names"""
    facts = []
    
    if len(name) <= 3:
        facts.append(f"'{name}' is a short name! Short names are easy to remember.")
    elif len(name) >= 8:
        facts.append(f"'{name}' is a long name! Long names often have interesting histories.")
    
    if name.lower() == name.lower()[::-1]:
        facts.append(f"Wow! '{name}' is a palindrome (reads the same forwards and backwards)!")
    
    # Add 2 random general facts
    facts.append(random.choice(NAME_FACTS))
    facts.append(random.choice(NAME_FACTS))
    
    return facts[:3]  # Return max 3 facts

@app.route('/')
def index():
    """Homepage with name input form"""
    # Pass app info to template
    app_info = {
        'name': app.config['APP_NAME'],
        'version': app.config['APP_VERSION']
    }
    return render_template('index.html', app_info=app_info)

@app.route('/greet', methods=['POST'])
def greet():
    """Process name form submission"""
    name = request.form.get('name', '').strip()
    
    # Validate the name
    if not name:
        session['error'] = 'Please enter your name!'
        return redirect(url_for('index'))
    
    if len(name) > 50:
        name = name[:50]
        session['info'] = 'Name was too long, truncated to 50 characters'
    
    # Store in session
    session['username'] = name
    session['name_facts'] = get_name_fact(name)
    
    return redirect(url_for('show_greeting'))

@app.route('/greeting')
def show_greeting():
    """Display personalized greeting"""
    name = session.get('username', 'Guest')
    now = datetime.now()
    name_facts = session.get('name_facts', [])
    visit_count = session.get('visit_count', 1)
    total_visits = session.get('total_visits', 1000)
    
    # App info for template
    app_info = {
        'name': app.config['APP_NAME'],
        'version': app.config['APP_VERSION']
    }
    
    return render_template('greeting.html', 
                          name=name, 
                          now=now, 
                          name_facts=name_facts,
                          visit_count=visit_count,
                          total_visits=total_visits,
                          app_info=app_info)

@app.route('/reset')
def reset_name():
    """Clear session and return to homepage"""
    session.pop('username', None)
    session.pop('name_facts', None)
    session.pop('error', None)
    session.pop('info', None)
    return redirect(url_for('index'))

@app.route('/api/random-fact')
def random_fact():
    """API endpoint for random name fact"""
    return jsonify({
        'fact': random.choice(NAME_FACTS),
        'app': app.config['APP_NAME'],
        'version': app.config['APP_VERSION'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/health')
def health_check():
    """Health check endpoint for monitoring"""
    return jsonify({
        'status': 'healthy',
        'app': app.config['APP_NAME'],
        'version': app.config['APP_VERSION'],
        'visitors': session.get('total_visits', 0),
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def page_not_found(e):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    """500 error handler"""
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'False') == 'True')