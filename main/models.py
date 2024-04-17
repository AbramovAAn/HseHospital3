from django.db import models
from django.contrib.auth.models import User
class Phone(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    employee_name = models.CharField(max_length=50)
    employee_sname = models.CharField(max_length=50)
    employee_fname = models.CharField(max_length=70)
    employee_birthday = models.DateField()
    employee_address = models.CharField(max_length=255)
    employee_telephone = models.IntegerField()
    employee_sex = models.CharField(max_length=1, choices=GENDER_CHOICES)
    employee_passport = models.CharField(max_length=255)
    hospital = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f"{self.employee_sname} {self.employee_name}"
class Hospital(models.Model):
    address = models.CharField(max_length=255)
    employees = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='works_at_hospital')
    services = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='hospital_services')
    id_numbers = models.ForeignKey('Phone', on_delete=models.CASCADE)
    def __str__(self):
        return f"Hospital {self.id}: {self.address}"

class Position(models.Model):
      position_name = models.CharField(max_length=50)
      position_code = models.CharField(max_length=20, blank=True, null=True)

      def __str__(self):
        return self.position_name

class EmployeePosition(models.Model):
    employee = models.ForeignKey('Employee',
        on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    employ_position_date = models.DateField()
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, null=True)

    def __str__(self):        return f"{self.employee} - {self.position}"
class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='appointments')
    address = models.CharField(max_length=256)
    cabinet = models.CharField(max_length=10)
    procedure = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    status = models.CharField(max_length=100)
    cost = models.CharField(max_length=50)
    feedback = models.ForeignKey('Feedback', on_delete=models.SET_NULL, null=True, blank=True, related_name='appointments')  # Предполагается, что у вас есть модель Feedback

    def __str__(self):
        return f"Appointment {self.id} on {self.date} at {self.time}"
class Feedback(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=255)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review {self.id} - Rating: {self.rating}"

class Service(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='hospital_services')
    staff = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='services_provided')
    cost = models.CharField(max_length=50)
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name
class Statistics(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return f"Statistics {self.id}"


class Payment(models.Model):
    sum = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')
    staff = models.ForeignKey('Employee', on_delete=models.CASCADE, related_name='received_payments')
    hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE, related_name='payments')
    service = models.ForeignKey('Service', on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"Payment {self.id} - {self.sum} on {self.date}"
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20)
    birth_date = models.DateField()
    gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=gender_choices)
    snils_number = models.CharField(max_length=11)
    medical_record_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username}'s profile"