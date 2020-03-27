from django.db import models

# Create your models here.

class user(models.Model):
    userObj = models.Manager()
    userid = models.CharField(max_length=20,default=False)
    username = models.CharField(max_length=20)
    userpassword = models.CharField(max_length=20)
    usertelephone = models.CharField(max_length=20)
    usergender = models.CharField(max_length=20)
    useremail = models.CharField(max_length=20)

    def __str__(self):
        return self.userid

    class Meta:
        db_table = "user"
        ordering = ['id']

class admin(models.Model):
    administratorObj = models.Manager()
    adminid = models.CharField(max_length=20,default=False)
    adminname = models.CharField(max_length=20)
    adminpassword = models.CharField(max_length=20)
    adminemail = models.CharField(max_length=20)
    admintelephone = models.CharField(max_length=20)
    adminauthority = models.CharField(max_length=20)

    def __str__(self):
        return self.adminid

    class Meta:
        db_table = "admin"
        ordering = ['id']

class application(models.Model):
    appObj = models.Manager()
    appid = models.CharField(max_length=20,default=False)
    appname = models.CharField(max_length=20)
    appreason = models.CharField(max_length=100)
    applocation = models.CharField(max_length=100)
    appgender = models.CharField(max_length=20)
    appage = models.CharField(max_length=20)
    appincome = models.CharField(max_length=20)
    appemail = models.CharField(max_length=20,default=False)

    def __str__(self):
        return self.appid

    class Meta:
        db_table = "application"
        ordering = ['id']

class cat(models.Model):
    catObj = models.Manager()
    catid = models.CharField(max_length=20,default=False)
    catname = models.CharField(max_length=20)
    catlocation = models.CharField(max_length=100)
    catintroduction = models.CharField(max_length=100)
    catbreed = models.CharField(max_length=100)
    catage = models.CharField(max_length=20)
    catpicture = models.ImageField(upload_to='img',default=False)

    def __str__(self):
        return self.catid

    class Meta:
        db_table = "cat"
        ordering = ['id']

