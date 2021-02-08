from django.views.generic import CreateView
from .forms import CreationForm, LoginForm
from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .service import id_generator
from .tasks import send_task_email
from app.views import index
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .auth_backend import PasswordlessAuthBackend
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
import random


authenticate = PasswordlessAuthBackend.authenticate

User = get_user_model()


def logout_view(request):
    """Выход из системы"""
    logout(request)
    return redirect(index)


class SignUp(CreateView):
    """Клласс обрабатывает страницу регистрации"""
    form_class = CreationForm
    template_name = "signup.html"

    def form_valid(self, form):
        a = form.cleaned_data.get('username')  # вытаскиевает поле с телефоном
        form.save()
        user = User.objects.get(email=form.instance.email)
        user.username = a  # сохранет поле с телефоном
        code = id_generator()  # генерация рандомного инвайт кода
        user.invait_code = code  # Добавил 6 значный код к пользователю
        user.save()
        # code_email = random.randint(1000, 9999)
        # send_task_email.delay(form.instance.email, code_email)
        return redirect(index)


@login_required()   # проверка что пользователь залогинен
def profile(request, user):
    """Профил пользователя"""
    user = get_object_or_404(User, id=user)
    if request.method == 'POST':
        code = request.POST['num']    # получаем инвайт код
        if user.invait_code_user is None and code != user.invait_code:  # Проверка что пользователь не вводил код
            if len(code) == 6:  # проверк ачто код 6 значный
                if User.objects.all().filter(invait_code=code):
                    user.invait_code_user = code
                    user.save()  # сохраняем инвайт код
                    return redirect(index)
                else:
                    messages.error(request, 'Код не найден')
            else:
                messages.error(request, 'Код должен состоять из 6 символов')
        else:
            messages.error(request, 'Можно использовать только один код и не свой!')
    invait_list = User.objects.all().filter(
        invait_code_user=user.invait_code)  # показывает какие телефоны ввели код юзера

    return render(request, 'profile.html', {'user': user, 'invait_list': invait_list},)


def login2(request, user, code_email):
    """Проверка кода для входа и если все верно пользователь входит в систему"""
    code_email = code_email
    if request.method == 'POST':
        code = request.POST['num']
        if int(code) == int(code_email):
            user = User.objects.get(id=user)
            user.code = code
            user.save
            authenticate(user.username)  # аутификация пользователя
            login(request, user)
            return redirect(profile, user=user.id)
    return render(request, 'login2.html', {'user': user, 'code_email': code_email})


def login_telefon(request):
    """Первая страница входа, если номер телефона есть в базе отправляет код на emeil.
       А так же показывает его в url адресе (для удобства)
       И перекидывает на страницу для ввода кода подтверждения
    """
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            try:
                user = User.objects.get(username=form.cleaned_data['username'])
                code_email = random.randint(1000, 9999)
                send_task_email.delay(user.email, code_email)  # таска отправялет код на email юзера
                return redirect('login2', user=user.id, code_email=int(code_email))
            except:
                messages.error(request, 'Пользователь не найден')
    return render(request, 'login.html', {'form': form})
