from django.shortcuts import redirect, render, get_object_or_404
from .models import Tweet
from .forms import TweetForms, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, "index.html")


def tweet_list(request):
    
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(request, 'tweet_list.html', {'tweets': tweets})


@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForms(request.POST)
        if form.is_valid():
            new_tweet = form.save(commit=False)
            new_tweet.user = request.user
            new_tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForms()

    return render(request, "tweet_form.html", {"form": form})


@login_required
def tweet_edit(request, tweet_id):
    tweet_instance = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForms(request.POST, request.FILES, instance=tweet_instance)
        if form.is_valid():
            form.save()
            return redirect('tweet_list')
    else:
        form = TweetForms(instance=tweet_instance)

    return render(request, 'tweet_form.html', {'form': form, 'tweet': tweet_instance})


@login_required
def tweet_delete(request, tweet_id):
    tweet_instance = get_object_or_404(Tweet, id=tweet_id)
    if request.method == "POST":
        tweet_instance.delete()
        return redirect('tweet_list')

    return render(request, "tweet_confirm_delete.html", {"tweet": tweet_instance})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def work():
    print("hi my name mohit")
