from pandas.core.api import DataFrame as DataFrame

def fractional_knapsack(profits, weights, max_weight):
    """A function that uses the fractional knapsack algorithm"""
    data = {
        'profits': profits,
        'weights': weights
    }   
    df = DataFrame(data)
    
    # Compute ratios for items
    ratios = []
    for i in range(len(df)):
        ratios.append(df.iloc[i,0] / df.iloc[i,1])       
    df['ratios'] = ratios

    # Sort by the ratios 
    df = df.sort_values('ratios', ascending=False)
    df = df.reset_index(drop=True)     
    
    curWeights = 0
    counter = 0
    subset = DataFrame(columns=['profits', 'weights', 'ratios'])
    fraction = DataFrame(columns=['profits', 'weights', 'ratios'])
    
    # While the maximum weight is not exceeded, remove the first row from the dataframe, 
    # and add it to a subset dataframe.
    while True:
        curWeights += df.iloc[0, 1]
        
        if curWeights > max_weight:
            fraction.loc[0] = df.loc[0]
            break
        else:
            subset.loc[counter] = df.loc[0]
            counter += 1
            
            df.drop(0, axis=0, inplace=True)
            df = df.reset_index(drop=True) 
    
    
    total_profit = 0
    curWeights = 0 # Total Weight of items in the subset dataframe
    items = []
    # Compute the total profit
    for i in range(len(subset)):
        total_profit +=  subset.iloc[i, 0]
        curItemText = f'Item {i+1} -- Profit: {subset.iloc[i, 0]}'
        items.append(curItemText)
        curWeights += subset.iloc[i, 1]
    total_profit += (max_weight - curWeights) / fraction.iloc[0, 1] * fraction.iloc[0, 0]
    
    fraction_message = f'{max_weight - curWeights} / {fraction.iloc[0, 1]} of {fraction.iloc[0, 0]}'
    items.append(fraction_message)
    message = "The maximum profit is " + str(total_profit) + "\n"
    return message, items
    
#total_profit = fractional_knapsack([280, 100, 120, 120], [40, 10, 20, 24], 60)
#print(total_profit)

def job_sequencing_with_deadline(jobs, deadlines, profits):
    """In Job sequencing problem, the objective is to find a sequence of jobs 
    that will be completed within deadline and give maximum profit.
    Each job is associated with a deadline, and a profit.

    Args:
        jobs (list): list of jobs, in order
        deadlines (list): list of deadlines, in order
        profits (list): list of profits, in order
    """
    
    data = {
        'jobs': jobs,
        'deadlines': deadlines,
        'profits': profits
    }   
    df = DataFrame(data)
    df = df.sort_values(['deadlines', 'profits'], ascending=[True, False])
    df = df.reset_index(drop=True)  
    
    sequence_df = DataFrame(columns=['jobs', 'deadlines', 'profits'])
    max_profit = 0
    jobs_already_chosen = [] # List of deadlines that have already been chosen
    
    for i in range(len(df)):                
        if df.iloc[i, 1] in jobs_already_chosen:
            #df.drop(i, axis=0, inplace=True)
            pass
        else:
            sequence_df.loc[i] = df.loc[i]
            jobs_already_chosen.append(df.iloc[i, 1])
                                    
    sequence_df = sequence_df.reset_index(drop=True)
    
    for profit in sequence_df['profits']:
        max_profit += profit 
        
 
    job_sequence_msg = "The sequence of jobs is "
    for i in range(len(sequence_df)):
        job_sequence_msg +=  f'{sequence_df.iloc[i, 0]} ({sequence_df.iloc[i, 2]}), '

    return job_sequence_msg, max_profit

#test = job_sequencing_with_deadline(['j1', 'j2', 'j3', 'j4', 'j5'], [2, 1, 3, 2, 1], [60, 100, 20, 40, 20])
#print(test)