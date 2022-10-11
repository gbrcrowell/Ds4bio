import pandas as pd
states = pd.read_csv("state_health.csv")
states.set_index('State Name', inplace=True)
states_named = states
x = 10

sorted_incomes = states_named.sort_values('Per Capita Income')
low_income = sorted_incomes.head(x)
higher_income = sorted_incomes.tail(x)
# bottom = states.sort_values('Per Capita Income').head(x)
# top = states.sort_values('Per Capita Income').tail(x)


homes_low_income = low_income.loc[:, 'Homeownership']
homes_higher_income = higher_income.loc[:, 'Homeownership']

avg_home_low_income = homes_low_income.mean()
avg_home_higher_income = homes_higher_income.mean()

print(avg_home_higher_income)
print(avg_home_low_income)
# print(f'Average of the top states: {sum(top["Homeownership"]) / len(top["Homeownership"])}')
# print(f'Average of the bottom states: {sum(bottom["Homeownership"]) / len(bottom["Homeownership"])}')


sorted_incomes = states_named.sort_values('Per Capita Income')
diff_homes = avg_home_low_income - avg_home_higher_income
diff_voting = states_named.loc[:, 'Voter Participation (Presidential)'] - states_named.loc[:, 'Voter Participation (Midterm)']
# midterm = states['Voter Participation (Midterm)']
# presidential = states['Voter Participation (Presidential)']
# difference = midterm - presidential

sorted_voting = diff_voting.sort_values(ascending = False)
top_five = sorted_voting.head(5)

print(sorted_voting)
# print(f'Difference: {abs((sum(top["Homeownership"]) / len(top["Homeownership"])) - (sum(bottom["Homeownership"]) / len(bottom["Homeownership"])))}')
print(top_five)
# print(f'the states with eh biggest difference between their votes are: {abs(difference.sort_values().head(5))} and the least are: {abs(difference.sort_values().tail(5))}')
