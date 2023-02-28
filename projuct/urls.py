from django.contrib import admin
from django.urls import path
from projuct import views
from rest_framework.urlpatterns import format_suffix_patterns
from projuct import views1
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('products/', views.product_list),
    path('products/<int:id>', views.product_detail),
    
    path('categorys/', views1.category_list),
    path('categorys/<int:id>', views1.category_detail),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += staticfiles_urlpatterns ()