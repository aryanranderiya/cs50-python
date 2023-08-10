months = {
    "01":"January",
    "02":"February",
    "03":"March",
    "04":"April",
    "05":"May",
    "06":"June",
    "07":"July",
    "08":"August",
    "09":"September",
    "10":"October",
    "11":"November",
    "12":"December"
}

def Main():

    while method() :
        method()

def method() :

    date = input("Date:").capitalize()

    for j in months :
        value = months[j]
        if "/" in date and value in date :
            return True
        if value in date and "," not in date :
            return True

    date = date.replace("/"," ").replace(","," ").split()

    if date[1].isalpha() :
        return True

    month = date[0].strip()
    day = int(date[1].strip())
    year = int(date[2].strip())

    if month.isnumeric() :
        month=int(month.strip())

        if month > 12 :
            return True

    for i in months :
        if month == months[i] :
            month = i

    if day > 31:
        return True

    print(f"{year:04}-{month:02}-{day:02}",end="")
    return False

Main()