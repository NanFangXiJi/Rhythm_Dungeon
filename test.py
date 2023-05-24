import pandas

monster_rule_file = pandas.read_excel('data/monster_rule.xlsx')
monster_rule_list = monster_rule_file.values.tolist()

print(monster_rule_list)