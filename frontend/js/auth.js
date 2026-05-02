const API_BASE = 'https://task-manager-swaraj.up.railway.app/api';

const Auth = {
    async login(email, password) {
        try {
            const response = await fetch(`${API_BASE}/accounts/login/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ email, password })
            });
            const data = await response.json();
            if (response.ok) {
                localStorage.setItem('access_token', data.access);
                localStorage.setItem('refresh_token', data.refresh);
                localStorage.setItem('user', JSON.stringify(data.user));
                return true;
            }
            return false;
        } catch (error) {
            console.error('Login error:', error);
            return false;
        }
    },

    async register(userData) {
        try {
            const response = await fetch(`${API_BASE}/accounts/users/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${localStorage.getItem('access_token')}`
                },
                body: JSON.stringify(userData)
            });
            if (response.ok) return true;
            const data = await response.json();
            return data.detail || data.email || data.employee_id || false;
        } catch (error) {
            console.error('Register error:', error);
            return false;
        }
    },

    async fetchProfile() {
        const token = localStorage.getItem('access_token');
        if (!token) return null;

        try {
            const response = await fetch(`${API_BASE}/accounts/profile/`, {
                headers: { 'Authorization': `Bearer ${token}` }
            });
            if (response.ok) {
                const data = await response.json();
                localStorage.setItem('user', JSON.stringify(data));
                return data;
            }
            return null;
        } catch (error) {
            return null;
        }
    },

    logout() {
        localStorage.clear();
        const path = window.location.pathname;
        if (path.includes('/pages/')) {
            window.location.href = '../index.html';
        } else {
            window.location.href = 'index.html';
        }
    },

    confirmLogout() {
        console.log('Logout requested');
        if (!document.getElementById('logoutModal')) {
            const modal = document.createElement('div');
            modal.id = 'logoutModal';
            modal.className = 'modal-overlay';
            modal.innerHTML = `
                <div class="glass animate-fade" style="padding: 2rem; width: 350px; text-align: center;">
                    <i class="fas fa-sign-out-alt" style="font-size: 3rem; color: var(--danger); margin-bottom: 1.5rem;"></i>
                    <h3 style="margin-bottom: 0.5rem;">Confirm Logout</h3>
                    <p style="color: var(--text-muted); margin-bottom: 2rem;">Are you sure you want to log out?</p>
                    <div style="display: flex; gap: 1rem;">
                        <button onclick="document.getElementById('logoutModal').style.display='none'" class="btn" style="flex: 1; border: 1px solid var(--border);">No</button>
                        <button onclick="Auth.logout()" class="btn btn-danger" style="flex: 1;">Yes, Logout</button>
                    </div>
                </div>
            `;
            document.body.appendChild(modal);
        }
        document.getElementById('logoutModal').style.display = 'flex';
    },

    getUser() {
        const user = localStorage.getItem('user');
        return user ? JSON.parse(user) : null;
    },

    isAuthenticated() {
        return !!localStorage.getItem('access_token');
    }
};

// Protect routes
if (!Auth.isAuthenticated() && !window.location.pathname.endsWith('index.html') && !window.location.pathname.includes('register.html')) {
    const isInsidePages = window.location.pathname.includes('/pages/');
    window.location.href = isInsidePages ? '../index.html' : 'index.html';
}

window.Auth = Auth;

// Theme Management
const Theme = {
    init() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        this.apply(savedTheme);
    },
    apply(theme) {
        document.body.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);

        // Update any theme toggles on the page
        const toggles = document.querySelectorAll('.theme-toggle');
        toggles.forEach(btn => {
            btn.innerHTML = theme === 'light' ? '<i class="fas fa-moon"></i>' : '<i class="fas fa-sun"></i>';
        });
    },
    toggle() {
        const current = document.body.getAttribute('data-theme') || 'light';
        const next = current === 'light' ? 'dark' : 'light';
        this.apply(next);
    }
};

// Device Restriction System
const DeviceRestriction = {
    check() {
        const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        const isSmallScreen = window.innerWidth <= 768;

        if (isMobile || isSmallScreen) {
            this.showRestriction();
        } else {
            this.removeRestriction();
        }
    },

    showRestriction() {
        if (document.getElementById('mobileRestrictionOverlay')) return;

        const overlay = document.createElement('div');
        overlay.id = 'mobileRestrictionOverlay';
        overlay.style = `
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle at center, rgba(30, 41, 59, 0.9) 0%, rgba(15, 23, 42, 0.98) 100%);
            backdrop-filter: blur(15px);
            z-index: 99999; display: flex; align-items: center; justify-content: center;
            padding: 2rem; animation: fadeIn 0.5s ease;
        `;

        overlay.innerHTML = `
                        <!-- Full Screen Overlay -->
            <div id="deviceWrapper">
                
                <div class="glass animate-fade">
                    
                    <div class="icon-box">
                        <i class="fas fa-desktop"></i>
                    </div>

                    <h2>Desktop Only Workspace</h2>

                    <p>
                        To maintain professional standards, this platform is restricted to 
                        <strong>laptops and desktops</strong>. Please switch devices to continue.
                    </p>

                    <button onclick="window.location.reload()">
                        Reconnect on Desktop
                    </button>

                </div>

            </div>

            <style>
                /* Fullscreen Centering Wrapper */
            #deviceWrapper {
                position: fixed;
                inset: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                padding: 20px;
                background: rgba(15, 23, 42, 0.85);
                backdrop-filter: blur(8px);
                z-index: 100000;
            }

            /* Card */
            .glass {
                width: 100%;
                max-width: 440px;
                padding: 3rem 2rem;
                text-align: center;
                border-radius: 20px;
                border: 1px solid rgba(99, 102, 241, 0.2);
                background: rgba(30, 41, 59, 0.7);
                box-shadow: 0 0 50px rgba(99, 102, 241, 0.1),
                            0 25px 50px -12px rgba(0,0,0,0.5);
            }

            /* Icon */
            .icon-box {
                width: 80px;
                height: 80px;
                margin: 0 auto 2rem;
                border-radius: 20px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 2.5rem;
                color: #fff;
                background: linear-gradient(135deg, #6366f1, #a855f7);
                box-shadow: 0 15px 30px rgba(99, 102, 241, 0.3);
                animation: float 3s ease-in-out infinite;
            }

            /* Title */
            .glass h2 {
                font-size: 1.8rem;
                font-weight: 800;
                color: #fff;
                margin-bottom: 1rem;
            }

            /* Text */
            .glass p {
                color: #cbd5e1;
                font-size: 1rem;
                line-height: 1.6;
                margin-bottom: 2rem;
            }

            /* Button */
            .glass button {
                width: 100%;
                padding: 14px;
                font-weight: 700;
                font-size: 0.95rem;
                background: #fff;
                color: #0f172a;
                border: none;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.3s;
            }

            .glass button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
            }

            /* Animation */
            @keyframes float {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-8px); }
            }

            /* Mobile Adjustments */
            @media (max-width: 480px) {
                .glass {
                    padding: 2.5rem 1.5rem;
                }

                .glass h2 {
                    font-size: 1.5rem;
                }

                .glass p {
                    font-size: 0.95rem;
                }
            }
            </style>

            <script>
                document.body.style.overflow = "hidden";
                document.documentElement.style.overflow = "hidden";
            </script>
        `;

        document.body.appendChild(overlay);
        document.body.style.overflow = 'hidden';

        // Add custom animations
        if (!document.getElementById('restrictionStyles')) {
            const style = document.createElement('style');
            style.id = 'restrictionStyles';
            style.textContent = `
                @keyframes pulseFloat {
                    0% { transform: rotate(-5deg) scale(1); box-shadow: 0 15px 30px rgba(99, 102, 241, 0.3); }
                    50% { transform: rotate(5deg) scale(1.05); box-shadow: 0 25px 50px rgba(168, 85, 247, 0.4); }
                    100% { transform: rotate(-5deg) scale(1); box-shadow: 0 15px 30px rgba(99, 102, 241, 0.3); }
                }
            `;
            document.head.appendChild(style);
        }
    },

    removeRestriction() {
        const overlay = document.getElementById('mobileRestrictionOverlay');
        if (overlay) {
            overlay.remove();
            document.body.style.overflow = '';
        }
    },

    init() {
        this.check();
        window.addEventListener('resize', () => this.check());
    }
};

window.Auth = Auth;
document.addEventListener('DOMContentLoaded', () => {
    Theme.init();
    DeviceRestriction.init();
});

// Custom Notification & Confirmation System
const Notification = {
    show(message, type = 'success') {
        const modal = document.createElement('div');
        modal.className = 'modal-overlay';
        modal.style.display = 'flex';
        modal.style.background = 'rgba(0,0,0,0.3)';

        const color = type === 'success' ? 'var(--success)' : 'var(--danger)';
        const icon = type === 'success' ? 'fa-check-circle' : 'fa-exclamation-circle';

        modal.innerHTML = `
            <div class="glass animate-fade" style="padding: 2rem; width: 350px; text-align: center; border-top: 4px solid ${color};">
                <i class="fas ${icon}" style="font-size: 3rem; color: ${color}; margin-bottom: 1rem;"></i>
                <h3 style="margin-bottom: 1rem;">${type === 'success' ? 'Success' : 'Attention'}</h3>
                <p style="color: var(--text-muted); margin-bottom: 1.5rem;">${message}</p>
                <button onclick="this.closest('.modal-overlay').remove()" class="btn btn-primary" style="width: 100%;">OK</button>
            </div>
        `;
        document.body.appendChild(modal);
    },

    confirm(message, onConfirm) {
        const modal = document.createElement('div');
        modal.className = 'modal-overlay';
        modal.style.display = 'flex';
        modal.innerHTML = `
            <div class="glass animate-fade" style="padding: 2rem; width: 380px; text-align: center;">
                <i class="fas fa-question-circle" style="font-size: 3rem; color: var(--primary); margin-bottom: 1rem;"></i>
                <h3 style="margin-bottom: 1rem;">Confirm Action</h3>
                <p style="color: var(--text-muted); margin-bottom: 2rem;">${message}</p>
                <div style="display: flex; gap: 1rem;">
                    <button onclick="this.closest('.modal-overlay').remove()" class="btn" style="flex: 1; border: 1px solid var(--border);">Cancel</button>
                    <button id="confirmYesBtn" class="btn btn-primary" style="flex: 1;">Confirm</button>
                </div>
            </div>
        `;
        document.body.appendChild(modal);
        document.getElementById('confirmYesBtn').onclick = () => {
            modal.remove();
            onConfirm();
        };
    }
};

window.Notification = Notification;
