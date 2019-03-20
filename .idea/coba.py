import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import xlsxwriter

testSet = pd.read_excel("TestsetTugas1ML.xlsx")
trainSet = pd.read_excel("TrainsetTugas1ML.xlsx")
#testSet.set_index("id", inplace=True)

#print("Column headings:")
#print(testSet.columns)
#print(testSet['age'])

#INISIALISASI
#income :
lebihdari = 0 ; kurangdari = 0
#Age
adultlebih = 0 ; adultkurang = 0
oldlebih = 0 ; oldkurang = 0
younglebih = 0 ; youngkurang = 0

#Workclass
locallebih = 0 ; localkurang = 0
privatelebih = 0 ; privatekurang = 0
selflebih = 0; selfkurang = 0

#EDUCATION :
Bachelorslebih=0 ; Bachelorskurang = 0
hslebih = 0 ; hskurang = 0
collegelebih = 0; collegekurang = 0

#MARITAL-STATUS :
divorcedlebih = 0 ; divorcedkurang = 0
marriedlebih = 0 ; marriedkurang = 0
neverlebih = 0 ; neverkurang = 0

#OCCUPATION
craftlebih = 0 ; craftkurang = 0
execlebih = 0 ; execkurang = 0
proflebih = 0 ; profkurang = 0

#RELATIONSHIP
husbandlebih = 0 ; husbandkurang = 0
notlebih = 0 ; notkurang = 0
ownlebih = 0 ; ownkurang = 0

#HOURS-PER-WEEK
lowlebih = 0 ; lowkurang = 0
manylebih = 0 ; manykurang = 0
normallebih = 0 ; normalkurang = 0

hasilakhir = []
#
j=0

#Algoritma
for i in trainSet.index :
    if (trainSet['income'][i] == '>50K'):
        lebihdari +=1
    else:
        kurangdari += 1
    j +=1
lebih = lebihdari/j
kurang = kurangdari/j
print('probabilitas income : ')
print('>50K = ',lebih)
print('<=50K = ',kurang)

