from django.db import models

class MobileUser(models.Model):
    username = models.TextField()
    password= models.TextField()

    class Meta:
        verbose_name = 'Data Karyawan'
        verbose_name_plural = 'Data Karyawan'
    def __str__(self):
        return self.username
    

class DataSupir(models.Model):
    idSup = models.TextField("ID SUPIR")
    namaSupir = models.TextField("NAMA SUPIR")
    passSupir = models.TextField("PASSWORD SUPIR")
    jenis = models.TextField("JENIS")
    noPol = models.TextField("PLAT NOMOR")
    class Meta:
        verbose_name = 'Data Supir'
        verbose_name_plural = 'Data Supir'
    def __str__(self):
        return self.namaSupir
class Note(models.Model):
    id = models.CharField(max_length=128,primary_key=True)
    idSupir = models.CharField("ID SUPIR",max_length=100, default='',null=False, blank=False)
    theBorrower = models.TextField("NAMA SUPIR")
    platNomor = models.CharField("PLAT NOMOR",max_length=100, default='',null=False, blank=False)
    nominal = models.TextField("NOMINAL")
    jumlahRit = models.CharField("JUMLAH RIT",max_length=100,default='',null=False, blank=False)
    description = models.CharField("DESKRIPSI",max_length=200, blank=True)
    imagePaths = models.ImageField("PHOTO",upload_to='images',default='test.jpg',null=True, blank=True)
    createdTime=  models.DateTimeField("TANGGAL DIBUAT",auto_now_add=True)
    editedTime = models.DateTimeField("TANGGAL DIUBAH",auto_now=True)
    createdBy = models.TextField("DIBUAT OLEH")
    lastEditedBy = models.TextField("TERAKHIR DIEDIT OLEH",default='',blank=False, null=False)
    lastSync = models.CharField("TERAKHIR DISYNC",max_length=128,blank=True, null=True)
    isDeleted = models.TextField("STATUS HAPUS",default='false', null=False, blank=False)
    
    
        
    def __str__(self):
        return self.theBorrower[0:50]
    
    class Meta:
        verbose_name = 'Data BON Supir'
        verbose_name_plural = 'Data BON Supir'
        ordering = ['editedTime']