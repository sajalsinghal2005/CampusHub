from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User
from students.models import Student


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

        email_value = validated_data.get("emails")
        if email_value and "username" not in validated_data:
            base_username = email_value.split("@")[0]
            username = base_username
            counter = 1
            while User.objects.filter(username=username).exists():
                username = f"{base_username}{counter}"
                counter += 1
            validated_data["username"] = username

        user = User(**validated_data)
        user.set_password(password)
        try:
            user.save()
        except IntegrityError:
            raise serializers.ValidationError(
                {"email": "A user with this email already exists."}
            )

        Student.objects.create(user=user)

        return user