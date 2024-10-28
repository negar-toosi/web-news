from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request=None, username=None, password=None, **kwargs):
        user_model = get_user_model()

        if username is None:
            username = kwargs.get(user_model.USERNAME_FIELD)  # Get the identifier (email or username)

        # Now perform your query
        try:
            user = user_model.objects.get(email=username)  # Use the correct field based on USERNAME_FIELD
        except user_model.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None