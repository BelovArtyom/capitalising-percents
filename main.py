""" Case-study #3, Cycles
Developers:
Belov A. (50%)
Vlasov V. (55%)

"""

# Asking user for his preferred localisation

# None is a None type, which is why it's something the user can't type for us and break the loop.
preferred_localisation = None
while preferred_localisation == None:
	preferred_localisation = input("Choose your localisation E for English, R - Русский, J - 日本語")
	if preferred_localisation == 'E':
		import localisation_en as l
	elif preferred_localisation == 'R':
		import localisation_ru as l
	elif preferred_localisation == 'J':
		import localisation_jp as l
	# Else catches all other inputs, resetting while cycle
	else: preferred_localisation = None


# Taking initial inputs from user
years = None
while years == None:
	years = input(l.years)
	try:
		int(years)
		if years <= 0: years = None
	except: print(l.incorrectinput)


initial_capital = None
while initial_capital == None:
	years = input(l.initial_capital)
	try:
		float(initial_capital)
		if initial_capital <= 0: initial_capital = None
	except: print(l.incorrectinput)
	

percent = None
while percent == None:
	years = input(l.percent)
	try:
		float(percent)
		if percent <= 0: percent = None
	except: print(l.incorrectinput)

investment_infusion = None
while investment_infusion == None:
	years = input(l.investment_infusion)
	try:
		float(investment_infusion)
		# Investment infusion can be 0.
		if investment_infusion < 0: investment_infusion = None
	except: print(l.incorrectinput)

# Enter loop of calculating percents (Vlas)
# variables: years, initial_capital, percent, investment_infusion
# Outputs states for 1 year in and every 10th year and last year?
# Honestly, who knows what the program is supposed to be. (Vlas)

# CODE FROM EXAMPLE OF THE CASE STUDY, PLEASE USE AS REFERENCE
for year in range (1, years + 1):
    print(year,"год")
    print ("-------------------------------------------")
    print ("|       |   основа   | сумма %  |         |")
    print ("| месяц | инвестиций | за месяц | капитал |")
    print ("-------------------------------------------")



