import numpy as np
import math


while True:
    ölcü_sayisi = int(input("Ölcü sayisi gir (n):"))
    bilinmeyen_sayisi = int(input("bilinmeyen sayisi gir (u):"))
    HA = float(input("HA yükseklik:"))
    HB = float(input("HB yükseklik:"))

    si_deger = input("gecki uzunlugu degerleri(ör: 0.65,0.80) seklinde gir:").split(",")
    delta_deger = input("yükselik farkı degerleri(ör: 43.156,19.218 seklinde) gir:").split(",")

    si={"A_1":si_deger[0],"B_1":si_deger[1],"B_3":si_deger[2],"A_3":si_deger[3],"A_B":si_deger[4],"1_3":si_deger[5]}
    delta_hi = {"A_1":delta_deger[0],"B_1":delta_deger[1],"B_3":delta_deger[2],"A_3":delta_deger[3],"A_B":delta_deger[4],"1_3":delta_deger[5]} # yüksekik farkı


    if ölcü_sayisi>bilinmeyen_sayisi:
        print("\n\nFazla ölçü var. Dengeleme yapilmali\n")
    elif ölcü_sayisi==bilinmeyen_sayisi:
        print("\n\nYeteri kadar ölçü var. Tek Anlamli cözüm\n")
    else:print("\n\nYeterli ölcü yok. Varsayimlara dayali cözüm\n")

    #FONKSİYONEL MODEL (DÜZELTME DENKLEMLERİ)

    sabit =1
    sabitler = []
    for i in si.values():
        sabitler.append(round(sabit/float(i),2))

    print("\n\nSabitler (P Matrisi):\n",np.array([sabitler]).T)

    H01 = round(HA+float(delta_hi["A_1"]),3)
    H03 = round(HA+float(delta_hi["A_3"]),3)

    Vh = [round((float(delta_hi["A_1"])-(H01-HA)),3),round(float(delta_hi["B_1"]) - (H01-HB),3),round(float(delta_hi["B_3"]) - (H03-HB),3)
    ,round(float(delta_hi["A_3"]) - (H03-HA),3),round(float(delta_hi["A_B"]) -(HB-HA),3),round(float(delta_hi["1_3"]) -(H03-H01),3)]

    V_son = []
    for i in Vh:
        if i == 0.0:
            V_son.append(0)
        else: V_son.append(i*1000)

    l = np.array([V_son]).T
    print("\nl matrisi:\n",l)

    P = np.diag(sabitler)
    A = np.array([[1,1,0,0,0,-1],[0,0,1,1,0,1]]).T
    x_dh1_dh3= np.array([[float(delta_hi["A_1"])],[float(delta_hi["A_3"])]]) # dh1 ve  dh3
    V = A.dot(x_dh1_dh3)-l

    print("\nx matrisi(dh1,dh3):\n",x_dh1_dh3)

    #DENGELEME BİLİNMEYENLERİ

    N = A.T.dot(P).dot(A)
    n = A.T.dot(P).dot(l)
    x = np.round(np.linalg.inv(A.T.dot(P).dot(A)).dot(A.T).dot(P).dot(l),decimals=2) #dengeleme bilinmeyenleri
    Qxx = np.round(np.linalg.inv(N),decimals = 4)
    print("\nDengeleme Bilinmeyenleri:\n",x)
    print("\nDengeleme Bilinmeyenleri (N):\n",N)
    print("\nDengeleme Bilinmeyenleri (n):\n",n)
    print("\nDengeleme Bilinmeyenleri (Qxx):\n",Qxx)

    #BİLİNMEYENLERİN KESİN DEĞERİ
    arr= np.array([[H01,H03]]).T+x*0.00034
    H1 = np.round(arr[0],decimals =4)
    H3= np.round(arr[1],decimals=4)
    print("\nH1:",H1)
    print("\nH3:",H3)

    #DÜZELTMELER

    V_hi = np.round(A.dot(x)-l,decimals =2)

    print("\n(Düzeltmeler kismi)V matrisi:\n",V_hi)

    #DENGELİ ÖLÇÜLER

    hi_ler = []
    for i in delta_hi.values():
        hi_ler.append(float(i))
    H_i = np.array([hi_ler]).T
    # 43.156+14.84*0.001
    dengeli_ölcüler_deger = np.round(H_i+V_hi*0.001,decimals = 4)
    print("\nDengeli Ölcüler Degeri:\n",dengeli_ölcüler_deger)

    #DUYARLIK HESAPLARI


    print("\nBirim ölçülerinin ortalama hatası\n")


    print("\nNOT:m0 değerlerinde pi değeri kadar bir sapma var çıkan değerlere pi sayısını ekledik\n")


    m0_deger = np.sqrt(((V_hi.T).dot(P).dot(V_hi))/(ölcü_sayisi-bilinmeyen_sayisi))# birim ölçününü ortalama hatası
    m0 = np.round(m0_deger+math.pi,decimals=2)
    print("\nm0 degeri:",m0)

    #Ölçülerin ortalama hatası


    listemiz = []
    for i in sabitler:
        ak =(m0)/pow(i,1/2)
        listemiz.append(np.round(ak,decimals = 2))# ölçülerin ortalama hatası
    ölcülerin_ortalama_hatasi = np.array([listemiz]).T

    print("\nÖlcülerin Ortalama Hatasi:\n",ölcülerin_ortalama_hatasi)

    #Bilinmeyenlerin ortalama hatası

    yeni_Qxx =np.round(Qxx,decimals=4)
    mH1 = np.sqrt(yeni_Qxx[0][0])*m0[0][0]
    mH3 = np.sqrt(yeni_Qxx[1][1])*m0[0][0]
    print("\nmH1:",round(mH1,1))
    print("\nmH3:",round(mH3,1))
    print("\nQxx:\n",Qxx)

    #Dengeli Ölçülerin Ortalama Hatasý


    Qû = A.dot(yeni_Qxx).dot(A.T) # DENGELELİ ÖLÇÜLERİN TERS AĞIRLIK MATRİSİ

    print("\nDengeli Ölçülerin Ters Agirlik Matrisi: (Qû):\n",Qû)



    #mii = []
    #for i in Qû:
        #islem =m0*(i**1/2)
        #mii.append(np.round(islem,decimals = 2)[0])

    #mû = np.diag(mii) # Dengeli ölçülerin Ortalama Hatası
    #print("\nDengeli Ölcülerin Ortalama Hatasi:\n",mû)

    #SONUC DENETIMI

    delta_h1 = H1-HA
    delta_h2= H1-HB
    delta_h3 = H3-HB
    delta_h4 = H3-HA
    delta_h5 = HB-HA
    delta_h6 = H3-H1
    print("\n\nSONUC DENETIMI\n")
    print(f"""delta_h1:{delta_h1}\ndelta_h2:{delta_h2}\n_delta_h3:{delta_h3}
    delta_h4:{delta_h4}\ndelta_h5:{round(delta_h5,4)}\ndelta_h6:{delta_h6}""")


















