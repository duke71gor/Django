from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from .forms import ShopUserRegisterForm
from .models import ShopUser

def register(request):
    #работа руками
    if request.method == 'POST':
        #формируем пред.заполненную форму
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        #если форма валидна, продолжаем выполнение if
        if register_form.is_valid():
            user = register_form.save()
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    else:
        #если register_form не валидна - все поля стираются и передаем пользователю пустую форму
        register_form = ShopUserRegisterForm()

    context = {'form': register_form}
    return render(request, 'authapp/register.html', context)

def login(request):
    #автоматизация обработки формы
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if next:
                return HttpResponseRedirect(next)
            else:
                return HttpResponseRedirect(reverse('main'))

    return render(request, 'authapp/login.html', {'title': 'Войти', 'next': request.GET.get('next')})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

#лаконичная форма classBaseView(CBV)
class EditView(UpdateView):
    #что редактировать
    model = ShopUser
    #какйо шаблон использовать
    template_name = 'authapp/register.html'
    #поля для формы в шаблоне register.html
    fields = 'username', 'email', 'avatar'
    #после update нас перекинет на нужную url --> main
    success_url = reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context['title'] = 'Редактирование профиля'
        context['submit label'] = 'Применить'
        return context

