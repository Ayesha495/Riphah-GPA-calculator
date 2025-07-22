from django.shortcuts import render, redirect
from .forms import GPAForm, SubjectForm, CGPAForm, SemesterForm

def home_view(request):
    return render(request, 'calculator/home.html')

def gpa_form_view(request):
    if request.method == 'POST':
        form = GPAForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['subject_count']
            return redirect(f'/gpa/subjects/{count}/')
    else:
        form = GPAForm()
    return render(request, 'calculator/gpa_form.html', {'form': form})

def subject_input_view(request, count):
    count = int(count)
    SubjectFormSet = [SubjectForm(request.POST or None, prefix=str(i)) for i in range(count)]

    if request.method == 'POST' and all(f.is_valid() for f in SubjectFormSet):
        total_points = 0
        total_credits = 0
        for form in SubjectFormSet:
            marks = form.cleaned_data['marks']
            credit = form.cleaned_data['credit']

            if marks >= 90:
                grade_point = 4.0
            elif marks >= 80:
                grade_point = 4.0
            elif marks >= 70:
                grade_point = 3.0 + ((marks - 70) / 9) * 0.9
            elif marks >= 60:
                grade_point = 2.0 + ((marks - 60) / 9) * 0.9
            elif marks >= 50:
                grade_point = 1.0 + ((marks - 50) / 9) * 0.9
            else:
                grade_point = 0.0

            total_points += grade_point * credit
            total_credits += credit

        gpa = round(total_points / total_credits, 2)
        return render(request, 'calculator/gpa_result.html', {'gpa': gpa})

    return render(request, 'calculator/subject_form.html', {'forms': SubjectFormSet})

def cgpa_form_view(request):
    if request.method == 'POST':
        form = CGPAForm(request.POST)
        if form.is_valid():
            count = form.cleaned_data['semester_count']
            return redirect(f'/cgpa/semesters/{count}/')
    else:
        form = CGPAForm()
    return render(request, 'calculator/cgpa_form.html', {'form': form})

def semester_input_view(request, count):
    count = int(count)
    SemesterFormSet = [SemesterForm(request.POST or None, prefix=str(i)) for i in range(count)]

    if request.method == 'POST' and all(f.is_valid() for f in SemesterFormSet):
        total_points = 0
        total_credits = 0
        for form in SemesterFormSet:
            gpa = form.cleaned_data['gpa']
            credit = form.cleaned_data['credit']
            total_points += gpa * credit
            total_credits += credit

        cgpa = round(total_points / total_credits, 2)
        return render(request, 'calculator/cgpa_result.html', {'cgpa': cgpa})

    return render(request, 'calculator/semester_form.html', {'forms': SemesterFormSet})
