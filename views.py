from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Skill, Project, Experience, Education, Contact
from .forms import ContactForm


def home(request):
    skills_by_category = {}
    for skill in Skill.objects.all():
        cat = skill.get_category_display()
        skills_by_category.setdefault(cat, []).append(skill)

    projects = Project.objects.prefetch_related('bullets').all()
    experiences = Experience.objects.prefetch_related('bullets').all()
    education = Education.objects.all()
    form = ContactForm()

    context = {
        'skills_by_category': skills_by_category,
        'projects': projects,
        'experiences': experiences,
        'education': education,
        'form': form,
    }
    return render(request, 'portfolio/index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
            messages.success(request, 'Your message has been sent!')
            return redirect('home')
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors})
    return redirect('home')
