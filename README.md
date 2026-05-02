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
- **Accessing the App**: Open your browser and go to `http://127.0.0.1:8000/`.
- **Login**: Enter your registered email and password. Use the "Eye" icon to toggle password visibility.
- **Role Detection**: 
  - **Admin**: Log in with an email ending in `@task.com` to unlock all administrative features.
  - **Member**: Use any other registered email to access the member dashboard.
- **Forgot Password**: If you forget your password, contact your system administrator for a reset.

### 2. Creating & Managing Projects (Admin)
- **Navigation**: Click on the **Projects** link in the sidebar.
- **Creation**: Click the blue **"Create Project"** button. Provide a clear title and a detailed description.
- **Grid View**: Projects are displayed as premium glassmorphism cards. Each card shows the project status, creation date, and assigned members.
- **Details**: Click on any project card to view its specific tasks and team members.

### 3. Managing Team Members (Admin)
- **Add Members**: Go to the **Team Members** tab and click **"Add Member"**.
- **Employee ID**: The system automatically generates a unique, stylized Employee ID for every new user.
- **Role Assignment**: Choose between **Member** (default) or **Admin**.
- **User Management**: You can edit user details or delete accounts directly from the table.

### 4. Creating & Assigning Tasks
- **Creation**: In the **Tasks** tab, use the **"Create Task"** button.
- **Assignment**: Select a project and assign the task to a specific team member.
- **Priority**: Set the priority level (High, Medium, Low) which will be color-coded in the UI.
- **Deadlines**: Tasks track their creation and update times for progress monitoring.

### 5. Using AI Task Intelligence
- **AI Assistant Page**: Access the dedicated **AI Assistant** tab for general queries.
- **Task Breakdown**: When creating a complex task, paste the description into the "Task Intelligence" block and click **"Break Down"**. The AI will return a list of smaller, manageable sub-tasks.
- **Priority Suggestion**: If you're unsure of a task's urgency, enter the title and description and click **"Suggest Priority"**. The AI will recommend a priority level based on the task's context.

### 6. Task Submission Flow (Member)
- **Viewing Tasks**: Members see a "Recent Tasks" table on their dashboard and a full list in the **Tasks** tab.
- **Submission**: Click on an assigned task to open the submission modal.
- **Details**: Provide a summary of the work done and paste your code or include links to the completed work.
- **Status**: The task status will change to "Review Pending" once submitted.

### 7. Review & Rating System (Admin)
- **Notifications**: Admins can see which tasks are pending review in the task list.
- **Reviewing**: Click on a pending task to see the member's submission.
- **Rating**: Admins can rate the submission from 1 to 5 stars using the interactive rating UI.
- **Completion**: Once reviewed and rated, the Admin can mark the task as **"Done"**, moving it to the project's completed history.

### 8. Settings & Customization
- **Theme Toggle**: Use the moon/sun icon in the top navbar to switch between **Dark Mode** and **Light Mode**.
- **Profile**: Update your profile information or change your password in the **Settings** tab.

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
