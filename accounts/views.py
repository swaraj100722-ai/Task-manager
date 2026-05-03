import logging

from rest_framework import generics, permissions, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserSerializer, RegisterSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import get_user_model

logger = logging.getLogger(__name__)

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RegisterSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def perform_create(self, serializer):
        # Ensure only Admins can create new users
        if self.request.user.role != 'Admin':
            from rest_framework.exceptions import PermissionDenied
            raise PermissionDenied("Only admins can create members.")
        
        user = serializer.save()
        
        # Send Welcome Email
        raw_password = self.request.data.get('password')
        from django.core.mail import send_mail
        from django.conf import settings
        
        subject = "Welcome to the team!"
        
        # HTML version for rich formatting
        html_message = f"""
        <div style="font-family: Arial, sans-serif; line-height: 1.6; color: var(--text-secondary);">
            <p>Dear <strong>{user.name}</strong>,</p>
            <p>Welcome to the team! We’re excited to have you on board.</p>
            <p>Please find your login credentials below:</p>
            
            <div style="background: #f9f9f9; padding: 15px; border-left: 4px solid #10b981; margin: 20px 0;">
                <h3 style="margin-top: 0;">Username: <span style="color: #10b981;">{user.email}</span></h3>
                <h3>Employee ID: <span style="color: #10b981;">{user.employee_id}</span></h3>
                <h3 style="margin-bottom: 0;">Temporary Password: <span style="color: #10b981;">{raw_password}</span></h3>
            </div>

            <h2 style="color: #ef4444; border-bottom: 1px solid #eee; padding-bottom: 5px;">Login URL:</h2>
            <p>You can login using the following URL:</p>
            <a href="https://task-manager-production-eb18.up.railway.app/" style="color: #10b981; text-decoration: none;">Task Manager Login</a>

            <h2 style="color: #ef4444; border-bottom: 1px solid #eee; padding-bottom: 5px;">Important Instructions:</h2>
            <ul>
                <li><strong>For security reasons, please log in using the above credentials and change your password immediately.</strong></li>
                <li>Choose a strong password that includes a mix of letters, numbers, and special characters.</li>
                <li><strong>Do not share your login details with anyone.</strong></li>
            </ul>

            <p>If you face any issues while logging in or changing your password, please contact the IT support team.</p>
            <p>We wish you a great start and a successful journey with us.</p>
            
            <p style="margin-top: 30px;">
                Best regards,<br>
                <strong>Task Manager Team</strong><br>
                [HR / IT Team]
            </p>
        </div>
        """
        
        # Plain text version for fallback
        plain_message = f"""Dear {user.name},
Welcome to the team! We're excited to have you on board.

Username: {user.email}
Employee ID: {user.employee_id}
Temporary Password: {raw_password}

Login URL: https://task-manager-production-eb18.up.railway.app/login

Important Instructions:
* Please log in and change your password immediately.
* Do not share your login details with anyone.

Best regards,
Task Manager Team
[HR / IT Team]
"""

        try:
            logger.info(
                "Attempting to send welcome email to %s (host=%s, port=%s, user=%s)",
                user.email,
                settings.EMAIL_HOST,
                settings.EMAIL_PORT,
                settings.EMAIL_HOST_USER,
            )
            send_mail(
                subject,
                plain_message,
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                html_message=html_message,
                fail_silently=False,
            )
            logger.info("Welcome email sent successfully to %s", user.email)
        except Exception as e:
            logger.error(
                "Failed to send welcome email to %s: %s",
                user.email,
                e,
                exc_info=True,
            )
            # We don't raise here so the user creation still succeeds


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChangePasswordView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not user.check_password(old_password):
            return Response({"detail": "Current password is incorrect."}, status=status.HTTP_400_BAD_REQUEST)
        
        user.set_password(new_password)
        user.save()
        return Response({"detail": "Password changed successfully."})
