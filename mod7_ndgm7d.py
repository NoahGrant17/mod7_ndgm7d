## Write Unit Tests for 5 Inputs
# 1. symbol: capitalized, 1-7 alpha characters
# 2. chart type: 1 numeric character, 1 or 2
# 3. time series: 1 numeric character, 1 - 4
# 4. start date: date type YYYY-MM-DD
# 5. end date: date type YYYY-MM-DD
import datetime
# 1. symbol function
def get_symbol(inp):
    upp = 0
    for i in inp:
        if (i.isupper()):
            upp+=1  

    if(upp >= 1):
        if(upp <= 7):
            return "1"
        else:
            return "0"
    else:
        return "0"
    
# 2. chart type function
def get_chart_type(inp):
    if(inp == "1"):
        return "1"
    elif(inp == "2"):
        return "2"
    else:
        return "0"

# 3. time series function
def get_time(inp):
    if(inp == "1"):
        return "1"
    elif(inp == "2"):
        return "2"
    elif(inp == "3"):
        return "4"
    elif(inp == "4"):
        return "4"
    else:
        return "0"

# 4. check date function
#YYYY-MM-DD
def check_date(inp):
    if((len(inp)) != 10):
        return "0"
    if (inp[0].isdigit):
        if (inp[1].isdigit):
            if (inp[2].isdigit()):
                if (inp[3].isdigit()):
                    if (inp[4]=='-'):
                        if (inp[5].isdigit()):
                            if (inp[6].isdigit()):
                                if (inp[7]=='-'):
                                    if (inp[8].isdigit()):
                                        if (inp[9].isdigit()):
                                            year, month, day = inp.split('-')

                                            isValidDate = True
                                            try:
                                                datetime.datetime(int(year), int(month), int(day))
                                            except ValueError:
                                                isValidDate = False

                                            if(isValidDate):
                                                return inp
                                            else:
                                                return "0"
                                        else:
                                            return "0"
                                    else:
                                        return "0"
                                else:
                                    return "0"
                            else:
                                return "0"
                        else:
                            return "0"
                    else:
                        return "0"
                else:
                    return "0"
            else:
                return "0"                                    
        else:
            return "0"
    else:
        return "0"
            
# 4. future-past function
def past_future_date(start, end):
    startyear, startmonth, startday = start.split('-')
    endyear, endmonth, endday = end.split('-')
    if(startyear < endyear):
        return "1"
    elif(startyear == endyear):
        if(startmonth < endmonth):
            return "1"
        elif(startmonth == endmonth):
            if(startday < endday):
                return "1"
            else:
                return "0"
        else:
            return "0"
    else:
        return "0"    

# 1. symbol function is called
symbol = get_symbol(input("Enter at least 1 to 7 capitalized alphabetic characters: "))
while(symbol == "0"):
    symbol = get_symbol(input("Please enter at least 1 to 7 capitalized alphabetic characters: "))

# 2. chart type function is called
chart_type = get_chart_type(input("Enter the chart type you want (1, 2): "))
while (chart_type == "0"):
    chart_type = get_chart_type(input("Please enter the chart type you want (1, 2): "))

# 3. time series function is called
time = get_time(input("Enter 1 numeric character 1-4: "))
while (time == "0"):
    time = get_time(input("Please enter 1 numeric character 1-4: "))

logic = "0"
while (logic == "0"):
    # 4. date function is called
    start_date = check_date(input("Enter the start date as YYYY-MM-DD: "))
    while(start_date == "0"):
        start_date = check_date(input("Please enter the start date as YYYY-MM-DD: "))

    # 5. date function is called
    end_date = check_date(input("Enter the end date as YYYY-MM-DD: "))
    while(end_date == "0"):
        end_date = check_date(input("Please enter the end as YYYY-MM-DD: "))
        
    # 6. logic function is called
    logic = past_future_date(start_date,end_date)
    if(logic == "0"):
        print("Dates do not add up!")
    if(logic == "1"):
        print("Dates work!")