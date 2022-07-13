
from django.urls import path
from .views import ( ContactViewClassBased, FindBlogAPI , 
DetailViewPost , AddPost,
DeleteBlogAPI , AddPostAPI,
UpdateBlogAPI , ListViewPostall, 
searchview , AddPostClassBased, DeleteViewClassBased,
ContactViewClassBased , contactview, UpdateViewClassBased
)

urlpatterns = [
    # path('blog/' , BlogView , name='blogviewname'),
    path('' , ListViewPostall.as_view() , name="ListViewPostallNAME"),
    path('ContactClassBased/Contacts/' , contactview.as_view() , name="ListViewcontactallNAME"),
    path('search/' , searchview , name="searchviewname"),
    path('Edit/<int:pk>' , UpdateViewClassBased.as_view() , name='EditPostNAME'),
    path('delete/<int:pk>' , DeleteViewClassBased.as_view() , name='DeletePostNAME'),
    path('add/' , AddPost , name='AddPostNAME'),
    path('AddClassBased/' , AddPostClassBased.as_view() , name='AddPostClassBasedNAME'),
    path('ContactClassBased/' , ContactViewClassBased.as_view() , name='ContactClassBasedNAME'),
    path('AddPostAPI/' , AddPostAPI , name='AddPostAPIName'),
    path('FindAPI/<int:id>/' , FindBlogAPI , name='FindBlogAPIName'),
    path('Find/<int:pk>' , DetailViewPost.as_view() , name="DetailViewPostNAME"),   
    path('DeleteAPI/<int:id>/' , DeleteBlogAPI , name='DeleteBlogAPIName'),   
    path('UpdateAPI/<int:id>/' , UpdateBlogAPI , name='UpdateBlogAPIName'),
] 
 