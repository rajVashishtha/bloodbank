from banks.models import BloodBag, BloodBank, Size, BloodGroup


def init_bloodbags(bank: BloodBank):
    groups = BloodGroup.objects.all()
    sizes = Size.objects.all()
    for group in groups:
        for size in sizes:
            bag = BloodBag(blood_bank=bank, blood_group=group, size_in_ml=size, quantity=0, total_ml=0)
            bag.save()





