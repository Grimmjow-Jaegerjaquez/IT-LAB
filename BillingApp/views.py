from django.shortcuts import render, redirect
from django.utils import timezone

def calculate_cgpa(request):
	if request.method == 'POST':
		student_name = request.POST['student_name']
		total_marks = float(request.POST['total_marks'])
		session_key = request.session.session_key
		request.session[session_key] = {"name" : student_name, "total_marks" : total_marks}
		request.session["cgpa"] = total_marks / 50
		return redirect("cgpa result")

	return render(request, 'BillingApp/calculate_cgpa.html')

def show_cgpa(request):
	session_key = request.session.session_key
	result = request.session.get(session_key, {})
	del request.session[session_key]
	return render(request, 'BillingApp/show_cgpa.html', {"name" : result["name"], "cgpa" : result.get("cgpa", " ")})
