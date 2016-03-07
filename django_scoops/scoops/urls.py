from django.conf.urls import url
import views

urlpatterns = [
    url(r'^current_date/$',views.current_date,name='current_date'),
    url(r'^hours_ahead/$',views.hours_ahead,name='hours_ahead'),
        
        ]

