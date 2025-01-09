from django.urls import path
from tasks.views import contact, show_task

urlpatterns = [
	path("contact/", contact),
	path("show_task/", show_task),
]