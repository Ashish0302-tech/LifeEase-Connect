from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_user, name='create_user'),
    path('display/', views.display_users, name='display_users'),
    path('remove/<int:user_id>/', views.remove_user, name='remove_user'),
    path('view_plan/<int:user_id>/', views.view_plan, name='view_plan'),
    path('view_plan/<int:user_id>/', views.view_plan2, name='view_plan2'),
    path('view_plan/<int:user_id>/', views.view_plan3, name='view_plan3'),
    path('diet_plan/', views.diet_plan, name='diet_plan'),
    path('exercise_plan/', views.exercise_plan, name='exercise_plan'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('docters/', views.docters, name='docters'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

