from django.contrib import admin
from django.urls import path, include
import blogapp.views
import portfolio.views
#습관처럼 외우기
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>', blogapp.views.detail, name="detail"),
    path('blog/new/', blogapp.views.new, name='new'),
    path('blog/create/', blogapp.views.create, name="create"),
    path('blog/portfolio/', portfolio.views.portfolio, name="portfolio"),  
    path('blog/accounts/', include('accounts.urls')), 
    path('blog/newblog/', blogapp.views.blogpost, name="newblog"),
 
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
