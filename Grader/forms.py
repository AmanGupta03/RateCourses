from django import forms

from .models import course

class CourseForm(forms.ModelForm):

    class Meta:
        model = course
        fields = ('name', 'domain', 'link', 'price', 'duration', 'rating', 'star', 'text',)