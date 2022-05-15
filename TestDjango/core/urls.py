from django.urls import path
from .views import index, reservarhora, pagaranularhora, confirmarhora, delhora, agregargastocomunmensual, gastocomun, interfazadministradorcondominio, interfazconcerje, agregarespacio, interfazdirectiva


urlpatterns = [
    path('', index, name="index"),
    path('reservarhora', reservarhora, name="reservarhora"),
    path('confirmarhora', confirmarhora, name="confirmarhora"),
    path('pagaranularhora', pagaranularhora, name="pagaranularhora"),
    path('delhora/<id>', delhora, name="delhora"),
    path('agregargastocomunmensual', agregargastocomunmensual, name="agregargastocomunmensual"),
    path('gastocomun', gastocomun, name="gastocomun"),
    path('interfazadministradorcondominio', interfazadministradorcondominio, name="interfazadministradorcondominio"),
    path('interfazconcerje', interfazconcerje, name="interfazconcerje"),
    path('agregarespacio', agregarespacio, name="agregarespacio"),
    path('interfazdirectiva', interfazdirectiva, name="interfazdirectiva"),

]
