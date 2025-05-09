def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_input = str(input("Date: ")).strip().capitalize()

        try:
            if "/" in date_input:
                split_date = date_input.split("/")

            if "," in date_input:
                split_date = date_input.split(" ")

            year = split_date[2]
            month = split_date[0]
            date = split_date[1]

            if month in months:
                if "/" in date_input:
                    continue
                month_number = months.index(month) + 1
                month = str(month_number)



            if "," in date:
                date_no_comma = date.replace(",", "")
            else:
                date_no_comma = date

            if len(date_no_comma) == 1:
                date_no_comma = f"0{date_no_comma}"
            if len(month) == 1:
                month = f"0{month}"

            if int(date_no_comma) > 31 or int(month) > 12:
                continue

            date_output = f"{year}-{month}-{date_no_comma}"
            print(date_output)
            break


        except:
            continue
main()

