from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements

def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)
    return measurement

def update_measurement(var_pk, new_var):
    measurement = get_measurement(var_pk)
    measurement.value = new_var["value"]
    measurement.save()
    return measurement

def create_measurement(var):
    measurement = Measurement(value=var["value"])
    measurement.save()
    return measurement

def delete_measurement(id):
    Measurement.objects.filter(pk=id).delete()