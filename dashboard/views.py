from django.shortcuts import render
from jobs.models import JobApplication
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login/')
def home(request):

    jobs = JobApplication.objects.filter(
        user=request.user
    )

    # Search
    search = request.GET.get('search')

    if search:
        jobs = jobs.filter(company_name__icontains=search)

    # Filter
    status = request.GET.get('status')

    if status:
        jobs = jobs.filter(status=status)

    # Dashboard Counts
    total_jobs = JobApplication.objects.count()

    interview_jobs = JobApplication.objects.filter(
        status='Interview'
    ).count()

    selected_jobs = JobApplication.objects.filter(
        status='Selected'
    ).count()

    rejected_jobs = JobApplication.objects.filter(
        status='Rejected'
    ).count()

    context = {

        'jobs': jobs,

        'total_jobs': total_jobs,

        'interview_jobs': interview_jobs,

        'selected_jobs': selected_jobs,

        'rejected_jobs': rejected_jobs,
    }

    return render(request, 'index.html', context)