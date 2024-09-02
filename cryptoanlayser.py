

#---------------------------------------------
#Function to display the main menu.
#---------------------------------------------

print()
print("=============================================")
print("           CRYPTO ANALYSER          ")
print("*********************************************")
print("1-About Cryptoanalyser\n")
print("2-Current Prices\n")
print("3-Frequently Asked Questions\n")
print("4-Data Visualisation\n")
print("5-Price Comparison with Bar graph\n")
print("6-Trading Profit Calculator\n")
print("7-Exit")
print("This Project is made by Varun,Tejas and Karthik")
print("=============================================")
opt=input("Enter your choice:")
if opt=='1':
    print("This project is all about cryptocurrency.We have used python libraries to make this program.We used a python library which is called CryptoCompare,It has all the information and live prices of all the cryptocurrencies.This program is used to track the prices of cryptocurrencies and help us to predict the future prices.")

elif opt=='2':
    import cryptocompare
    def get_crypto_price(cryptocurrency,currency):
        return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
    def get_crypto_name(cryptocurrency):
        return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
    n=input("Enter the name of cryptocurrency-")
    print(get_crypto_price(n,'USD'))
    print(get_crypto_name(n))
elif opt=='3':
    while True:
        print("\n\nFrequently Asked Questions")
        print("******************************")
        print("\n1-What is Cryptocurrency?\n2-What is blockchain?\n3-What are public and private keys?\n4-How do cryptocurrencies work?\n5-What are the reasons for the popularity of cryptocurrencies?\n6-Who controls cryptocurrencies?\n7-Is it reasonable to invest in cryptocurrencies?\n8-How can I buy cryptocurrencies?\n9-How can I start investing in cryptocurrencies?\n10-EXIT\n")
        print("==============================")
        mch=int(input("Enter your choice:"))
        if mch==1:
            print("\nThe first and obvious addition among cryptocurrency FAQs would turn the emphasis towards definition of cryptocurrencies. Cryptocurrency is basically a digital form of currency with the support of cryptographic security for conducting trusted transactions. The underlying technology which runs cryptocurrencies is blockchain, and it offers a ledger for documenting all transactions. As of now, you can find multiple cryptocurrencies in circulation, such as Bitcoin, Ether, and many new cryptocurrencies. The cryptocurrencies run as decentralized systems or networks without allowing complete control to a specific entity. Another important highlight of cryptocurrencies refers to the method for generating them. For example, miners could use their computing resources and electricity for mining cryptocurrency or stake their assets in a network for earning governance tokens.")
        elif mch==2:
            print("\nYou could not find any list of cryptocurrency questions for beginners without the mention of blockchain. The first-ever cryptocurrency, Bitcoin, is the first successful implementation of blockchain in the real world. Blockchain technology is basically a transparent, publicly accessible, trustless, and secure ledger. It helps in secure transfer of the ownership of units of value by leveraging proof of work consensus and public-key encryption methods. Blockchain leverages decentralized consensus for maintaining the network, thereby excluding intermediaries such as government, banks, or corporations from the process. On top of it, the expansion of the blockchain network increases the level of decentralization, thereby strengthening security on blockchain. Interestingly, the capabilities of blockchain technology don’t focus on Bitcoin only and also extend to financial services, healthcare, and gaming.")
        elif mch==3:
            print("\nThe next important addition among best questions about crypto would draw attention towards the basic elements in working of cryptocurrencies. The primary foundation of Bitcoin and other notable cryptocurrencies is public-key cryptography. According to the cryptographic system, two different types of keys, such as public key and private key in pairs, can support crypto transactions. The public keys are important for identification and should be publicly visible. On the other hand, the private keys help in authentication and encryption, thereby implying that they are secret in nature. ")
        elif mch==4:
            print("\nThe working of cryptocurrencies is also a common highlight in cryptocurrency questions and answers for beginners. Popular cryptocurrencies such as Ethereum and Bitcoin work by using three basic pieces of information. The first important aspect in the working of cryptocurrencies is the address related to a specific account. The second important piece of information is the balance you would use for sending and receiving funds. Another significant aspect for the working of cryptocurrencies would refer to the public and private keys associated with a specific address. You can generate a private key by generating a Bitcoin address which would also help in identifying the corresponding public key. Subsequently, you can use the address as a representative of the public key for different transactions. On the other hand, the private key offers control over ownership of the funds in a specific address.")
        elif mch==5:
            print("\nThe reasons for popularity of cryptocurrencies also set the foundation for some frequently asked questions about cryptocurrencies. Interestingly, you can find various reasons for the popularity of cryptocurrencies. One of the most common reasons for popularity of cryptocurrencies refers to the assumptions suggesting that cryptocurrencies are the currency of the future. In addition, cryptocurrencies also remove banks and other financial intermediaries from focusing on reducing the value of money.Most important of all, the technology behind cryptocurrencies, i.e., blockchain, is the biggest draw for the future of crypto. Blockchain offers a decentralized system for processing and documenting transactions with better security in comparison to conventional payment systems. On top of it, the rising value of cryptocurrencies also encourages people to turn towards cryptocurrencies in large numbers.")
        elif mch==6:
            print("\nThe commonly asked cryptocurrency questions for beginners would also point towards the implication of control and ownership of cryptocurrencies. Blockchain does not allocate control to a single entity in the case of cryptocurrencies. However, the creators or developers of cryptocurrencies can set specific parameters such as rules for purchasing or selling cryptocurrency. On the other hand, users get the privilege of controlling or managing the day-to-day operations of cryptocurrencies in a distributed manner. In addition, the identity of owners is anonymous, and you could not find any solid regulatory framework for verifying ownership of cryptocurrencies. However, some countries are investing efforts in introducing some regulations in this area for countering illegal activities. The legal framework for cryptocurrencies could help governments in fighting off the concerns of terrorism financing and money laundering with cryptocurrencies. Furthermore, regulations could also strengthen control of governments over monetary policies with respect to cryptocurrencies.")
        elif mch==7:
            print("\nInvestment in cryptocurrencies is also one of the notable highlights in cryptocurrency FAQs, especially for beginners. If you want to find whether cryptocurrencies are a good investment, then you should definitely know that they are volatile. Cryptocurrencies do not generate any cash flow like real currencies and are not stable. A currency should have stability which could help merchants and consumers in deciding the fair price for goods.Bitcoin and many other popular cryptocurrencies have barely shown any sign of stability since their inception. For example, after rising to almost $20,000 in 2017, the value of Bitcoin dropped to almost $3200 in 2018. Now in 2021, Bitcoin has been successful in attaining record high levels. With price volatility as the main concern, it is quick to arrive at a conclusion about investments in cryptocurrency.")
        elif mch==8:
            print("\nAnother common entry among common cryptocurrency questions and answers would point out methods for buying cryptocurrencies. Beginners who want to learn about cryptocurrencies are also likely to express interest in owning and trading cryptocurrency. Interestingly, you could purchase some cryptocurrencies such as Bitcoin directly with fiat currency like US dollars. On the other hand, you might also find some cryptocurrencies which you have to purchase with Bitcoins or other cryptocurrencies. You can buy cryptocurrencies through a wallet, which is basically an online app for holding your crypto assets. Users generally have to create an account for a specific exchange and transfer actual money for purchasing cryptocurrencies such as Ethereum or Bitcoin. One of the popular examples of platforms to buy and sell cryptocurrency is Coinbase. The renowned cryptocurrency trading exchange helps you create a wallet and conduct cryptocurrency transactions easily.")
        elif mch==9:
            print("\nYou could also have some of the best questions about crypto dealing directly with investment in cryptocurrencies. Beginners have doubts regarding the best practices for investing in cryptocurrencies and need the best practices for doing the same. You can take the example of Bitcoin and start investing by joining a Bitcoin exchange and obtaining a wallet. After obtaining the Bitcoin wallet, you need to connect it with a bank account, and then you can place your Bitcoin order. Once you have Bitcoin in your account, you can invest it in liquidity pools, yield farming, or staking for earning passive income. On the other hand, some crypto owners could also choose to hold their crypto and wait for their prices to rise before trading. The key to successful investments in cryptocurrencies largely revolves around successful management of your Bitcoin investments.")
        elif mch==10:
            print("Thank You..Exitng now......")
            exit()
        else:
            print("Invalid choice.Please Try Again")
