from banks.models import BloodBag, BloodBank, Size, BloodGroup, TotalBlood


def init_bloodbags(bank: BloodBank):
    groups = BloodGroup.objects.all()
    sizes = Size.objects.all()
    for group in groups:
        total_obj = TotalBlood(blood_bank=bank, blood_group=group)
        total_obj.total_ml = 0
        total_obj.save()  
        for size in sizes:
            bag = BloodBag(blood_bank=bank, blood_group=group, size_in_ml=size, quantity=0)
            bag.save()

         





