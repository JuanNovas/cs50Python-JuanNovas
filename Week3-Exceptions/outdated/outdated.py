
months_names = {

    "January" : "01",
    "February": "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"

}

while True:
    date = input("Date: ").strip()
    #barras
    try:
        slash = date.index("/")
        month = date[:slash]
        date = date[slash+1:]
        slash = date.index("/")
        day = date[:slash]
        year = date[slash+1:]

        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day

        if len(day) != 2 or len(month) != 2 or len(year) != 4:
            int(date)
        else:
            if 0 < int(month) <= 12 and 0 < int(day) <= 31:
                print(f"{year}-{month}-{day}")
                break
    except:
        pass
        #coma
        try:
            date.capitalize()
            coma = date.index(",")
            space = date.index(" ")
            month_str = date[:space]
            day = date[space+1:coma]
            year = date[coma+2:]


            if len(day) == 1:
                day = "0" + day

            if len(day) != 2 or len(months_names[month_str]) != 2 or len(year) != 4:
                int(date)
            else:
                if 0 < int(day) <= 31:
                    print(f"{year}-{months_names[month_str]}-{day}")
                    break
        except:
            pass
