from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/user/', include('apps.user.urls')),

    path('api/workouts/', include('apps.workout_plan.urls')),

    path('api/exercises/', include('apps.exercises.urls')),

    path('api/tracker/', include('apps.tracker.urls')),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),  # OpenAPI schema
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),  # Swagger UI
]
