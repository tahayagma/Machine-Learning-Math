def compML():
    print("DİKKAT!! VERİLER ÖN İŞLEMDEN GEÇMİŞ OLMALIDIR.\nALGORİTMALAR PARAMETRESİZ OLARAK FİT EDİLMİŞTİR.\n\n")
    models = [MLPRegressor,LinearRegression,
              DecisionTreeRegressor,RandomForestRegressor,
              GradientBoostingRegressor,SVR,
             KNeighborsRegressor,Ridge,Lasso
             ]
    rmse = []
    for j in models:
        model = j().fit(X_train,y_train)
        y_pred = model.predict(X_test)
        RMSE = np.sqrt(mean_squared_error(y_test,y_pred))
        rmse.append(RMSE)
        print("{} algoritması RMSE değeri: {}\n".format(j.__name__,RMSE))
    print("En iyi değer:",pd.DataFrame(rmse).sort_values(by=0).iloc[0][0])
    
compML()

READ ME : BURADA VERİLER DIŞARIDAN(x,Y) GİRİLEBİLİR.
yada test_split işlemi fonksiyon içinde yapılabilir.
her bir algoritma için if-else ile daha detaylı işlemler yapılabilir.