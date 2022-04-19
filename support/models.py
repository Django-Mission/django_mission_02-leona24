from django.db import models

# Create your models here.
class Faq(models.Model):
    Question = models.TextField(verbose_name='질문')
    CommonCategory = '일반'
    AccountCategory = '계정'
    ExtraCategory = '기타'
    Categories_CHOICES = [
        ( CommonCategory, '일반카테고리'),
        ( AccountCategory, '계정카테고리'),
        ( ExtraCategory, '기타카테고리')
        ]
    Answer = models.TextField(verbose_name='답변')
    Editor = models.TextField(verbose_name='생성자')
    Date = models.TextField(verbose_name='생성일시')
    LastEditor = models.TextField(verbose_name='최종 수정자')
    Lastdate = models.TextField(verbose_name='최종 수정일시')
    