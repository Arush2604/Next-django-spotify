from django.urls import path, re_path
from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView
)

urlpatterns = [
    #regex for <provider>=google,fb,etc 
    re_path(
         r'^o/(?P<provider>\S+)/$',
         CustomProviderAuthView.as_view(),   
         name = 'provider-path'                                    
    ),
    path('jwt/create/', CustomTokenObtainPairView.as_view()),  #.asview because class based view
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
]