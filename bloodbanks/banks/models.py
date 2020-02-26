from django.db import models

# Create your models here.
class State(models.Model):
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} ({self.code})"


class BloodBank(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=400)
    address = models.TextField(max_length=400)
    pincode = models.IntegerField()
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name="banks")
    city = models.CharField(max_length=64)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    
     
    def __str__(self):
        return f"{self.name} in {self.city}, {self.state}"


class BloodGroup(models.Model):
    group = models.CharField(max_length=2)
    positive = models.BooleanField()

    def __str__(self):
        if self.positive:
            return f"{self.group}+"   
        return f"{self.group}-"



class Size(models.Model):
    size_in_ml = models.IntegerField()

    def __str__(self):
        return f"{self.size_in_ml} ml"


class BloodBag(models.Model):
    blood_bank = models.ForeignKey(BloodBank,on_delete=models.CASCADE, related_name="bloodbags")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name="available")
    size_in_ml = models.ForeignKey(Size, on_delete=models.CASCADE, related_name="available")
    quantity = models.IntegerField()
    # total_ml = models.IntegerField()

    def __str__(self):
        return f"{self.blood_bank} has {self.quantity} bags ({self.size_in_ml}) of {self.blood_group} group"


class TotalBlood(models.Model):
    blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE, related_name='total_blood')
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE, related_name='total_blood')
    total_ml = models.IntegerField()

    def __str__(self):
        return f"{self.blood_bank} has {self.total_ml} ml of {self.blood_group}"



