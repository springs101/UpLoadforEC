from django.shortcuts import render
import os
from django.views.decorators.csrf import csrf_exempt
from .forms import UploadFileForm
from .forms1 import UploadFileForm1
from .forms2 import UploadFileForm2
from .forms3 import UploadFileForm3
from chandleExcel.models import StorageFileLocal
from django.http import HttpResponse
from chandleExcel import models
import time
import datetime
from xlrd import xldate_as_tuple
import csv
import platform
# Create your views here.

import xlrd

@csrf_exempt
def showpage(request):
    form = UploadFileForm()
    form1 = UploadFileForm1()
    form2 = UploadFileForm2()
    form3 = UploadFileForm3()

    return render(request, 'update.html',{'form': form,'form1':form1,'form2':form2,'form3':form3})
@csrf_exempt
def getExcel_tuijian(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)  # 注意获取数据的方式
        if form.is_valid():
           storagefile=StorageFileLocal()
           storagefile.excelFile=form.cleaned_data["file1"]
           if IdentifyFileExist(storagefile.excelFile.path):
              return HttpResponse("文件已经上传完毕！请检查", content_type="application/json")
           try:
             storagefile.save()
           except Exception as err:
               return HttpResponse(err, content_type="application/json")
           msg=handle_uploaded_file(storagefile.excelFile,"超级推荐")
           return HttpResponse(msg, content_type="application/json")
        else:
           return HttpResponse("表单有问题", content_type="application/json")

    else:
        form = UploadFileForm()

    return render(request, 'update.html')
@csrf_exempt
def getExcel_zhitongche(request):
    if request.method == 'POST':
        form = UploadFileForm1(request.POST, request.FILES)  # 注意获取数据的方式
        if form.is_valid():
           storagefile=StorageFileLocal()
           storagefile.excelFile=form.cleaned_data["file1"]
           if IdentifyFileExist(storagefile.excelFile.path):
               return HttpResponse("文件已经上传完毕！请检查", content_type="application/json")
           try:
             storagefile.save()
           except Exception as err:
               return HttpResponse(err, content_type="application/json")
           handle_uploaded_file(storagefile.excelFile,"直通车")
           return HttpResponse("上传成功", content_type="application/json")
        else:
           return HttpResponse("表单有问题", content_type="application/json")

    else:
        form = UploadFileForm()

    return render(request, 'update.html')
@csrf_exempt
def getExcel_zzdanpin(request):
    if request.method == 'POST':
        form = UploadFileForm2(request.POST, request.FILES)  # 注意获取数据的方式
        if form.is_valid():
           storagefile=StorageFileLocal()
           storagefile.excelFile=form.cleaned_data["file1"]
           if IdentifyFileExist(storagefile.excelFile.path):
               return HttpResponse("文件已经上传完毕！请检查", content_type="application/json")
           try:
             storagefile.save()
           except Exception as err:
               return HttpResponse(err, content_type="application/json")
           handle_uploaded_file(storagefile.excelFile,"钻展-单品")
           return HttpResponse("上传成功", content_type="application/json")
        else:
           return HttpResponse("表单有问题", content_type="application/json")

    else:
        form = UploadFileForm()

    return render(request, 'update.html')
@csrf_exempt
def getExcel_zzquandian(request):
    if request.method == 'POST':
        form = UploadFileForm3(request.POST, request.FILES)  # 注意获取数据的方式
        if form.is_valid():
           storagefile=StorageFileLocal()
           storagefile.excelFile=form.cleaned_data["file1"]
           if IdentifyFileExist(storagefile.excelFile.path):
               return HttpResponse("文件已经上传完毕！请检查", content_type="application/json")
           try:
             storagefile.save()
           except Exception as err:
               return HttpResponse(err, content_type="application/json")
           handle_uploaded_file(storagefile.excelFile,"钻展-全店")
           return HttpResponse("上传成功", content_type="application/json")
        else:
           return HttpResponse("表单有问题", content_type="application/json")

    else:
        form = UploadFileForm()

    return render(request, 'update.html')


