from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import SignUpForm
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            mail = EmailMultiAlternatives(
                subject="Finish Your SplatStats Registration",
                body=render_to_string(
                    "site_auth/account_activation_email.html",
                    {
                        "user": user,
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": account_activation_token.make_token(user),
                    },
                ),
                from_email="SplatStats Signup <splatstats-signup@cass-dlcm.dev>",
                to=[form.cleaned_data["email"]],
                headers={"Reply-To": "splatstats-webmaster@cass-dlcm.dev"},
            )
            mail.send()
            return redirect("account_activation_sent")
    else:
        form = SignUpForm()
    return render(request, "site_auth/signup.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect("../../../account/two_factor/setup")
    return render(request, "site_auth/account_activation_invalid.html")


def account_activation_sent(request):
    return render(request, "site_auth/account_activation_sent.html")
