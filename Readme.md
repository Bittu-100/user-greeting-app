```markdown
# User Greeting App 👋

A simple Flask web application that provides personalized greetings to users. Enter your name and get a customized greeting with fun facts!

## ✨ Features

- **Personalized Greetings**: Enter your name and get a customized greeting
- **Time-based Messages**: Different greetings for morning, afternoon, and evening
- **Session Management**: Remembers your name during your visit
- **Fun Facts**: Learn interesting facts about names
- **Visitor Statistics**: Track your visits and see stats
- **Responsive Design**: Works on desktop and mobile devices
- **Beautiful UI**: Clean, modern interface with Bootstrap 5
- **Error Handling**: Custom 404 and 500 error pages

## 🛠️ Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5, Custom CSS
- **Icons**: Bootstrap Icons
- **Session**: Flask Session
- **Environment**: Python-dotenv


## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Bittu-100/user-greeting-app.git
   cd user-greeting-app
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Create environment file**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your secret key:
   ```env
   SECRET_KEY=your_random_secret_key_here
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open your browser** and visit:
   ```
   http://localhost:5000
   ```

## 📝 How to Use

1. **Visit the homepage** (`http://localhost:5000`)
2. **Enter your name** in the input field
3. **Click "Get Greeting"** button
4. **View your personalized greeting** with fun facts about names
5. **Change your name anytime** using the "Change Name" button

### Features in Detail

#### 1. Name Validation
- Cannot submit empty name
- Names longer than 50 characters are automatically truncated
- Shows appropriate error messages

#### 2. Time-based Greetings
- **Morning** (before 12 PM): "Good morning! Hope you have a wonderful day ahead!"
- **Afternoon** (12 PM - 6 PM): "Good afternoon! Hope you're having a great day!"
- **Evening** (after 6 PM): "Good evening! Hope you had a wonderful day!"

#### 3. Session Management
- Remembers your name during browser session
- Can reset/change name anytime using "Change Name" button
- Tracks number of visits per user

#### 4. Fun Facts
- Provides interesting facts about names
- Shows name length statistics
- Name-specific facts based on characteristics (short names, long names, palindromes)

#### 5. Visitor Statistics
- Shows your personal visit count
- Displays simulated total app visits
- Shows recent visitors list

## 🌐 API Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/` | GET | Homepage with name input form | HTML page |
| `/greet` | POST | Process name and show greeting | Redirect to `/greeting` |
| `/greeting` | GET | Display personalized greeting | HTML page with greeting |
| `/reset` | GET | Clear session and return to homepage | Redirect to `/` |
| `/api/random-fact` | GET | Get random name fact | JSON response |
| `/api/health` | GET | Health check endpoint | JSON response |
| Any invalid URL | GET | Custom 404 error page | HTML error page |

### API Examples

**Get random fact:**
```bash
curl http://localhost:5000/api/random-fact
```
Response:
```json
{
  "fact": "The most common name in the world is Mohammed.",
  "app": "User Greeting App",
  "version": "1.0.0",
  "timestamp": "2023-10-05T14:30:00.123456"
}
```

## 🙏 Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Styled with [Bootstrap 5](https://getbootstrap.com/)
- Icons from [Bootstrap Icons](https://icons.getbootstrap.com/)
- Inspired by beginner-friendly Flask tutorials
- Project structure inspired by best practices


## 🎓 Learning Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Jinja2 Template Documentation](https://jinja.palletsprojects.com/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)

## 📊 Project Status

✅ **Complete and Functional**  
✅ **Tested Locally**  
✅ **Documented**  
✅ **Ready for Deployment**  
🚀 **Production Ready**

---

## 🏆 What This Project Demonstrates

- Flask application setup and configuration
- Route handling and HTTP methods
- Template rendering with Jinja2
- Form handling and validation
- Session management
- Error handling
- Static file serving
- Environment configuration
- Project structure best practices
- Git workflow and deployment

## 🚀 Next Steps After This Project

1. **Add a Database**: Learn Flask-SQLAlchemy for data persistence
2. **User Authentication**: Implement login/logout with Flask-Login
3. **REST API**: Create a full REST API with Flask-RESTful
4. **Real-time Features**: Add WebSockets with Flask-SocketIO
5. **Testing**: Implement unit tests with pytest
6. **CI/CD**: Set up GitHub Actions for automated testing and deployment
