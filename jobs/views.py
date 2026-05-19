
from django.shortcuts import render, redirect
from .models import JobApplication
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/users/login/')
def add_job(request):

    if request.method == "POST":

        company_name = request.POST.get('company_name')
        role = request.POST.get('role')
        status = request.POST.get('status')
        applied_date = request.POST.get('applied_date')
        notes = request.POST.get('notes')
        JobApplication.objects.create(

            user=request.user,

            company_name=company_name,

            role=role,

            status=status,

            applied_date=applied_date,

            notes=notes
        )

        return redirect('/')

    return render(request, 'add_job.html')

@login_required(login_url='/users/login/')
def update_job(request, id):

    job = JobApplication.objects.get(id=id)

    if request.method == "POST":

        job.company_name = request.POST.get('company_name')

        job.role = request.POST.get('role')

        job.status = request.POST.get('status')

        job.applied_date = request.POST.get('applied_date')

        job.notes = request.POST.get('notes')

        job.save()

        return redirect('/')

    context = {
        'job': job
    }

    return render(request, 'update_job.html', context)

@login_required(login_url='/users/login/')
def delete_job(request, id):

    job = JobApplication.objects.get(id=id)

    job.delete()

    return redirect('/')