for i in trainSet.index:
    # Probabilitas Age :
    if (trainSet['age'][i]) == 'young' and trainSet['income'][i] == '>50K':
        younglebih +=1
    elif trainSet['age'][i] == 'young' and trainSet['income'][i] == '<=50K':
        youngkurang += 1

    if trainSet['age'][i] == 'adult' and trainSet['income'][i] == '<=50K':
        adultkurang += 1
    elif (trainSet['age'][i]) == 'adult' and trainSet['income'][i] == '>50K':
        adultlebih += 1

    if (trainSet['age'][i]) == 'old' and trainSet['income'][i] == '>50K':
        oldlebih += 1
    elif (trainSet['age'][i]) == 'old' and trainSet['income'][i] == '<=50K':
        oldkurang += 1

    # Probabilitas Worckclass :
    if (trainSet['workclass'][i]) == 'Local-gov' and trainSet['income'][i] == '>50K':
        locallebih += 1
    elif (trainSet['workclass'][i]) == 'Local-gov' and trainSet['income'][i] == '<=50K':
        localkurang += 1

    if (trainSet['workclass'][i]) == 'Private' and trainSet['income'][i] == '>50K':
        privatelebih += 1
    elif (trainSet['workclass'][i]) == 'Private' and trainSet['income'][i] == '<=50K':
        privatekurang += 1

    if (trainSet['workclass'][i]) == 'Self-emp-not-inc' and trainSet['income'][i] == '>50K':
        selflebih += 1
    elif (trainSet['workclass'][i]) == 'Self-emp-not-inc' and trainSet['income'][i] == '<=50K':
        selfkurang += 1

    # Probabilitas education :
    if (trainSet['education'][i]) == 'Bachelors' and trainSet['income'][i] == '>50K':
        Bachelorslebih += 1
    elif (trainSet['education'][i]) == 'Bachelors' and trainSet['income'][i] == '<=50K':
        Bachelorskurang += 1

    if (trainSet['education'][i]) == 'HS-grad' and trainSet['income'][i] == '>50K':
        hslebih += 1
    elif (trainSet['education'][i]) == 'HS-grad' and trainSet['income'][i] == '<=50K':
        hskurang += 1

    if (trainSet['education'][i]) == 'Some-college' and trainSet['income'][i] == '>50K':
        collegelebih += 1
    elif (trainSet['education'][i]) == 'Some-college' and trainSet['income'][i] == '<=50K':
        collegekurang += 1

    # Probabilitas marital-status :
    if (trainSet['marital-status'][i]) == 'Divorced' and trainSet['income'][i] == '>50K':
        divorcedlebih += 1
    elif (trainSet['marital-status'][i]) == 'Divorced' and trainSet['income'][i] == '<=50K':
        divorcedkurang += 1

    if (trainSet['marital-status'][i]) == 'Married-civ-spouse' and trainSet['income'][i] == '>50K':
        marriedlebih += 1
    elif (trainSet['marital-status'][i]) == 'Married-civ-spouse' and trainSet['income'][i] == '<=50K':
        marriedkurang += 1

    if (trainSet['marital-status'][i]) == 'Never-married' and trainSet['income'][i] == '>50K':
        neverlebih += 1
    elif (trainSet['marital-status'][i]) == 'Never-married' and trainSet['income'][i] == '<=50K':
        neverkurang += 1

    # Probabilitas occupation :
    if (trainSet['occupation'][i]) == 'Craft-repair' and trainSet['income'][i] == '>50K':
        craftlebih += 1
    elif (trainSet['occupation'][i]) == 'Craft-repair' and trainSet['income'][i] == '<=50K':
        craftkurang += 1

    if (trainSet['occupation'][i]) == 'Exec-managerial' and trainSet['income'][i] == '>50K':
        execlebih += 1
    elif (trainSet['occupation'][i]) == 'Exec-managerial' and trainSet['income'][i] == '<=50K':
        execkurang += 1

    if (trainSet['occupation'][i]) == 'Prof-specialty' and trainSet['income'][i] == '>50K':
        proflebih += 1
    elif (trainSet['occupation'][i]) == 'Prof-specialty' and trainSet['income'][i] == '<=50K':
        profkurang += 1

    # Probabilitas RELATIONSHIP :
    if (trainSet['relationship'][i]) == 'Husband' and trainSet['income'][i] == '>50K':
        husbandlebih += 1
    elif (trainSet['relationship'][i]) == 'Husband' and trainSet['income'][i] == '<=50K':
        husbandkurang += 1

    if (trainSet['relationship'][i]) == 'Not-in-family' and trainSet['income'][i] == '>50K':
        notlebih += 1
    elif (trainSet['relationship'][i]) == 'Not-in-family' and trainSet['income'][i] == '<=50K':
        notkurang += 1

    if (trainSet['relationship'][i]) == 'Own-child' and trainSet['income'][i] == '>50K':
        ownlebih += 1
    elif (trainSet['relationship'][i]) == 'Own-child' and trainSet['income'][i] == '<=50K':
        ownkurang += 1

    # Probabilitas HOURS PER WEEK :
    if (trainSet['hours-per-week'][i]) == 'low' and trainSet['income'][i] == '>50K':
        lowlebih += 1
    elif (trainSet['hours-per-week'][i]) == 'low' and trainSet['income'][i] == '<=50K':
        lowkurang += 1

    if (trainSet['hours-per-week'][i]) == 'many' and trainSet['income'][i] == '>50K':
        manylebih += 1
    elif (trainSet['hours-per-week'][i]) == 'many' and trainSet['income'][i] == '<=50K':
        manykurang += 1

    if (trainSet['hours-per-week'][i]) == 'normal' and trainSet['income'][i] == '>50K':
        normallebih += 1
    elif (trainSet['hours-per-week'][i]) == 'normal' and trainSet['income'][i] == '<=50K':
        normalkurang += 1

