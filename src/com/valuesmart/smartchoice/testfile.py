from flask import Flask, session, render_template_string

app = Flask(__name__)

# Secret key for session management
app.secret_key = 'your_secret_key'  # Replace with a strong secret key

# Configure session to use filesystem (or you can choose other backends)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True

# Initialize the session
from flask_session import Session
Session(app)

# Main route to load the web page
@app.route('/')
def index():
    # Create a session ID if it doesn't exist
    if 'session_id' not in session:
        session['session_id'] = session.sid  # Generate a session ID
    return render_template_string('''
        <h1>Welcome to the Main Web Page</h1>
        <p>Your Session ID: {{ session_id }}</p>
    ''', session_id=session['session_id'])

# Route to create a new session
@app.route('/create-session')
def create_session():
    session['session_id'] = session.sid  # Assign a new session ID
    return f'Session created with ID: {session["session_id"]}'

# Start the server
if __name__ == '__main__':
    app.run(debug=True)
