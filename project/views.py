# i have creared this

from django.http import HttpResponse
from django.shortcuts import render


# ------------------------------  index   --------------------------------

# def index(request):
#     # params = {"name":"raman dahiya","place":"shamli"}
#     return  render(request,'index.html')

# ----------------------------------------------------------------------

# ---------------------------   doattack ---------------------------------

# def doattack(request):
#     import os
#     mn = request.GET.get("mn")
#     fq = request.GET.get("fq")
#     command = f"heroku run:detached python rdxbomb.py {mn} {fq}  --app rdxbomber"
#     os.system(command)
#     datasend = {"texts" :f"ATTACK COMPLETE WITH  : MOBILE NUMBER :{mn}  AND WITH {fq} SMS"}
#     return render(request,'result.html',datasend)