def handle_uploaded_file(f,type='超级推荐'):
    print("开始解析excel")
    if type=='直通车':
        try:
          csv_reader = csv.reader(open(f.path, encoding='utf-8'))
        except Exception as err:
            os.remove(f.path)
            return err
        res=filter_cvs(csv_reader,f.path)
        if res=='ok':
            res='上传成功'
        else:
            os.remove(f.path)
        return res
    else:
       try:
          data = xlrd.open_workbook(f.path)
       except Exception as err:
          os.remove(f.path)
          print(err)
       res=filter_excel(data,type)
       if res=='ok':
           res='上传成功'
       else:
           os.remove(f.path)
       return res
def filter_cvs(cvs_reader,fpath):
    setType="直通车"
    try:
      listFile=filter_cvs_sort(cvs_reader)
    except Exception as err:
        return err
    MinDate = getMinTime(listFile, setType)

    rander_reader=csv.reader(open(fpath, encoding='utf-8'))
    table_header = []
    for i, rows in enumerate(rander_reader):
        if i == 0:
            table_header = rows
            table_header[0]='日期'
            break
    print(table_header)

    resCom = compareHead(table_header,setType)
    if not resCom['status'] == 'ok':
        return resCom['status']

    rander_reader1 = csv.reader(open(fpath, encoding='utf-8'))
    excel_list = []
    for j, rows in enumerate(rander_reader1):  # 也就是从Excel第二行开始，第一行表头不算
        if j==0:
            continue
        Tempdate=''
        if rows:
            row_object = {}
            i = 0
            for node in rows:
                key = table_header[i]
                newkey=getkeyvalue(resCom['data'],key)
                if newkey=='date':
                    Tempdate = node
                row_object[newkey] = node  # 表头与数据对应
                i = i + 1
            row_object["Conversion_time"] = getchangetime(MinDate, Tempdate)
            excel_list.append(row_object)
    print(excel_list)
    outlist = []
    outlist = changeList(excel_list, setType)
    try:
          models.ThroughTrain.objects.bulk_create(outlist)
    except Exception as err:
          print(err)
    return 'ok'
def filter_cvs_sort(cvs_reader):
    table_header =[]
    for i, rows in enumerate(cvs_reader):
        if i == 0:
            table_header = rows
            break
    print(table_header)

    excel_list = []
    for j,rows in enumerate(cvs_reader):  # 也就是从Excel第二行开始，第一行表头不算
        if rows:
            row_object = {}
            i=0
            for node in rows:
                key = table_header[i]
                row_object[key] = node  # 表头与数据对应
                i=i+1
            excel_list.append(row_object)
    print(excel_list)
    return excel_list
def filter_excel(workbook, type,column_name=0):

    table = workbook.sheets()[0]  # 获第一张表格
    table_header = table.row_values(0)
    resCom = compareHead(table_header, type)
    if not resCom['status'] == 'ok':
        return resCom['status']

    listFile=filter_excel_sort(workbook)
    MinDate=getMinTime(listFile,type)


    total_rows = table.nrows  # 拿到总共行数
    columns = table.row_values(column_name)  # 某一行数据 ['姓名', '用户名', '联系方式', '密码']




    excel_list = []
    for one_row in range(1, total_rows):  # 也就是从Excel第二行开始，第一行表头不算
        row = table.row_values(one_row)
        if row:
            row_object = {}
            for i in range(0, len(columns)):
                key = getkeyvalue(resCom['data'],columns[i])
                if type=='钻展-单品' and key=='time' or type=='钻展-全店' and key=='time':
                    row_object[key] = changeXlrdTimeToDate(row[i])  # 转换时间
                else:
                    row_object[key] = row[i]

            if type=='钻展-单品' or type=='钻展-全店':
                row_object["Conversion_time"] = getchangetime(MinDate, changeXlrdTimeToDate(row[3]))
                typeobj=gettypeName(row[1],row[0],row[2])
                if typeobj==None:
                    return '产品名称不在【胶原,酵素,益生菌,玛咖,牡蛎】内'
                for key, values in typeobj.items():
                  row_object["Product_name"] =key
                  row_object["Shop_name"] =values
            elif type=='超级推荐':
                typeobj = gettypeName(row[2],row[4])
                if typeobj == None:
                    return '产品名称不在【胶原,酵素,益生菌,玛咖,牡蛎】内'
                for key, values in typeobj.items():
                    row_object["Product_name"] = key
                    row_object["Shop_name"] = values
                row_object["Conversion_time"] = getchangetime(MinDate, row[0])
            else:
                row_object["Conversion_time"] = getchangetime(MinDate, row[0])



            excel_list.append(row_object)

    outlist=[]
    outlist = changeList(excel_list, type)
    if type=='超级推荐':
        try:
            models.SuperRecommendation.objects.bulk_create(outlist)
        except Exception as err:
            print(err)
    elif type=='钻展-单品':
        try:
          models.DrillingExhibitionSingleProducts.objects.bulk_create(outlist)
        except Exception as err:
            print(err)
    elif type=='钻展-全店':
        try:
          models.DrillingExhibitionWholeStore.objects.bulk_create(outlist)
        except Exception as err:
            print(err)

    return 'ok'
