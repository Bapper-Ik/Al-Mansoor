from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Product, Shoes, Atampa, Comments
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


def trends(request):
    return render(request, 'trends.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def gov(request):
    try:
        govs = Product.objects.filter(name__startswith='governor')
        contex = {
            'govs': govs,
        }
    except govs.DoesNotExist:
        context['error_msg'] = 'Not a governor yard!'
    else:
        return render(request, 'gov.html', contex)


def atampa(request):
    try:
        atampas = Atampa.objects.filter(name__contains='atampa')
        contex = {
            'atampas': atampas,
        }
    except atampas.DoesNotExist:
        context['error_msg'] = 'Not a Atampa yard!'
    else:
        return render(request, 'atampa.html', contex)


def plain(request):
    try:
        plains = Product.objects.filter(name__startswith='plain')
        contex = {
            'plains': plains,
        }
    except plains.DoesNotExist:
        context['error_msg'] = 'Not a governor yard!'

    return render(request, 'plain.html', contex)


def staroz(request):
    try:
        starozes = Product.objects.filter(name__startswith='staroz')
        contex = {
            'starozes': starozes,
        }
    except starozes.DoesNotExist:
        context['error_msg'] = 'Not a staroz yard!'

    return render(request, 'staroz.html', contex)


def tissue(request):
    try:
        tissues = Product.objects.filter(name__startswith='tissue')
        contex = {
            'tissues': tissues,
        }
    except govs.DoesNotExist:
        context['error_msg'] = 'Not a governor yard!'

    return render(request, 'tissue.html', contex)


def cashmere(request):
    try:
        cashmeres = Product.objects.filter(name__startswith='cashmere')
        contex = {
            'cashmeres': cashmeres,
        }
    except cashmeres.DoesNotExist:
        context['error_msg'] = 'Not a Cashmere yard!'

    return render(request, 'cashmere.html', contex)


def lana(request):
    try:
        lanas = Product.objects.all().filter(name__startswith='lana')
        context = {
            'lanas': lanas,
        }
    except lanas.DoesNotExist:
        contex['error_msg'] = 'product not a lana!'
    else:
        return render(request, 'lana.html', context)


def osaka(request):
    try:
        osakas = Product.objects.filter(name__startswith='osaka')
        contex = {
            'osakas': osakas,
        }
    except govs.DoesNotExist:
        context['error_msg'] = 'Not a Osaka yard!'

    return render(request, 'osaka.html', contex)


def getzner(request):
    try:
        getzners = Product.objects.filter(name__contains='getzner')
        contex = {
            'getzners': getzners,
        }
    except getzners.DoesNotExist:
        context['error_msg'] = 'not a getzner '
    else:
        return render(request, 'getzner.html', contex)

    return render(request, 'getzner.html', contex)


def nbtx(request):
    try:
        nbtxs = Product.objects.filter(name__startswith='nbtx')
        contex = {
            'nbtxs': nbtxs,
        }
    except nbtxs.DoesNotExist:
        context['error_msg'] = 'Not a NBTX Shadda!'

    return render(request, 'nbtx.html', contex)


def shampo(request):
    try:
        shampos = Product.objects.filter(name__contains='shampo')
        contex = {
            'shampos': shampos,
        }
    except shampos.DoesNotExist:
        context['error_msg'] = 'Not a Shampo Shadda!'

    return render(request, 'shampo.html', contex)


def wagambari(request):
    try:
        wagambaris = Product.objects.filter(name__contains='wagambari')
        contex = {
            'wagambaris': wagambaris,
        }
    except wagambaris.DoesNotExist:
        context['error_msg'] = 'Not a wagambari yard!'

    return render(request, 'wagambari.html', contex)


def water(request):
    try:
        water_proofs = Product.objects.filter(name__contains='water')
        context = {
            'water_proofs': water_proofs,
        }
    except water_proofs.DoesNotExist:
        context['error_msg'] = 'Not a water Proof Shadda!'
    return render(request, 'water.html', context)


def men(request):
    mens = Shoes.objects.filter(male=True)
    contex = {'mens': mens}
    return render(request, 'men.html', contex)


def women(request):
    try:
        womens = Shoes.objects.filter(male=False)
        context = {
            'womens': womens,
        }
    except womens.DoesNotExist:
        context['error_msg'] = 'Not a Women Shoes!'
    return render(request, 'women.html', context)


def adding_comment(request):
    try:
        c_email = request.POST['email'].capitalize()
        c_name = request.POST['name'].capitalize()
        c_subject = request.POST['subject'].capitalize()
        c_message = request.POST['message'].capitalize()
    except c_message.DoesNotExist:
        context = {'error_msg': 'You did not write any message'}
        return render(request, 'contact.html', context)
    else:
        if c_email == '' or c_message == '' or c_name == '' or c_subject == '':
            context = {'error_msg': 'Fields Required!'}
            return render(request, 'contact.html', context)
        comments = Comments.objects.create(customer_email=c_email, customer_name=c_name, customer_subject=c_subject, customer_message=c_message)
        comments.save()
        context = {'comments': comments}
        return render(request, 'contact.html', context)

