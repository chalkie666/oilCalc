#!/usr/bin/python

#****************************************************************************
#*                                                                          *
#*                          immersion oil calculator v0.1                        *
#*                                                                          *
#*                         Copyright 2014 Dan White                   *
#*                                                                          *				
#****************************************************************************

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# this script attempt to calculate the refractive index of immersion oil needed 
# to correct out spherical aberrations caused by the 
# early or late arrival (compared to the design specification of an objective lens) 
# of photons going in a straight line from an object a few microns deep embedded in 
# mounting media of known refractive index, under a coverslip of known thickness and
# refractive index, and then finally through a thickness of immersion oil of some 
# refractive index. Oil layer thickness is calculated from working distance (WD)  of lens,
# minus the cover glass thickness and object depth into the mounting medium, and we
# assume its the same in both the designed and aberrated cases. Not sure thats right
# and we also make no mention of numerical aperture of the lens, which is probably
# an important detail. Or does it end up being the same due to trigonometry?
# 
# Rather than using fancy physics and complex equations to work this out, we take a
# simple approach of assuming the spherical aberration is caused by the difference in 
# optical path in ideal designed scenario vs. real abberated situations. 
# (optical path length is the distance the photon "feels" it went, 
# which is just a clever way of saying the time it takes the photon to travel
# dependent on the real distance and the regractive indices of the stuff photons go
# through - that is to say the different speed of light in different media) 
# We only consider photons travelling is a straight line from the object emitting
# light to the lens front surface. 
# So far we make no calculations about photons going in other directions, 
# which is perhaps required. So this might all be totally wrong!!! 

# equations 

# speed in medium = c/n = speed of light / refractive index
# time = distance . n / c

# model:
# time taken for photons to get from sample to lens surface should be the same
# for the reference design of a lens (design spec of coverglass and immersion oil, 
# and sample refractive index)
# AND for some other case with different sample refractive index and/or coverslip 
# and or refractive index immersion oil. 

# simple algebra then tells us the right immersion oil refractive index to use 
# in order to correct a wrong refractive index sample with object at a certain depth
# and some wrong cover glass thickness.

# time designed = timewrongsample

# time = timeinsample + time in cover glass + time in immersion oil

# timeinsample = objectDepthFromCoverslip . sampleRefractiveIndex / c
# times for other layers are calculated the same way: distance.RI/c

# so
# timeDesign = objDepth.RIsampledes + covSlipThickdes.RIcsdes + (WD-objDepth-covSlipThickdes).RIoildes
#             ----------------------------------------------------------------------------------------
#                                                          c

# likewise
# timeWrongSample = objDepth.RIsamplereal + covSlipThickreal.RIcsreal + (WD-objDepth-covSlipThickreal).RIoilneeded
#                   -----------------------------------------------------------------------------------------------
#                                                         c
# multiple out by c eliminates c, then rearranging to isolate RIoilneeded:

#                 objDepth.RIsampledes + covSlipThickdes.RIcsdes + (WD-objDepth-covSlipThickdes).RIoildes - objDepth.RIsamplereal - covSlipThickreal.RIcsreal
# RIoilneeded  =    -----------------------------------------------------------------------------------------------------------------------------------------
#								(WD-objDepth-covSlipThickreal)



# here we set the values fopr all the physical variables descrbing the 
# optical setup the lens is designed for and the actual, real optical setup 
# we need to compensate for using some refractive index immersion oil or other 

# distances in micrometers, refractive index is dimensionless

RIoilneeded          =  0.00   # refractive index of immersion oil needed compensate for the sample: the goal!
objDepth             =  5.00   # distance of object emitting light, from the coverslip / mounting media interface. 
RIsampledes          =  1.5255 # refractive index of the sample and/or mounting medium, according to lens design, eg 1.52
covSlipThickdes      =  170.0  # cover slip glass thickness by lens design, typically 170 micrometers
RIcsdes              =  1.5255 # refractive index of coverslip in lens design, eg 1.52, 1.5255 plus minus 0.0015 at 541 nm, or 1.5230 at 589.3 nm, Abbe value, ve 55.from http://www.menzel.de/fileadmin/Templates/Menzel/pdf/en/Produktinfo_Deckglas_englisch_01.pdf
WD                   =  (150.0+covSlipThickdes)  # lens working distance - lens dependent, look it up on the manufactuer website, eg http://microscope.olympus-global.com/uis2/en/plapon60xo/
RIoildes             =  1.515  # refractive index of immersion oil used in lens design, as provided by manufacturer of the lens. Olympus oil for 60x1.42 is 1.515. 
RIsamplereal         =  1.42   # real refractive index of the sample and/or mounting medium, eg water is 1.33, glycerol 1.47, 50% glycerol 1.42.
covSlipThickreal     =  170.0  # real coverslip thickness, hopefully exactly 170 micrometers, might be something else.
RIcsreal             =  1.5255 # real refractive index of the coverslip glass, eg 1.52

# the equation to calculate the refractive index of the immersion oil 
# to compensate for the spherical aberration caused by the sample.

RIoilneeded = ( (objDepth*RIsampledes) + (covSlipThickdes*RIcsdes) + ((WD-objDepth-covSlipThickdes)*RIoildes) - (objDepth*RIsamplereal) - (covSlipThickreal*RIcsreal) ) / (WD-objDepth-covSlipThickreal)

print "RI of immersion oil to correct SA is " + str(RIoilneeded)
print "object depth is " + str(objDepth)
print "RI of sample is "+ str(RIsamplereal)
print "real coverslip thickness is "+ str(covSlipThickreal)



