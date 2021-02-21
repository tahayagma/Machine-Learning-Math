#---------------ABSOLUTE DEVIATION (MUTLAK SAPMA) --------------------
'''data = 3,4,6,7,10#34,38,46,50,64,72,85,91
n = len(data) #number of data values
mX =sum(data)/n #average value
absolute_deviation = 0
for xi in data:
    absolute_deviation += (abs(xi-mX)/n)
print(absolute_deviation)'''


#---------------------------------------------
#-------------VARYANS (VARIANCE) VE STANDART SAPMA----------------------------
# anakütle(population) için varyans
                                                                            
'''data = 24,28,36,40,54,62,75,81
N = len(data)
mX = sum(data)/N
variance = 0
for xi in data:
    variance += (((xi-mX)**2)/N)
print("variance:",variance)
standart_deviation = pow(variance,1/2)
print("Sd:",standart_deviation)


# örneklem için

data = 24,28,36,40,54,62,75,81
n = len(data)
mX = sum(data)/n
variance = 0
for xi in data:
    #variance += (((xi-mX)**2)/n-1)
print("sample variance:",variance)
standart_deviation = pow(variance,1/2)
print("Sd:",standart_deviation)'''
#---------------------------------------------------------------
#----------------VARYASYON KATSAYISI(coefficient of variation)-----------------------------
'''xi = 3,4,5,6,7
yi = 2,8,10,12,13

xi_mean = sum(xi)/len(xi)
yi_mean = sum(yi)/len(yi)

xi_variance= 0
yi_variance = 0
for Xi in xi:
  xi_variance += (((Xi-xi_mean)**2)/len(xi))
for Yi in yi:
    yi_variance += (((Yi-yi_mean)**2)/len(yi))

standart_deviationX = pow(xi_variance,1/2)
standart_deviationY = pow(yi_variance,1/2)
cofficient_varianceX = (standart_deviationX/xi_mean)*100
cofficient_varianceY = (standart_deviationY/yi_mean)*100

print("Xi Coef Varaiance:",cofficient_varianceX)
print("Yi Coef Varaiance:",cofficient_varianceY)'''

#------------KOVARYANS (covariance)----------------
#anakütle(population) için

'''x = 5,6,7,8,9
y = 6,9,11,16,18
N = len(x) #number of data values
x_mean = (sum(x)/N) # mean of x
y_mean = (sum(y)/N) # mean of y

total=0 # this is +((xi-m(x)*(yi-m(y))
for xi,yi in zip(x,y):
    total += ((xi-x_mean)*(yi-y_mean))
                                                                      

population_covariance = total/N

sample_covariance = total/(N-1)
print("population_covariance:",population_covariance)
print("sample_covariance:",sample_covariance)'''
    
#--------------------------------------------------
#------------------KOLERASTON KATSAYISI (correlation coefficient)(KOVARYANS/STX.STY)------------------------

'''x = 30,32,25,20,36,32,35,28,12,20#10,15,16,22,25,28,29,40,45,50
y = 200,220,180,140,320,280,340,250,150,220#5,12,15,20,10,26,25,38,42,47
N = len(x) #number of data values
x_mean = (sum(x)/N) # mean of x
y_mean = (sum(y)/N) # mean of y

total=0 # this is +((xi-m(x)*(yi-m(y))
varianceX = 0
varianceY = 0
for xi,yi in zip(x,y):
    total += ((xi-x_mean)*(yi-y_mean))
    varianceX += (((xi-x_mean)**2)/N)
    varianceY += (((yi-y_mean)**2)/N)
                                                                      

population_covariance = total/N
standart_deviationX = pow(varianceX,1/2)
standart_deviationY = pow(varianceY,1/2)

correlation_coefficient = population_covariance/(standart_deviationX*standart_deviationY)
print("Ortalamalar:",x_mean,y_mean)
print("standart_deviationX:",standart_deviationX)
print("standart_deviationY:",standart_deviationY)
print("population_covariance:",population_covariance)
print("correlation_coefficient:",correlation_coefficient)'''
#-----------------------------------------------------------------

