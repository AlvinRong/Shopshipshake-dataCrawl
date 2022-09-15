# Generated by Django 2.2 on 2021-09-01 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dealhubmodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='dealhub_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'DEALHUB',
                'db_table': 'dealhub',
            },
        ),
        migrations.CreateModel(
            name='fixmodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='fix_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'FIX',
                'db_table': 'fix',
            },
        ),
        migrations.CreateModel(
            name='jjshousemodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='jjshouse_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'JJSHOUSE',
                'db_table': 'jjshouse',
            },
        ),
        migrations.CreateModel(
            name='kikuumodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='kikuu_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'KIKUU',
                'db_table': 'kikuu',
            },
        ),
        migrations.CreateModel(
            name='kilimallmodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='kilimall_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'KILIMALL',
                'db_table': 'kilimall',
            },
        ),
        migrations.CreateModel(
            name='lovelywholesalemodel',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', upload_to='lovelywholesale_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'LOVELYWHOLE',
                'db_table': 'lovelywholesale',
            },
        ),
        migrations.CreateModel(
            name='settingmodel',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='电商名称')),
                ('hour', models.IntegerField(default=0, verbose_name='小时')),
                ('minute', models.IntegerField(default=0, verbose_name='分钟')),
            ],
            options={
                'verbose_name_plural': '配置数据',
                'db_table': 'setting',
            },
        ),
        migrations.CreateModel(
            name='wholesale7model',
            fields=[
                ('date', models.DateField(auto_now=True, null=True, verbose_name='日期')),
                ('Image', models.CharField(default=None, max_length=1000, null=True, verbose_name='图片链接')),
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, verbose_name='产品ID')),
                ('Title', models.CharField(default=None, max_length=100, null=True, verbose_name='商品名称(电商)')),
                ('price', models.CharField(default=None, max_length=100, null=True, verbose_name='商品价格')),
                ('offer_url', models.URLField(default=None, max_length=1000, null=True, verbose_name='1688商品链接')),
                ('saledCount', models.FloatField(default=0, null=True, verbose_name='已售商品数量')),
                ('service', models.FloatField(default=0, null=True, verbose_name='服务能力')),
                ('huitou', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='回头率')),
                ('wwxy', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='旺旺响应')),
                ('cfmj', models.FloatField(default=0, null=True, verbose_name='厂房面积')),
                ('zrs', models.FloatField(default=0, null=True, verbose_name='员工人数')),
                ('num_comment', models.FloatField(default=0, null=True, verbose_name='评价数目')),
                ('good_percent', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='好评率')),
                ('rateAverageStarLevel', models.DecimalField(decimal_places=1, default=0, max_digits=2, null=True, verbose_name='商品评分')),
                ('weight', models.FloatField(default=0, null=True, verbose_name='重量')),
                ('deliverySpeed', models.DecimalField(decimal_places=2, default=0, max_digits=3, null=True, verbose_name='配送速度')),
                ('picture', models.ImageField(default='static/default.jpg', null=True, upload_to='wholesale7_img/', verbose_name='商品图片')),
            ],
            options={
                'verbose_name_plural': 'WHOLESALE7',
                'db_table': 'wholesale7',
            },
        ),
    ]
