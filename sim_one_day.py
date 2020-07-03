def simulate_agent_infected(df_agent_records, agent_id, 
                            ProbabilityHomeInfections, LambdaInteractions, 
                            NumberOfAgents, ProbabilityUnsafeInteraction
                           ):
    agent_infected = False
    
    # agent infected at home?
    agent_infected = (np.random.uniform(0, 100) <= ProbabilityHomeInfections)
    
    # agent infected during interactions?
    number_of_interactions = int(np.random.poisson(LambdaInteractions)) # number of interactions
    agents_interactions_list = [int(x) for x in np.random.uniform(0, NumberOfAgents, number_of_interactions)] # agents
    infect_interactions_list = [1 if df_agent_records.infected[x] else 0 for x in agents_interactions_list] # infected agents
    unsafe_interactions_list = [1 if x <= ProbabilityUnsafeInteraction else 0 for 
                                x in np.random.uniform(0, 100, number_of_interactions)] # unsafe interactions
    result_list = [a and b for a, b in zip(infect_interactions_list, unsafe_interactions_list)] # cross infected and unsafe
    
    if sum(result_list):
        agent_infected = True
   
    return agent_infected
    
def simulate_day(NumberOfAgents, day_number, df_agent_records, 
                 ProbabilityHomeInfections, LambdaInteractions, 
                 ProbabilityUnsafeInteraction):
    # Check each agent
    df_agent_records_today = df_agent_records.copy()
    for i in range(NumberOfAgents):
        # 1. Agent Inactive or recovered, no actions
        if ((not df_agent_records_today.active[i]) 
            or (df_agent_records_today.recovered[i]) 
            or (not df_agent_records_today.susceptible[i])):
            continue
        
        # 2. Agent in Isolation, check if recovery is due
        if df_agent_records_today.isolated[i]:
            if (df_agent_records.recovery_day[i] == day_number):
                # data.loc[data.bidder == 'parakeet2004', 'bidderrate'] = 100
                df_agent_records_today.loc[df_agent_records_today.id == i, 'recovered'] = True
                df_agent_records_today.loc[df_agent_records_today.id == i, 'isolated'] = False
            continue
        
        # 3. Agent is Infected, check if isolation is due
        if df_agent_records_today.infected[i]:
            if (df_agent_records_today.isolation_day[i] == day_number):
                # check fatality
                if df_agent_records_today.fatal[i]:
                    df_agent_records_today.loc[df_agent_records_today.id == i, 'active'] = False
                    # no longer infection threat as agent isolated from employees
                df_agent_records_today.loc[df_agent_records_today.id == i, 'isolated'] = True
                df_agent_records_today.loc[df_agent_records_today.id == i, 'infected'] = False
                recovery_day = df_agent_records_today.recovery_time[i] + day_number
                df_agent_records_today.loc[df_agent_records_today.id == i, 'recovery_day'] = recovery_day
                
            continue
            
        # 4. Agent is healty, simulate day
        agent_infected = simulate_agent_infected(df_agent_records=df_agent_records, # send previous day record!
                                                 agent_id=i, 
                                                 ProbabilityHomeInfections=ProbabilityHomeInfections, 
                                                 LambdaInteractions=LambdaInteractions,
                                                 NumberOfAgents=NumberOfAgents,
                                                 ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction
                                                ) 
    
        if agent_infected:
            df_agent_records_today.loc[df_agent_records_today.id == i, 'infected'] = True
            isolation_day = df_agent_records_today.incubation_time[i] + day_number
            df_agent_records_today.loc[df_agent_records_today.id == i, 'isolation_day'] = isolation_day
            
    return df_agent_records_today # todays record

# Show one day
df_one_day = simulate_day(NumberOfAgents=NumberOfAgents, 
                          day_number=1, 
                          df_agent_records=df_agent_records,
                          ProbabilityHomeInfections=ProbabilityHomeInfections, 
                          LambdaInteractions=LambdaInteractions, 
                          ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction)
# Resulting Record
df_one_day.head(5)    