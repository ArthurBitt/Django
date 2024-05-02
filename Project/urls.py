
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.model_pagination.urls')),
    path('', include('app.form_model.urls'))

]

