def main():
    num_days=int(input("Enter number of days: "))
    hours=num_days * 24
    minutes=hours * 60
    seconds=minutes * 60

    print(f"Hours - {hours}, Minutes - {minutes}, Seconds - {seconds}")

if __name__ == "__main__":
    main()