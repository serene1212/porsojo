from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    FormViewSet,
    ProcessFormViewSet,
    ProcessViewSet,
    QuestionViewSet,
    SendFormTemplateView,
    SendProccessTemplateView,
)

router = DefaultRouter()
router.register("forms", FormViewSet)
router.register("process-forms", ProcessFormViewSet)
router.register("processes", ProcessViewSet)
router.register("questions", QuestionViewSet)

app_name = "surveys"
urlpatterns = [
    path("", include(router.urls)),
    path("processes/<int:pk>/template/", SendProccessTemplateView.as_view(), name="send_process_template"),
    path("forms/<int:pk>/template/", SendFormTemplateView.as_view(), name="send_forms_template"),
]
