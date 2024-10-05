from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from startup.portfolio.models import Experience, Skill, Project, Contact
from startup.portfolio.api.serializers import ExperienceSerializer, SkillSerializer, ProjectSerializer, ContactSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can access this view

    def get_queryset(self):
        user = self.request.user
        return Experience.objects.filter(user=user)  # Assuming 'user' is a ForeignKey in Experience model

class SkillViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Skill.objects.filter(user=user)  # Assuming 'user' is a ForeignKey in Skill model

class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user=user)  # Assuming 'user' is a ForeignKey in Project model

class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Contact.objects.filter(user=user)  # Assuming 'user' is a ForeignKey in Contact model
