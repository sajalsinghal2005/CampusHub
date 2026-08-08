from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = [
            "id",
            "user",
            "branch",
            "semester",
            "cgpa",
            "phone",
            "github",
            "linkedin",
            "resume",
        ]
        read_only_fields = ["id", "user"]