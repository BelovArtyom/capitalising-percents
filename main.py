""" Case-study #3, Cycles
Developers:
Belov A. (50%)
Vlasov V. (55%)

"""

# Asking user for his preferred localisation

# None is a None type, which is why it's something the user can't type for us and break the loop.
preferred_localisation = None
while preferred_localisation == None:
	preferred_localisation = input("E for English, R - Русский, J - 日本語")
	if preferred_localisation == 'E':
		import localisation_en as l
	elif preferred_localisation == 'R':
		import localisation_ru as l
	elif preferred_localisation == 'J':
		import localisation_jp as l
	# Else catches all other inputs, resetting while cycle
	else:
		print(l.incorrectinput)
		preferred_localisation = None

# Taking initial inputs from user
years = None
while years == None:
	years = input(l.years)
	try:
		int(years)
		if years <= 0:
		print(l.incorrectinput)
		years = None
	except:
		print(l.incorrectinput)
		years = None

initial_capital = None
while initial_capital == None:
	years = input(l.initial_capital)
	try:
		float(initial_capital)
		# Calculating increases of capital means that capital is positive
		if initial_capital <= 0:
		print(l.incorrectinput)
		initial_capital = None
	except:
		print(l.incorrectinput)
		initial_capital = None	

percent = None
while percent == None:
	years = input(l.percent)
	try:
		float(percent)
		# Calculating percent increases means that percent is positive
		if percent <= 0:
		print(l.incorrectinput)
		percent = None
	except:
		print(l.incorrectinput)
		percent = None

investment_infusion = None
while investment_infusion == None:
	years = input(l.investment_infusion)
	try:
		float(investment_infusion)
		# Investment infusion can be 0.
		if investment_infusion < 0:
		print(l.incorrectinput)
		investment_infusion = None
	except:
		print(l.incorrectinput)
		investment_infusion = None

# variables used: years, initial_capital, percent, investment_infusion
# Outputs states for 1 year in and every 10th year and last year (?)
# Honestly, who knows what the program is supposed to be. (Vlas)

# CODE BELOW IS FROM EXAMPLE OUT OF THE CASE STUDY
for year in range (1, years + 1):
    print(year,"год")
    print ("-------------------------------------------")
    print ("|       |   основа   | сумма %  |         |")
    print ("| месяц | инвестиций | за месяц | капитал |")
    print ("-------------------------------------------")
# inputs go:   ^7        ^12        ^10         ^9 characters and
# are optimised for this kind of output length. Read localisation_ru.py


