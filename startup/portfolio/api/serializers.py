import re
from rest_framework import serializers
from startup.portfolio.models import Experience, Skill, Project, Contact

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'
        read_only_fields = ["user"]

    def create(self, validated_data):
        user = self.context['request'].user
        experience = Experience.objects.create(user=user, **validated_data)
        return experience

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'
        read_only_fields = ['user']

    def validate_name(self, value):
        """Validate that name is a list of strings."""
        if not isinstance(value, list):
            raise serializers.ValidationError("Skills must be provided as a list.")
        if not all(isinstance(skill, str) for skill in value):
            raise serializers.ValidationError("Each skill must be a string.")
        return value

    def create(self, validated_data):
        """Override the create method to handle the skills array."""
        user = self.context['request'].user
        return Skill.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        """Override the update method to handle the skills array."""
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        read_only_fields = ["user"]

    def create(self, validated_data):
        user = self.context['request'].user
        project = Project.objects.create(user=user, **validated_data)
        return project

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ["user"]
    
    def validate_mobile(self, value):
        """Validate the mobile field."""
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Mobile number must be exactly 10 digits.")
        return value

    def validate_work_phone(self, value):
        """Validate the work phone field."""
        if not value.isdigit() or len(value) != 10:
            raise serializers.ValidationError("Work phone number must be exactly 10 digits.")
        return value

    def validate_email(self, value):
        """Validate the email field."""
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', value):
            raise serializers.ValidationError("Enter a valid email address.")
        return value

    def create(self, validated_data):
        user = self.context['request'].user
        contact = Contact.objects.create(user=user, **validated_data)
        return contact