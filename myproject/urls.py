
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/",include('users.urls')),
    path("api/profile/",include('userprofile.urls')),    

    path('api/diary/',include('diary.urls'))
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 


admin.site.site_header = "Resturant Visitors Dairy"
admin.site.site_title = "Resturant Visitors Admin Portal"
admin.site.index_title = "Welcome to Resturant Portal"

