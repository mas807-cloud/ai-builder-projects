def implied_prob(odds):
    if odds > 0:
        return 100/(odds+100)
    elif odds < 0:
        return abs(odds)/(abs(odds)+100)

exampleodds = [+120, +310, -400, -130, +110]

#for i in exampleodds:
    #if implied_prob(i) > .5:
        #print(i, '- Not Value')
    #elif implied_prob(i) <= .5:
        #print(i, '- Value')


def check_arbitrage(odds1, odds2):
    if implied_prob(odds1) + implied_prob(odds2) < 1:
        return(True, 1-(implied_prob(odds1) + implied_prob(odds2)))
    elif implied_prob(odds1) + implied_prob(odds2) >= 1:
        return(False, 1-(implied_prob(odds1) + implied_prob(odds2)))

print(check_arbitrage(-191, +1001))