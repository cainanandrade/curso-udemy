from django.conf.urls import url
from accounts.views import add_user, user_login, user_logout, change_password

urlpatterns = [
    url(r'^add-user/$', add_user, name="add_user"),
    url(r'^user-login/$', user_login, name="user_login"),
    url(r'^user-logout/$', user_logout, name="user_logout"),
    url(r'^change-password/$', change_password, name="change_password"),
]