from django.shortcuts import render, redirect
from .forms import *
from .models import *
# Create your views here.


def home(request):
    form = PasteForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            title = form.cleaned_data['title']
            paste_text = form.cleaned_data['paste_text']
            p_language = form.cleaned_data['p_language']
            user = form.cleaned_data['user']
            if (p_language):
                new_item = Paste(title=title, paste_text=paste_text,
                                 p_language=p_language, user=user)
            else:
                new_item = Paste(title=title, paste_text=paste_text, user=user)
            new_item.save()
            return render(request, 'pastebin_app/views/index.html',  {'form': form})
    return render(request, 'pastebin_app/views/index.html',  {'form': form})


def list(request):
    pastes = Paste.objects.all()
    return render(request, 'pastebin_app/views/pastes.html',  {'pastes': pastes})


def display(request, id):
    paste = Paste.objects.filter(id=id)
    comments = Comment.objects.filter(id_paste=id)
    form = CommentForm(request.POST or None)
    return render(request, 'pastebin_app/views/display.html',  {'paste': paste[0], 'form': form, 'comments': comments})


def save_comment(request, id):
    form = CommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['Name']
            comment = form.cleaned_data['comment']
            new_comment = Comment(name=name, comment=comment, id_paste=id)
            new_comment.save()
            return redirect("/pastes/"+str(id))
        else:
            return redirect("/pastes/"+str(id))

def delete(request, id):
    paste=Paste.objects.filter(id=id)
    try:
        paste[0].delete()
    except:
        pass
    return redirect("/pastes/")