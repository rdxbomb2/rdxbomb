
from django.http import HttpResponse
from django.shortcuts import render
from .models import Attackinfo
from .models import Userinfo
from .models import Workerinfo


def index(request):
    # params = {"name":"raman dahiya","place":"shamli"}
    return  render(request,'index.html')

def about(request):
    return HttpResponse("This is about page")

def help(request):
    return render(request,'help.html')

def register(request):
    return render(request,'register.html')

def powerfulindex(request):
    return render(request,'powerfulindex.html')

def useradded(request):
    return render(request,'useradded.html',)

def adduser(request):

    username = request.GET.get('username')
    password = request.GET.get('password')
    api_token = request.GET.get('api_token')

    if username == "" or password == "" or len(api_token) <= 10:
        data = {"line": f"You Enter Invalid Details"}
        return render(request,'useradded.html',data)

    Useri = Userinfo( username = username, password=password,api_token=api_token)
    Useri.save()


    data = {"line":f"Account created Username: {username} and Password is :{password}"}

    return render(request,'useradded.html',data)

def doattack(request):
    import os
    import time
    import datetime
    import random

    mobile_no = request.GET.get("mn")
    frequency_no = request.GET.get("fq")

    if mobile_no == "" or int(frequency_no) < 0 or len(mobile_no) != 10 or frequency_no == "" or (frequency_no.isdigit() == False) or (mobile_no.isdigit() == False) :
        datasend = {"texts": f"You Enter Invalid Details"}
        return render(request,'attackresult.html',datasend)


    Producti = Attackinfo( mobile_n = mobile_no, frequency_n=frequency_no)
    Producti.save()


    if int(frequency_no) >= 51 :
        frequency_no = "30"



    # ------------------------ UPDATE DATABASE ---------------------

    def updatedatabase():
        workers_list = ["worker0", "worker1", "worker2", "worker3"]
        for i in workers_list:
            swor = Workerinfo.objects.get(workername=i)
            swor_ctime = swor.workerctime
            swor_rtime = swor.workerrtime

            swor_dto = datetime.datetime.strptime(swor_ctime, '%Y-%m-%d %H:%M:%S.%f')

            ctime = datetime.datetime.now()
            delta = ctime - swor_dto
            worrsec = delta.total_seconds()

            print(f"working sec {worrsec}")
            print(f"sworr itme sec {swor_rtime}")

            if int(worrsec) > int(swor_rtime):
                swor.status = "free"
                swor.save()

    # -----------------------------------------------------------------

    updatedatabase()


    worker0 = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber"
    worker1= f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber1"
    worker2 = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber2"
    worker3 = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber3"


    awor = Workerinfo.objects.filter(status="free")

    for_wrkr1 = Workerinfo.objects.get(workername="worker1")
    ctime = for_wrkr1.workerctime
    rtime = for_wrkr1.workerrtime
    time_c_worker = datetime.datetime.strptime(ctime, '%Y-%m-%d %H:%M:%S.%f')


    curr_time = datetime.datetime.now()

    time_left_in_Sec = time_c_worker - curr_time

    totalsecleft = time_left_in_Sec.total_seconds()
    totalsecleft += int(rtime)


    if len(awor) == 0:
        datasend = {"texts": f"ALL SERVERS ARE BUSY TILL NOW PLEASE TRY SOME TIME LATER TRY AGAIN AFTER {round(int(totalsecleft),2)} Seconds"}
        return render(request, 'attackresult.html', datasend)

    wrknn = awor[0].workername
    wrkn = Workerinfo.objects.get(workername=wrknn)
    wrkn.workerctime = datetime.datetime.now()
    wrkn.workerrtime = str(int(frequency_no) * 12)
    wrkn.status = "working"
    wrkn.save()

    numberofworker = wrknn[6:7]

    if int(numberofworker) == 0:
        numberofworker = ""

    os.system(f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber{numberofworker}")

    datasend = {"texts" :f"ATTACK COMPLETE WITH  : MOBILE NUMBER :{mobile_no}  AND WITH {frequency_no} SMS WITH SERVER  : RDXBOMBSERVER{numberofworker}"}
    print(datasend["texts"])

    return render(request,'attackresult.html',datasend)


def powerfulattack(request):
    import os
    import time

    mobile_no = request.GET.get("mn")
    frequency_no = request.GET.get("fq")
    username = request.GET.get("username")
    password = request.GET.get("password")
    # api_token = request.GET.get("api_token")

    if mobile_no == ""  or len(mobile_no) != 10 or frequency_no == ""  or username == "" or password == "" or (frequency_no.isdigit() == False) or (mobile_no.isdigit() == False) :
        datasend = {"userinfo": f"You Enter Invalid Details"}
        return render(request,'powerfulattackresult.html',datasend)



    Producti = Attackinfo(mobile_n=mobile_no, frequency_n=frequency_no)
    Producti.save()

    users = Userinfo.objects.filter(username=username,password=password)

    try:
        _username = users[0].username
        # _password = users[0].password
        _api_token = users[0].api_token

        frequency_no = int(frequency_no) // 4
        frequency_no = str(frequency_no)

        datasend = {"userinfo": f"Dear {_username} Attack Is Succesful At {mobile_no} With {int(frequency_no) * 4} Sms "}

        os.environ["HEROKU_API_KEY"] = _api_token
        command = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber"
        command1 = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber1"
        command2 = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber2"
        command3 = f"heroku run:detached python rdxbomb.py {mobile_no} {frequency_no}  --app rdxbomber3"

        os.system(command)
        time.sleep(1)
        os.system(command1)
        time.sleep(1)
        os.system(command2)
        time.sleep(1)
        os.system(command3)

    except:

        datasend = {"userinfo": "YOUR ACCOUNT IS INVALID PLESE ENTER CORRECT USERNAME AND PASSWORD"}



    return render(request, 'powerfulattackresult.html', datasend)



