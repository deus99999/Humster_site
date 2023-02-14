from django.urls import path
from .views import MainView, PostDetailView, SignUpView, SignInView, \
    SearchResultView, WriteArticleView, AboutView, create_article
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('blog/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('search/', SearchResultView.as_view(), name='search_results'),
    path('write_article/', create_article, name='write_article'),
    # path('new_article/<int>:post_id/', new_article, name="new_article"),
    path('about/', AboutView.as_view(), name='about'),

]

