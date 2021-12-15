from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic.base import TemplateView
from rest_framework import routers

# Router for the API. Exceptions (for now) are the auth/* routes, which don't need to be in the /api/ router

router = routers.DefaultRouter()

api_patterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include(router.urls))
]

# URL Patterns

urlpatterns = [
    # Site URLs
    path('admin/', admin.site.urls),
    path('api/', include(api_patterns)),

    # These URLs are used to generate email content
    re_path(r'^password-reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]+)/$',
            TemplateView.as_view(template_name="index.html"),
            name='password_reset_confirm'),
    re_path(r'^confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(template_name='index.html'),
            name='account_confirm_email'),

    # Catch-All URL
    re_path(r'^(?!admin/|api/).*', TemplateView.as_view(template_name='index.html'))
]
