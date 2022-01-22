from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import user
# Create your views here.
@csrf_protect
def index(request):
    return render(request,'index.html')
def resume(request):
    try : 
        if request.method == "POST":
            #Getting Data From HTML Template
            name = request.POST.get('name')
            email = request.POST.get('email')
            job_profile = request.POST.get('jobpro')
            mno = request.POST.get('Mobile')
            website = request.POST.get('website')
            facebook = request.POST.get('facebook')
            twitter = request.POST.get('twitter')
            linkedin = request.POST.get('linkedin')
            youtube = request.POST.get('linkedin')
            address = request.POST.get('address')
            about = request.POST.get('about')
            skills = request.POST.get('skills')
            percentage = request.POST.get('percentage')
            yrs1 = request.POST.get('yrs1')
            ins1 = request.POST.get('ins1')
            firstdesc = request.POST.get('firstdesc')
            yrs2 = request.POST.get('yrs2')
            ins2 = request.POST.get('ins2')
            secdesc = request.POST.get('secdesc')
            dur1 = request.POST.get('dur1')
            namecom1 = request.POST.get('namecom1')
            exdesc1 = request.POST.get('exdesc1')
            dur2 = request.POST.get('dur2')
            namecom2 = request.POST.get('namecom2')
            exdesc2 = request.POST.get('exdesc2')
            dur3 = request.POST.get('dur3')
            namecom3 = request.POST.get('namecom3')
            exdesc3 = request.POST.get('exdesc3')
            #Making a Object of Class User Prsent In Model
            data = user()
            #Fetching Data Into Our Models
            #Basic Info
            data.new_name = name
            data.new_email = email
            data.new_address = address
            data.new_mno = mno
            #Carrier Info
            data.new_about=about
            data.new_website = website
            data.new_job = job_profile
            # Creating Different Models for Different Skills
            data.new_skills = skills
            data.new_skills = data.new_skills.split(',')
            data.new_skills0 = data.new_skills[0]
            data.new_skills1 = data.new_skills[1]
            data.new_skills2 = data.new_skills[2]
            data.new_skills3 = data.new_skills[3]
            data.new_skills4 = data.new_skills[4]
            # Creating Different Percentage Models for Different Skill Percentage
            data.new_percentage = percentage
            data.new_percentage = data.new_percentage.split(',')
            data.new_percentage0 = data.new_percentage[0]
            data.new_percentage1 = data.new_percentage[1]
            data.new_percentage2 = data.new_percentage[2]
            data.new_percentage3 = data.new_percentage[3]
            data.new_percentage4 = data.new_percentage[4]
            #Educational Info
            data.new_yrs1 = yrs1
            data.new_ins1 = ins1
            data.new_firstdesc = firstdesc
            data.new_yrs2 = yrs2
            data.new_ins2 = ins2
            data.new_secdesc = secdesc
            #Experience Info
            data.new_dur1 = dur1
            data.new_namecom1 = namecom1
            data.new_exdesc1 = exdesc1
            data.new_dur2 = dur2
            data.new_namecom2 = namecom2
            data.new_exdesc2 = exdesc2
            data.new_dur3 = dur3
            data.new_namecom3 = namecom3
            data.new_exdesc3 = exdesc3
            #Social Media Info
            data.new_facebook = facebook
            data.new_twitter = twitter
            data.new_linkedin = linkedin
            data.new_youtube = youtube
    except Exception as err:
        print(err)
    return render(request,'resume.html',{'data':data})
