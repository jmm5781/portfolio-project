from django.shortcuts import render, get_object_or_404
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects.all().order_by('id')
    return render(request, 'jobs/home.html', {'jobs':jobs})

def detail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    jobs = Job.objects.all().order_by('id')
    job_index = list(jobs).index(job)

    prev_job_id = jobs[job_index - 1].id if job_index > 0 else jobs.last().id
    next_job_id = jobs[job_index + 1].id if job_index < len(jobs) - 1 else jobs.first().id

    return render(request, 'jobs/detail.html', {
        'job': job,
        'prev_job_id': prev_job_id,
        'next_job_id': next_job_id,
    })