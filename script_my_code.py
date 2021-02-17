# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
conversion = {'M':1000000, 'B':1000000000}

def update_damages(damages):
	damages_updated = []
	for i in damages:
		if i == 'Damages not recorded':
			i = i
			damages_updated.append(i)
		elif 'M' in i:
			i = float(i[:-1])*conversion['M']
			damages_updated.append(i)
		elif 'B' in i:
			i = float(i[:-1])*conversion['B']
			damages_updated.append(i)
		else:
			print("Check input on damages")
	return damages_updated
damages_new = update_damages(damages)
print(damages_new)
print('')

# write your construct hurricane dictionary function here:
def hurricane_dictionary(names,months,years,max_sustained_winds,areas_affected,damages_new,deaths):
	list1 = names
	clist = list(zip(names, months, years, max_sustained_winds, areas_affected, damages_new, deaths))
	list2 = [{'Name': a, 'Month': b, 'Year': c, 'Max Sustained Wind': d, 'Areas Affected': e, 'Damage': f, 'Deaths': g} for (a,b,c,d,e,f,g) in clist]
	dictionary = {key:value for key,value in zip(list1,list2)}
	return dictionary

hurricanes = hurricane_dictionary(names,months,years,max_sustained_winds,areas_affected,damages_new,deaths)
print(hurricanes)
print('')

# write your construct hurricane by year dictionary function here:
def hurricanes_year(hurricanes):
	current_year = []
	current_cane = []
	new_dict = {}
	for hurricane in hurricanes:
		current_year.append(hurricanes[hurricane]['Year'])
		current_cane.append(hurricanes[hurricane])
	for i in range(0,len(current_year)):
		if not(current_year[i] in new_dict):
			new_dict[current_year[i]] = [current_cane[i]]
		else:
			new_dict[current_year[i]] = new_dict.get(current_year[i]) + [current_cane[i]]
	return new_dict

print(hurricanes_year(hurricanes))

# write your count affected areas function here:
def hurricanes_areas(hurricanes):
	new_dict = {}
	for cane in hurricanes:
		for i in range (0,len(hurricanes[cane]['Areas Affected'])):
			if not(hurricanes[cane]['Areas Affected'][i] in new_dict):
				new_dict[hurricanes[cane]['Areas Affected'][i]] = 1
			else:
				new_dict[hurricanes[cane]['Areas Affected'][i]] += 1
	return new_dict

area_dictionary = hurricanes_areas(hurricanes)
print('')
print(area_dictionary)


# write your find most affected area function here:
def most_affected_area(area_dictionary):
	count = 0
	most_area = ''
	for area in area_dictionary:
		if area_dictionary[area] > count:
			most_area = area
			count = area_dictionary[area]
	
	return 'The most affected area is {area}, affected for {count} times'.format(area=most_area, count=count)

print('')
print(most_affected_area(area_dictionary))

# write your greatest number of deaths function here:
def hurricane_with_most_deaths(hurricanes):
	count = 0
	most_death = ''
	for cane in hurricanes:
		if hurricanes[cane]['Deaths'] > count:
			most_death = cane
			count = hurricanes[cane]['Deaths']

	return 'The hurricanes with most death number is {cane}, with {count} deaths.'.format(cane=most_death, count=count)

print('')
print(hurricane_with_most_deaths(hurricanes))

# write your catgeorize by mortality function here:
def mortality_rating(hurricanes):
	new_dict = {0:[],1:[],2:[],3:[],4:[],5:[]}
	for cane in hurricanes:
		if hurricanes[cane]['Deaths'] == 0:
			new_dict[0] = new_dict.get(0) + [cane]
		elif 0 < hurricanes[cane]['Deaths'] <= 100:
			new_dict[1] = new_dict.get(1) + [cane]
		elif 100 < hurricanes[cane]['Deaths'] <= 500:
			new_dict[2] = new_dict.get(2) + [cane]
		elif 500 < hurricanes[cane]['Deaths'] <= 1000:
			new_dict[3] = new_dict.get(3) + [cane]
		elif 1000 < hurricanes[cane]['Deaths'] <= 10000:
			new_dict[4] = new_dict.get(4) + [cane]
		else:
			new_dict[5] = new_dict.get(5) + [cane]

	return new_dict
print('')
print(mortality_rating(hurricanes))

# write your greatest damage function here:
def hurricane_with_most_damage(hurricanes):
	count = 0
	most_damage = ''
	for cane in hurricanes:
		if hurricanes[cane]['Damage'] != 'Damages not recorded':		
			if hurricanes[cane]['Damage'] > count:
				most_damage = cane
				count = hurricanes[cane]['Damage']

	return 'The hurricanes with most damage is {cane}, with damages of {count} dollars.'.format(cane=most_damage, count=count)

print('')
print(hurricane_with_most_damage(hurricanes))

# write your catgeorize by damage function here:
def damage_rating(hurricanes):
	new_dict = {0:[],1:[],2:[],3:[],4:[],5:[],'Not recorded':[]}
	for cane in hurricanes:
		if hurricanes[cane]['Damage'] != 'Damages not recorded':	
			if hurricanes[cane]['Damage'] == 0:
				new_dict[0] = new_dict.get(0) + [cane]
			elif 0 < hurricanes[cane]['Damage'] <= 10**8:
				new_dict[1] = new_dict.get(1) + [cane]
			elif 10**8 < hurricanes[cane]['Damage'] <= 10**9:
				new_dict[2] = new_dict.get(2) + [cane]
			elif 10**9 < hurricanes[cane]['Damage'] <= 10**10:
				new_dict[3] = new_dict.get(3) + [cane]
			elif 10**10 < hurricanes[cane]['Damage'] <= 5*(10**10):
				new_dict[4] = new_dict.get(4) + [cane]
			elif hurricanes[cane]['Damage'] > 5*(10**10):
				new_dict[5] = new_dict.get(5) + [cane]
		else:
			new_dict['Not recorded'] = new_dict.get('Not recorded') + [cane]

	return new_dict

print('')
print(damage_rating(hurricanes))