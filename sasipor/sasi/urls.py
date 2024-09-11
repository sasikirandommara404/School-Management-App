from django.urls import path,include
from sasi import views

urlpatterns = [
    path("",views.home,name="home"),
    path("signup/",views.signup,name="signup"),
    path("for/",views.for_get,name="for"),
    path("update/",views.update,name="update"),
    path("main/",views.main,name="main"),
    path("adminhome",views.adminview,name="adminhome"),
    path("stuupload/",views.student_details,name="stuupload"),
    path("fill/",views.filling,name="fill"),
    path("show/",views.show,name="show"),
    path("show1/",views.show1,name="show1"),
    path("res/",views.resup,name="res"),
    path("result/",views.results,name="result"),
    path("f/",views.updateform,name="f"),
    path("final/",views.finall,name="final"),
    path("resu/",views.res_function,name="resu"),
    path("check/",views.checking_res,name="check")

   

]