from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.

def display_jobs(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print(request.session.get('user_id'))
    allthisUserjobs = User.objects.first().jobs_joined.all()
    other_jobs = Job.objects.exclude(users_joined = request.session.get('user_id'))
    alljobs = Job.objects.all()
    context = {
        'thisUser': User.objects.get(id=request.session['user_id']),
        'thisUserjobs' :allthisUserjobs,
        'allJobs': alljobs,
        'otherjobs' : other_jobs 
    }

    return render(request, "dashboard.html", context)

def Process_display_job_creation(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print(request.session.get('user_id'))

    context = {
        'thisUser': User.objects.get(id=request.session['user_id']),
        "allmessages": messages,
    }
    return render(request, 'create_job.html', context )


def process_new_job(request):
    errors = Job.objects.job_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/jobs/new')

    currentUser = User.objects.get(id=request.session['user_id'])
    allcate = (request.POST['edu']), request.POST['avia'], request.POST['food'],  request.POST['other']
    new_job = Job.objects.create(
        Title = request.POST['title'],
        Description = request.POST['desc'],
        Location = request.POST['location'],
        Categories = allcate,
        Posted_by = currentUser
    )
    new_job.users_joined.add(currentUser)
    new_job.save()
    return redirect('/jobs')


def display_job(request, jobid):
    job_display = Job.objects.get(id = jobid)
    print(job_display.Posted_by)
    currentUser = User.objects.get(id=request.session['user_id'])
    
    context = {
        'jobtodisplay' : job_display,
        'thisUser' : currentUser,
        
    }
    return render(request, 'job_details.html', context)


def displayedit(request, jobid):
    job_edit = Job.objects.get(id = jobid)
    currentUser = User.objects.get(id=request.session['user_id'])

    context = {
        'thisUser' : currentUser,
        'jobtoedit' : job_edit
    }

    return render(request, 'edit_job.html', context)

def editjob(request, jobtoeditid):
    print(jobtoeditid)
    errors = Job.objects.job_validation(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            urls = (f"/editJob/{jobtoeditid}")
        return redirect(urls)
    currentUser = User.objects.get(id=request.session['user_id'])
    job_to_update = Job.objects.get(id= jobtoeditid)
    job_to_update.Title = request.POST['title']
    job_to_update.Description = request.POST['desc']
    job_to_update.Location = request.POST['location']
    job_to_update.Posted_by =currentUser
    job_to_update.save()

    return redirect('/jobs')

def addJob(request, jobid):
    jobtoadd = Job.objects.get(id=jobid)
    currentUser = User.objects.get(id=request.session['user_id'])
    jobtoadd.users_joined.add(currentUser)
    jobtoadd.save()
    return redirect('/jobs')



def cancelJob(request, jobid):
    job_to_delete = Job.objects.get(id=jobid)	# let's retrieve a single movie,
    job_to_delete.delete()
    # job_to_cancel = Job.objects.get(id=jobid)
    # currentUser = User.objects.get(id=request.session['user_id'])
    # job_to_cancel.users_joined.remove(currentUser)
    # job_to_cancel.save()
    return redirect('/jobs')


def done_job(request, jobid):
    job_to_cancel = Job.objects.get(id=jobid)
    currentUser = User.objects.get(id=request.session['user_id'])
    job_to_cancel.users_joined.remove(currentUser)
    job_to_cancel.save()
    return redirect('/jobs') 

def addJobfromview(request, jobtodisplayid):
    jobtoadd = Job.objects.get(id=jobtodisplayid)
    currentUser = User.objects.get(id=request.session['user_id'])
    jobtoadd.users_joined.add(currentUser)
    jobtoadd.save()
    return redirect('/jobs')
