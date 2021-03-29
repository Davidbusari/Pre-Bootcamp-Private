from django.urls import path
from . import views

urlpatterns = [

    path('jobs', views.display_jobs),
    path('jobs/new', views.Process_display_job_creation),
    path('jobs/create', views.process_new_job),
    path("job/details/<jobid>", views.display_job),
    path("editJob/<jobid>",views.displayedit),
    path("job/edit/<jobtoeditid>", views.editjob),
    path('cancelJob/<jobid>', views.cancelJob),
    path('addJob/<jobid>', views.addJob),
    path('doneJob/<jobid>', views.done_job),
    path('addJob/<jobtodisplayid>', views.addJobfromview),



    


]