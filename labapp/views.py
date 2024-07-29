from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic    
from labapp.models import course, projectForm, student
import csv
from reportlab.lib.pagesizes import letter 
from reportlab.platypus import SimpleDocTemplate, Table
from django.shortcuts import render 
import datetime
from django.http import HttpResponse # Create your views here.

def cdt(request): 
    dt=datetime.datetime.now()
    resp="<h1>Current Date and Time is %s<h1>"%(dt) 
    return HttpResponse(resp)

def aheadtime(request): 
    dt=datetime.datetime.now()+datetime.timedelta(hours=4) 
    resp="<html><head><title>Current Time Ahead by 4hrs</title></head><body><h1>Current date and Time ahead by 4 hrs is %s</h1></body></html>"%(dt) 
    return HttpResponse(resp)

def fruit_student(request):
    fruitlist=['Banana','Apple','Mango','Kiwi','Orange']
    studentlist=['Sumit','Mansoor','Suhaas','Priya','Supritha']
    return render(request,'fruit_student.html',{'fruitlist':fruitlist,'studentlist':sorted(studentlist)})


def home(request):
    return render(request,'home.html')

def contactus(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'about.html')

def studentlist(request):
    s=student.objects.all()
    return render(request,'studentlist.html',{'student_list':s})

def courselist(request):
    c=course.objects.all()
    return render(request,'courselist.html',{'course_list':c})

def register(request):
    if request.method=="POST":
        sid=request.POST.get("student")
        cid=request.POST.get("course")
        studentobj=student.objects.get(id=sid)
        courseobj=course.objects.get(id=cid)
        res=studentobj.courses.filter(id=cid)
        if res:
            resp="<h1>Student with usn %s has already enrolled for the  %s<h1>"%(studentobj.usn,courseobj.courseCode)
            return HttpResponse(resp)
        studentobj.courses.add(courseobj)
        resp="<h1>student with usn %s successfully enrolled for the course with sub code %s</h1>"%(studentobj.usn,courseobj.courseCode)
        return HttpResponse(resp)
    else:
        studentlist=student.objects.all()
        courselist=course.objects.all()
    return render(request,'register.html',{'student_list':studentlist,'course_list':courselist})  

def enrolledStudents(request):
    if request.method=="POST":
        cid=request.POST.get("course")
        courseobj=course.objects.get(id=cid)
        studentlistobj=courseobj.student_set.all()
        return render(request,'enrolledlist.html',{'course':courseobj,'student_list':studentlistobj}) 
    else:
        courselist=course.objects.all()
    return render(request,'enrolledlist.html',{'Course_List':courselist})

def add_project(request):
    if request.method=="POST":
        form=projectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Project Data Successfully saved</h1>")
        else:
            return HttpResponse("<h1>Project details not saved</h1>")
    else:
        form=projectForm()
    return render(request, "projectReg.html",{'form':form})

class StudentListView(generic.ListView):
    model=student
    template_name="GenericListViewStudent.html"

class StudentDetailView(generic.DetailView):
    model=student
    template_name="GenericDetailedViewStudent.html"

def generateCSV(request):
    courses=course.objects.all()
    resp=HttpResponse(content_type="text/csv")
    resp['Content-Disposition']='attachment; filename=course_data.csv'
    writer=csv.writer(resp)
    writer.writerow(['Course Code','Course Name','Course Credits'])
    for c in courses:
        writer.writerow([c.courseCode,c.courseName,c.courseCredits])
    return resp


def generatePDF(request):
    courses=course.objects.all()
    resp=HttpResponse(content_type="text/pdf")
    resp['Content-Disposition']='attachment; filename=course_data.pdf'
    pdf=SimpleDocTemplate(resp,pagesize=letter)
    table_data=[['Course Code','Course Name','Course Credits']]
    for c in courses:
        table_data.append([c.courseCode,c.courseName,str(c.courseCredits)])
    table=Table(table_data)
    pdf.build([table])
    return resp

def registerAjax(request): 
    if request.method == "POST": 
        sid=request.POST.get("susn") 
        cid=request.POST.get("ccode") 
        studentobj=student.objects.get(id=sid) 
        courseobj=course.objects.get(id=cid) 
        res=studentobj.courses.filter(id=cid) 
        if res: 
            return HttpResponse("<h1>Student already enrolled</h1>") 
        studentobj.courses.add(courseobj) 
        return HttpResponse("<h1>Student enrolled successfully</h1>") 
        
    else: 
        studentsobj=student.objects.all() 
        coursesobj=course.objects.all() 
        return render(request,"courseRegUsingAjax.html",{"students":studentsobj,"courses":coursesobj})

def enrolledStudentsUsingAjax(request):
    if request.method=="POST":
        cid=request.POST.get("cname")
        
        courseobj=course.objects.get(id=cid)
        studentlistobj=courseobj.student_set.all()
        return render(request,'EnrolledStudentsAjax.html',{'course':courseobj,'student_list':studentlistobj})                                                                                   
    else:
        courselist=course.objects.all()
        return render(request,'Course_search_ajax.html',{'Course_List':courselist})