def gettypeName(creativeName1,creativeName2={},creativeName3={}):
    typelist={'胶原':'姿美堂旗舰店','酵素':'姿美堂旗舰店','益生菌':'姿美堂旗舰店','玛咖':'京姿美堂旗舰店','牡蛎':'京姿美堂旗舰店',}
    for key,values in typelist.items():
        if key in creativeName1:
            obj={key:values}
            return obj
    for key,values in typelist.items():
        if key in creativeName2:
            obj={key:values}
            return obj
    for key,values in typelist.items():
        if key in creativeName3:
            obj={key:values}
            return obj

    return {'待定':'待定'}
def compareHead(srource,type):
    obj=models.DownloadMysql.objects.filter(download_table=type)

    if not obj.exists():
       msg = {'status': "在download_table未发现内容"}
       return msg

    if type=='直通车':
        if not obj.__len__() == len(srource)+3:
           msg = {'status': "上传表的字段和表定义字段数量不合"}
           return msg
    elif type=='超级推荐':
        if not obj.__len__() == len(srource)+5:
           msg = {'status': "上传表的字段和表定义字段数量不合"}
           return msg
    else:
        if not obj.__len__() == len(srource) + 5:
           msg = {'status': "上传表的字段和表定义字段数量不合"}
           return msg

    for line in obj:
        if not line.download_column in srource:
            if not line.download_column in ['主键ID','导入时间','转化时间','产品名称','店铺名称']:
               msg = {'status': "【"+line.download_column+"】"+'该字段未在表中定义'}
               return msg
    data=list(obj.values())
    msg={'status':'ok','data':data}
    return msg
def getkeyvalue(keylist,oldkey):
    for node in keylist:
        if node['download_column'] == oldkey:
            return node['mysql_column']
    return 'null'
def changeXlrdTimeToDate(xlrdTime):
    newdate = xldate_as_tuple(xlrdTime, 0)
    month = '0'
    day = '0'
    if newdate[1] < 10:
       month='0'+str(newdate[1])
    else:
       month=str(newdate[1])

    if newdate[2]<10:
        day='0'+str(newdate[2])
    else:
        day=str(newdate[2])
    return str(str(newdate[0])+"-" +month+"-"+day)
def getMinTime(listdic,type):

    if type=='钻展-单品':
        newlist = sorted(listdic, key=lambda e: e.__getitem__('时间'), reverse=False)
        newdate=changeXlrdTimeToDate(newlist[0]['时间'])
        return newdate
    elif type=='钻展-全店':
        newlist = sorted(listdic, key=lambda e: e.__getitem__('时间'), reverse=False)
        newdate = changeXlrdTimeToDate(newlist[0]['时间'])
        return newdate
    elif type=='直通车':
        newlist = sorted(listdic, key=lambda e: e.__getitem__('\ufeff日期'), reverse=False)
        newdate = newlist[0]['\ufeff日期']
        return newdate
    else:
      newlist=sorted(listdic, key=lambda e:e.__getitem__('日期'), reverse=False)
      return newlist[0]['日期']
def getchangetime(mindate,notedata):
    date1=time.strptime(mindate, "%Y-%m-%d")
    date2=time.strptime(notedata, "%Y-%m-%d")

    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])

    print((date2-date1).days)
    return str(7-(date2-date1).days) ##最少是1
def filter_excel_sort(workbook, column_name=0, by_name='Sheet0'):

    table = workbook.sheets()[0]  # 获得表格
    total_rows = table.nrows  # 拿到总共行数
    columns = table.row_values(column_name)  # 某一行数据 ['姓名', '用户名', '联系方式', '密码']
    table_header = table.row_values(0)
    excel_list = []
    for one_row in range(1, total_rows):  # 也就是从Excel第二行开始，第一行表头不算

        row = table.row_values(one_row)
        if row:
            row_object = {}
            for i in range(0, len(columns)):
                key = columns[i]
                row_object[key] = row[i]  # 表头与数据对应

            excel_list.append(row_object)

    return excel_list
