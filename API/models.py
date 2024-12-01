from django.db import models
from django.contrib.auth.hashers import check_password

# Create your models here.
class userData(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    imgURL = models.CharField(max_length=100, blank=True, null=True)
    workSpaceMemberOrder = models.JSONField(default=list, blank=True, null=True)
    workSpaceOwnerOrder = models.JSONField(default=list, blank=True, null=True)
    workSpaceRequest = models.JSONField(default=list, blank=True, null=True)

    def __str__(self):
        return self.username
    def check_password(self, password):
        return check_password(password, self.password)

class workSpace(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    members = models.JSONField(default=list, null=True, blank=True)
    owner = models.ForeignKey(userData, on_delete=models.CASCADE, null=True, blank=True)
    icon_unified = models.CharField(max_length=100)
    request = models.JSONField(default=list, null=True, blank=True)


    def __str__(self):
        return self.name

class column(models.Model):
    cards = models.JSONField(default=list, null=True, blank=True)
    columnIndex = models.IntegerField()
    title = models.CharField(max_length=100, blank=True, null=True)
    workSpaceID = models.ForeignKey(workSpace, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class card(models.Model):
    assignID = models.ForeignKey(userData, on_delete=models.CASCADE, null=True, blank=True)
    cardIndex = models.IntegerField()
    columnID = models.ForeignKey(column, on_delete=models.CASCADE)
    content = models.CharField(max_length=100, blank=True, null=True)
    dueDate = models.DateTimeField( blank=True, null=True)
    task = models.JSONField(default=list, null=True, blank=True)

    def __str__(self):
        return self.content

