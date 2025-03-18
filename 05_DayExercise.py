cempty_list = list()
st1 = ['Optimus Prime','Bumblebee','Ironhide','Ratchet','Jazz','Megatron','Starscream','Barricade','Brawl','Bonecrusher','Blackout','Scorponok','Frenzy']
print(len(st1))

ST111=st1[0],st1[6],st1[12]
st11=', '.join(ST111)
print(ST111)

mixed_data_types=['Santiago Mendoza','18 años','1.84 metros','Soltero','Encarnación de Díaz, Jalisco, México']
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(mixed_data_types)
print(it_companies)
print('La lista tiene',len(it_companies),'compañias')

IT2=it_companies[0],it_companies[3],it_companies[6]
IT22=', '.join(IT2)
print(IT22)

it_companies.remove('Oracle')
it_companies.insert(5,'Shockwave')
print(it_companies)

it_companies.insert(1,'IT')
print(it_companies)

it_companies.insert(4,'IT2')
print(it_companies)

it_companies.remove('Google')
it_companies.insert(2,'GOOGLE')
print(it_companies)

it_2= '#; '.join(it_companies)
print(it_2)

XYZ=input('ingrese una compañia: ')
XXX = XYZ in it_companies
print(XXX)

print(sorted(it_companies))
IT5=reversed(it_companies)
print(list(IT5))

print(list(it_companies[3:]))
print(list(it_companies[:6]))
print(list(it_companies[2:5]))

it_companies.remove('IT')
print(it_companies)

it_companies.remove('IT2')
print(it_companies)

it_companies.remove('Amazon')
print(it_companies)

it_companies.clear()
print(it_companies)

it_companies=()
print(it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
Full_Stack= ['HTML', 'CSS', 'JS', 'React', 'Redux','Python', 'SQL' 'Node','Express', 'MongoDB']

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('la menor edad es:',ages[0],'y la mayor edad es:',ages[-1])

ages.insert(0,19)
ages.insert(-1,26)
print(ages)

print('La edad media es:',ages[5])

P=sum(ages)
Prom=P/12
print('la edad promedio es:',Prom)

Rang=ages[0], ages[-1]
print('el rango de edades es:',Rang)

L5=abs(ages[0]-Prom)
L6=abs(ages[-1]-Prom)
print('La comparacion entre el minimo y el promedio es:',L5)
print('La comparacion entre el maximo y el promedio es:',L6)

countries = ['Afghanistan','Albania','Algeria','Andorra','Angola','Antigua and Barbuda','Argentina','Armenia','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados',
  'Belarus','Belgium','Belize','Benin','Bhutan','Bolivia','Bosnia and Herzegovina','Botswana','Brazil','Brunei','Bulgaria','Burkina Faso','Burundi',
  'Cambodia','Cameroon','Canada','Cape Verde','Central African Republic','Chad','Chile','China','Colombi','Comoros','Congo (Brazzaville)','Congo',
  'Costa Rica',"Cote d'Ivoire",'Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

med_country = len(countries)//2
print('La mediana es:',countries[med_country]) 

Mit_1=countries[0:med_country]
Mit_2=countries[med_country:-1]
print('La primera mitad es:',Mit_1)
print('La segunda mitad es:',Mit_2)