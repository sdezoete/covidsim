# import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# initialize variables
NumberOfAgents = 200
NumberOfDays = 365
ProbabilitySusceptible = 95
ProbabilityPreInfected = 5
LambdaInteractions = 10
ProbabilityInteractionAgent = NumberOfAgents
ProbabilityUnsafeInteraction = 2
ProbabilityHomeInfections = 0.3
MeanIncubationTime = 14
StandardDeviationIncubationTime = 2
LambdaRecoveryTime = 30
ProbabilityFatality = 1.5
NumberOfSimulationRuns = 10

# create agent records
def create_agent_records(NumberOfAgents,
                         ProbabilitySusceptible,
                         PreInfectedAgents,
                         MeanIncubationTime, # Incubation time is preset only used when infection occurs
                         StandardDeviationIncubationTime,
                         LambdaRecoveryTime, # Recovery time is preset only used when infection occurs
                         ProbabilityFatality # If fatal is true, recovery time is not considered, agent is inactive permanently
                        ):
    
    df_columns = ['id','active', 'susceptible', 
                  'infected', 'incubation_time', 'isolation_day',
                  'isolated', 'recovery_time', 'recovery_day',
                  'recovered', 'fatal']
    
    # Create agent records in DataFrame
    record_list = []
    for i in range (NumberOfAgents):
        agent_id = i
        agent_active = True
        agent_susceptible = (np.random.uniform(0, 100) <= ProbabilitySusceptible) # True or False susceptible
        agent_infected = ((np.random.uniform(0, 100) <= ProbabilityPreInfected) and agent_susceptible)
        agent_incubation_time = int(np.random.normal(MeanIncubationTime, StandardDeviationIncubationTime))
        agent_isolation_day = 0
        if agent_infected:
            agent_isolation_day = agent_incubation_time
        agent_isolated = False
        agent_recovery_time = int(np.random.exponential(LambdaRecoveryTime))
        agent_recovery_day = 0
        agent_recovered = False
        agent_fatal = (np.random.uniform(0, 100) <= ProbabilityFatality) # True or False fatal
        agent_record = [agent_id, agent_active, agent_susceptible,
                        agent_infected, agent_incubation_time, agent_isolation_day,
                        agent_isolated, agent_recovery_time, agent_recovery_day,
                        agent_recovered, agent_fatal
                       ]
        record_list.append(agent_record)
    df_agent_records = pd.DataFrame(record_list, columns=df_columns)
    return df_agent_records

# create the record to check
df_agent_records = create_agent_records(NumberOfAgents = NumberOfAgents,
                                         ProbabilitySusceptible = ProbabilitySusceptible,
                                         PreInfectedAgents = PreInfectedAgents,
                                         MeanIncubationTime = MeanIncubationTime, 
                                         StandardDeviationIncubationTime = StandardDeviationIncubationTime,
                                         LambdaRecoveryTime = LambdaRecoveryTime,
                                         ProbabilityFatality = ProbabilityFatality
                                        )

# show sample record										
df_agent_records.head()