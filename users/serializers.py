from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('name', 'last_name', 'email', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            name=validated_data['name'],
            last_name=validated_data['last_name'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email", "")
        password = data.get("password", "")
        user = User.objects.filter(email=email).first()
        if user and user.check_password(password):
            return user
        raise serializers.ValidationError("Invalid credentials")


class GoogleSignInSerializer(serializers.Serializer):
    access_token = serializers.CharField(required=True)

    class Meta:
        ref_name = 'GoogleSignIn'

    def validate_access_token(self, access_token):
        google_user_data = Google.validate(access_token)
        try:
            userId = google_user_data['sub']
        except Exception as e:
            raise serializers.ValidationError("Invalid token or Expired")

        if google_user_data['aud'] != settings.GOOGLE_CLIENT_ID:
            raise serializers.ValidationError("Could not verify the token")
        email = google_user_data['email']
        name = google_user_data['given_name']
        last_name = google_user_data['family_name']
        provider = 'google'
        return register_social_user(provider, email, name, last_name)


class PasswordResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

    class Meta:
        ref_name = 'PasswordResetRequest'

    def validate_email(self, value):
        if not User.objects.filter(email=value).exists():
            raise serializers.ValidationError("No user with this email address.")
        return value


class PasswordResetSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        ref_name = 'PasswordReset'

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return attrs