from django.shortcuts import render
from .forms import CourseForm
def course_detail(request, pk):
 course = get_object_or_404(course, pk=pk)
 #return render(request,'blog/post_detail.html',{'post':post})