#!/usr/bin/python

from math import exp
def Logistic (x) : 
    return (1/(1+exp(-x))) 

def Probability (x) : 
    if x < 0 :
        return 0
    elif x > 1 :
        return 1
    else : 
        return x

def expression (Pclass, Sex, Age, SibSp, Parch) : 

    scaled_Pclass=2*(Pclass-1)/(3-1)-1
    scaled_Sex=2*(Sex-0)/(1-0)-1
    scaled_Age=2*(Age-0.42)/(80-0.42)-1
    scaled_SibSp=2*(SibSp-0)/(8-0)-1
    scaled_Parch=2*(Parch-0)/(6-0)-1
    principal_component_1=(0.174144*scaled_Pclass-0.977567*scaled_Sex-0.0929589*scaled_Age+0.012784*scaled_SibSp+0.0723318*scaled_Parch)
    principal_component_2=(-0.955178*scaled_Pclass-0.194197*scaled_Sex+0.189282*scaled_Age-0.100001*scaled_SibSp-0.0639964*scaled_Parch)
    principal_component_3=(0.237703*scaled_Pclass-0.0681695*scaled_Sex+0.78358*scaled_Age-0.387355*scaled_SibSp-0.4181*scaled_Parch)
    principal_component_4=(-0.0250865*scaled_Pclass-0.0154765*scaled_Sex-0.542755*scaled_Age-0.243607*scaled_SibSp-0.803246*scaled_Parch)
    principal_component_5=(-0.0133354*scaled_Pclass-0.041994*scaled_Sex+0.21668*scaled_Age+0.88343*scaled_SibSp-0.413111*scaled_Parch)
    y_1_1=Logistic(-0.368531
    +11.3222*principal_component_1
    -0.877315*principal_component_2
    -8.7558*principal_component_3
    -2.28413*principal_component_4
    -5.62623*principal_component_5)
    y_1_2=Logistic(-11.0111
    -0.570438*principal_component_1
    +4.23801*principal_component_2
    -11.7107*principal_component_3
    -0.676316*principal_component_4
    +5.74558*principal_component_5)
    y_1_3=Logistic(1.58462
    +5.36887*principal_component_1
    +5.83626*principal_component_2
    +0.274359*principal_component_3
    -2.18569*principal_component_4
    -3.27673*principal_component_5)
    y_1_4=Logistic(-4.16289
    +1.30645*principal_component_1
    +5.7809*principal_component_2
    -1.00453*principal_component_3
    +12.5563*principal_component_4
    -5.1772*principal_component_5)
    y_1_5=Logistic(2.429
    -1.75226*principal_component_1
    +1.78837*principal_component_2
    +0.435624*principal_component_3
    -0.873859*principal_component_4
    +3.99032*principal_component_5)
    y_1_6=Logistic(-1.41938
    +9.50652*principal_component_1
    -4.29089*principal_component_2
    +7.78106*principal_component_3
    +11.8989*principal_component_4
    -7.12249*principal_component_5)
    scaled_Survived=Logistic(11.4562
    -3.79782*y_1_1
    +7.16006*y_1_2
    -0.582109*y_1_3
    -8.85039*y_1_4
    -11.0061*y_1_5
    -7.26602*y_1_6)
    (Survived) = Probability(non_probabilistic_Survived)
    
    return Survived 
