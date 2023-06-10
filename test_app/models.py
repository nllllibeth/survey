from django.db import models
import uuid

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=100)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                               primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
CHOICES = (
    ("a", "a"),
    ("b", "b"),
    ("c", "c"),
    ("d", "d"),
)
    
class Question(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    question_text = models.TextField(max_length=400)
    option_a = models.TextField(max_length=200)
    option_b = models.TextField(max_length=200)
    option_c = models.TextField(max_length=200)
    option_d = models.TextField(max_length=200)
    correct_answer = models.CharField(max_length=50, 
                                      choices=CHOICES)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                               primary_key=True, editable=False)

    def __str__(self):
        return self.question_text

    
class Test_form(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    login = models.CharField(max_length=50)
    results = models.IntegerField(blank=True, null=True)
    correct = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    percent = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    answers = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.login

