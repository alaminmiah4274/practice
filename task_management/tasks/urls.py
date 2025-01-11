from django.urls import path
from tasks.views import contact, show_task, show_specific_task

urlpatterns = [
	path("contact/", contact),
	path("show_task/", show_task),
	path("show_task/<int:id>", show_specific_task),
]