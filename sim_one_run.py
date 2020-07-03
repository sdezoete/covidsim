def simulation_run(NumberOfDays = NumberOfDays,
                   NumberOfAgents = NumberOfAgents,
                   ProbabilitySusceptible = ProbabilitySusceptible,
                   PreInfectedAgents = PreInfectedAgents,
                   MeanIncubationTime = MeanIncubationTime, 
                   StandardDeviationIncubationTime = StandardDeviationIncubationTime,
                   LambdaRecoveryTime = LambdaRecoveryTime,
                   ProbabilityFatality = ProbabilityFatality,
                   ProbabilityHomeInfections=ProbabilityHomeInfections, 
                   LambdaInteractions=LambdaInteractions, 
                   ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction
                  ):
    # Create Agent Records
    df_agent_records = create_agent_records(NumberOfAgents = NumberOfAgents,
                                         ProbabilitySusceptible = ProbabilitySusceptible,
                                         PreInfectedAgents = PreInfectedAgents,
                                         MeanIncubationTime = MeanIncubationTime, 
                                         StandardDeviationIncubationTime = StandardDeviationIncubationTime,
                                         LambdaRecoveryTime = LambdaRecoveryTime,
                                         ProbabilityFatality = ProbabilityFatality
                                        )
    # Simulate number of days
    df_agent_records_today = df_agent_records.copy()
    sim_days_list = []
    sim_days_list.append(df_agent_records_today)
    for day_number in range(1, NumberOfDays+1): #starting day 1
        df_agent_records_today = simulate_day(NumberOfAgents=NumberOfAgents, 
                                              day_number=day_number, 
                                              df_agent_records=df_agent_records_today,
                                              ProbabilityHomeInfections=ProbabilityHomeInfections, 
                                              LambdaInteractions=LambdaInteractions, 
                                              ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction)
    
        sim_days_list.append(df_agent_records_today)
    return sim_days_list
    
# Check single Run
daily_records_list_single_run = simulation_run(NumberOfDays = NumberOfDays,
                                               NumberOfAgents = NumberOfAgents,
                                               ProbabilitySusceptible = ProbabilitySusceptible,
                                               PreInfectedAgents = PreInfectedAgents,
                                               MeanIncubationTime = MeanIncubationTime, 
                                               StandardDeviationIncubationTime = StandardDeviationIncubationTime,
                                               LambdaRecoveryTime = LambdaRecoveryTime,
                                               ProbabilityFatality = ProbabilityFatality,
                                               ProbabilityHomeInfections=ProbabilityHomeInfections, 
                                               LambdaInteractions=LambdaInteractions, 
                                               ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction
                                              )
                                              
# Show a record
df_one_record = daily_records_list_single_run[4] # example day 4
df_one_record.head(20)