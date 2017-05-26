#!/usr/bin/python

from math import exp
def Logistic (x) : 
    return (1/(1+exp(-x))) 

from math import tanh

def Binary (x) : 
    if x < 0.5 : 
        return 0
    else : 
        return 1

def expression (class, genero, idade, sibSp, fare, embarque) : 

    scaled_class=2*(class-1)/(3-1)-1
    scaled_genero=2*(genero-0)/(1-0)-1
    scaled_idade=2*(idade-0.42)/(80-0.42)-1
    scaled_sibSp=2*(sibSp-0)/(8-0)-1
    scaled_fare=2*(fare-0)/(263-0)-1
    scaled_embarque=2*(embarque-1)/(3-1)-1
    principal_component_1=(0.167793*scaled_class+0.984015*scaled_genero+0.0314632*scaled_idade+0.00393279*scaled_sibSp-0.0447321*scaled_fare+0.0235139*scaled_embarque)
    principal_component_2=(-0.946545*scaled_class+0.164488*scaled_genero+0.188384*scaled_idade-0.060181*scaled_sibSp+0.111046*scaled_fare-0.15986*scaled_embarque)
    principal_component_3=(0.142716*scaled_class-0.000456507*scaled_genero-0.0685629*scaled_idade+0.0916634*scaled_sibSp-0.0313991*scaled_fare-0.98262*scaled_embarque)
    principal_component_4=(-0.185384*scaled_class+0.0635026*scaled_genero-0.895013*scaled_idade+0.370035*scaled_sibSp+0.13902*scaled_fare+0.0655717*scaled_embarque)
    principal_component_5=(-0.0331777*scaled_class+0.0143431*scaled_genero-0.396323*scaled_idade-0.89479*scaled_sibSp-0.194966*scaled_fare-0.0544119*scaled_embarque)
    principal_component_6=(-0.141643*scaled_class-0.0204626*scaled_genero-0.0264701*scaled_idade+0.224467*scaled_sibSp-0.962987*scaled_fare+0.0329952*scaled_embarque)
    y_1_1=tanh(0.70843
    -0.186134*principal_component_1
    +0.0281128*principal_component_2
    +0.511943*principal_component_3
    +0.894281*principal_component_4
    +0.0176556*principal_component_5
    +0.145032*principal_component_6)
    y_1_2=tanh(0.0278978
    +1.47384*principal_component_1
    +0.721139*principal_component_2
    -0.0304542*principal_component_3
    -0.85876*principal_component_4
    +0.221852*principal_component_5
    -0.0824609*principal_component_6)
    y_2_1=tanh(-0.117602
    +0.0568724*y_1_1
    -1.55833*y_1_2)
    y_2_2=tanh(1.06225
    +1.75148*y_1_1
    -0.230258*y_1_2)
    y_2_3=tanh(-2.07899
    -0.28618*y_1_1
    -0.257921*y_1_2)
    y_3_1=tanh(-1.08781
    -0.929662*y_2_1
    -0.347269*y_2_2
    +0.569281*y_2_3)
    y_3_2=tanh(0.832094
    +0.0447198*y_2_1
    -0.160573*y_2_2
    +2.49534*y_2_3)
    y_3_3=tanh(-1.45593
    +0.558938*y_2_1
    -0.403865*y_2_2
    -0.469542*y_2_3)
    y_3_4=tanh(-1.29867
    -1.45801*y_2_1
    +1.78454*y_2_2
    +0.208229*y_2_3)
    y_4_1=tanh(-0.0675288
    -0.408917*y_3_1
    +0.622558*y_3_2
    -0.240507*y_3_3
    -1.11706*y_3_4)
    y_4_2=tanh(-1.39466
    -1.64782*y_3_1
    -0.961422*y_3_2
    +1.12958*y_3_3
    -1.46989*y_3_4)
    y_4_3=tanh(-0.173129
    -0.542896*y_3_1
    -0.1271*y_3_2
    +0.0634489*y_3_3
    +0.754925*y_3_4)
    y_4_4=tanh(-0.407504
    +0.359613*y_3_1
    -2.53859*y_3_2
    -0.913933*y_3_3
    +0.0199269*y_3_4)
    scaled_sobreviveu=Logistic(1.47929
    +1.11273*y_4_1
    +1.73023*y_4_2
    -0.841847*y_4_3
    -1.32199*y_4_4)
    (sobreviveu) = Binary(non_probabilistic_sobreviveu)
    
    return sobreviveu 
