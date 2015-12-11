def main():

	print "You work for the currency exhange station and need the"
	print "exchange rate for US citizens for different currenies"
	print "around the world." 

	def curr_selection():
		print "Currency exchange options:"
		print " 'e' convert to Euro"
		print " 'y' convert to Chinese Yaun"
		print " 'r' convert to Indian Rupee"
		print " 'c' convert to Canadian dollar"
		print " 'n' convert to Japanese Yen"
		print " 'u' convert to Russian Ruble"
                print " 'b' convert to Brazilian Real"
                print " 'p' convert to Mexican Peso"
		print " 'q' quit the program"

	def usd_to_euro(e):
		return (e)*.91
	def usd_to_yaun(y):
		return (y)*6.44
	def usd_to_rupee(r):
		return (r)*66.71
	def usd_to_cdollar(c):
		return (c)*1.36
	def usd_to_yen(n):
		return (n)*121.61
        def usd_to_ruble(u):
                return (u)*69.34
        def usd_to_breal(b):
                return (b)*3.81
        def usd_to_peso(p):
                return (p)*17.20

	choice = ""
	while choice != "q":
		if choice == "e":
			Euro = input("USD: $")
			print "You will have %.2f Euros" %usd_to_euro(Euro)
		elif choice == "y":
	       	        Yaun = input("USD: $")
        	  	print "You will have %.2f Chinese Yaun" %usd_to_yaun(Yaun)
		elif choice == "r":
		        Rupee = input("USD: $")
		        print "You will have %.2f Indian Rupee" %usd_to_rupee(Rupee)
	        elif choice == "c":
        	        Cdollar = input("USD: $")
	               	print "You will have %.2f Canadian Dollars" % usd_to_cdollar(Cdollar)
		elif choice == "n":
		        Yen = input("USD: $")
	                print "You will have %.2f Japanese Yen" %usd_to_yen(Yen)
                elif choice == "u":
                        Ruble = input("USD: $")
                        print "You will have %.2f Russian Ruble" %usd_to_ruble(Ruble)
                elif choice == "b":
                        Breal = input("USD: $")
                        print "You will have %.2f Brazilian Real" %usd_to_breal(Breal)
                elif choice == "p":
                        Peso = input("USD: $")
                        print "You will have %.2f Mexican Peso" %usd_to_peso(Peso)

		else:
			curr_selection()	

		print("")
		choice = raw_input("Enter currency exchange: ")

if __name__== "__main__":
	main()
