from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    createddate = models.DateTimeField(
        auto_now_add=True, db_column='createddate')
    updateddate = models.DateTimeField(auto_now=True, db_column='updateddate')

    class Meta:
        abstract = True


class Strategy(TimeStampedModel):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username

    class Meta:
        db_table = "Strategy"

class NetPosition(TimeStampedModel):
    date = models.DateField(auto_now_add=True, null=False, db_column='date')
    positionno = models.CharField(
        max_length=300, unique=True, db_column='positionno')

    userid = models.CharField(max_length=30, db_column='userid')

    segment = models.CharField(max_length=15, null=False, db_column='segment')

    ctclid = models.CharField(max_length=25, default=0, db_column='ctclid')
    membercode = models.CharField(
        max_length=25, default=0, db_column='membercode')
    accountcode = models.CharField(
        max_length=25, default=0, db_column='accountcode')
    symbol = models.CharField(max_length=15, null=False, db_column='symbol')
    expirydate = models.CharField(
        max_length=10, null=False, db_column='expirydate')

    exchange = models.CharField(
        max_length=10, null=False, db_column='exchange')

    token = models.DecimalField(
        max_digits=30, decimal_places=0, null=False, db_column='token')

    securitytype = models.CharField(
        max_length=10, null=False, db_column='securitytype')

    strikeprice = models.DecimalField(
        max_digits=22, decimal_places=2, null=False, db_column='strikeprice')
    opttype = models.CharField(max_length=5, null=False, db_column='opttype')
    bfqty = models.IntegerField(default=0, db_column='bfqty')
    bfrate = models.FloatField(default=0, db_column='bfrate')
    bfamt = models.FloatField(default=0, db_column='bfamt')
    buyqty = models.IntegerField(default=0, db_column='buyqty')
    buyrate = models.FloatField(default=0, db_column='buyrate')
    buyamt = models.FloatField(default=0, db_column='buyamt')
    sellqty = models.IntegerField(default=0, db_column='sellqty')
    sellrate = models.FloatField(default=0, db_column='sellrate')
    sellamt = models.FloatField(default=0, db_column='sellamt')
    netqty = models.IntegerField(default=0, db_column='netqty')
    netrate = models.FloatField(default=0, db_column='netrate')
    netamt = models.FloatField(default=0, db_column='netamt')
    cfqty = models.IntegerField(default=0, db_column='cfqty')
    cfrate = models.FloatField(default=0, db_column='cfrate')
    cfamt = models.FloatField(default=0, db_column='cfamt')
    ltp = models.FloatField(default=0, db_column='ltp')
    grossmtm = models.FloatField(default=0, db_column='grossmtm')

    charges = models.FloatField(default=0)
    netmtm = models.FloatField(default=0)
    multiplier = models.IntegerField(
        null=True, default=1, db_column='multiplier')
    basecurrency = models.CharField(
        max_length=4, null=False, db_column='basecurrency')

    buybrokrate = models.FloatField(
        default=0, null=False, db_column='buybrokrate')
    sellbrokrate = models.FloatField(
        default=0, null=False, db_column='sellbrokrate')
    expirybuybrokrate = models.FloatField(
        default=0, null=False, db_column='expirybuybrokrate')
    expirysellbrokrate = models.FloatField(
        default=0, null=False, db_column='expirysellbrokrate')
    broktype = models.CharField(
        max_length=50, null=False, db_column='broktype', default='')
    isusdlive = models.BooleanField(
        default=True, null=False, db_column='isusdlive')
    usdrate = models.FloatField(default=1, null=False, db_column='usdrate')
    usdcost = models.FloatField(default=0, null=False, db_column='usdcost')
    clientsharingrate = models.FloatField(
        default=0, null=False, db_column='clientsharingrate')
    brokersharingrate = models.FloatField(
        default=0, null=False, db_column='brokersharingrate')
    comsharingrate = models.FloatField(
        default=100, null=False, db_column='comsharingrate')

    sender = models.CharField(max_length=30, null=False)

    ex_buyqty = models.FloatField(default=0, null=True)
    ex_buyamt = models.FloatField(default=0, null=True)
    ex_sellqty = models.FloatField(default=0, null=True)
    ex_sellamt = models.FloatField(default=0, null=True)
    ex_charges = models.FloatField(default=0, null=True)

    class Meta:
        managed = True
        db_table = 'netposition'


class TradeBook(TimeStampedModel):
    date = models.DateField(auto_now_add=True, null=False, db_column='date')
    time = models.TimeField(auto_now_add=True, null=False, db_column='time')
    tradenum = models.CharField(
        max_length=40, null=False, db_column='tradenum')
    userId = models.CharField(max_length=15, null=False, db_column='userid')
    ctclid = models.CharField(max_length=15, default=0, db_column='ctclid')
    accountcode = models.CharField(
        max_length=15, default=0, db_column='accountcode')
    membercode = models.CharField(
        max_length=15, default=0, db_column='membercode')
    segment = models.CharField(max_length=15, null=False, db_column='segment')
    token = models.DecimalField(
        max_digits=30, decimal_places=0, null=False, db_column='token')
    multiplier = models.IntegerField(
        null=True, default=1, db_column='multiplier')
    opttype = models.CharField(max_length=3, null=False, db_column='opttype')
    expirydate = models.CharField(
        max_length=10, null=False, db_column='expirydate')
    strikeprice = models.DecimalField(
        max_digits=25, decimal_places=6, null=False, db_column='strikeprice')
    symbol = models.CharField(max_length=19, null=False, db_column='symbol')
    buysellflag = models.IntegerField(null=False, db_column='buysellflag')
    tradeqty = models.IntegerField(null=False, db_column='tradeqty')
    tradeprice = models.DecimalField(
        max_digits=25, decimal_places=6, null=False, db_column='tradeprice')
    maintradeid = models.IntegerField(null=False, db_column='maintradeid')
    securitytype = models.CharField(
        max_length=10, null=False, db_column='securitytype')
    sender = models.CharField(max_length=3, null=False, db_column='sender')
    lotsize = models.DecimalField(
        max_digits=30, decimal_places=0, null=False, db_column='lotsize')
    basecurrency = models.CharField(
        max_length=5, null=False, db_column='basecurrency')
    divider = models.IntegerField(null=False, db_column='divider')

    class Meta:
        managed = True
        db_table = 'tradebook'
        


    