from django.urls import path

from .views import SignUp, LikeNews, LikeCommentList, SignIn, LogOut


urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', SignIn.as_view(), name='signin'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('likenews/<slug:slug>', LikeNews.as_view(), name='likenewss'),
    path('likecomment/<int:id>', LikeCommentList.as_view(), name='likecomment'),
]
