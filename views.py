from django.shortcuts import render,redirect
from models import Players,Question,Qattempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from random import randint
import datetime

def home(request):
	return render(request,'regi.html')

def ques_page(request):
	return render(request,'question_make.html')

def ques(request):
	if request.method == "POST":
		Question.objects.create(question=request.POST['question_text'],correct_option=request.POST['correct'])
		return render(request,'question_make.html')

def createuser(request):
	if request.method == "POST":
		if User.objects.filter(username = request.POST['regusername']).exists():
		#for i in User.objects.all():
		#	if request.POST['regusername'] == i.username:
		#		print "username already taken"
			return render(request,'regi.html',{'message':'username already exists'})
		else:	
			user=User.objects.create_user(username=request.POST['regusername'],password=request.POST['reguserpassword'])
			q=Players.objects.create(pname1=request.POST['Player1'],phone1=request.POST['Player1no'],email1=request.POST['Player1email'],pname2=request.POST['Player2'],phone2=request.POST['Player2no'],email2=request.POST['Player2email'],user=user)
			username=request.POST['regusername']
			password=request.POST['reguserpassword']		
			user=authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				return render(request,'instructions.html')
			else:
				return render(request,'regi.html')
	else:
		return render(request,'regi.html')

def time_start(request):
	u=request.user.players
	now=datetime.datetime.now()
	u.end_time=int(now.hour)*3600+int(now.minute)*60+int(now.second)+1500
	u.save()
	return Level(request)

def login_page(request):
	return render(request,'login.html')

def log_in(request): #need to combine with signup
	if request.method == "POST":
		username=request.POST['username']
		password=request.POST['userpassword']		
		user=authenticate(username=username,password=password)

		if user is not None:
			login(request,user)
			return Level(request)
		else:
			return render(request,'login.html')
	else:
		return render(request,'regi.html')

def log_out(request):
	res=request.user.players.total_score
	right=request.user.players.right_count
	wrong=request.user.players.wrong_count
	logout(request)
	return render(request,'rc_index.html',{'res':res,'right':right,'wrong':wrong})

def Level(request):
	if (set_timezone(request) <=0):
		return log_out(request)
	u=request.user.players
	#u.marks=4
	count=0
	for k in Question.objects.all():
		count=count+1
	i=randint(1,count)
	q1=Question.objects.get(id=i)
	for q in Qattempt.objects.filter(user_id=request.user.id):
		if q.question_id==q1.id:
			return Level(request)
	else:
		Qattempt.objects.create(question=q1,user=request.user)
		return render(request,'rcr1.html',{'q1':q1})
	return Level(request)

def check(request):
	if request.method == "POST":
		p=request.POST['id']
		u=request.user.players
		q1=Question.objects.get(id=p)
		attempted_opt=request.POST['correct']
		if q1.correct_option==attempted_opt and u.count==2:
			u.total_score=u.total_score+4
			u.right_count=u.right_count+1
		else:
			if u.count==2:
				u.previous_answer=attempted_opt
				u.save()
				return dis(request)
			elif q1.correct_option==attempted_opt and u.count==1:
				u.total_score=u.total_score+2
				u.right_count=u.right_count+1
				u.previous_answer="NULL"
			else:
				u.total_score=u.total_score-2
				u.wrong_count=u.wrong_count+1
				u.previous_answer="NULL"
			u.count=2
		u.questions_attempted=u.questions_attempted+1	
		u.save()
		return Level(request)
	else:
		return render(request,'regi.html')

def dis(request):
	if request.method == "POST":
		p=request.POST['id']
		u=request.user.players
		u.count=u.count-1
		q1=Question.objects.get(id=p)
		u.save()
		return render(request,'rcr1.html',{'q1':q1})
	else:
		return render(request,'regi.html')

def result(request):
	return render(request,'rc_index.html')

def set_timezone(request):
	u=request.user.players
	now=datetime.datetime.now()
	curr_time=int(now.hour)*3600+int(now.minute)*60+int(now.second)
	time=u.end_time-curr_time
	#if time<=0:
	#	return "logout"
	#print time
	return time
	#return HttpResponse(time)

def return_timezone(request):
	u=request.user.players
	now=datetime.datetime.now()
	curr_time=int(now.hour)*3600+int(now.minute)*60+int(now.second)
	time=u.end_time-curr_time
	#if time<=0:
	#	return "logout"
	return HttpResponse(time)

def light_gone(request):
	if request.method == "POST":
		if "abizer" == request.POST['username']:
			q = Players.objects.all()
			add_time = request.POST['add_time']
			try:
				add_time = int(add_time)
			except:
				return render(request,'Add.html',{'message':'Fuck You'})
			add_time = add_time*60
			for i in q:
				i.end_time = i.end_time+add_time
				i.save()
			return render(request,'Add.html',{'message':'Time successfully added'})
	else:
		return render(request,'Add.html',{'message':'Fuck You'})

def add_time(request):
	return render(request,'Add.html')



"""
def detail(request,question_id):
	p=Question.objects.filter(id=question_id)
	user = User.objects.get(pk = request.user.id)
	print question_id
	print BASE_DIR
	context={'q':q,'user':user}
	return render(request,'detail.html',context)"""

    


