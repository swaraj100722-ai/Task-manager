const API = {
    async request(endpoint, method = 'GET', body = null) {
        const token = localStorage.getItem('access_token');
        const headers = {
            'Authorization': token ? `Bearer ${token}` : ''
        };

        if (!(body instanceof FormData)) {
            headers['Content-Type'] = 'application/json';
        }

        const options = { method, headers };
        if (body) {
            options.body = (body instanceof FormData) ? body : JSON.stringify(body);
        }

        try {
            const response = await fetch(`${API_BASE}${endpoint}`, options);
            if (response.status === 401) {
                // Handle token expiration (simplified)
                Auth.logout();
                return null;
            }
            if (!response.ok) return null;
            if (response.status === 204) return true;
            return await response.json();
        } catch (error) {
            console.error('API request error:', error);
            return null;
        }
    },

    // Users
    getUsers() {
        return this.request('/accounts/users/');
    },

    // Dashboard
    getDashboard() {
        return this.request('/projects/dashboard/');
    },

    // Projects
    getProjects() {
        return this.request('/projects/');
    },

    getProject(id) {
        return this.request(`/projects/${id}/`);
    },

    createProject(data) {
        return this.request('/projects/', 'POST', data);
    },

    // Tasks
    getTasks(projectId = null) {
        let url = '/tasks/';
        if (projectId) url += `?project=${projectId}`;
        return this.request(url);
    },

    createTask(data) {
        return this.request('/tasks/', 'POST', data);
    },

    updateTask(id, data) {
        return this.request(`/tasks/${id}/`, 'PUT', data);
    },

    // AI
    aiGenerateTasks(description) {
        return this.request('/ai/generate-tasks/', 'POST', { description });
    },

    aiSuggestPriority(title, description) {
        return this.request('/ai/suggest-priority/', 'POST', { title, description });
    },

    aiSummary(tasksData) {
        return this.request('/ai/summary/', 'POST', { tasks: tasksData });
    },

    // UI Helpers
    showLoader() {
        const loader = document.getElementById('screen-loader');
        if (loader) loader.classList.remove('hidden');
    },

    hideLoader() {
        const loader = document.getElementById('screen-loader');
        if (loader) loader.classList.add('hidden');
    },

    setButtonLoading(btn, isLoading, loadingText = 'Processing...') {
        if (!btn) return;
        if (isLoading) {
            if (!btn.dataset.originalContent) {
                btn.dataset.originalContent = btn.innerHTML;
            }
            btn.innerHTML = `<i class="fas fa-spinner fa-spin"></i> ${loadingText}`;
            btn.disabled = true;
        } else {
            if (btn.dataset.originalContent) {
                btn.innerHTML = btn.dataset.originalContent;
                delete btn.dataset.originalContent;
            }
            btn.disabled = false;
        }
    }
};
