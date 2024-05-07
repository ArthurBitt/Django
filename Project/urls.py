from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pagination_model/', include('app.model_pagination.urls')),
    path('search_model/', include('app.search_model.urls')),
    path('authentication_model/', include('app.authentication_model.urls')),
    path('form_model/', include('app.form_model.urls'))

]

