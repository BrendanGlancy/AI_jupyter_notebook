from empyrial import empyrial, Engine
portfolio = Engine(    
         start_date= "2018-06-09", 
         portfolio= ["BABA", "PDD", "KO", "AMD","^IXIC"], 
         weights = [0.2, 0.2, 0.2, 0.2, 0.2], 
         benchmark = ["SPY"], #SPY is set by default
         
)
empyrial(portfolio)

