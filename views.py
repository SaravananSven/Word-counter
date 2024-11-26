from django.shortcuts import render

# Create your views here.
def counter(request):
    if request.method=="POST":
        txt = request.POST.get('txttocount', '')
        if txt!='':
            word=len(txt.split())
            i=True
            return render(request, 'counter.html',{'word': word, 'text': txt, 'i': i, 'on': 'active'})
        else:
            return render(request, 'counter.html', {
                'error': 'Please enter some text.',
            })
    else:
        return render(request, 'counter.html', {'on': 'active'})
