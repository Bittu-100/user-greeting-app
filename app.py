from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import random
import requests



app = Flask(__name__)
# In production, use a more secure key
app.secret_key = 'your_secret_key_here_change_in_production'


# Add this near the top, after imports
visitor_count = 0

@app.before_request
def count_visitors():
    global visitor_count
    visitor_count += 1
    # Store in session for this user
    if 'visit_count' not in session:
        session['visit_count'] = 1
    else:
        session['visit_count'] = session.get('visit_count', 0) + 1

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

def get_name_fact(name):
    """Get a fun fact about names"""
    # Simple logic based on name characteristics
    facts = []
    
    if len(name) <= 3:
        facts.append(f"'{name}' is a short name! Short names are easy to remember.")
    elif len(name) >= 8:
        facts.append(f"'{name}' is a long name! Long names often have interesting histories.")
    
    if name.lower() == name.lower()[::-1]:
        facts.append(f"Wow! '{name}' is a palindrome (reads the same forwards and backwards)!")
    
    # Add a random general fact
    facts.append(random.choice(NAME_FACTS))
    
    return facts

@app.route('/')
def index():
    # Clear any previous messages
    session.pop('error', None)
    session.pop('info', None)
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():
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
    # Store name facts in session
    session['name_facts'] = get_name_fact(name)
    
    return redirect(url_for('show_greeting'))

@app.route('/greeting')
def show_greeting():
    name = session.get('username', 'Guest')
    now = datetime.now()
    name_facts = session.get('name_facts', [])
    visit_count = session.get('visit_count', 1)
    
    return render_template('greeting.html', 
                          name=name, 
                          now=now, 
                          name_facts=name_facts,
                          visit_count=visit_count)

@app.route('/reset')
def reset_name():
    session.pop('username', None)
    session.pop('name_facts', None)
    session.pop('error', None)
    session.pop('info', None)
    return redirect(url_for('index'))

# API endpoint to get random fact (optional)
@app.route('/api/random-fact')
def random_fact():
    return jsonify({
        'fact': random.choice(NAME_FACTS),
        'timestamp': datetime.now().isoformat()
    })

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)