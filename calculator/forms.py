from django import forms

class GPAForm(forms.Form):
    subject_count = forms.IntegerField(min_value=1, label='Number of Subjects')

class SubjectForm(forms.Form):
    marks = forms.FloatField(min_value=0, max_value=100, label='Marks')
    credit = forms.FloatField(min_value=0, label='Credit Hours')

class CGPAForm(forms.Form):
    semester_count = forms.IntegerField(min_value=1, label='Number of Semesters')

class SemesterForm(forms.Form):
    gpa = forms.FloatField(min_value=0, max_value=4.0, label='GPA')
    credit = forms.FloatField(min_value=0, label='Total Credit Hours')
