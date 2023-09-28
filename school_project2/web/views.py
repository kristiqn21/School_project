from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def speed_and_power_considerations(request):
    return render(request, 'index.html')


def item1(request):
    return render(request, 'item1.html')


def item2(request):
    return render(request, 'item2.html')


def item3(request):
    return render(request, 'item3.html')


def item4(request, ):
    return render(request, 'item4.html')


def item5(request, ):
    return render(request, 'item5.html')


def item6(request, ):
    return render(request, 'item6.html')


def universel_page(request):
    return render(request, 'universel.html')


def builtin_systems(request):
    return render(request, 'builtin_systems.html')


def signal_processor(request):
    return render(request, 'signal_processor.html')


def kesh_storage(request):
    return render(request, 'kesh_storage.html')


def memory_card(request):
    return render(request, 'memory_card.html')


def pyramid_memory(request):
    return render(request, 'pyramid_memory.html')


def virtual_storage(request):
    return render(request, 'virtual_storage.html')


def microkontroller(request):
    return render(request, 'microkontroller.html')


def processor(request):
    return render(request, 'cpu.html')