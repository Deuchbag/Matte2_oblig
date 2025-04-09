import numpy as np

#Blir feil etter 15 itterasjoner, altså når h = 1*10**(-15)
for i in range(1,20):
    h = 1*10**(-i)
    f = (np.exp(1.5+h)- np.exp(1.5-h))/(2*h)
    print(f, i)

    """
    Dersom vi ser på taylorrekken, så kan det bli sett at den første verdien vi får, er den rette/sanne verdien for den deriverte, og jo
    mindre h er, jo mindre blir feilleddet. Dette er derimot kun til et visst punkt, fordi etter rundt 10**(-15) vil vi få avrundingsfeiler
    som påvirker svaret. Svaret kan dermed bli sett å øke, og presisjonen minker. Forskjellen mellom de to metodene, er simpelt nok
    at i oppgave 1 vil feilen være proposjonal med h, mens i oppgave 2 vil feilen være proposjonal med h**2. Formelen i oppgave 2 vil dermed
    ha en feil som synker mye raskere, og vi kommer til svaret på færre steg
    """
    