#----------------------KOLERASYON KATSAYISI(KENDİ FORMUL)--------
'''x = 30,32,25,20,36,32,35,28,12,20
y = 200,220,180,140,320,280,340,250,150,220
N = len(x) #number of data values
x_mean = (sum(x)/N) # mean of the values of the x-variable
y_mean = (sum(y)/N) # mean of the values of the y-variable

total = 0
total2 =0
total3 =0
for xi,yi in zip(x,y):
    total += (xi-x_mean)*(yi-y_mean)
    total2 += ((xi-x_mean)**2)
    total3 += ((yi-y_mean)**2)
r = total/pow((total2*total3),1/2) #correlation coefficient
print(r)
#--------------BELİRLİLİK KATSAYISI----------------------------------
print("Belirlilik Katsayısı:",pow(r,2))'''
#---------------SIRALAMA KOLERASYONU (RANKİNG CORRELATİON)----------------------------
#Ranking of importance by firms x and y among institutions A,B,C,D,E,F

'''x = 1,2,4,3,6,5 #Ranking by x
y = 2,1,6,3,5,4 #Ranking by y

n = len(x) # number of observations

di = 0 #difference between the two ranks of each observation
for xi,yi in zip(x,y):
    di += ((xi-yi)**2)

p = 1-((6*di)/(n*((n**2)-1))) #Spearman's rank correlation coefficient
print("Ranking Correlation:",p))'''
#----------------------------------------------------------------------------------
#----------------------REGRESYON ANALİZİ------------------------------------------
'''Xi= 30,32,25,20,36,32,35,28,12,20 # independent variable
Yi = 200,220,180,140,320,280,340,250,150,220 # dependent variable
n = len(Xi) # number of data points
x_mean = sum(Xi)/n
y_mean= sum(Yi)/n
# Let's first find the b1 b0 coefficients
total =0
x_total = 0
for xi,yi in zip(Xi,Yi):
    total += (xi-x_mean)*(yi-y_mean)
    x_total += ((xi-x_mean)**2)
b1 = total/x_total
b0 = y_mean-(b1*x_mean)
SSE = 0
for xî,y in zip(Xi,Yi):
    yû = b0+(b1*xî) # predicted values
    SSE += ((y-yû)**2)
MSE = SSE/n # mean squared error
RMSE = pow((SSE/n),1/2) # root mean squared error
print("MSE:",MSE)
print("RMSE:",RMSE)'''
#-------------------------------------------------------
#--------------MEDIAN(medyan(=ortanca) ÇEYREKLIK---------------------------------
'''X = 1,3,6,10,15,21,28,36,40,60,58,95,58,78,96,63,20,14,52,80
K = list(X)
n = len(X)
print("Len Data:",n)
if n%2 == 0:
    median = (K[(n//2)]+K[(n//2)-1])/2
    q1 = K[0:(n//2)]
    q1L = len(K[0:(n//2)])
    q3 = K[(n//2):]
    q3L = len(q3)
    if q3L%2==0 and q1L%2==0:
        Q1 = (K[(q1L//2)]+K[(q1L//2)-1])/2
        Q3 = (q3[(q3L//2)]+q3[(q3L//2)-1])/2
        IQR = Q3-Q1
        OutlierMin = Q1-(1.5*IQR)
        OutlierMax = Q3+(1.5*IQR)
        print("IQR:",IQR)
        print("OutlierMin:",OutlierMin)
        print("OutlierMax:",OutlierMax)
        print("Q1:",Q1)
        print("Q3:",Q3)
    print("Median(Q2) value:",median)
else:
    median = K[(n//2)]
    q1 = K[0:(n//2)]
    q1L = len(K[0:(n//2)])
    q3 = K[((n//2)+1):]
    q3L = len(q3)
    if q3L%2==0 and q1L%2==0:
        Q1 = (K[(q1L//2)]+K[(q1L//2)-1])/2
        Q3 = (q3[(q3L//2)]+q3[(q3L//2)-1])/2
        print("Q1:",Q1)
        print("Q3:",Q3)
        IQR = Q3-Q1
        OutlierMin = Q1-(1.5*IQR)
        OutlierMax = Q3+(1.5*IQR)
        print("IQR:",IQR)
        print("OutlierMin:",OutlierMin)
        print("OutlierMax:",OutlierMax)
    else:
        Q1 = q1[(q1L//2)]
        Q3 = q3[(q3L//2)]
        print("Q1:",Q1)
        print("Q3:",Q3)
        IQR = Q3-Q1
        OutlierMin = Q1-(1.5*IQR)
        OutlierMax = Q3+(1.5*IQR)
        print("IQR:",IQR)
        print("OutlierMin:",OutlierMin)
        print("OutlierMax:",OutlierMax)
    print("Median(Q2) value:",median)'''
    
