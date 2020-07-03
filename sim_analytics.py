def count_column_boolean(df_list, column_name):
    true_count_list = []
    for i in range(len(df_list)):
        df = df_list[i]
        true_count = df[column_name].sum()
        true_count_list.append(true_count)
    return true_count_list  

# Single Run Example
df_list = simulation_results[0] # chose a simulation result
# Retrieve statistics from records, counting True in status columns
number_days = len(df_list)
x1 = list(range(0, number_days))
tc_active = count_column_boolean(df_list=df_list, column_name='active')
tc_infected = count_column_boolean(df_list=df_list, column_name='infected')
tc_isolated = count_column_boolean(df_list=df_list, column_name='isolated')
tc_recovered = count_column_boolean(df_list=df_list, column_name='recovered')
tc_fatal = [NumberOfAgents-x for x in tc_active]
tc_workforce_inactive = [x + y for x, y in zip(tc_isolated, tc_fatal)]
tc_workforce_active = [NumberOfAgents-x for x in tc_workforce_inactive]

# Set Font Size for Plotting
font = {'family' : 'arial',
        'weight' : 'bold',
        'size'   : 22}

plt.rc('font', **font)
plt.rcParams['figure.figsize'] = [15,15]

# Plot the data
# Prepare the data
x = x1
y1 = tc_infected
y2 = tc_isolated
y3 = tc_recovered
y4 = tc_fatal
y5 = tc_workforce_active
plt.ylim(top = NumberOfAgents, bottom = 0)
y_ticks = range(NumberOfAgents+1)
#plt.subplot(1, 4, 4)
plt.ylim(top = NumberOfAgents, bottom = 0)
#plt.yticks(y_ticks)
plt.plot(x, y1, label='infected', lw=5.0, color='red')
plt.plot(x, y2, label='isolated', lw=5.0, color='yellow')
plt.plot(x, y3, label='recovered', lw=5.0, color='blue')
plt.plot(x, y4, label='fatal', lw=5.0, color='black')
plt.plot(x, y5, label='workforce', lw=5.0, color='green')
plt.legend()
# Show the plots
plt.show()