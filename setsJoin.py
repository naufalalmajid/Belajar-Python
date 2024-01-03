# we can join two or more sets by using several methods
# by using union() method can make new sets by two or more sets, or update() method for inserting another set into set
life = {"alma", "always", "smile"}
relation = {"keep", "humble"}
lifeRelation = life.union(relation)
print(lifeRelation)

# or using update() to insert another set into set we selected
learning = {"life", "learning"}
sharing = {"always", "sharing"}
learning.update(sharing)
print(learning)

# for notes both union() and update() will exclude any duplicates items

# for keep only the duplicates when join sets, we can using intersection_update() for update sets
mind = {"knowledge", "patient", "consistency"}
setup = {"wealth", "patient", "knowledge"}
mind.intersection_update(setup)
print(mind)

# or we can using intersection() which the method will return a new set for only keep the duplicates items in sets
mindset = {"learning", "consistency", "trying"}
connection = {"sharing", "humble", "learning"}
mindsetConnection = mindset.intersection(connection)
print(mindsetConnection)

# for keep all but not duplicates we can using symmetric_difference_update(), this methods is will update sets
daily = {"internet", "coffee", "caffeine"}
routine = {"learning", "caffeine", "sharing"}
daily.symmetric_difference_update(routine)
print(daily)

# symmetric_difference() method will return a new set, and only element are not present in both sets
play = {"prepare", "life"}
habit = {"learning", "builds", "life"}
playHabit = play.symmetric_difference(habit)
print(playHabit)
