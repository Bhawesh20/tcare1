from django.conf.urls import url
from . import views

app_name = 'service'

urlpatterns = [
	url(r'^$', views.home, name='index'),
	url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^appointment/$', views.appointment, name='appointment'),
	url(r'^add_appointment/$', views.add_appointment, name='add_appointment'),
	url(r'^prescription/$', views.prescription, name='prescription'),
	url(r'^add_prescription/$', views.add_prescription, name='add_prescription'),
	url(r'^package/$', views.package, name='package'),
	url(r'^add_package/$', views.add_package, name='add_package'),
	url(r'^home/$', views.home, name='home'),
	url(r'^logout/$', views.logout_user, name='logout_user'),
	url(r'^user/$', views.user_detail, name = 'user_detail'),
	url(r'^edit_user/(?P<id>\d+)/$', views.edit_user, name = 'edit_user'),
]