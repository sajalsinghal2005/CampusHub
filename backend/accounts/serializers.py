from django.contrib.auth import authenticate
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from students.models import Student


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        user = authenticate(
            request=self.context.get("request"),
            username=email,
            password=password,
        )
        if not user:
            raise serializers.ValidationError(
                {"non_field_errors": ["Unable to log in with provided credentials."]}
            )
        if not user.is_active:
            raise serializers.ValidationError(
                {"non_field_errors": ["User account is disabled."]}
            )
        data["user"] = user
        return data


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        source="emails",
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with this email already exists.",
            )
        ],
    )

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["full_name", "email", "password"]

    def create(self, validated_data):
        password = validated_data.pop("password")

        email = validated_data.get("emails")

        base_username = email.split("@")[0]
        username = base_username
        count = 1

        while User.objects.filter(username=username).exists():
            username = f"{base_username}{count}"
            count += 1

        validated_data["username"] = username

        user = User(**validated_data)
        user.set_password(password)

        try:
            user.save()
        except IntegrityError:
            raise serializers.ValidationError(
                {"email": "Email already exists"}
            )

        Student.objects.create(user=user)

        return user


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source="emails")

    class Meta:
        model = User
        fields = ["id", "full_name", "email", "role"]
