from django.db import models

# Create your models here.


class WeatherRegionParameters(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    region = models.CharField(null=False, blank=False, max_length=100)
    parameter = models.CharField(null=False, blank=False, max_length=100)
    order = models.CharField(null=False, blank=False, max_length=100)
    last_updated_on_MONCIL = models.DateTimeField(null=True, blank=True)
    last_updated_in_db = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'WeatherRegionParameters'
        verbose_name_plural = 'WeatherRegionParameters'
        unique_together = ('region', 'parameter', 'order', 'last_updated_on_MONCIL')

    def __str__(self):
        return self.region, self.parameter, self.order


class RankWiseWeatherInfo(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    weather = models.ForeignKey(WeatherRegionParameters, on_delete=models.CASCADE, db_column='weather')
    jan = models.FloatField(blank=True, null=True)
    feb = models.FloatField(blank=True, null=True)
    mar = models.FloatField(blank=True, null=True)
    apr = models.FloatField(blank=True, null=True)
    may = models.FloatField(blank=True, null=True)
    jun = models.FloatField(blank=True, null=True)
    jul = models.FloatField(blank=True, null=True)
    aug = models.FloatField(blank=True, null=True)
    sep = models.FloatField(blank=True, null=True)
    oct = models.FloatField(blank=True, null=True)
    nov = models.FloatField(blank=True, null=True)
    dec = models.FloatField(blank=True, null=True)
    win = models.FloatField(blank=True, null=True)
    spr = models.FloatField(blank=True, null=True)
    sum = models.FloatField(blank=True, null=True)
    aut = models.FloatField(blank=True, null=True)
    ann = models.FloatField(blank=True, null=True)
    jan_year = models.DateField(blank=True, null=True)
    feb_year = models.DateField(blank=True, null=True)
    mar_year = models.DateField(blank=True, null=True)
    apr_year = models.DateField(blank=True, null=True)
    may_year = models.DateField(blank=True, null=True)
    jun_year = models.DateField(blank=True, null=True)
    jul_year = models.DateField(blank=True, null=True)
    aug_year = models.DateField(blank=True, null=True)
    sep_year = models.DateField(blank=True, null=True)
    oct_year = models.DateField(blank=True, null=True)
    nov_year = models.DateField(blank=True, null=True)
    dec_year = models.DateField(blank=True, null=True)
    win_year = models.DateField(blank=True, null=True)
    spr_year = models.DateField(blank=True, null=True)
    sum_year = models.DateField(blank=True, null=True)
    aut_year = models.DateField(blank=True, null=True)
    ann_year = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'RankWiseWeatherInfo'
        verbose_name_plural = 'Rank_Wise_Weather_Info'

    def __str__(self):
        return str(self.last_updated)


class YearWiseWeatherInfo(models.Model):
    id = models.BigAutoField(primary_key=True, null=False)
    weather = models.ForeignKey(WeatherRegionParameters, on_delete=models.CASCADE, db_column='weather')
    jan = models.FloatField(blank=True, null=True)
    feb = models.FloatField(blank=True, null=True)
    mar = models.FloatField(blank=True, null=True)
    apr = models.FloatField(blank=True, null=True)
    may = models.FloatField(blank=True, null=True)
    jun = models.FloatField(blank=True, null=True)
    jul = models.FloatField(blank=True, null=True)
    aug = models.FloatField(blank=True, null=True)
    sep = models.FloatField(blank=True, null=True)
    oct = models.FloatField(blank=True, null=True)
    nov = models.FloatField(blank=True, null=True)
    dec = models.FloatField(blank=True, null=True)
    win = models.FloatField(blank=True, null=True)
    spr = models.FloatField(blank=True, null=True)
    sum = models.FloatField(blank=True, null=True)
    aut = models.FloatField(blank=True, null=True)
    ann = models.FloatField(blank=True, null=True)
    year = models.DateField(blank=True, null=True)
    last_updated = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'YearWiseWeatherInfo'
        verbose_name_plural = 'Year_Wise_Weather_Info'

    def __str__(self):
        return str(self.year)
