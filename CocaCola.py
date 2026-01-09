import scale      #  +/- 0.01 g
import micropipette      #  1000 µL
import cylinder      #  50 mL
import bottles      #  1 L
import heatResistantBeakers

mixtureA = "7X Flavor" * 1mL
mixtureB = "Water-based Mixture" * 10mL
sugar = 104g
carbonatedWater = H2O + CO2

def mix():
    mix(mixtureA + mixtureB + sugar + carbonatedWater)
    return CocaCola

setHeatResistantBeaker()
mix()
print("1 liter o' CocaCola")
