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
print('la menor edad es:',ages[0],'y la mayor edad es:',ages[-1])