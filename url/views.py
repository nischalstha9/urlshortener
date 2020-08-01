from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView
from .models import urls
import random
import string
# Create your views here.
def HomeView(request):
    def get_random_alphanumeric_string(length):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        return result_str
    urlss = urls.objects.all()
    context = {"urls":urlss}
    def check(long_):
        if long_[:8] != 'https://' and long_[:7] != 'http://':
            long_ = 'https://'+long_
            return long_
        return long_
    
    if request.method=='POST':
        _long=request.POST.get('full_url').strip()
        _long = check(_long)
        if urls.objects.filter(nlong=_long).exists():
            return render(request, "base.html", context)
        _short = get_random_alphanumeric_string(random.randint(1,10))
        urls.objects.create(nlong=_long, short=_short)    
        return render(request, 'complete.html', {'shrunk_url':_short})
    return render(request, "base.html", context)

def redirectView(request, *args, **kwargs):
    attr = kwargs.get("attr")
    full = urls.objects.get(short=attr)
    long_ = full.nlong
    # if long_[:7] or long_[:8] != 'http://' or 'https://':
    #     long_ = 'http://'+long_
    # print(long_)
    return redirect(long_)