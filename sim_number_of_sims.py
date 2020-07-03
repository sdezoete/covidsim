def full_simulation(NumberOfDays = NumberOfDays,
                    NumberOfAgents = NumberOfAgents,
                    NumberOfSimulationRuns = NumberOfSimulationRuns,
                    ProbabilitySusceptible = ProbabilitySusceptible,
                    PreInfectedAgents = PreInfectedAgents,
                    MeanIncubationTime = MeanIncubationTime, 
                    StandardDeviationIncubationTime = StandardDeviationIncubationTime,
                    LambdaRecoveryTime = LambdaRecoveryTime,
                    ProbabilityFatality = ProbabilityFatality,
                    ProbabilityHomeInfections=ProbabilityHomeInfections, 
                    LambdaInteractions=LambdaInteractions, 
                    ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction):
    simulation_list = []
    for i in range(NumberOfSimulationRuns):
        print("Simulation Run: ", i)
        sim_days_list = simulation_run(NumberOfDays = NumberOfDays,
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
        simulation_list.append(sim_days_list)
    return simulation_list
    
simulation_results =full_simulation(NumberOfDays = NumberOfDays,
                                    NumberOfAgents = NumberOfAgents,
                                    NumberOfSimulationRuns = NumberOfSimulationRuns,
                                    ProbabilitySusceptible = ProbabilitySusceptible,
                                    PreInfectedAgents = PreInfectedAgents,
                                    MeanIncubationTime = MeanIncubationTime, 
                                    StandardDeviationIncubationTime = StandardDeviationIncubationTime,
                                    LambdaRecoveryTime = LambdaRecoveryTime,
                                    ProbabilityFatality = ProbabilityFatality,
                                    ProbabilityHomeInfections=ProbabilityHomeInfections, 
                                    LambdaInteractions=LambdaInteractions, 
                                    ProbabilityUnsafeInteraction=ProbabilityUnsafeInteraction)

# Check Results of a record (day) in a simulation (run)
df_one_record = simulation_results[0][223] # status of agents from first simulation [0], day 223 [223]
df_one_record.head(20)