elif opt=='4':
    while True:
        print("******************************")
        print("\n\nData Visualisation")
        print("******************************")
        menu="\n1-BitCoin Live Price Graph\n2-Etherium Live Price Graph\n3-Dogecoin Live Price Graph\n4-Cardano Live Price Graph\n5-XRP Live Price Graph\n6-Litecoin Live Price Graph\n7-Polkadot Live Price Graph\n8-TRON Live Price Graph\n9-Solana Live Price Graph\n10-Terra Live Price Graph\n11-Other than these cryptocurrencies\n12-EXIT\n"
        print (menu)
        print("------------------------------")
        ch_an=int(input("Enter your choice:"))
        if ch_an==1:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('BTC','USD'))
            print(get_crypto_name('BTC'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('BTC','USD'))
                plt.cla()
                plt.title(get_crypto_name('BTC') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani = FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==2:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('ETH','USD'))
            print(get_crypto_name('ETH'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('ETH','USD'))
                plt.cla()
                plt.title(get_crypto_name('ETH') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==3:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('DOGE','USD'))
            print(get_crypto_name('DOGE'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('DOGE','USD'))
                plt.cla()
                plt.title(get_crypto_name('DOGE') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==4:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('ADA','USD'))
            print(get_crypto_name('ADA'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('ADA','USD'))
                plt.cla()
                plt.title(get_crypto_name('ADA') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==5:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('XRP','USD'))
            print(get_crypto_name('XRP'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('XRP','USD'))
                plt.cla()
                plt.title(get_crypto_name('XRP') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==6:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('LTC','USD'))
            print(get_crypto_name('LTC'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('LTC','USD'))
                plt.cla()
                plt.title(get_crypto_name('LTC') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==7:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('DOT','USD'))
            print(get_crypto_name('DOT'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('DOT','USD'))
                plt.cla()
                plt.title(get_crypto_name('DOT') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==8:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('TRX','USD'))
            print(get_crypto_name('TRX'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('TRX','USD'))
                plt.cla()
                plt.title(get_crypto_name('TRX') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==9:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('SOL','USD'))
            print(get_crypto_name('SOL'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('SOL','USD'))
                plt.cla()
                plt.title(get_crypto_name('SOL') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==10:
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price('LUNA','USD'))
            print(get_crypto_name('LUNA'))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price('LUNA','USD'))
                plt.cla()
                plt.title(get_crypto_name('LUNA') + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()
        elif ch_an==11:
            n1=input("Enter the name of cryptocurrency-")
            import cryptocompare
            def get_crypto_price(cryptocurrency,currency):
                return cryptocompare.get_price(cryptocurrency,currency)[cryptocurrency][currency]
            def get_crypto_name(cryptocurrency):
                return cryptocompare.get_coin_list()[cryptocurrency]['FullName']
            print(get_crypto_price(n1,'USD'))
            print(get_crypto_name(n1))
            import matplotlib.pyplot as plt
            from datetime import datetime
            from matplotlib.animation import FuncAnimation
            x_vals = []
            y_vals = []
            def animate(i):
                x_vals.append(datetime.now())
                y_vals.append(get_crypto_price(n1,'USD'))
                plt.cla()
                plt.title(get_crypto_name(n1) + ' Price Live Plotting')
                plt.xlabel('Date')
                plt.ylabel('Price(USD$)')
                plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
                plt.tight_layout()
            ani=FuncAnimation(plt.gcf(), animate, interval=1000)
            plt.show()            
            
        elif ch_an==12:
            print("Thank You..Exitng now......")
            exit()
        else:
            print("Invalid choice.Please Try Again")
elif opt=='5':
    import numpy as np
    import matplotlib.pyplot as plt
    # creating the dataset
    data = {'Binance Coin':280,'Etherium':1559,'Litecoin':55,'BNB':340,'Solana':35}
    Name_of_CryptoCurrency = list(data.keys())
    Prices = list(data.values())
    fig = plt.figure(figsize = (10, 5))
    # creating the bar plot
    plt.bar(Name_of_CryptoCurrency,Prices,color ='Blue',width = 0.4)
    plt.xlabel("Name of Cryptocurrency")
    plt.ylabel("Prices")
    plt.title("Price Comparison in USD")
    plt.show()

elif opt=='6':
    # Crypto to Fiat Price
    buy = float(input('Enter buying price '))
    sell = float(input('Enter selling price '))
    # Investment
    inv = float(input('Enter amount invested '))
    # Volume Calculation
    vol = (inv/buy)
    # Trading Fee Buying
    buy_fee = 0.001 * inv
    # Return
    retn = (sell * vol)
    # Trading Fee Selling
    sell_fee = 0.001 * retn
    # Profit?
    net_profit = round((retn - inv - buy_fee - sell_fee), 2)
    if net_profit > 1:
        print()
        print('Net Profit', net_profit)
        print('Net Estimate 30 Days', round(30 * net_profit, 2))
        print()
        print('Current Transaction Profit %', (net_profit/inv) * 100)
        print('Estimated 30 Days Profit %', (30*net_profit/inv) * 100)
    else:
        print('Trade Not Profitable')
        print('Loss', net_profit)
elif opt=='7':
    print("Thank You..Exitng now......")
    exit()
else:
    print("Invalid choice.Please Try Again")
   

#**********************************************

            
                  
                  
                  
     
                  
                
    
