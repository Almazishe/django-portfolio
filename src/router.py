from django.urls import path, include


urlpatterns = [
    path('', include(('src.posts.urls', 'post'))),
    path('accounts/', include(('src.accounts.urls', 'account')))
]