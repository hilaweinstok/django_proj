from django.shortcuts import render, redirect


def welcome(req):
    if req.user.is_authenticated:
        # Player has the right auth and can redirect to this page.
        return redirect('player_home')
    else:
        return render(req, 'gobblet/welcome.html')
