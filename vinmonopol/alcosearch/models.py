# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AlcoholType(models.Model):
    ALCOHOL_CHOICES = (
        ("Akevitt", "Akevitt"),
        ("Hvitvin", "Hvitvin"),
        ("Vodka", "Vodka"),
    )
    title = models.CharField(max_length=100, choices=ALCOHOL_CHOICES)


class Butikkol(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    produktnavn = models.CharField(
        db_column="Produktnavn", max_length=250, blank=True, null=True)
    varemerke = models.CharField(
        db_column="Varemerke", max_length=45, blank=True, null=True)
    pris = models.DecimalField(
        db_column="Pris", max_digits=10, decimal_places=2, blank=True, null=True)
    literpris = models.DecimalField(
        db_column="Literpris", max_digits=10, decimal_places=2, blank=True, null=True)
    volum = models.DecimalField(
        db_column="Volum", max_digits=10, decimal_places=2, blank=True, null=True)
    varetype = models.CharField(
        db_column="Varetype", max_length=250, blank=True, null=True)
    alkohol = models.DecimalField(
        db_column="Alkohol", max_digits=10, decimal_places=2, blank=True, null=True)
    emballasjetype = models.CharField(
        db_column="Emballasjetype", max_length=250, blank=True, null=True)
    butikk = models.CharField(
        db_column="Butikk", max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'butikkOl'


class Fullinfo(models.Model):
    # Field name made lowercase.
    datotid = models.DateTimeField(db_column='Datotid', blank=True, null=True)
    # Field name made lowercase.
    varenummer = models.IntegerField(
        db_column='Varenummer', blank=True, null=True)
    # Field name made lowercase.
    varenavn = models.CharField(
        db_column='Varenavn', max_length=100, blank=True, null=True)
    # Field name made lowercase.
    volum = models.DecimalField(
        db_column='Volum', max_digits=7, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    pris = models.DecimalField(
        db_column='Pris', max_digits=10, decimal_places=2)
    # Field name made lowercase.
    literpris = models.DecimalField(
        db_column='Literpris', max_digits=12, decimal_places=2)
    # Field name made lowercase.
    varetype = models.CharField(
        db_column='Varetype', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    produktutvalg = models.CharField(
        db_column='Produktutvalg', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    butikkategori = models.CharField(
        db_column='Butikkategori', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    fylde = models.IntegerField(db_column='Fylde', blank=True, null=True)
    # Field name made lowercase.
    friskhet = models.IntegerField(db_column='Friskhet', blank=True, null=True)
    # Field name made lowercase.
    garvestoffer = models.IntegerField(
        db_column='Garvestoffer', blank=True, null=True)
    # Field name made lowercase.
    bitterhet = models.IntegerField(
        db_column='Bitterhet', blank=True, null=True)
    # Field name made lowercase.
    sodme = models.IntegerField(db_column='Sodme', blank=True, null=True)
    # Field name made lowercase.
    farge = models.CharField(
        db_column='Farge', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    lukt = models.CharField(
        db_column='Lukt', max_length=120, blank=True, null=True)
    # Field name made lowercase.
    smak = models.CharField(
        db_column='Smak', max_length=120, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    passer_til_1 = models.CharField(
        db_column='Passer til 1', max_length=70, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    passer_til_2 = models.CharField(
        db_column='Passer til 2', max_length=70, blank=True, null=True)
    # Field name made lowercase. Field renamed to remove unsuitable characters.
    passer_til_3 = models.CharField(
        db_column='Passer til 3', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    land = models.CharField(
        db_column='Land', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    distrikt = models.CharField(
        db_column='Distrikt', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    underdistrikt = models.CharField(
        db_column='Underdistrikt', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    argang = models.IntegerField(db_column='Argang', blank=True, null=True)
    # Field name made lowercase.
    rastoff = models.CharField(
        db_column='Rastoff', max_length=150, blank=True, null=True)
    # Field name made lowercase.
    metode = models.CharField(
        db_column='Metode', max_length=260, blank=True, null=True)
    # Field name made lowercase.
    alkohol = models.DecimalField(
        db_column='Alkohol', max_digits=4, decimal_places=2, blank=True, null=True)
    # Field name made lowercase.
    sukker = models.CharField(
        db_column='Sukker', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    syre = models.CharField(
        db_column='Syre', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    lagringsgrad = models.CharField(
        db_column='Lagringsgrad', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    produsent = models.CharField(
        db_column='Produsent', max_length=70, blank=True, null=True)
    # Field name made lowercase.
    grossist = models.CharField(
        db_column='Grossist', max_length=60, blank=True, null=True)
    # Field name made lowercase.
    distributor = models.CharField(
        db_column='Distributor', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    emballasjetype = models.CharField(
        db_column='Emballasjetype', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    korktype = models.CharField(
        db_column='Korktype', max_length=45, blank=True, null=True)
    # Field name made lowercase.
    vareurl = models.CharField(
        db_column='Vareurl', max_length=80, blank=True, null=True)
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)

    def __str__(self):
        return self.varetype

    class Meta:
        managed = False
        db_table = 'Fullinfo'


"""
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        'DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
"""