#---------------skewness coefficient (çarpiklik katsaiyi)----------------------------
'''X = 10,15,22,26,31,40
N = len(X) # number of variables in the distribution
x_mean = sum(X)/N
m = list(X)
medianOdd = (m[N//2]+m[(N//2)-1])/2 # if n is odd (veri uzunlugu çift ise )
medianEven = m[(N//2)] # if n is even (veri uzunlugu tek ise)
variance = 0
for xi in X:
    variance += (((xi-x_mean)**2)/(N-1))

standart_deviation = pow(variance,1/2)
total = 0
for xi in X:
    total += (xi-x_mean)**3
skewness = round(total/((N-1)*(standart_deviation**3)))
print(skewness)
#---control------------------
if skewness>0:
    print("Dagilim saga çarpiktir.")
elif skewness<0:
    print("Dagilim sola çarpiktir.")
else:print("dagilim simetriktir.")
#--------------2. solution-----------------------
a = (3*(x_mean-medianOdd))/standart_deviation
print(a)'''
#------------------------BASIKLIK KAYSAYISI-------------------------
'''total =0
for xi in X:
    total += ((xi-x_mean)**4)/N

kurtosis = total/(standart_deviation**4)
print("normal:",kurtosis)
#kurtosis = 3 ise standart normal kurt>3 ise standart normalden daha dik
# kurtosis<3 ise standart normal dagilimdan daha basik'''
#--------------------------------------------------------

#----------------Z-Skoru (Z-Score)--------------------------------
# anakitle için
# sd-->Standart deviation
'''a = 125,100,200,130,154 # select 200
b = 12,58,95,63,20 # select 20

a_mean = sum(a)/len(a)
b_mean = sum(b)/len(b)

varianceA = 0
varianceB = 0
örneklem = 0
for ai,bi in zip(a,b):
    varianceA += (((ai-a_mean)**2)/len(a))
    varianceB += (((bi-b_mean)**2)/len(b))
    örneklem += (((ai-a_mean)**2)/(len(a)-1))

sdÖ = pow(örneklem,1/2)
sdA = pow(varianceA,1/2)
sdB = pow(varianceB,1/2)
Z_örneklem = (200-a_mean)/sdÖ
Z_scoreA = (200-a_mean)/sdA
Z_scoreB = (20-b_mean)/sdB

print("200 örneklem",Z_örneklem,örneklem)
print("200 Z-score:",Z_scoreA,varianceA)
print("20 Z-score:",Z_scoreB)'''
#-----------------------------------------------------------
#---------KOMBINASYON--------------------
'''def combi(n,x):
    fakN = 1
    b = n
    while b-(x-1)>1:
        fakN = fakN*b
        b -= 1
    
    fakX = 1
    a = n-x
    while a>1:
        fakX = fakX*a
        a-=1
    print("{}'in {} ile kombinasyonu: {}/{}".format(n,x,fakN,fakX))
    print("tam degeri:",fakN/fakX)
combi(7,2)'''
#----------------BINOM DAGILIM--------------------------
'''FORMUL = P(x) = (n)*(p**x)*(q**n-x)
                   (x)
p = bir denemedeki basari olasiligi
x = rasgele degiskenin aldigi deger
n = denemelerin sayisi
q = bir denemedeki basarisizlik olasiligi(1-p)

VARIACNE = n*P*q standart sapmasi ise varyansaýn karekökü


örnek: Hileli bir paranini tura gelme olasiligi 0,6 yazi gelmez olasiligi 0,4 olsun
bu para 5 kez atiliyor. iki kez yazi gelme olasiligi nedir?
n= 5
yazi gelme basari olasiligi = 0,4  (p)
tura gelme bararisizlik olasiligi = 0,6 (q)
rasgele degiskenimiz = 2 olacaktir.
'''
#Çözüm:
'''p = 0.07
n = 100
#q = 0.6 (1-p)
x = 6

def binom(n,x,p):
    q = 1-p
    fakN = 1
    b = n
    while b-(x-1)>1:
        fakN = fakN*b
        b -= 1
    
    fakX = 1
    a = n-x
    while a>1:
        fakX = fakX*a
        a-=1
    solution = (fakN/fakX)*(p**x)*(q**(n-x))*100
    variance = n*p*q
    sd = pow(variance,1/2)
    return round(solution,4)

    
print(binom(n,x,p))'''
#----------------------------------------
#-----------------ARALIK TAHMINI---------------------------
''' (1) populasyon varyansi biliniyorken (Z TABLOSU ILE)

formul = mean(x)-z(alfa/2)*standart_sapma/(n**(1/2))

alfa degeri = önem düzeyidir güven düzeyini tamamlayan degerdir.
ör: %90 güven düzeyinin alfa degeri %10 = 0.10 olur. 0.10/2= 0.05 cikar. 1-0.05 = 0.95 cikar ve bunu z tablosunda bulunmasi lazim  #    1.645
ör: %95 güven düzeyinin alfa degeri %5= 0.05 olur   # 1.96
ör: %99 güven düzeyinin alfa degeri %1 = 0.01 olur  # 2.575
ve bu alfa degerlerini yerine yazip(alfa/2) cikan degeri 1 den cikarip son degeri z tablosundan bulmaya çalisiriz.
ardindan yerine yazilip bulunur.'''