def IdentifyFileExist(fileName):
    (filepath, tempfilename) = os.path.split(fileName);
    (shotname, extension) = os.path.splitext(tempfilename);
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print("Call Windows tasks")
        newfilepath = filepath + "\\" + "excelFile" + "\\" + shotname + extension
    elif (sysstr == "Linux"):
        print("Call Linux tasks")
        newfilepath = filepath + "//"+"excelFile"+"//"+shotname+extension
    print("检查文件："+newfilepath)
    if os.path.exists(newfilepath):
        return True
    else:
        return False
def changeList(excel_list,type):
    newlist=[]
    if type=='超级推荐':
        for val in excel_list:
            newobj=models.SuperRecommendation(date= val['date'],\
plan= val['plan'],\
unit= val['unit'],\
originality= val['Originality'], \
originality_id=val['Originality_ID'], \
number_of_collection_stores=val['Number_of_Collection_Stores'], \
effective_display= val['Effective_display'],\
number_of_valid_clicks= val['Number_of_valid_clicks'],\
thousands_of_exhibition_costs= val['Thousands_of_exhibition_costs'],\
consume= val['consume'],\
click_the_unit_price= val['Click_the_unit_price'],\
click_through_rate= val['Click_through_rate'],\
lead_in_the_store= val['Lead_in_the_store'],\
lead_in_rate= val['Lead_in_rate'],\
number_of_guided_shopkeepers= val['Number_of_guided_shopkeepers'],\
number_of_sneakers_guided_into_stores= val['Number_of_sneakers_guided_into_stores'],\
directing_divers_into_stores= val['Directing_divers_into_stores'],\
deep_store_entry= val['Deep_Store_Entry'],\
average_access_time= val['Average_access_time'],\
average_number_of_pages_accessed= val['Average_number_of_pages_accessed'],\
pay_attention_to_store_volume= val['Pay_attention_to_store_volume'],\
new_passenger_acquisition= val['New_passenger_acquisition'],\
new_customer_acquisition_rate= val['New_customer_acquisition_rate'],\
pull_new_cost= val['Pull_new_cost'],\
pull_new_consumption= val['Pull_new_consumption'],\
collection_of_baby_numbers= val['Collection_of_Baby_Numbers'],\
add_the_number_of_shopping_carts= val['Add_the_number_of_shopping_carts'],\
take_orders= val['Take_orders'],\
take_the_order_amount= val['Take_the_order_amount'],\
transaction_order_quantity= val['Transaction_Order_Quantity'],\
transaction_order_amount= val['Transaction_order_amount'],\
display_conversion_rate= val['Display_conversion_rate'],\
click_conversion_rate= val['Click_Conversion_Rate'],\
return_on_investment= val['Return_on_investment'],\
conversion_time= val['Conversion_time'],\
product_name = val['Product_name'], \
shop_name = val['Shop_name'])
            newlist.append(newobj)
        return newlist
    elif type=='直通车':
        for val in excel_list:
            newobj = models.ThroughTrain(date= val['date'],\
name_of_promotion_plan= val['Name_of_Promotion_Plan'],\
baby_name= val['Baby_name'],\
baby_type= val['Baby_type'],\
commodity_id= val['Commodity_ID'],\
search_type= val['Search_type'],\
traffic_source= val['Traffic_source'],\
display_quantity= val['Display_quantity'],\
clicks= val['Clicks'],\
cost_points= val['Cost_points'],\
click_through_rate= val['Click_through_rate'],\
average_click_cost_points= val['Average_Click_Cost_Points'],\
thousands_of_showcases_points= val['Thousands_of_showcases_points'],\
click_conversion_rate= val['Click_Conversion_Rate'],\
direct_transaction_amount_points= val['Direct_Transaction_Amount_Points'],\
number_of_direct_transactions= val['Number_of_direct_transactions'],\
indirect_transaction_amount_points= val['Indirect_transaction_amount_points'],\
number_of_indirect_transactions= val['Number_of_indirect_transactions'],\
total_transaction_amount_points= val['Total_transaction_amount_points'],\
number_of_total_transactions= val['Number_of_total_transactions'],\
number_of_baby_collections= val['Number_of_Baby_Collections'],\
store_collection_number= val['Store_Collection_Number'],\
total_collection= val['Total_collection'],\
input_output_ratio= val['Input_output_ratio'],\
number_of_direct_shopping_carts= val['Number_of_direct_shopping_carts'],\
number_of_indirect_shopping_carts= val['Number_of_indirect_shopping_carts'],\
total_number_of_shopping_carts= val['Total_number_of_shopping_carts'],\
conversion_time= val['Conversion_time'])
            # for val in excel_list:
            #  for key in val.keys():
            #      print(str(key).lower()+"= val['"+key+"'],\\")
            #  break
            newlist.append(newobj)
        return newlist
    elif type=='钻展-单品':
        for val in excel_list:
            newobj=models.DrillingExhibitionSingleProducts(basic_planning_information= val['Basic_Planning_Information'],\
creative_name= val['Creative_name'],\
basic_information_of_extension_unit= val['Basic_Information_of_Extension_Unit'],\
time= val['time'],\
to_show= val['To_show'],\
click= val['click'],\
consume= val['consume'],\
click_rate= val['Click_rate'],\
click_on_unit_price_yuan= val['Click_on_unit_price_yuan'],\
thousands_of_exhibition_costs_yuan= val['Thousands_of_exhibition_costs_yuan'],\
visitor= val['Visitor'],\
deep_store_entry= val['Deep_Store_Entry'],\
length_of_visit= val['Length_of_visit'],\
number_of_pages_accessed= val['Number_of_pages_accessed'],\
collection_of_baby_quantity= val['Collection_of_Baby_Quantity'],\
collection_store_quantity= val['Collection_Store_Quantity'],\
add_shopping_cart_volume= val['Add_shopping_cart_volume'],\
take_orders= val['Take_orders'],\
take_the_order_amount= val['Take_the_order_amount'],\
transaction_order_quantity= val['Transaction_Order_Quantity'],\
transaction_order_amount= val['Transaction_order_amount'],\
click_conversion= val['Click_conversion'],\
return_on_investment= val['Return_on_investment'],\
conversion_time= val['Conversion_time'], \
product_name=val['Product_name'],\
shop_name=val['Shop_name'])
        # for val in excel_list:
        #  for key in val.keys():
        #      print(str(key).lower()+"= val['"+key+"'],\\")
        #  break
            newlist.append(newobj)
        return newlist
    elif type=='钻展-全店':
        for val in excel_list:
            newobj=models.DrillingExhibitionWholeStore(basic_planning_information= val['Basic_Planning_Information'],\
creative_name= val['Creative_name'],\
basic_information_of_extension_unit= val['Basic_Information_of_Extension_Unit'],\
time= val['time'],\
to_show= val['To_show'],\
click= val['click'],\
consume= val['consume'],\
click_rate= val['Click_rate'],\
click_on_unit_price_yuan= val['Click_on_unit_price_yuan'],\
thousands_of_exhibition_costs_yuan= val['Thousands_of_exhibition_costs_yuan'],\
visitor= val['Visitor'],\
deep_store_entry= val['Deep_Store_Entry'],\
length_of_visit= val['Length_of_visit'],\
number_of_pages_accessed= val['Number_of_pages_accessed'],\
collection_of_baby_quantity= val['Collection_of_Baby_Quantity'],\
collection_store_quantity= val['Collection_Store_Quantity'],\
add_shopping_cart_volume= val['Add_shopping_cart_volume'],\
take_orders= val['Take_orders'],\
take_the_order_amount= val['Take_the_order_amount'],\
transaction_order_quantity= val['Transaction_Order_Quantity'],\
transaction_order_amount= val['Transaction_order_amount'],\
click_conversion= val['Click_conversion'],\
return_on_investment= val['Return_on_investment'],\
action_volume= val['Action_volume'],\
action_cost= val['Action_cost'],\
conversion_time= val['Conversion_time'],\
product_name = val['Product_name'], \
shop_name = val['Shop_name'])
        # for val in excel_list:
        #  for key in val.keys():
        #      print(str(key).lower()+"= val['"+key+"'],\\")
        #  break
            newlist.append(newobj)
        return newlist
