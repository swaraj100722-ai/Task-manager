# 🚀 TaskMaster AI: Smart Task Management System

TaskMaster AI is a premium, full-stack task management application designed for teams to collaborate efficiently with the power of Artificial Intelligence. Featuring a modern Glassmorphism UI, role-based access control, and Gemini AI integration for intelligent task breakdown and prioritization.

---

## ✨ Key Features

### 🏢 Organization & Management
- **Role-Based Access**: Specialized dashboards for **Admin** and **Member** roles.
- **Project Grid**: Visual management of all ongoing projects with status tracking.
- **Team Management**: Admins can create accounts, assign roles, and manage team members.

### 🤖 AI-Powered Intelligence
- **Task Breakdown**: Use Gemini AI to decompose complex task descriptions into actionable sub-tasks.
- **Priority Suggestion**: AI analyzes task titles and descriptions to suggest the most appropriate priority level.
- **AI Assistant**: A dedicated interface for interacting with the AI project helper.

### 🎨 Premium User Experience
- **Glassmorphism Design**: Sleek, modern interface using CSS blur and transparency effects.
- **Dark/Light Mode**: Full theme support with smooth transitions.
- **Interactive Dashboards**: Real-time stats, activity feeds, and progress tracking.
- **Desktop Restricted**: Optimized for a professional desktop environment.

---

## 🛠️ Technology Stack

- **Frontend**: Vanilla JavaScript (ES6+), HTML5, CSS3 (Glassmorphism).
- **Backend**: Django REST Framework.
- **Database**: MySQL.
- **AI Engine**: Google Gemini Pro API.
- **Authentication**: JWT (JSON Web Tokens) with Secure Local Storage.

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.10+
- MySQL Server
- Node.js (Optional, for advanced frontend tools)
- A Google Gemini API Key

---

## ⚙️ Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/swaraj100722-ai/Task-manager.git
   cd Task-manager
   ```

2. **Setup Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables**
   Create a `.env` file in the root directory and add:
   ```env
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   MYSQLDATABASE=task_manager_db
   MYSQLUSER=your_mysql_user
   MYSQLPASSWORD=your_mysql_password
   MYSQLHOST=127.0.0.1
   MYSQLPORT=3306
   GEMINI_API_KEY=your_gemini_api_key
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   ```

5. **Run Migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create Admin Account**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start the Server**
   ```bash
   python manage.py runserver
   ```

---

## 📖 User Guide: Step-by-Step

### 1. Authentication & Login
- Access the application at `http://127.0.0.1:8000/`.
- Use your email and password to log in.
- **Admin Note**: Users with emails ending in `@task.com` are automatically granted Admin privileges in the frontend.

### 2. Creating a Project (Admin)
- Navigate to the **Projects** tab.
- Click **"Create Project"**.
- Fill in the Name and Description and save. Your project will appear in the beautiful project grid.

### 3. Managing Team Members (Admin)
- Go to the **Team Members** tab.
- Click **"Add Member"**.
- The system generates a unique **Employee ID** automatically.
- Assign a role (**Admin** or **Member**) and save.

### 4. Task Intelligence (Using AI)
- Open any project or go to the **AI Assistant** tab.
- **Break Down**: Paste a long task description and click "Break Down". The AI will generate a structured list of sub-tasks.
- **Suggest Priority**: Enter a task title, and the AI will analyze the urgency and suggest a Priority (High, Medium, or Low).

### 5. Assigning Tasks
- In the **Tasks** tab, click **"Create Task"**.
- Select the project, priority, and assign it to a team member.
- The member will immediately see the task on their dashboard.

### 6. Task Submission & Review
- **Members**: Click on an assigned task, upload your submission code or files, and provide a description.
- **Admins**: Review submissions, rate the work (1-5 stars), and mark the task as "Done".

---

## 📁 Project Structure

```text
├── accounts/          # User management and authentication
├── projects/          # Project creation and assignment logic
├── tasks/             # Task lifecycle and submission handling
├── ai/                # Gemini AI integration and utilities
├── core/              # Global permissions and helpers
├── frontend/          # Vanilla JS, HTML, and CSS assets
│   ├── css/           # Glassmorphism styles
│   ├── js/            # API wrappers and auth logic
│   ├── pages/         # Dashboard, Projects, Tasks, etc.
│   └── index.html     # Login Page (Root)
└── manage.py          # Django entry point
```

---

## 🤝 Contributing

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

**Developed with ❤️ by Swaraj**
