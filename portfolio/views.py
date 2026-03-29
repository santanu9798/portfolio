from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill
from django.core.mail import send_mail
from django.conf import settings
from .models import Skill, Project, Certification, Publication, ContactMessage

def index(request):
    context = {
        'frontend_skills': Skill.objects.filter(category='frontend'),
        'backend_skills': Skill.objects.filter(category='backend'),
        'projects': Project.objects.all(),
        'certifications': Certification.objects.all(),
        'publications': Publication.objects.all(),
    }
    return render(request, 'portfolio/index.html', context)

def home(request):
    frontend_skills = Skill.objects.filter(category='frontend')
    backend_skills = Skill.objects.filter(category='backend')

    return render(request, 'index.html', {
        'frontend_skills': frontend_skills,
        'backend_skills': backend_skills
    })

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        # Send email
        try:
            send_mail(
                f'Portfolio Contact: {subject}',
                f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
                settings.DEFAULT_FROM_EMAIL,
                ['8579santanu@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, 'Message sent successfully!')
        except Exception as e:
            messages.warning(request, 'Message saved but email failed to send.')
        
        return redirect('portfolio:index')
    
    return redirect('portfolio:index')