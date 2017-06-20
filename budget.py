'''
Updated Budget class!!

Format external data as folows:

<description>=<amount>

At this point in development, MAKE ABSOLUTELY SURE <description> is --> U N I Q U E ! ! <--
'''
class budget():
    def __init__(self,budget_data):
        import datetime
        def spacex():
            print('')
        def hor_line():
            print(72*'_'+'\n')
        f = open(budget_data)
        working = []
        self.holy_grail = []
        balance = 0
        for i in f.readlines():
            working.append(i.split("="))
        f.close()
        self.holy_grail.append('{:%Y%m%d%H%M}'.format(datetime.datetime.today()))
        self.holy_grail.append(dict())
        for a in working:
            zorro = tuple(a[0])
            self.holy_grail[1].update({''.join(zorro):float(a[1])})
            # Need to turn key in dictionary into a tuple!!!!
        print('BUDGET: {}\n{}\n'.format(self.holy_grail[0],((len(self.holy_grail[0])+8) * "-")))
        for key,value in self.holy_grail[1].items():
            print('{:25s}{:7.2f}'.format(key.upper(),value))
            balance = balance + value
        spacex()
        print('{:25s}{:7.2f}'.format('balance'.upper(),float(balance)))
        spacex()
        hor_line()
        spacex()
