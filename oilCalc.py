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

# this script calculates the refractive index of immersion oil needed to correct out spherical aberrations caused by the 
# early or late arrival (compared to the design specification of an objective lens) 
# of photons going in a straight line from an object a few microns deep embedded in 
# mounting media of known refractive index, under a coverslip of known thickness and
# refractive index, and then finally through a thickness of immersion oil of some 
# refractive index. Oil layer thickness is calculated from working distance (WD)  of lens,
# minus the cover glass thickness and object depth into the mounting medium, and we
# assume its the same in both the designed and aberrated cases. Nt sure thats right…
# and we also make no mention of numerical aperture of the lens… which is probably
# and important detail…

# equations 

# speed in medium = c/n = speed of light / refractive index
# time = distance . n / c

# model:
# time taken for photons to get from sample to lens surface should be the same
# for the reference design of a lens (design spec of coverglass and immersion oil, 
# and sample refractive index…)
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
                                                         c
# multiple out by c eliminates c, then rearranging to isolate RIoilneeded:

#                   objDepth.RIsampledes + covSlipThickdes.RIcsdes + (WD-objDepth-covSlipThickdes).RIoildes - objDepth.RIsamplereal - covSlipThickreal.RIcsreal
# RIoilneeded  =    -----------------------------------------------------------------------------------------------------------------------------------------
#								(WD-objDepth-covSlipThickreal)

 


