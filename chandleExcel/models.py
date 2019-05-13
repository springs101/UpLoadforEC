# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StorageFileLocal(models.Model):
    excelFile = models.FileField(upload_to="excelFile")

    class Meta:
        managed = False

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    last_name = models.CharField(max_length=150)
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


class ChandleexcelStoragefilelocal(models.Model):
    excelfile = models.CharField(db_column='excelFile', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chandleexcel_storagefilelocal'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
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


class DownloadMysql(models.Model):
    download_table = models.CharField(db_column='Download_table', max_length=255, blank=True, null=True)  # Field name made lowercase.
    download_column = models.CharField(db_column='Download_column', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mysql_table = models.CharField(max_length=255, blank=True, null=True)
    mysql_column = models.CharField(max_length=255, blank=True, null=True)
    primary_key_id = models.AutoField(db_column='Primary_key_ID', primary_key=True)  # Field name made lowercase.
    import_time = models.DateTimeField(db_column='Import_time')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'download_mysql'


class DrillingExhibitionSingleProducts(models.Model):
    basic_planning_information = models.CharField(db_column='Basic_Planning_Information', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creative_name = models.CharField(db_column='Creative_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basic_information_of_extension_unit = models.CharField(db_column='Basic_Information_of_Extension_Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(max_length=255, blank=True, null=True)
    to_show = models.CharField(db_column='To_show', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click = models.CharField(max_length=255, blank=True, null=True)
    consume = models.CharField(max_length=255, blank=True, null=True)
    click_rate = models.CharField(db_column='Click_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_on_unit_price_yuan = models.CharField(db_column='Click_on_unit_price_yuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thousands_of_exhibition_costs_yuan = models.CharField(db_column='Thousands_of_exhibition_costs_yuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visitor = models.CharField(db_column='Visitor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deep_store_entry = models.CharField(db_column='Deep_Store_Entry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    length_of_visit = models.CharField(db_column='Length_of_visit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_pages_accessed = models.CharField(db_column='Number_of_pages_accessed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collection_of_baby_quantity = models.CharField(db_column='Collection_of_Baby_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collection_store_quantity = models.CharField(db_column='Collection_Store_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    add_shopping_cart_volume = models.CharField(db_column='Add_shopping_cart_volume', max_length=255, blank=True, null=True)  # Field name made lowercase.
    take_orders = models.CharField(db_column='Take_orders', max_length=255, blank=True, null=True)  # Field name made lowercase.
    take_the_order_amount = models.CharField(db_column='Take_the_order_amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transaction_order_quantity = models.CharField(db_column='Transaction_Order_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transaction_order_amount = models.CharField(db_column='Transaction_order_amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_conversion = models.CharField(db_column='Click_conversion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    return_on_investment = models.CharField(db_column='Return_on_investment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversion_time = models.CharField(db_column='Conversion_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary_key_id = models.AutoField(db_column='Primary_key_ID', primary_key=True)  # Field name made lowercase.
    import_time = models.DateTimeField(db_column='Import_time',auto_now_add=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=255, blank=True,null=True)  # Field name made lowercase.
    shop_name = models.CharField(db_column='Shop_name', max_length=255, blank=True,null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'drilling_exhibition_single_products'


class DrillingExhibitionWholeStore(models.Model):
    basic_planning_information = models.CharField(db_column='Basic_Planning_Information', max_length=255, blank=True, null=True)  # Field name made lowercase.
    creative_name = models.CharField(db_column='Creative_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    basic_information_of_extension_unit = models.CharField(db_column='Basic_Information_of_Extension_Unit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    time = models.CharField(max_length=255, blank=True, null=True)
    to_show = models.CharField(db_column='To_show', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click = models.CharField(max_length=255, blank=True, null=True)
    consume = models.CharField(max_length=255, blank=True, null=True)
    click_rate = models.CharField(db_column='Click_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_on_unit_price_yuan = models.CharField(db_column='Click_on_unit_price_yuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thousands_of_exhibition_costs_yuan = models.CharField(db_column='Thousands_of_exhibition_costs_yuan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visitor = models.CharField(db_column='Visitor', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deep_store_entry = models.CharField(db_column='Deep_Store_Entry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    length_of_visit = models.CharField(db_column='Length_of_visit', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_pages_accessed = models.CharField(db_column='Number_of_pages_accessed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collection_of_baby_quantity = models.CharField(db_column='Collection_of_Baby_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collection_store_quantity = models.CharField(db_column='Collection_Store_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    add_shopping_cart_volume = models.CharField(db_column='Add_shopping_cart_volume', max_length=255, blank=True, null=True)  # Field name made lowercase.
    take_orders = models.CharField(db_column='Take_orders', max_length=255, blank=True, null=True)  # Field name made lowercase.
    take_the_order_amount = models.CharField(db_column='Take_the_order_amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transaction_order_quantity = models.CharField(db_column='Transaction_Order_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transaction_order_amount = models.CharField(db_column='Transaction_order_amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_conversion = models.CharField(db_column='Click_conversion', max_length=255, blank=True, null=True)  # Field name made lowercase.
    return_on_investment = models.CharField(db_column='Return_on_investment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    action_volume = models.CharField(db_column='Action_volume', max_length=255, blank=True, null=True)  # Field name made lowercase.
    action_cost = models.CharField(db_column='Action_cost', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversion_time = models.CharField(db_column='Conversion_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary_key_id = models.AutoField(db_column='Primary_key_ID', primary_key=True)  # Field name made lowercase.
    import_time = models.DateTimeField(db_column='Import_time',auto_now_add=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=255, blank=True,null=True)  # Field name made lowercase.
    shop_name = models.CharField(db_column='Shop_name', max_length=255, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drilling_exhibition_whole_store'


class SuperRecommendation(models.Model):
    date = models.CharField(max_length=255, blank=True, null=True)
    plan = models.CharField(max_length=255, blank=True, null=True)
    unit = models.CharField(max_length=255, blank=True, null=True)
    originality_id = models.CharField(db_column='Originality_ID', max_length=255, blank=True,null=True)  # Field name made lowercase.
    number_of_collection_stores= models.CharField(db_column='Number_of_Collection_Stores', max_length=255, blank=True,null=True)  # Field name made lowercase.
    originality = models.CharField(db_column='Originality', max_length=255, blank=True, null=True)  # Field name made lowercase.
    effective_display = models.CharField(db_column='Effective_display', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_valid_clicks = models.CharField(db_column='Number_of_valid_clicks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thousands_of_exhibition_costs = models.CharField(db_column='Thousands_of_exhibition_costs', max_length=255, blank=True, null=True)  # Field name made lowercase.
    consume = models.CharField(max_length=255, blank=True, null=True)
    click_the_unit_price = models.CharField(db_column='Click_the_unit_price', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_through_rate = models.CharField(db_column='Click_through_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lead_in_the_store = models.CharField(db_column='Lead_in_the_store', max_length=255, blank=True, null=True)  # Field name made lowercase.
    lead_in_rate = models.CharField(db_column='Lead_in_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_guided_shopkeepers = models.CharField(db_column='Number_of_guided_shopkeepers', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_sneakers_guided_into_stores = models.CharField(db_column='Number_of_sneakers_guided_into_stores', max_length=255, blank=True, null=True)  # Field name made lowercase.
    directing_divers_into_stores = models.CharField(db_column='Directing_divers_into_stores', max_length=255, blank=True, null=True)  # Field name made lowercase.
    deep_store_entry = models.CharField(db_column='Deep_Store_Entry', max_length=255, blank=True, null=True)  # Field name made lowercase.
    average_access_time = models.CharField(db_column='Average_access_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    average_number_of_pages_accessed = models.CharField(db_column='Average_number_of_pages_accessed', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pay_attention_to_store_volume = models.CharField(db_column='Pay_attention_to_store_volume', max_length=255, blank=True, null=True)  # Field name made lowercase.
    new_passenger_acquisition = models.CharField(db_column='New_passenger_acquisition', max_length=255, blank=True, null=True)  # Field name made lowercase.
    new_customer_acquisition_rate = models.CharField(db_column='New_customer_acquisition_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pull_new_cost = models.CharField(db_column='Pull_new_cost', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pull_new_consumption = models.CharField(db_column='Pull_new_consumption', max_length=255, blank=True, null=True)  # Field name made lowercase.
    collection_of_baby_numbers = models.CharField(db_column='Collection_of_Baby_Numbers', max_length=255, blank=True, null=True)  # Field name made lowercase.
    add_the_number_of_shopping_carts = models.CharField(db_column='Add_the_number_of_shopping_carts', max_length=255, blank=True, null=True)  # Field name made lowercase.
    take_orders = models.CharField(db_column='Take_orders', max_length=255, blank=True, null=True)  # Field name made lowercase.
    take_the_order_amount = models.CharField(db_column='Take_the_order_amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transaction_order_quantity = models.CharField(db_column='Transaction_Order_Quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    transaction_order_amount = models.CharField(db_column='Transaction_order_amount', max_length=255, blank=True, null=True)  # Field name made lowercase.
    display_conversion_rate = models.CharField(db_column='Display_conversion_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_conversion_rate = models.CharField(db_column='Click_Conversion_Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    return_on_investment = models.CharField(db_column='Return_on_investment', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversion_time = models.CharField(db_column='Conversion_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    import_time = models.DateTimeField(db_column='Import_time',blank=True,auto_now_add=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=255, blank=True,null=True)  # Field name made lowercase.
    shop_name = models.CharField(db_column='Shop_name', max_length=255, blank=True,null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'super_recommendation'


class TbSycmQsDpztJzmt(models.Model):
    tjrq = models.CharField(max_length=50, blank=True, null=True)
    pcdfks = models.CharField(max_length=50, blank=True, null=True)
    pcdlll = models.CharField(max_length=50, blank=True, null=True)
    fks = models.CharField(max_length=50, blank=True, null=True)
    wxdfks = models.CharField(max_length=50, blank=True, null=True)
    lll = models.CharField(max_length=50, blank=True, null=True)
    wxdlll = models.CharField(max_length=50, blank=True, null=True)
    spfks = models.CharField(max_length=50, blank=True, null=True)
    wxdspfks = models.CharField(max_length=50, blank=True, null=True)
    pcdspfks = models.CharField(max_length=50, blank=True, null=True)
    splll = models.CharField(max_length=50, blank=True, null=True)
    wxdsplll = models.CharField(max_length=50, blank=True, null=True)
    pcdsplll = models.CharField(max_length=50, blank=True, null=True)
    pjtlsc = models.CharField(max_length=50, blank=True, null=True)
    wxdpjtlsc = models.CharField(max_length=50, blank=True, null=True)
    pcdpjtlsc = models.CharField(max_length=50, blank=True, null=True)
    tsl = models.CharField(max_length=50, blank=True, null=True)
    wxdtsl = models.CharField(max_length=50, blank=True, null=True)
    pcdtsl = models.CharField(max_length=50, blank=True, null=True)
    spscmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdspscmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdspscmjs = models.CharField(max_length=50, blank=True, null=True)
    spsccs = models.CharField(max_length=50, blank=True, null=True)
    wxdspsccs = models.CharField(max_length=50, blank=True, null=True)
    pcdspsccs = models.CharField(max_length=50, blank=True, null=True)
    jgrs = models.CharField(max_length=50, blank=True, null=True)
    wxdjgrs = models.CharField(max_length=50, blank=True, null=True)
    pcdjgrs = models.CharField(max_length=50, blank=True, null=True)
    zfje = models.CharField(max_length=50, blank=True, null=True)
    pcdzfje = models.CharField(max_length=50, blank=True, null=True)
    wxdzfje = models.CharField(max_length=50, blank=True, null=True)
    zfmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdzfmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdzfmjs = models.CharField(max_length=50, blank=True, null=True)
    zfzdds = models.CharField(max_length=50, blank=True, null=True)
    pcdzfzdds = models.CharField(max_length=50, blank=True, null=True)
    wxdzfzdds = models.CharField(max_length=50, blank=True, null=True)
    zfjs = models.CharField(max_length=50, blank=True, null=True)
    pcdzfjs = models.CharField(max_length=50, blank=True, null=True)
    wxdzfjs = models.CharField(max_length=50, blank=True, null=True)
    xdje = models.CharField(max_length=50, blank=True, null=True)
    pcdxdje = models.CharField(max_length=50, blank=True, null=True)
    wxdxdje = models.CharField(max_length=50, blank=True, null=True)
    xdmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdxdmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdxdmjs = models.CharField(max_length=50, blank=True, null=True)
    xdjs = models.CharField(max_length=50, blank=True, null=True)
    pcdxdjs = models.CharField(max_length=50, blank=True, null=True)
    wxdxdjs = models.CharField(max_length=50, blank=True, null=True)
    rjlll = models.CharField(max_length=50, blank=True, null=True)
    pcdrjlll = models.CharField(max_length=50, blank=True, null=True)
    wxdrjlll = models.CharField(max_length=50, blank=True, null=True)
    xdzhl = models.CharField(max_length=50, blank=True, null=True)
    pcdxdzhl = models.CharField(max_length=50, blank=True, null=True)
    wxdxdzhl = models.CharField(max_length=50, blank=True, null=True)
    zfzhl = models.CharField(max_length=50, blank=True, null=True)
    pcdzfzhl = models.CharField(max_length=50, blank=True, null=True)
    wxdzfzhl = models.CharField(max_length=50, blank=True, null=True)
    kdj = models.CharField(max_length=50, blank=True, null=True)
    pcdkdj = models.CharField(max_length=50, blank=True, null=True)
    wxdkdj = models.CharField(max_length=50, blank=True, null=True)
    uvjz = models.CharField(max_length=50, blank=True, null=True)
    pcduvjz = models.CharField(max_length=50, blank=True, null=True)
    wxduvjz = models.CharField(max_length=50, blank=True, null=True)
    lfks = models.CharField(max_length=50, blank=True, null=True)
    xfks = models.CharField(max_length=50, blank=True, null=True)
    wxdlfks = models.CharField(max_length=50, blank=True, null=True)
    wxdxfks = models.CharField(max_length=50, blank=True, null=True)
    pcdlfks = models.CharField(max_length=50, blank=True, null=True)
    pcdxfks = models.CharField(max_length=50, blank=True, null=True)
    jgjs = models.CharField(max_length=50, blank=True, null=True)
    pcdjgjs = models.CharField(max_length=50, blank=True, null=True)
    wxdjgjs = models.CharField(max_length=50, blank=True, null=True)
    zflmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdzflmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdzflmjs = models.CharField(max_length=50, blank=True, null=True)
    lmjzfje = models.CharField(max_length=50, blank=True, null=True)
    ztcxh = models.CharField(max_length=50, blank=True, null=True)
    zszwxh = models.CharField(max_length=50, blank=True, null=True)
    tbkyj = models.CharField(max_length=50, blank=True, null=True)
    cgtkje = models.CharField(max_length=50, blank=True, null=True)
    pjs = models.CharField(max_length=50, blank=True, null=True)
    ytpjs = models.CharField(max_length=50, blank=True, null=True)
    zmpjs = models.CharField(max_length=50, blank=True, null=True)
    fmpjs = models.CharField(max_length=50, blank=True, null=True)
    lmjzmpjs = models.CharField(max_length=50, blank=True, null=True)
    lmjfmpjs = models.CharField(max_length=50, blank=True, null=True)
    zffdds = models.CharField(max_length=50, blank=True, null=True)
    lsbgs = models.CharField(max_length=50, blank=True, null=True)
    fhbgs = models.CharField(max_length=50, blank=True, null=True)
    psbgs = models.CharField(max_length=50, blank=True, null=True)
    qscgbgs = models.CharField(max_length=50, blank=True, null=True)
    pjzf_qssc = models.CharField(max_length=50, blank=True, null=True)
    msxfpf = models.CharField(max_length=50, blank=True, null=True)
    wlfwpf = models.CharField(max_length=50, blank=True, null=True)
    fwtdpf = models.CharField(max_length=50, blank=True, null=True)
    xd_zfzhl = models.CharField(max_length=50, blank=True, null=True)
    pcdxd_zfzhl = models.CharField(max_length=50, blank=True, null=True)
    wxdxd_zfzhl = models.CharField(max_length=50, blank=True, null=True)
    zfsps = models.CharField(max_length=50, blank=True, null=True)
    pcdzfsps = models.CharField(max_length=50, blank=True, null=True)
    wxdzfsps = models.CharField(max_length=50, blank=True, null=True)
    dpscmjs = models.CharField(max_length=50, blank=True, null=True)
    pcddpscmjs = models.CharField(max_length=50, blank=True, null=True)
    wxddpscmjs = models.CharField(max_length=50, blank=True, null=True)
    p_id = models.AutoField(db_column='P_id', primary_key=True)  # Field name made lowercase.
    p_new = models.DateTimeField(db_column='P_new')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_sycm_qs_dpzt_jzmt'


class TbSycmQsDpztZmt(models.Model):
    tjrq = models.CharField(max_length=50, blank=True, null=True)
    pcdfks = models.CharField(max_length=50, blank=True, null=True)
    pcdlll = models.CharField(max_length=50, blank=True, null=True)
    fks = models.CharField(max_length=50, blank=True, null=True)
    wxdfks = models.CharField(max_length=50, blank=True, null=True)
    lll = models.CharField(max_length=50, blank=True, null=True)
    wxdlll = models.CharField(max_length=50, blank=True, null=True)
    spfks = models.CharField(max_length=50, blank=True, null=True)
    wxdspfks = models.CharField(max_length=50, blank=True, null=True)
    pcdspfks = models.CharField(max_length=50, blank=True, null=True)
    splll = models.CharField(max_length=50, blank=True, null=True)
    wxdsplll = models.CharField(max_length=50, blank=True, null=True)
    pcdsplll = models.CharField(max_length=50, blank=True, null=True)
    pjtlsc = models.CharField(max_length=50, blank=True, null=True)
    wxdpjtlsc = models.CharField(max_length=50, blank=True, null=True)
    pcdpjtlsc = models.CharField(max_length=50, blank=True, null=True)
    tsl = models.CharField(max_length=50, blank=True, null=True)
    wxdtsl = models.CharField(max_length=50, blank=True, null=True)
    pcdtsl = models.CharField(max_length=50, blank=True, null=True)
    spscmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdspscmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdspscmjs = models.CharField(max_length=50, blank=True, null=True)
    spsccs = models.CharField(max_length=50, blank=True, null=True)
    wxdspsccs = models.CharField(max_length=50, blank=True, null=True)
    pcdspsccs = models.CharField(max_length=50, blank=True, null=True)
    jgrs = models.CharField(max_length=50, blank=True, null=True)
    wxdjgrs = models.CharField(max_length=50, blank=True, null=True)
    pcdjgrs = models.CharField(max_length=50, blank=True, null=True)
    zfje = models.CharField(max_length=50, blank=True, null=True)
    pcdzfje = models.CharField(max_length=50, blank=True, null=True)
    wxdzfje = models.CharField(max_length=50, blank=True, null=True)
    zfmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdzfmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdzfmjs = models.CharField(max_length=50, blank=True, null=True)
    zfzdds = models.CharField(max_length=50, blank=True, null=True)
    pcdzfzdds = models.CharField(max_length=50, blank=True, null=True)
    wxdzfzdds = models.CharField(max_length=50, blank=True, null=True)
    zfjs = models.CharField(max_length=50, blank=True, null=True)
    pcdzfjs = models.CharField(max_length=50, blank=True, null=True)
    wxdzfjs = models.CharField(max_length=50, blank=True, null=True)
    xdje = models.CharField(max_length=50, blank=True, null=True)
    pcdxdje = models.CharField(max_length=50, blank=True, null=True)
    wxdxdje = models.CharField(max_length=50, blank=True, null=True)
    xdmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdxdmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdxdmjs = models.CharField(max_length=50, blank=True, null=True)
    xdjs = models.CharField(max_length=50, blank=True, null=True)
    pcdxdjs = models.CharField(max_length=50, blank=True, null=True)
    wxdxdjs = models.CharField(max_length=50, blank=True, null=True)
    rjlll = models.CharField(max_length=50, blank=True, null=True)
    pcdrjlll = models.CharField(max_length=50, blank=True, null=True)
    wxdrjlll = models.CharField(max_length=50, blank=True, null=True)
    xdzhl = models.CharField(max_length=50, blank=True, null=True)
    pcdxdzhl = models.CharField(max_length=50, blank=True, null=True)
    wxdxdzhl = models.CharField(max_length=50, blank=True, null=True)
    zfzhl = models.CharField(max_length=50, blank=True, null=True)
    pcdzfzhl = models.CharField(max_length=50, blank=True, null=True)
    wxdzfzhl = models.CharField(max_length=50, blank=True, null=True)
    kdj = models.CharField(max_length=50, blank=True, null=True)
    pcdkdj = models.CharField(max_length=50, blank=True, null=True)
    wxdkdj = models.CharField(max_length=50, blank=True, null=True)
    uvjz = models.CharField(max_length=50, blank=True, null=True)
    pcduvjz = models.CharField(max_length=50, blank=True, null=True)
    wxduvjz = models.CharField(max_length=50, blank=True, null=True)
    lfks = models.CharField(max_length=50, blank=True, null=True)
    xfks = models.CharField(max_length=50, blank=True, null=True)
    wxdlfks = models.CharField(max_length=50, blank=True, null=True)
    wxdxfks = models.CharField(max_length=50, blank=True, null=True)
    pcdlfks = models.CharField(max_length=50, blank=True, null=True)
    pcdxfks = models.CharField(max_length=50, blank=True, null=True)
    jgjs = models.CharField(max_length=50, blank=True, null=True)
    pcdjgjs = models.CharField(max_length=50, blank=True, null=True)
    wxdjgjs = models.CharField(max_length=50, blank=True, null=True)
    zflmjs = models.CharField(max_length=50, blank=True, null=True)
    pcdzflmjs = models.CharField(max_length=50, blank=True, null=True)
    wxdzflmjs = models.CharField(max_length=50, blank=True, null=True)
    lmjzfje = models.CharField(max_length=50, blank=True, null=True)
    ztcxh = models.CharField(max_length=50, blank=True, null=True)
    zszwxh = models.CharField(max_length=50, blank=True, null=True)
    tbkyj = models.CharField(max_length=50, blank=True, null=True)
    cgtkje = models.CharField(max_length=50, blank=True, null=True)
    pjs = models.CharField(max_length=50, blank=True, null=True)
    ytpjs = models.CharField(max_length=50, blank=True, null=True)
    zmpjs = models.CharField(max_length=50, blank=True, null=True)
    fmpjs = models.CharField(max_length=50, blank=True, null=True)
    lmjzmpjs = models.CharField(max_length=50, blank=True, null=True)
    lmjfmpjs = models.CharField(max_length=50, blank=True, null=True)
    zffdds = models.CharField(max_length=50, blank=True, null=True)
    lsbgs = models.CharField(max_length=50, blank=True, null=True)
    fhbgs = models.CharField(max_length=50, blank=True, null=True)
    psbgs = models.CharField(max_length=50, blank=True, null=True)
    qscgbgs = models.CharField(max_length=50, blank=True, null=True)
    pjzf_qssc = models.CharField(max_length=50, blank=True, null=True)
    msxfpf = models.CharField(max_length=50, blank=True, null=True)
    wlfwpf = models.CharField(max_length=50, blank=True, null=True)
    fwtdpf = models.CharField(max_length=50, blank=True, null=True)
    xd_zfzhl = models.CharField(max_length=50, blank=True, null=True)
    pcdxd_zfzhl = models.CharField(max_length=50, blank=True, null=True)
    wxdxd_zfzhl = models.CharField(max_length=50, blank=True, null=True)
    zfsps = models.CharField(max_length=50, blank=True, null=True)
    pcdzfsps = models.CharField(max_length=50, blank=True, null=True)
    wxdzfsps = models.CharField(max_length=50, blank=True, null=True)
    dpscmjs = models.CharField(max_length=50, blank=True, null=True)
    pcddpscmjs = models.CharField(max_length=50, blank=True, null=True)
    wxddpscmjs = models.CharField(max_length=50, blank=True, null=True)
    p_id = models.AutoField(db_column='P_id', primary_key=True)  # Field name made lowercase.
    p_new = models.DateTimeField(db_column='P_new')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tb_sycm_qs_dpzt_zmt'


class ThroughTrain(models.Model):
    date = models.CharField(max_length=255, blank=True, null=True)
    name_of_promotion_plan = models.CharField(db_column='Name_of_Promotion_Plan', max_length=255, blank=True, null=True)  # Field name made lowercase.
    baby_name = models.CharField(db_column='Baby_name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    baby_type = models.CharField(db_column='Baby_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    commodity_id = models.CharField(db_column='Commodity_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    search_type = models.CharField(db_column='Search_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    traffic_source = models.CharField(db_column='Traffic_source', max_length=255, blank=True, null=True)  # Field name made lowercase.
    display_quantity = models.CharField(db_column='Display_quantity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    clicks = models.CharField(db_column='Clicks', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cost_points = models.CharField(db_column='Cost_points', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_through_rate = models.CharField(db_column='Click_through_rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    average_click_cost_points = models.CharField(db_column='Average_Click_Cost_Points', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thousands_of_showcases_points = models.CharField(db_column='Thousands_of_showcases_points', max_length=255, blank=True, null=True)  # Field name made lowercase.
    click_conversion_rate = models.CharField(db_column='Click_Conversion_Rate', max_length=255, blank=True, null=True)  # Field name made lowercase.
    direct_transaction_amount_points = models.CharField(db_column='Direct_Transaction_Amount_Points', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_direct_transactions = models.CharField(db_column='Number_of_direct_transactions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indirect_transaction_amount_points = models.CharField(db_column='Indirect_transaction_amount_points', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_indirect_transactions = models.CharField(db_column='Number_of_indirect_transactions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_transaction_amount_points = models.CharField(db_column='Total_transaction_amount_points', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_total_transactions = models.CharField(db_column='Number_of_total_transactions', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_baby_collections = models.CharField(db_column='Number_of_Baby_Collections', max_length=255, blank=True, null=True)  # Field name made lowercase.
    store_collection_number = models.CharField(db_column='Store_Collection_Number', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_collection = models.CharField(db_column='Total_collection', max_length=255, blank=True, null=True)  # Field name made lowercase.
    input_output_ratio = models.CharField(db_column='Input_output_ratio', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_direct_shopping_carts = models.CharField(db_column='Number_of_direct_shopping_carts', max_length=255, blank=True, null=True)  # Field name made lowercase.
    number_of_indirect_shopping_carts = models.CharField(db_column='Number_of_indirect_shopping_carts', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total_number_of_shopping_carts = models.CharField(db_column='Total_number_of_shopping_carts', max_length=255, blank=True, null=True)  # Field name made lowercase.
    conversion_time = models.CharField(db_column='Conversion_time', max_length=255, blank=True, null=True)  # Field name made lowercase.
    primary_key_id = models.AutoField(db_column='Primary_key_ID', primary_key=True)  # Field name made lowercase.
    import_time = models.DateTimeField(db_column='Import_time',auto_now_add=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'through_train'
