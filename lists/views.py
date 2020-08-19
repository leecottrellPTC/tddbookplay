from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.

#home_page = None
def home_page(request):
    #pass   #just passes the test
    #if request.method == 'POST':
    #    return HttpResponse(request.POST['item_text'])
    # item = Item()
    # item.text = request.POST.get('item_text', '')
    # item.save()
    # return render(request, 'home.html', { 'new_item_text': item.text})
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text']) #save to the database
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
