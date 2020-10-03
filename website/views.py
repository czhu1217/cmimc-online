from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from website.models import Contest, Problem, Competitor, Exam
from website.forms import UserCreationForm


def home(request):
    return render(request, 'home.html')

def contest_list(request):
    all_contests = Contest.objects.all()
    context = {
        'all_contests': all_contests
    }
    return render(request, 'contest_list.html', context)


def problem_info(request, exam_id, problem_number):
    problem = get_object_or_404(Problem, exam=exam_id, problem_number=problem_number)
    context = {
        'problem': problem,
    }
    return render(request, 'problem_info.html', context)


def submit(request, exam_id, problem_number):
    exam = get_object_or_404(Exam, pk=exam_id)
    problem = get_object_or_404(Problem, exam=exam, problem_number=problem_number)
    competitor = Competitor.objects.mathleteToCompetitor(exam, request.user.mathlete)
    if request.method == 'POST':
        submission = Submission(problem=problem, competitor=competitor, text=request.POST['submission'])
        submission.save()
        submission.grade()
        return redirect('problems', exam=exam)
    elif request.method == 'GET':
        context = {
            'problem': problem,
        }
        return render(request, 'submit.html', context)


# User Account Signup
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
