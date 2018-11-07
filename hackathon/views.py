from django.shortcuts import render
from hackathon.models import Hackathon

def index(request):
    fund_goal = Hackathon.fundraising_goal
    fund_current = Hackathon.total_funding_raised
    fund_deadline = Hackathon.fundraising_deadline
    hack_date = Hackathon.hackathon_date

    context = {
        "fund_goal" : fund_goal,
        "fund_current" : fund_current,
        "fund_deadline" : fund_deadline,
        "hack_date" : hack_date,
    }

    return render(request, "index.html", context=context)