# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Core.models import *


# Create your models here.
class Medicine(models.Model):
    name = models.CharField(max_length=128)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Complain(models.Model):
    complain = models.CharField(max_length=256)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.complain


class LabTest(models.Model):
    name = models.CharField(max_length=128)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Radiology(models.Model):
    name = models.CharField(max_length=128)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Patient(models.Model):
    code = models.CharField(max_length=32, null=True, blank=True)
    instance = models.ForeignKey(Instance, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=128)
    date_added = models.DateField(auto_now_add=True)
    husband_name = models.CharField(max_length=128, null=True, blank=True)
    age = models.CharField(max_length=16, null=True, blank=True)
    job = models.CharField(max_length=16, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    ################ LADIES #################
    # Investigations
    blood_choices = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    )
    blood_group = models.CharField(choices=blood_choices, max_length=16, null=True, blank=True)
    rh = models.CharField(max_length=16, null=True, blank=True)
    cbc = models.CharField(max_length=16, null=True, blank=True)
    hb = models.CharField(max_length=16, null=True, blank=True, verbose_name='HB%')
    taxoplasma = models.CharField(max_length=16, null=True, blank=True)
    rubella = models.CharField(max_length=16, null=True, blank=True)
    other_investigation = models.CharField(max_length=16, null=True, blank=True)
    # Hermones
    fsh = models.CharField(max_length=16, null=True, blank=True)
    lh = models.CharField(max_length=16, null=True, blank=True)
    e2 = models.CharField(max_length=16, null=True, blank=True)
    tsh = models.CharField(max_length=16, null=True, blank=True)
    hs = models.CharField(max_length=16, null=True, blank=True)
    male_f = models.CharField(max_length=16, null=True, blank=True)
    other_hermones = models.CharField(max_length=16, null=True, blank=True)
    # Laprospic Finding
    ut = models.CharField(max_length=64, null=True, blank=True)
    rt_tube = models.CharField(max_length=64, null=True, blank=True)
    lt_tube = models.CharField(max_length=64, null=True, blank=True)
    rt_ov = models.CharField(max_length=64, null=True, blank=True)
    lt_ov = models.CharField(max_length=64, null=True, blank=True)
    dp = models.CharField(max_length=64, null=True, blank=True)
    other_laprospic_finding = models.CharField(max_length=64, null=True, blank=True)
    laprospic_report = models.FileField(null=True, blank=True)
    # Relevant Family History
    twins = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    cfm = models.BooleanField(default=False)
    hypertention = models.BooleanField(default=False)
    cancer = models.BooleanField(default=False)
    cns = models.BooleanField(default=False)
    operations = models.BooleanField(default=False)
    drugs = models.BooleanField(default=False)
    # Previous Obstetris History
    abortion = models.BooleanField(default=False)
    ectopic = models.BooleanField(default=False)
    v_mole = models.BooleanField(default=False)
    deliveries = models.BooleanField(default=False)
    xx = models.BooleanField(default=False)
    xy = models.BooleanField(default=False)
    still_birth = models.BooleanField(default=False)
    # CO
    co = models.ManyToManyField(Complain, blank=True)
    l_n_m_b = models.DateField(null=True, blank=True)
    e_d_d = models.DateField(null=True, blank=True)
    ################# BABIES ###################
    # Antenatal History
    antenatal_history = models.CharField(max_length=1024, null=True, blank=True)
    # Natal History
    wt_at_birth = models.FloatField(null=True, blank=True)
    duration_of_pregnancy = models.FloatField(null=True, blank=True)
    mode_of_delivery = models.CharField(max_length=128, null=True, blank=True)
    hospital = models.CharField(max_length=128, null=True, blank=True)
    doctor = models.CharField(max_length=128, null=True, blank=True)
    # Family History
    father_abo = models.CharField(max_length=3, null=True, blank=True)
    mother_abo = models.CharField(max_length=3, null=True, blank=True)
    consanguinity = models.CharField(max_length=128, null=True, blank=True)
    order = models.CharField(max_length=128, null=True, blank=True)
    diseases = models.CharField(max_length=512, null=True, blank=True)
    # Nutrition
    nutrition = models.CharField(max_length=1024, null=True, blank=True)
    # Immunization
    # BCG
    bcg = models.BooleanField(default=False)
    # TOPV
    topv_0 = models.BooleanField(default=False)
    topv_2m = models.BooleanField(default=False)
    topv_4m = models.BooleanField(default=False)
    topv_6m = models.BooleanField(default=False)
    topv_9m = models.BooleanField(default=False)
    topv_1y = models.BooleanField(default=False)
    # DPT
    dpt_2m = models.BooleanField(default=False)
    dpt_4m = models.BooleanField(default=False)
    dpt_6m = models.BooleanField(default=False)
    # HBV
    hbv_0 = models.BooleanField(default=False)
    hbv_2m = models.BooleanField(default=False)
    hbv_4m = models.BooleanField(default=False)
    hbv_6m = models.BooleanField(default=False)
    # MMR
    mmr_12m = models.BooleanField(default=False)
    mmr_18m = models.BooleanField(default=False)
    # Others
    other_0 = models.BooleanField(default=False)
    other_1 = models.BooleanField(default=False)
    # Developmental History
    social_smile = models.IntegerField(null=True, blank=True)
    head_support = models.IntegerField(null=True, blank=True)
    set_alone = models.IntegerField(null=True, blank=True)
    start_teething = models.IntegerField(null=True, blank=True)
    crawl = models.IntegerField(null=True, blank=True)
    walk_alone = models.IntegerField(null=True, blank=True)
    speech = models.IntegerField(null=True, blank=True)

    def balance(self):
        balance = 0
        for transaction in self.patienttransaction_set.all():
            balance -= transaction.credit
            balance += transaction.debit
        return balance

    def __str__(self):
        return self.name


class PatientRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    lab_tests_asked = models.ManyToManyField(LabTest, blank=True)
    radiology_asked = models.ManyToManyField(Radiology, blank=True)

    ################### LADIES ######################
    b_p = models.CharField(verbose_name='B/P', max_length=16, null=True, blank=True)
    weight = models.FloatField(verbose_name="Wt.", null=True, blank=True)
    oedama = models.FloatField(verbose_name="Oedama", null=True, blank=True)
    fundel_level = models.FloatField(verbose_name="Lt.", null=True, blank=True)
    urine_suger = models.CharField(verbose_name='Age', max_length=16, null=True, blank=True)
    urine_albumin = models.CharField(max_length=16, verbose_name="Med.", null=True, blank=True)
    week = models.CharField(max_length=1024, null=True, blank=True)
    h_b_percent = models.CharField(verbose_name='HB%', max_length=1024, null=True, blank=True)
    comments_complain = models.CharField(max_length=1024, null=True, blank=True)
    prescription = models.ManyToManyField(Medicine, blank=True)

    ################## BABIES ########################

    problem = models.CharField(max_length=1024, null=True, blank=True)
    h_c = models.FloatField(verbose_name="H.C", null=True, blank=True)
    l_t = models.FloatField(verbose_name="Lt.", null=True, blank=True)
    age = models.CharField(verbose_name='Age', max_length=16, null=True, blank=True)

    def __str__(self):
        return str(self.date)


class PatientLabTest(models.Model):
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True)
    result = models.TextField(null=True)
    result_at = models.DateField(null=True)
    img1 = models.FileField(null=True, blank=True)
    img2 = models.FileField(null=True, blank=True)
    img3 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.test.name


class PatientRadiology(models.Model):
    date = models.DateField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True)
    test = models.ForeignKey(Radiology, on_delete=models.SET_NULL, null=True)
    result = models.TextField(null=True)
    result_at = models.DateField(null=True)
    img1 = models.FileField(null=True, blank=True)
    img2 = models.FileField(null=True, blank=True)
    img3 = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.test.name
