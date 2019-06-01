import os

#os.system("pip install pandas")
import pandas as pd
import time
import datetime, calendar
"""
List of Global veriables
"""
rfm_table = []
most_list = []
today = datetime.datetime.today()
sample_set = 10
product_list = []
product_count = []
product_name = []
"""
Utility Function
"""
def assign_value_in_scale(num):
    if num > 10:
        return 10;
    elif num < 1:
        return 1
    else:
        return num


"""
Recency = the maximum of "10 – the number of months that have passed since the customer last purchased" and 1
Frequency = the maximum of "the number of purchases by the customer in the last 12 months (with a limit of 10)" and 1
Monetary = the highest value of all purchases by the customer expressed as a multiple of some benchmark value
"""
def make_rfm_table_utils(data, custid, index, size, max_money):
    count =0
    l_count = 0
    order_id =[]
    while index +count < size - 1:
        if custid ==data[index+count][1]:
            date_this = data[index+count][2].split()[0] 
            trans_date = datetime.datetime.strptime(date_this, "%Y-%m-%d")
            if (today - trans_date).days > 366:
                l_count += 1
            count +=1
            order_id.append(data[index+count][3])
        else:
            break
    this_cust_data = data[index:index+count]
    if this_cust_data != []:
        maxR = max(this_cust_data)[0]
        maxM= max(this_cust_data)[2]
        idate = maxM.split()
        date_leatest = datetime.datetime.strptime(idate[0], "%Y-%m-%d")
        Recency = assign_value_in_scale(((today - date_leatest).days)/30)
        Frequency = assign_value_in_scale(l_count)
        Monetary = (maxR/max_money)*10
        score = Recency+ Frequency+Monetary
        this_cust = (custid, Recency, Frequency, Monetary, score, order_id)
        rfm_table.append(this_cust)
        return index+count
    return index+count

def make_rfm_table(data):
    i = 0
    data.sort(key = lambda x: x[1])
    max_money = int(max(data)[0])
    if max_money < 1:
        max_money = 1
    i = make_rfm_table_utils(data,data[i][1],0,len(data), max_money)
    while i < len(data) -1:
        i = make_rfm_table_utils(data,data[i][1],i,len(data),max_money)
    
"""
Customer Segment	                          Activity	
Champions	              Bought recently, buy often and spend the most!	
Loyal Customers	              Spend good money with us often. Responsive to promotions.	
Recent Customers	      Bought most recently, but not often
Promising	              Recent shoppers, but haven’t spent much.	
Customers Needing Attention   Above average recency, frequency and monetary values. May not have bought very recently though..	
Lost	                      Lowest recency, frequency and monetary scores.
"""
def find_champion():
    rfm_table.sort(key = lambda x: x[2]) 
    data = rfm_table[0:sample_set]
    data = max(data)[3]
    print("Champion customer is with id ")
    print(data)

def find_loyal():
    rfm_table.sort(key = lambda x: x[2])
    data = rfm_table[0:sample_set]
    data.sort(key = lambda x: x[3])
    print_list(data, "List of Loyal customer id are as follow ")
    
def find_recent():
    rfm_table.sort(key = lambda x: x[1])
    data = rfm_table[0:sample_set]
    data.sort(key = lambda x: x[2])
    print_list(data, "List of recent customer id are as follow ")

def find_promising():
    rfm_table.sort(key = lambda x: x[1])
    data = rfm_table[0:sample_set]
    data.sort(key = lambda x: x[3], reverse= 1)
    print_list(data, "List of recent customer id are as follow ")

def find_need_attention():
    rfm_table.sort(key = lambda x: x[4])
    data = rfm_table[0:sample_set]
    data.sort(key = lambda x: x[3], reverse= 1)
    print_list(data, "List of recent customer id are as follow ")

def find_lost():
    rfm_table.sort(key = lambda x: x[4] ,reverse= 1)
    data = rfm_table[0:sample_set]
    data.sort(key = lambda x: x[0])
    print_list(data, "List of recent customer id are as follow ")
"""
Print the data passed here as array
"""
def print_list(data, term):
    print("*******************************"+term+"*******************************")
    for item in data:
        print(item[0])
"""
Ask fo options for customer menu
"""

def options_cust():
    user_input = input ("Enter  your Option")
    try:
       val = int(user_input)
       if val ==1:
           find_champion()
       elif val ==2:
           find_loyal()
       elif val ==3:
           find_recent()
       elif val == 4:
           find_promising()
       elif val == 5:
           find_need_attention()
       elif val == 6:
           find_lost()
       elif val == 7:
           product()
    except ValueError:
       return -1
"""
Customer menu on RFM creteria and its driver function
"""
def init_msg_cust():
    print("**************************Customer menu***************************************")
    print("Enter Option for processing")
    print("1). Champions")
    print("2).Loyal Customers")
    print("3).Recent Customers")	     
    print("4). Promising")	             	
    print("5). Customers Needing Attention")   	
    print("6).Lost")
    print("7). Go to product menu")
    print("Press any other key to exit")

def customer():
    init_msg_cust()
    options_cust()

"""
Product List utilities
"""
def make_product_table_utils(data, custid, index, size):
    count =0
    while index +count < size - 1:
        if custid ==data[index+count][0]:
            count +=1
        else:
            break
    temp = [custid, count]
    product_count.append(temp)
    return index+count


def find_recent_purchese():
    product_desc.sort(key = lambda x: x[1])
    print_list(product_desc[0:sample_set], "List of recent Product id are as follow ")

def find_most_purchese():
    product_count.sort(key = lambda x: x[1])
    print_list(product_count[0:sample_set], "List of recent Product id are as follow ")
    
def make_product_table(data):
    i = 0
    data.sort(key = lambda x: x[0])
    i = make_product_table_utils(data,data[i][0],0,len(data))
    while i < len(data) -1:
        i = make_product_table_utils(data,data[i][0],i,len(data))


"""
Product menu and its driver function
"""
def init_msg_prod():
    print("**************************Product menu***************************************")
    print("Enter Option for processing")
    print("1). Most Purched")
    print("2).Recently purchesed")
    print("Press any other key to exit")
    
def product():
    init_msg_prod()
    options_prod()

def options_prod():
    user_input = input ("Enter  your Option")
    try:
       val = int(user_input)
       if val ==1:
           find_most_purchese()
       elif val ==2:
           find_recent_purchese()
       elif val == 3:
           customer()
    except ValueError:
       return -1
    

"""
Driver Function or main function
"""
if __name__ == "__main__":
    data = pd.read_csv("customer_order_history.csv")
    i = 0
    product_csv = pd.read_csv("product_order_data.csv")
    product_name = pd.read_csv("product.csv")
    while i< data.amount.size:
        temp = (data.amount[i],data.customerId[i],data.orderDate[i],data.orderId[i])
        i = i+1
        most_list.append(temp)
    make_rfm_table(most_list)
    j =0
    product_desc = []
    while j<product_csv.product_id.size:
        local_data = [product_csv.product_id[j],product_csv.event_date[j], product_csv.event_id[j]]
        product_desc.append(local_data)
        j += 1
    product_list = product_desc
    make_product_table(product_desc)
    print("**********************Start Menu********************")
    print("Select the menu")
    print("1). Customer Menu")
    print("2). Product Menu")
    user_input = input ("Enter  your Option")
    value = 0
    while 1:   
        try:
            val = int(user_input)
            if val ==1:
                customer()
            else:
                product()
            if value == -1:
                break
        except ValueError:
            print("Correct your input")
            break
