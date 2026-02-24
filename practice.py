import datetime
import os
import datetime
import time

def search_shifts():
    search_term = input( "Enter a date or keyword to search (e.g. 'Feb 20' ): ")
    found = False
    try:
        with open("payroll_history.txt", "r") as file:
            print(f"\n--- Searching for: '{search_term}' --- ")
            for line in file:
                if search_term.lower() in line.lower():
                    print(line.strip())
                    found = True

            if not found:
                print( "No matching shifts found in your history ")
    except FileNotFoundError:
        print( "Error: No history file exists to search. ")
    input("\nSearch complete. Press ENTER to continue to daily entry...")

def show_recent_history():
    print("\n --- RECENT SHIFT HISTORY---")
    try:
        with open( "payroll_history.txt", "r") as file:
            all_lines = file.readlines()
            recent = all_lines[-25:]
            amounts = []
            for line in recent:
                    if "Total Earned: $" in line:
                        number_str = line.split("$") [1].strip()
                        amounts.append(float(number_str))
            if len(amounts) > 0:
                total_recent = sum(amounts)
                print(f"Total for these shifts: ${total_recent:.2f}")
            else:
                print( "No shift data found in the last 15 lines.")
                print("--------------------------")
        for line in recent:
                        print(line.strip())
    except FileNotFoundError:
        print( "No history file found yet. ")

def get_shift_count():
    try:
        with open( "payroll_history.txt", "r") as file:
            content = file.read()
            return content.count("Date") + 1
    except FileNotFoundError:
        return 1   
#-------Security Gate----------------
SECRET_PASSCODE = "Mexico2026"
worker_name = "Emmanuel"
#CREATE A BOX CALLED USER_ATTEMPT,ask the user for a string of text, and put that text in the box
user_attempt = input("What is the passcode? ")
if user_attempt.lower() == SECRET_PASSCODE.lower():
    print( "ACCESS GRANTED. Welcome, " + worker_name )
    show_recent_history()
else:
    print( "SECURITY BREACH. ACCESS DENIED. ") 
    exit()

show_recent_history()
search_shifts()

total_mexico_savings = 0

def calculate_shift_stats(hours_float, rate_float):
    total_pay = hours_float * rate_float
    mexico_cut = total_pay * 0.10
    return total_pay, mexico_cut

time.sleep(0.2)
os.system(r'clear && printf "\e[3J"' )
#----step 2: SECURITY GATE ---------


lifetime_balance = 0.0
with open( "payroll_history.txt" , mode="r") as file:
    for line in file:
        if "$" in line:
            parts = line.split("$")
            lifetime_balance = lifetime_balance + float(parts[1])
print(f"LIFETIME CAREER EARNINGS: $ {round(lifetime_balance,2)}")
start_time = datetime.datetime.now()
hours_today = input("How many hours have you worked today? ")
hours_float = float(hours_today)
rate_today = input( "What is your hourly pay rate for this shift? ")
rate_float = float(rate_today)
todays_pay, mexico_fund = calculate_shift_stats(hours_float, rate_float)
total_mexico_savings += mexico_fund
shift_num = get_shift_count()
grand_total = lifetime_balance + todays_pay
print(f"Added to Vault today: ${mexico_fund:,.2f}")
print(f"Total VAULT savings: $ {total_mexico_savings:,.2f}")
#-----STEP 3; MEXICO TRACKER------
mexico_goal = 50000
percent_complete = (total_mexico_savings / mexico_goal) * 100
print(f"\n--- \033[92mMEXICO TRIP TRACKER\033[0m ---")
print(f"Goal: ${mexico_goal} ")
print(f"Current Fund in Vault: $ {total_mexico_savings:,.2f}")
print(f"Progress: {round(percent_complete, 1)}% of the way to the beach! ")
if mexico_fund >= 20.0:
    print(" Great Shift! Tell Macey we're one step closer to the beach! ")
#----------STEP 4:CURRENT TIME + HOURS LEFT = FINISH LINE

#---------TIME CALCULATIONS---------
hours_left = 10 - hours_float
minutes_left = round(hours_left * 60)
#--------The Finish Line----------
print(f"Only {minutes_left} minutes until the 10-hour mark ")
if minutes_left < 120:
    print("--- YOU ARE IN THE FINAL STRETCH!---")
    if minutes_left < 60:
        print( "---- LESS THAN AN HOUR TO GLORY!------")
