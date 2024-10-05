from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from startup.portfolio.api.views import ContactViewSet, ExperienceViewSet, ProjectViewSet, SkillViewSet
from startup.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register('experience', ExperienceViewSet, basename="experience")
router.register('skills', SkillViewSet, basename="skill")
router.register('projects', ProjectViewSet, basename="project")
router.register('contact', ContactViewSet, basename="contact")

app_name = "api"
urlpatterns = router.urls
