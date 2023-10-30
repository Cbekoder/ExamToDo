from django.contrib import admin
from django.urls import path
from Admin.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('studentlar/', studentlar),
    path('yoshi_kattalar/', yoshi_kattalar),
    path('bitiruvchilar/', student_gt_3),
    path('del_student/<int:talaba_id>', del_student),
    path('bitiruvchilar/', student_gt_3),
    path('rejalar/', planlar),
    path('bajarilmagan/', undone),
    path('del_plan/<int:plan_id>', del_plan),
]