end_time = start_time + datetime.timedelta(hours=hours_left)
print(f"\n SHIFT END TIME: {end_time.strftime( ' %I:%M %P ')}")
with open( "payroll_history.txt","a") as file:
    file.write(f"\n{'-' * 30}")
    file.write(f"\nDate: {datetime.date.today().strftime('%B %d, %Y')}")
    file.write(f"\nTotal Earned: $ {todays_pay}") 
    file.write( "\n" + "-" * 30 + "\n")
    goal = 10
    remaining = goal - hours_float
    print(f"\n---GOAL TRACKER---")
    print(f"You've crushed {hours_float} hours so far.")
    print(f"Only {round(remaining, 1)} hours left to hit your 10-hour shift goal. Keep grinding! ")
print(f"\n SHIFT #{shift_num} DATA BACKED UP AT: {datetime.datetime.now().strftime( '%I:%M:%S %p ' )}")
print("--------------------------------------------------------------------------------")




"""
Project: Payroll Reporter | Author: Emmanuel | Status: Day 2 Complete
"""



def greet_person(name):
    pass
   # print("Hello " + name + ", let's get back to work!")

#greet_person("Emmanuel")
#greet_person("Macey")

def calculate_bonus(hours):
    bonus = hours * 5
    
    #print(f"for working {hours} hours, your bonus is, $ {bonus}")
calculate_bonus(3)
calculate_bonus(10)

def smart_bonus(hours):
    if hours > 8:
        bonus = hours * 10 # Double bonus for overtime!
    else:
        bonus = hours * 5
    #print("Your smart bonus is: $" + str(bonus))

smart_bonus(5)
smart_bonus(10)






#This function calculates my gross pay at $25 an hour
my_rate = 25
def calculate_pay(tiempo):
    total = tiempo * my_rate
    return total 

all_shifts = []
total_hours_today = []
today_date = datetime.date.today() .strftime( "%B %d, %Y ")
starting_balance = 0.0
try:
    with open( "payroll_history.txt" , "r" ) as file:
        #print("Searching for payroll records...")
        time.sleep(2)
        for line in file:
            if "Total Earned: $" in line:
                parts = line.split("$")
                amount = float(parts[1])
                starting_balance += amount            
    #print(" Previous earnings loaded: $" + str(starting_balance))
    #if starting_balance > 1000:
        #print( "WOW! You've earned over $1,000! Keep crushing it, " + worker_name)
   # elif starting_balance > 500:
        #print( "Nice work! You're over the $500 mark.")
  #  else:
       # print( "Keep going, every dollar counts! ")
except: 
        print( "No history found. starting from 0.00 ")

#this tells the machine i worked 6.5 hours
bonus = 50

while True:
    print("hello")
    user_input = input( "Enter your total hours: ")
    if user_input == "quit": break
    try:
        hours = float(user_input)
        total_hours_today.append(hours)
        total = calculate_pay(hours)
        tax = total * 0.10
        take_home = total - tax
        all_shifts.append(take_home)
        print( "Take Home After Taxes: $" + str(take_home))
        print( "Money earned: $" + str(total))
        hours_done = sum(total_hours_today)
        hours_left = 10 - hours_done
        print( "Shift Progress: " + str(hours_done) + " / 10 hours completed.")
        print( "You have " + str(hours_left) + " hours to go until your 10-hour goal! ")
        
        #with open( "daily_progress.txt" , "a") as file:
#            timestamp = datetime.datetime.now() .strftime( "%b-%d %I:%M:%p ")
 #           file.write(f"Date: {timestamp} | Hours: {hours}\n")
  #      print( "\n" + "=" *30, flush=True)
   #     print( "----SUCCESS: PROGRESS SAVED!----" , flush=True)
    #    print( "=" * 30 + "\n" , flush=True)
     #   input( "<<<<<SUCCESS: PRESS ENTER TO CONTINUE>>>>>>", flush=True)
    except ValueError:
     print("Error: Please enter a number, not words.")
print("----------------------")

# lifetime_total = sum(all_shifts) + starting_balance
# print( "Grand Total For All Shifts: $" + str(lifetime_total))
# if len(all_shifts) > 0:
#     average = sum(all_shifts) / len(all_shifts)
#     print( "Average Earned Per Shift Today:$" + str(round(average, 2)))
# with open("payroll_history.txt", "a") as file:
#     file.write( "\n--- NEW SESSION ---")
#     file.write( "\nWorker: " + worker_name)
#     file.write( "\nDate: " + today_date)
#     file.write( f"\nShift Progress: {hours_float} / 10 hours completed. ")
#     for shift in all_shifts:
#         file.write( "\nShift Entry: " + str(shift) + " hours")
#         file.write( "\nSession Total: $" + str(sum(all_shifts)))
#         file.write( "\nLIFETIME TOTAL: $" + str(lifetime_total))
#         file.write( "\nReport Generated For " + worker_name + ". Great work today!")
