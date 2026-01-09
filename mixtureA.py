import warmth
import time

warmth = true
setFenchol = warmth

ethanol = 95%
lemonOil = 45.8mL
limeOil = 36.5mL
teaTreeOil = 8mL
cassiaCinnamonOil = 4.5mL
nutmegOil = 2.7mL
orangeOil = 1.2mL
corianderOil = 0.7mL
fenchol = 0.6ml

def concentratedMixtureA():
  mix(lemonOil + limeOil + teaTreeOil + cassiaCinnamoOil + nutmegOil + orangeOil + corianderOil + fenchol)
  time.sleep(100000)
  return concentratedMixtureA

concentratedMixtureA()

mix(concentratedMixtureA * 20.5mL + ethanol)
if (concentratedMixtureA * 20.5mL + ethanol) < 1L
  continue()
  mix()
  mix()
if (concentratedMixtureA * 20.5mL + ethanol) = 1L
  return(mixtureA)
  print("There's your Mixture A. You will only need 1mL of it for 1L of Coke")
if (concentratedMixtureA * 20.5mL + ethanol) > 1L
  return(sh_t)
  print("You have f_cked up")
  kill()
