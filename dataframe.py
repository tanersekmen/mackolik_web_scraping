import pandas as pd

with open('teams.txt') as f:
    lines = f.readlines()

fake_data = pd.DataFrame(lines, columns = ['home'])
fake_data.drop_duplicates()
b =  [i for i in range(1, len(fake_data), 3)]
fake_data = fake_data.drop(labels = b, axis = 0)
fake_data.reset_index(drop=True, inplace = True)
fake_data = fake_data['home'].str.replace('\n', '')
second_data = pd.DataFrame(fake_data)
row_list =  [i for i in range(1, len(second_data), 2)]
second_data['away'] = second_data['home'][row_list]
changing_list = [i for i in range(1, len(second_data), 2)]
changing_list_nan = [i for i in range(0, len(second_data), 2)]
empty = []
data = pd.DataFrame(empty)
filtering = [i for i in range(1, len(second_data), 2)]
data['away'] = second_data.iloc[filtering, 1]
data = data.reset_index(drop = True)
empty_two = []
data_two = pd.DataFrame(empty_two)
filtering_two = [i for i in range(0, len(second_data), 2)]
data_two['home'] = second_data.iloc[filtering_two, 0]
data_two = data_two.reset_index(drop = True)
data = pd.concat([data_two, data ], axis=1)


# Full time 
## Full time home
with open('ft1.txt') as ft1:
    full_time_one = ft1.readlines()
full_time_one = pd.DataFrame(full_time_one, columns = ['full_time_one'])
full_time_one = full_time_one['full_time_one'].str.replace('\n', '')
data = pd.concat([data, full_time_one], axis=1)

## full time away
with open('ft2.txt') as ft2:
    full_time_two = ft2.readlines()
full_time_two = pd.DataFrame(full_time_two, columns = ['full_time_two'])
full_time_two = full_time_two['full_time_two'].str.replace('\n', '')
data = pd.concat([data, full_time_two], axis=1)

## full time equal
with open('equal.txt') as eq:
    equal = eq.readlines()
equal = pd.DataFrame(equal, columns = ['equal'])
equal = equal['equal'].str.replace('\n', '')
data = pd.concat([data, equal], axis=1)

# Under - Over
## under
with open('under.txt') as und:
    under = und.readlines()
under = pd.DataFrame(under, columns = ['under'])
under = under['under'].str.replace('\n', '')
data = pd.concat([data, under], axis=1)

## over
with open('over.txt') as ov:
    over = ov.readlines()
over = pd.DataFrame(over, columns = ['over'])
over = over['over'].str.replace('\n', '')
data = pd.concat([data, over], axis=1)


# One - zero - two
## one - zero -- o_z
with open('zero_or_one.txt') as o_z:
    one_zero = o_z.readlines()
one_zero = pd.DataFrame(one_zero, columns = ['one_zero'])
one_zero = one_zero['one_zero'].str.replace('\n', '')
data = pd.concat([data, one_zero], axis=1)

## one - two -- o_t
with open('one_or_two.txt') as o_t:
    one_two = o_t.readlines()
one_two = pd.DataFrame(one_two, columns = ['one_two'])
one_two = one_two['one_two'].str.replace('\n', '')
data = pd.concat([data, one_two], axis=1)

## zero - two -- z_t
with open('zero_or_two.txt') as z_t:
    zero_two = z_t.readlines()
zero_two = pd.DataFrame(zero_two, columns = ['zero_two'])
zero_two = zero_two['zero_two'].str.replace('\n', '')
data = pd.concat([data, zero_two], axis=1)


# Both team score
## score

with open('both_teams_to_score.txt') as item:
    yes_score = item.readlines()

yes_score = pd.DataFrame(yes_score, columns = ['both_teams_to_score'])
yes_score = yes_score['both_teams_to_score'].str.replace('\n', '')
data = pd.concat([data, yes_score], axis=1)


## no score

with open('both_teams_no_score.txt') as text:
    no_score = text.readlines()
no_score = pd.DataFrame(no_score, columns = ['both_teams_no_score'])
no_score = no_score['both_teams_no_score'].str.replace('\n', '')
data = pd.concat([data, no_score], axis=1)

# str to numeric
data['full_time_one'] = pd.to_numeric(data['full_time_one'])
data['full_time_two'] = pd.to_numeric(data['full_time_two'])
data['equal'] = pd.to_numeric(data['equal'])
data['under'] =pd.to_numeric(data['under'])
data['over'] =pd.to_numeric(data['over'])
data['one_zero'] =pd.to_numeric(data['one_zero'])
data['one_two'] =pd.to_numeric(data['one_two'])
data['zero_two'] =pd.to_numeric(data['zero_two'])
data['both_teams_no_score'] = pd.to_numeric(data['both_teams_no_score'])
data['both_teams_to_score'] = pd.to_numeric(data['both_teams_to_score'])
# to see what data looks like
print(data.head())
# filtering part--> if both_teams_to_score > 2, gets the data with odds.
print(data.loc[data['both_teams_to_score'] > 2])