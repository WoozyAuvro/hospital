from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import esp, espTemp
import subprocess, os, threading
#from sheeesh import main, compare

def get_last_10_temperature_data(request):
    # Retrieve the last 10 temperature data points from the database
    temperature_data = espTemp.objects.all().order_by('-created')[:10]
    
    # Serialize the data into JSON format
    serialized_data = [{'temperature':entry.temp, 'created': str(entry.created)[:-21]} for entry in temperature_data]
    
    # Return the serialized data as a JSON response
    return JsonResponse(serialized_data, safe=False)

def get_last_10_gas_data(request):
    # Retrieve the last 10 gas data points from the database
    gas_data = esp.objects.all().order_by('-created')[:10]
    
    # Serialize the data into JSON format
    serialized_data = [{'data': entry.data, 'created': str(entry.created)[:-21]} for entry in gas_data]
    
    # Return the serialized data as a JSON response
    return JsonResponse(serialized_data, safe=False)

def run_process():
    # Start the OS process here, replace 'your_command' with your actual command
    subprocess.run('python "E:\\cOdiNg\\Automated-Health-Facility\\hospital\\sheeesh\\main.py"', shell=True)

def home(request):
    return render(request, "home.html")

def check_in(request):
    process_thread = threading.Thread(target=run_process)
    process_thread.start()
    return render(request, "wait.html")

def doctor(request):
    return render(request, "doctor.html")

def patient(request):
    return render(request, "patient.html")

@csrf_exempt
def esp_temp_data(request):
    if request.method == 'POST':
        # Assuming the ESP32 sends JSON data with 'data' and 'created' fields
        data = request.POST.get('temperature')
        #created = request.POST.get('created')

        # Create an instance of the esp model and save the data to the database
        esp_instance = espTemp.objects.create(temp=data)
        esp_instance.save()

        return JsonResponse({'message': 'Sensor data received and saved successfully.'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint.'}, status=405)
    
@csrf_exempt
def esp_gas_data(request):
    if request.method == 'POST':
        # Assuming the ESP32 sends JSON data with 'data' and 'created' fields
        data = request.POST.get('data')
        #created = request.POST.get('created')

        # Create an instance of the esp model and save the data to the database
        esp_instance = esp.objects.create(data=data)
        esp_instance.save()

        return JsonResponse({'message': 'Sensor data received and saved successfully.'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed for this endpoint.'}, status=405)
    
def staffdata(request):
    return render(request, "getData.html")

def tempData(request):
    sensor_data = espTemp.objects.all().order_by('-created')[:1]  # Get the latest 10 records, adjust as needed
    # Serialize the sensor data into JSON format
    serialized_data = [{'data': str(entry.temp) + " °C", 'created': str(entry.created)[:-21]} for entry in sensor_data]

    # Return the serialized sensor data as a JSON response
    return JsonResponse(serialized_data, safe=False)
def gasData(request):
    sensor_data = esp.objects.all().order_by('-created')[:1]  # Get the latest 10 records, adjust as needed
    # Serialize the sensor data into JSON format
    serialized_data = [{'data': entry.data, 'created': str(entry.created)[:-21]} for entry in sensor_data]

    # Return the serialized sensor data as a JSON response
    return JsonResponse(serialized_data, safe=False)