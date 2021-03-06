# Generated by Django 2.0.12 on 2019-10-30 20:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Edu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='学校名称')),
                ('graduate_start_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='开始时间')),
                ('graduate_end_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='结束时间')),
                ('major', models.CharField(max_length=16, verbose_name='专业')),
                ('colleges', models.CharField(max_length=16, verbose_name='院校')),
                ('education', models.CharField(default='', max_length=100, verbose_name='学历')),
                ('degree', models.CharField(default='', max_length=100, verbose_name='学位')),
            ],
        ),
        migrations.CreateModel(
            name='EducationInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduate_school', models.CharField(default='', max_length=200, verbose_name='毕业院校')),
                ('graduate_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='毕业院校')),
                ('education_type', models.CharField(default='', max_length=100, verbose_name='受教育类型')),
                ('degree', models.CharField(default='', max_length=100, verbose_name='学位')),
                ('education', models.CharField(default='', max_length=100, verbose_name='学历')),
                ('institutions', models.CharField(default='', max_length=100, verbose_name='院校')),
                ('professional', models.CharField(default='', max_length=100, verbose_name='专业')),
                ('work_experience', models.CharField(default='', max_length=100, verbose_name='海外工作/学习经历')),
            ],
        ),
        migrations.CreateModel(
            name='Honour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='荣誉奖章')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '国家级'), (2, '省部集团'), (3, '地厅省公司')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='MajorClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='类别名称')),
                ('weight', models.IntegerField(default=1, verbose_name='权重')),
                ('status', models.IntegerField(choices=[(1, '有效'), (0, '无效')], default=1, verbose_name='状态 1：有效 0：无效')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='插入时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后一次更新时间')),
            ],
        ),
        migrations.CreateModel(
            name='MajorFirst',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='一级专业名称')),
                ('weight', models.IntegerField(default=1, verbose_name='权重')),
                ('status', models.IntegerField(choices=[(1, '有效'), (0, '无效')], default=1, verbose_name='状态 1：有效 0：无效')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='插入时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后一次更新时间')),
                ('major_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MajorClass', verbose_name='类别')),
            ],
        ),
        migrations.CreateModel(
            name='MajorSecond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16, verbose_name='二级专业名称')),
                ('weight', models.IntegerField(default=1, verbose_name='权重')),
                ('status', models.IntegerField(choices=[(1, '有效'), (0, '无效')], default=1, verbose_name='状态 1：有效 0：无效')),
                ('declare_start_time', models.DateTimeField(verbose_name='申报开始时间')),
                ('declare_end_time', models.DateTimeField(verbose_name='申报结束时间')),
                ('review_start_time', models.DateTimeField(verbose_name='评审开始时间')),
                ('review_end_time', models.DateTimeField(verbose_name='评审结束时间')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='插入时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后一次更新时间')),
                ('major_first', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MajorFirst', verbose_name='一级专业')),
            ],
        ),
        migrations.CreateModel(
            name='NationalPatent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='国家专利')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '国家发明专利'), (2, '实用行新型专利'), (3, '地厅省公司')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='职称/职鉴')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '初级'), (2, '中级(中级技师)'), (3, '高级(高级技师)')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='ProfessionalCertificationOrQualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='专业认证或资质')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '国际认证证书高级'), (2, '国际认证证书中级'), (3, '国际认证证书初级'), (4, '国内认证证书高级'), (5, '国内认证证书中级'), (6, '国内认证证书初级')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='SkillsCompetition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='技能竞赛')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '国家级'), (2, '省部集团'), (3, '地厅省公司')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='TechnologicalInnovation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='科技创新')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '国家级'), (2, '省部集团'), (3, '地厅省公司')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='ThesisWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='论文著作')),
                ('obtain_time', models.DateTimeField(verbose_name='获取时间')),
                ('level', models.IntegerField(choices=[(1, '在核心期刊发表论文或被SCI、EI、ISTP等收录的论文(第一作者)'), (2, '在核心期刊发表论文或被SCI、EI、ISTP等收录的论文(合著者)'), (3, '在CN期刊上发表的论文(第一作者)'), (4, '在CN期刊上发表的论文(合著者)'), (5, '著作第一主编'), (6, '副主编或编委')], default=1, verbose_name='等级')),
                ('extra', models.CharField(blank=True, max_length=100, null=True, verbose_name='额外的资料')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('nickname', models.CharField(blank=True, default='', max_length=16, null=True, verbose_name='昵称')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], default='male', max_length=5, verbose_name='性别')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='出生日期')),
                ('enter_the_employment_time', models.DateTimeField(blank=True, null=True, verbose_name='入职时间')),
                ('household_register_province', models.CharField(blank=True, max_length=32, null=True, verbose_name='户口所在（省）')),
                ('household_register_city', models.CharField(blank=True, max_length=32, null=True, verbose_name='户口所在（市）')),
                ('live_province', models.CharField(blank=True, max_length=32, null=True, verbose_name='现居城市（省）')),
                ('live_city', models.CharField(blank=True, max_length=32, null=True, verbose_name='现居城市（市）')),
                ('live_district', models.CharField(blank=True, max_length=32, null=True, verbose_name='现居城市（县）')),
                ('mobile', models.CharField(blank=True, default='', max_length=11, null=True, verbose_name='手机号码')),
                ('email', models.CharField(blank=True, default='', max_length=64, null=True, verbose_name='邮箱')),
                ('work_unit', models.CharField(blank=True, max_length=32, null=True, verbose_name='工作单位')),
                ('department', models.CharField(blank=True, max_length=32, null=True, verbose_name='所在部门')),
                ('marriage_status', models.CharField(blank=True, choices=[('未婚', '未婚'), ('已婚', '已婚'), ('离异', '离异')], max_length=32, null=True, verbose_name='婚姻状况')),
                ('politics', models.CharField(blank=True, choices=[('群众', '群众'), ('团员', '团员'), ('中共党员(含预备党员)', '中共党员(含预备党员)'), ('民主党派', '民主党派'), ('无党派人士', '无党派人士')], max_length=32, null=True, verbose_name='政治面貌')),
                ('globetrotters', models.CharField(blank=True, choices=[('有', '有'), ('无', '无')], max_length=32, null=True, verbose_name='海外经历')),
                ('id_card', models.CharField(max_length=18, verbose_name='身份证号码')),
                ('portrait', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='头像')),
                ('salt', models.CharField(max_length=36, verbose_name='密码密钥')),
                ('type', models.IntegerField(choices=[(1, '用户'), (2, '管理员')], default=1, verbose_name='用户权限')),
                ('status', models.IntegerField(choices=[(1, '有效'), (0, '无效')], default=1, verbose_name='是否是有效用户')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default='image/default.png', upload_to='image/%Y/%m')),
                ('nick', models.CharField(max_length=16, verbose_name='姓名')),
                ('gender', models.CharField(choices=[('male', '男'), ('female', '女')], max_length=6, verbose_name='性别')),
                ('birth_time', models.DateTimeField(default=datetime.datetime(2019, 1, 1, 12, 0), verbose_name='出生日期')),
                ('id_card', models.CharField(max_length=18, verbose_name='身份证号码')),
                ('political_landscape', models.CharField(default='群众', max_length=20, verbose_name='政治面貌')),
                ('native_place', models.CharField(default='', max_length=20, verbose_name='籍贯')),
                ('work_units', models.CharField(default='', max_length=100, verbose_name='工作单位')),
                ('department', models.CharField(default='', max_length=100, verbose_name='所在部门')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号')),
            ],
        ),
        migrations.AddField(
            model_name='thesisworks',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='technologicalinnovation',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='skillscompetition',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='professionalcertificationorqualification',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='professional',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='nationalpatent',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='honour',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='educationinfo',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
        migrations.AddField(
            model_name='edu',
            name='uid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.User', verbose_name='账号'),
        ),
    ]
