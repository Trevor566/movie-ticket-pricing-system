# Get user input
base_price = 15  # You can keep this fixed or also ask the user

age = int(input("Enter your age: "))
seat_type = input("Enter seat type (Premium/Gold/Regular): ").strip().title()
show_time = input("Enter show time (Morning/Afternoon/Evening): ").strip().title()

is_member_input = input("Are you a member? (yes/no): ").strip().lower()
is_member = True if is_member_input == 'yes' else False

is_weekend_input = input("Is it a weekend? (yes/no): ").strip().lower()
is_weekend = True if is_weekend_input == 'yes' else False


# Check basic eligibility
if age > 17:
    print('User is eligible to book a ticket')

# Check eligibility for evening shows
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')


# Calculate discount
discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')

print('Discount:', discount)


# Calculate extra charges
extra_charges = 0
if is_weekend or show_time == 'Evening':
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')

print('Extra charges:', extra_charges)


# Final booking condition
if (age >= 21) or (age >= 18 and (show_time != 'Evening' or is_member)):
    print('Ticket booking condition satisfied')

    # Determine service charges
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1

    print('Service charges:', service_charges)

    # Final price calculation
    final_price = base_price + extra_charges + service_charges - discount

    print('Final price of ticket:', final_price)

else:
    print('Ticket booking failed due to restrictions')