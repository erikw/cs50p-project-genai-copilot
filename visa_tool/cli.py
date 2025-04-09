def main():
    import argparse
    from visa_tool.country_info import CountryInfo
    from visa_tool.exit_day_calculator import calculate_exit_day
    from datetime import datetime

    parser = argparse.ArgumentParser(description="Visa Tool: Get visa information and calculate exit days.")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for visa information
    visa_parser = subparsers.add_parser('visa', help='Get visa information for a country')
    visa_parser.add_argument('country', type=str, help='Name of the country to get visa information for')

    # Subparser for exit day calculation
    exit_parser = subparsers.add_parser('exit', help='Calculate last exit day from a country')
    exit_parser.add_argument('entry_date', type=str, help='Date of entry (YYYY-MM-DD)')
    exit_parser.add_argument('valid_days', type=int, help='Number of days the entry is valid for')

    # Interactive mode
    interactive_parser = subparsers.add_parser('interactive', help='Run in interactive mode')

    args = parser.parse_args()

    if args.command == 'visa':
        country_info = CountryInfo()
        info = country_info.get_visa_info(args.country)
        print(info)

    elif args.command == 'exit':
        entry_date = datetime.strptime(args.entry_date, '%Y-%m-%d')
        last_exit_day = calculate_exit_day(entry_date, args.valid_days)
        print(f'Last day to exit: {last_exit_day.strftime("%Y-%m-%d")}')

    elif args.command == 'interactive':
        while True:
            print("\nChoose an option:")
            print("1. Get visa information")
            print("2. Calculate last exit day")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                country = input("Enter the country name: ")
                country_info = CountryInfo()
                info = country_info.get_visa_info(country)
                print(info)

            elif choice == '2':
                entry_date_str = input("Enter date of entry (YYYY-MM-DD): ")
                valid_days = int(input("Enter number of valid days: "))
                entry_date = datetime.strptime(entry_date_str, '%Y-%m-%d')
                last_exit_day = calculate_exit_day(entry_date, valid_days)
                print(f'Last day to exit: {last_exit_day.strftime("%Y-%m-%d")}')

            elif choice == '3':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()