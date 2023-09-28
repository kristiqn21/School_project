from django.urls import path

from .views import index, about, speed_and_power_considerations, item1, item2, item3, item4, item5, item6, \
    universel_page, builtin_systems, signal_processor, kesh_storage, memory_card, pyramid_memory, virtual_storage, \
    microkontroller, processor

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about page'),
    path('page/', speed_and_power_considerations, name='dropdown page'),
    path('item/', item1, name='item1'),
    path('item2/', item2, name='item2'),
    path('ite3/', item3, name='item3'),
    path('item4/', item4, name='item4'),
    path('item5/', item5, name='item5'),
    path('item6/', item6, name='item6'),
    path('universel/', universel_page, name='universel page'),
    path('builtin/', builtin_systems, name='builtin page'),
    path('signal/', signal_processor, name='signal page'),
    path('kesh/', kesh_storage, name='kesh page'),
    path('memory/', memory_card, name='memory page'),
    path('pyramid/', pyramid_memory, name='pyramid page'),
    path('virtual/', virtual_storage, name='virtual page'),
    path('microcontroller/', microkontroller, name='micro controller'),
    path('processor/', processor, name='processor'),
]