#probabilitas setiap data
younglebih /= lebihdari;    youngkurang /= kurangdari
adultlebih /= lebihdari;    adultkurang /= kurangdari
oldlebih /= lebihdari;      oldkurang /=kurangdari

locallebih /= lebihdari;    localkurang /= kurangdari
privatelebih /= lebihdari;  privatekurang /= kurangdari
selflebih /= lebihdari ;    selfkurang /= kurangdari

Bachelorslebih/=lebihdari;  Bachelorskurang/=kurangdari
hslebih/=lebihdari;         hskurang/=kurangdari
collegelebih/=lebihdari;    collegekurang/=kurangdari

divorcedlebih/=lebihdari;   divorcedkurang/=kurangdari
marriedlebih/=lebihdari;    marriedkurang/=kurangdari
neverlebih/=lebihdari;      neverkurang/=kurangdari

#OCCUPATION
craftlebih /= lebihdari ;   craftkurang /= kurangdari
execlebih /= lebihdari ;    execkurang /= kurangdari
proflebih /= lebihdari ;    profkurang /= kurangdari

#RELATIONSHIP
husbandlebih /= lebihdari ; husbandkurang /= kurangdari
notlebih /= lebihdari ;     notkurang /= kurangdari
ownlebih /= lebihdari ;     ownkurang /= kurangdari

#HOURS-PER-WEEK
lowlebih /= lebihdari ;     lowkurang /= kurangdari
manylebih /= lebihdari ;    manykurang /= kurangdari
normallebih /= lebihdari ;  normalkurang /= kurangdari

print('probabilitas Age : ')
print('Young - >50K = ',younglebih)
print('Young - <=50K = ',youngkurang)
print('Adult - >50K = ',adultlebih)
print('Adult - <=50K = ',adultkurang)
print('Old - >50K = ',oldlebih)
print('Old - <=50K = ',oldkurang)
print()

print('Probabilitas Workclass : ')
print('Local-gov - >50K = ',locallebih)
print('Local-gov - <=50K = ',localkurang)
print('Private - >50K = ',privatelebih)
print('Private - <=50K = ',privatekurang)
print('Self-emp-not-inc - >50K = ',selflebih)
print('Self-emp-not-inc - <=50K = ',selfkurang)
print()

print('Probabilitas Education : ')
print('Bachelors - >50K = ',Bachelorslebih)
print('Bachelors - <=50K = ',Bachelorskurang)
print('HS-grad - >50K = ',hslebih)
print('HS-grad - <=50K = ',hskurang)
print('Some-college - >50K = ',collegelebih)
print('Some-college - <=50K = ',collegekurang)
print()

print('Probabilitas Marital-Status : ')
print('Divorced - >50K = ',divorcedlebih)
print('Divorced - <=50K = ',divorcedkurang)
print('Married-civ-spouse - >50K = ',marriedlebih)
print('Married-civ-spouse - <=50K = ',marriedkurang)
print('Never-married - >50K = ',neverlebih)
print('Never-married - <=50K = ',neverkurang)
print()

print('probabilitas Occupation : ')
print('Craft-repair - >50K = ',craftlebih)
print('Craft-repair - <=50K = ',craftkurang)
print('Exec-managerial - >50K = ',execlebih)
print('Exec-managerial - <=50K = ',execkurang)
print('Prof-specialty - >50K = ',proflebih)
print('Prof-specialty - <=50K = ',profkurang)
print()

print('probabilitas Relationship : ')
print('Husband - >50K = ',husbandlebih)
print('Husband - <=50K = ',husbandkurang)
print('Not-in-family - >50K = ',notlebih)
print('Not-in-family - <=50K = ',notkurang)
print('Own-child - >50K = ',ownlebih)
print('Own-child - <=50K = ',ownkurang)
print()

