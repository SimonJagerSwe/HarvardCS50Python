def main():
    time = input("What time is it? ").strip()
    dec_time = convert(time)

    if dec_time >= 7 and dec_time <= 9:
        print("breakfast time")

    elif dec_time >= 12 and dec_time <= 13:
        print("lunch time")

    elif dec_time >= 18 and dec_time <= 19:
        print("dinner time")

    else:
        print()


def convert(time):
    time = time.split(":")
    hrs = int(time[0])
    mins = int(time[1]) / 60
    dec_time = float(hrs + mins)
    return dec_time

if __name__ == "__main__":
    main()
