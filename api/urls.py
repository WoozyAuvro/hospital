from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('esp/uploadGas/', views.esp_gas_data, name='espGas'),
    path('esp/uploadTemp/', views.esp_temp_data, name='espTemp'),
    path('staff/data/', views.staffdata, name='staff_data'),
    path('api/get-temperature-data/', views.tempData, name='temp_data'),
    path('api/get-gas-data/', views.gasData, name='temp_data'),
    path('doctor/', views.doctor, name='doctor'),
    path('patient/', views.patient, name='patient'),
    path('checkin/', views.check_in, name='checkin'),
    path('api/get-last-10-temperature-data/', views.get_last_10_temperature_data, name='get_last_10_temperature_data'),
    path('api/get-last-10-gas-data/', views.get_last_10_gas_data, name='get_last_10_gas_data'),
    path('api/patient/ai/', views.ai, name='ai'),
]