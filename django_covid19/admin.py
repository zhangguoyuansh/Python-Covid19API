from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from . import models
import json
# Register your models here.


class BaseAdmin(admin.ModelAdmin):

    list_per_page = 50

    list_max_show_all = 200

    show_full_result_count = False

    preserve_filters = True


@admin.register(models.Statistics)
class StatisticsAdmin(BaseAdmin):

    list_display = (
        'id', 'jsonGlobalStatistics', 'jsonDomesticStatistics',
        'jsonInternationalStatistics', 'modifyTime', 'crawlTime'
    )
    search_fields = ('crawlTime', 'modifyTime')

    def jsonGlobalStatistics(self, obj):
        return self.to_json(obj.globalStatistics)
    jsonGlobalStatistics.short_description = _('globalStatistics')
    jsonGlobalStatistics.admin_order_field = 'globalStatistics'

    def jsonDomesticStatistics(self, obj):
        return self.to_json(obj.domesticStatistics)
    jsonDomesticStatistics.short_description = _('domesticStatistics')
    jsonDomesticStatistics.admin_order_field = 'domesticStatistics'

    def jsonInternationalStatistics(self, obj):
        return self.to_json(obj.internationalStatistics)
    jsonInternationalStatistics.short_description \
        = _('internationalStatistics')
    jsonInternationalStatistics.admin_order_field \
        = 'internationalStatistics'

    def to_json(self, data):
        try:
            data = json.loads(data)
        except:
            return
        result = []
        for k, v in sorted(data.items()):
            result.append(format_html('{}: {}', k, v))
        return mark_safe(format_html(
            '<pre>{}</pre>', format_html('<br>'.join(result))))

@admin.register(models.City)
class CityAdmin(BaseAdmin):

    list_display = (
        'countryCode', 'provinceName', 'provinceCode', 'cityName',
        'currentConfirmedCount', 'confirmedCount', 'suspectedCount',
        'curedCount', 'deadCount', 'createTime', 'modifyTime'
    )
    search_fields = (
        'cityName', 'countryCode', 'provinceCode', 'provinceName'
    )


@admin.register(models.Province)
class ProvinceAdmin(BaseAdmin):

    list_display = (
        'countryCode', 'provinceName',
        'currentConfirmedCount', 'confirmedCount', 'suspectedCount',
        'curedCount', 'deadCount', 'createTime', 'modifyTime'
    )
    search_fields = ('provinceName', 'countryCode')


@admin.register(models.Country)
class CountryAdmin(BaseAdmin):

    list_display = (
        'continents', 'countryCode', 'countryName', 'countryFullName',
        'currentConfirmedCount', 'confirmedCount', 'suspectedCount',
        'curedCount', 'deadCount', 'createTime', 'modifyTime'
    )
    search_fields = (
        'continents', 'countryFullName', 'countryCode', 'countryName'
    )