print('probabilitas Hours-per-week : ')
print('Low - >50K = ',lowlebih)
print('Low - <=50K = ',lowkurang)
print('Many - >50K = ',manylebih)
print('Many - <=50K = ',manykurang)
print('Normal - >50K = ',normallebih)
print('Normal - <=50K = ',normalkurang)
print()

#mencari probabilitas data TestSet :
for i in testSet.index:
    if testSet['age'][i] == 'young':
        x1 = younglebih ; y1 = youngkurang
    elif testSet['age'][i] == 'adult':
        x1 = adultlebih ; y1 = adultkurang
    elif testSet['age'][i] == 'old':
        x1 = oldlebih ; y1 = oldkurang

    if testSet['workclass'][i] == 'Local-gov':
        x2 = locallebih ; y2 = localkurang
    elif testSet['workclass'][i] == 'Private':
        x2 = privatelebih ; y2 = privatekurang
    elif testSet['workclass'][i] == 'Self-emp-not-inc':
        x2 = selflebih ; y2 = selfkurang

    if testSet['education'][i] == 'Bachelors':
        x3 = Bachelorslebih ; y3 = Bachelorskurang
    elif testSet['education'][i] == 'HS-grad':
        x3 = hslebih ; y3 = hskurang
    elif testSet['education'][i] == 'Some-college':
        x3 = collegelebih ; y3 = collegekurang

    if testSet['marital-status'][i] == 'Divorced':
        x4 = divorcedlebih ; y4 = divorcedkurang
    elif testSet['marital-status'][i] == 'Married-civ-spouse':
        x4 = marriedlebih ; y4 = marriedkurang
    elif testSet['marital-status'][i] == 'Never-married':
        x4 = neverlebih ; y4 = neverkurang

    if testSet['occupation'][i] == 'Craft-repair':
        x5 = craftlebih ; y5 = craftkurang
    elif testSet['occupation'][i] == 'Exec-managerial':
        x5 = execlebih ; y5 = execkurang
    elif testSet['occupation'][i] == 'Prof-specialty':
        x5 = proflebih ; y5 = profkurang

    if testSet['relationship'][i] == 'Husband':
        x6 = husbandlebih ; y6 = husbandkurang
    elif testSet['relationship'][i] == 'Not-in-family':
        x6 = notlebih ; y6 = notkurang
    elif testSet['relationship'][i] == 'Own-child':
        x6 = ownlebih ; y6 = ownkurang

    if testSet['hours-per-week'][i] == 'low':
        x7 = lowlebih ; y7 = lowkurang
    elif testSet['hours-per-week'][i] == 'many':
        x7 = manylebih ; y7 = manykurang
    elif testSet['hours-per-week'][i] == 'normal':
        x7 = normallebih ; y7 = normalkurang

    problebihdari = x1*x2*x3*x4*x5*x6*x7*lebih
    probkurangdari = y1*y2*y3*y4*y5*y6*y7*kurang

    #mencari nilai income dengan perbandingan
    if problebihdari > probkurangdari:
        hasil = '>50'
    elif probkurangdari > problebihdari:
        hasil = '<=50'

    #memasukan id dan income ke array hasil akhir
    hasilakhir.append([testSet['id'][i],hasil])
    #print(testSet['id'][i],problebihdari,probkurangdari,hasil)
print(hasilakhir)



df = pd.DataFrame(hasilakhir)       # Membuat dataFrame pandas dari data hasil akhir
#df.columns = ['id', 'income']       # mengubah nama kolom data
df = df.loc[:,1]#(hanya kolom income sesuai dgn aturan 1 kolom)
#Membuat excel pandas menggunakan XlsxWriter sebagai engine
writer = pd.ExcelWriter('TebakanTugas1ML.xlsx', engine='xlsxwriter')

df.to_excel(writer,'Sheet1',index=False,header=False)    # Convert dataframe ke excel tanpa index dan header
writer.save()   #tutup dan save excel