'''n= 25
st = 2 # population standart sapmasi biliniyorsa
#NOT : Eger populasyon st ve varyansi bilinmiyorsa populasyon st yerine örneklem st gelecektir.
alfa = 0.10
x_mean = 14.5

alt_sinir = x_mean-(1.645*(st/(n**(1/2))))
üst_sinir = x_mean+(1.645*(st/(n**(1/2))))
print("güven araligi:",alt_sinir,üst_sinir)'''
#-------------------------------------------------------------------------------
#----------------ÖRNEKLEM IcIN VARIACNE VE STANDART DEVIATON----------------------------
'''x = 29.5,30.5,28.6,31.6,27.9,28.1,28.5,28.7,30.3
n = len(x)
x_mean= sum(x)/n

variance =0
for xi in x:
    variance += ((xi-x_mean)**2)/(n-1)

standart_deviation = pow(variance,1/2)

print("Mean:",x_mean)
print("variance:",variance)
print("Standart Deviation:",standart_deviation)'''
#---------------------------------------------------------------------
#---------PEARSONS'S CORRELATION COEFFICIENT------------------------
'''x = 45,78,96,12,30
y = 36,58,78,10,12
x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)
total = 0
total1 = 0
total2 = 0
for xi,yi in zip(x,y):
    total += (xi-x_mean)*(yi-y_mean)
    total1 +=(xi-x_mean)**2
    total2 += (yi-y_mean)**2
r = total/(total1*total2)**(1/2)
print("Pearson correlation coefficient:",r)'''
    
#----------VARYANS ICIN GÜVEN ARALIGI BULMA-----------------------
'''Bir akü üreticisinin ürettigi ürünlerden rastgele 5 tanesi seçiliyor
Bu 5 akünün yasam suresi 1.9,2.4,3,3.5,4.2 yildir. Buna göre %95 güven düzeyi
araliginda varyans için aralýk bulunuz
'''
'''x = 1.9,2.4,3,3.5,4.2
n = len(x)
x_mean= sum(x)/n

variance = 0
for xi in x:
    variance += ((xi-x_mean)**2)/(n-1)
    
print("variance:",variance)
standart_deviation = (variance**(1/2))
print("st:",standart_deviation)
v = n-1  # serbestlik derecesi ( degree of freedom)
alfa = round(1-(0.95),2) # ki kare tablosunda orani bize verir.
chi_square_ki_kare  = alfa/2 ve serbestlik derecesi ile bulunur

lower_interval = v.variance/ki_kare degeri(alfa/2)
upper_interval = v.variance/ki_karedegeri (1-alfa/2)'''
