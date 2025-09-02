def pretty_print_int(number):
    return str(f"{number:,}")

# print(pretty_print_int(1000))
# print(pretty_print_int(5))
# print(pretty_print_int(547475874))
# print(pretty_print_int(-84989))
# print(pretty_print_int(999))

def pretty_print_dollars(number):
    if number < 0:
        return str(f"-${abs(number):,.2f}")
    else:
        return str(f"${abs(number):,.2f}")

# print(pretty_print_dollars(1000.0))
# print(pretty_print_dollars(5.99))
# print(pretty_print_dollars(547475874))
# print(pretty_print_dollars(-84989))
# print(pretty_print_dollars(999.50))

def make_field(content, length):
    output = str(content)
    output_length = len(output)
    if not output_length <= length-2:
        correction = (output_length-length)+2
        output = output[:-correction]
    output = output.rjust(length-1)
    output = '|' + output + ' |'
    return output

# print(make_field(1000, 7))
# print(make_field("year", 8))
# print(make_field("world", 5))

def make_line(length):
    return "+" + "".center(length,'-') + "+"

# print(make_line(6))
# print(make_line(8))

import math

def simulate_infection(population, initial_infected, r_number):
    infected = initial_infected
    day = 1
    while population > 0:
        print(f"{day} {population}")
        day +=1
        population -= infected
        infected = math.ceil(infected*r_number)
        
    print(f"{day} 0")

# simulate_infection(1000000, 1000, 1.1)

def compound_interest(init_principal, acc_rate, acc_cmp_freq, years):
    if acc_cmp_freq == 0:
        acc_total = init_principal*math.e**(acc_rate*years)
    else:
        acc_total = init_principal*(1+acc_rate/acc_cmp_freq)**(acc_cmp_freq*years)
    return acc_total

# print(compound_interest(10000.00, 0.025, 12, 4))
# print(compound_interest(10000.00, 0.025, 0, 4))

def simulate_account_balance(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    init_principal -= setup_fee
    for two_year in range(2,years,2):
        accumulation = round(compound_interest(init_principal, acc_rate, acc_cmp_freq, two_year),2)
        print(f"{two_year} {accumulation}")

# simulate_account_balance(10000.00, 0.025, 12, 25.00, 10)

def simulate_infection_pp(population, initial_infected, r_number):
    border = make_line(5) + make_line(12)           #start building table
    print(border)
    daily_report = make_field("Day", 5) + make_field("Population", 12)
    print(daily_report)
    print(border)

    infected = initial_infected                     #start calculating population
    day = 1
    while population > 0:
        daily_report = make_field(pretty_print_int(day), 5) + make_field(pretty_print_int(population), 12)
        print(daily_report)
        day +=1
        population -= infected
        infected = math.ceil(infected*r_number)
        
    daily_report = make_field(pretty_print_int(day), 5) + make_field(pretty_print_int(0), 12)
    print(daily_report)
    print(border)

# simulate_infection_pp(1000000, 1000, 1.1)

def simulate_account_balance_pp(init_principal, acc_rate, acc_cmp_freq, setup_fee, years):
    width = len(pretty_print_dollars(round(compound_interest(init_principal, acc_rate, acc_cmp_freq, years//2),2)))+2
    border = make_line(6) + make_line(width)           
    report = make_field("Year", 6) + make_field("Balance", width)
    print(border)
    print(report)
    print(border)
    
    init_principal -= setup_fee
    for two_year in range(2,years+1,2):
        accumulation = round(compound_interest(init_principal, acc_rate, acc_cmp_freq, two_year),2)
        report = make_field(pretty_print_int(two_year), 6) + make_field(pretty_print_dollars(accumulation), width)
        print(report)
    print(border)

#simulate_account_balance_pp(10000.00, 0.025, 12, 25.00, 10)