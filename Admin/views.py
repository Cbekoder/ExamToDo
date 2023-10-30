from django.shortcuts import render, redirect
from .models import *
from .forms import *


def homepage(request):
    return render(request, 'home.html')


def studentlar(request):
    if request.method == 'POST':
        forma = StudentForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect("/studentlar/")
    content = {
        'studentlar' : Author.objects.all(),
        "forma": StudentForm()
    }
    return render(request, 'studentlar.html', content)

def student_gt_3(request):
    content = {
        'studentlar': Author.objects.filter(course__gt = 2)
    }
    return render(request, 'student_gt_3.html', content)

def del_student(request, talaba_id):
    Author.objects.get(id=talaba_id).delete()
    return redirect("/studentlar/")

def yoshi_kattalar(request):
    content = {
        'talabalar' : Author.objects.filter(age__gt=20)
    }
    return render(request, 'katta_talabalar.html', content)

def bitiruvchilar_rejalar(request):
    content = {
        'planlar' : Plan.objects.filter(student_fk__course__gt = 2)
    }
    return render(request, "bitiruvchilar_rejalar.html", content)

def planlar(request):
    if request.method == 'POST':
        forma = PlanForm(request.POST)
        if forma.is_valid():
            forma.save()
        return redirect("/rejalar/")
    content = {
        'planlar' : Plan.objects.all(),
        'forma' : PlanForm()
    }
    return render(request, 'planlar.html', content)

def undone(request):
    content = {
        "planlar" : Plan.objects.filter(done = False)
    }
    return render(request, 'undone.html', content)

def talaba_rejalari(request, talaba_id):
    content = {
        "planlar" : Plan.objects.filter(student_fk__id=talaba_id),
        "student" : Author.objects.get(id = talaba_id)
    }
    return render(request, "talaba_rejalari.html", content)
def del_plan(request, plan_id):
    Plan.objects.get(id=plan_id).delete()
    return redirect("/rejalar/")