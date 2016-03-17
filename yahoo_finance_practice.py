from yahoo_finance import Share

rubi = Share('MSFT')

history = rubi.get_historical('2015-01-01' , '2015-12-31')

if rubi.get_dividend_share() == None:
	print "no dividend"
else:
	print rubi.get_dividend_share()