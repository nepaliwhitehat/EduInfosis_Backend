from django.urls import path,include
from rest_framework import routers

from student import views

router = routers.DefaultRouter()
# router.register('test',views.TestStudentViewSet)
router.register('get',views.StudentGetViewSet)


urlpatterns = [
	path('',include(router.urls))
]