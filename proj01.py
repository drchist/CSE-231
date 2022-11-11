#############################################
#
# CSE 231 Project 01
# 
# Convert a distance in rods to ↓
# 1 rod = 5.0292 meters
# 1 furlong = 40 rods
# 1 mile = 1609.34 meters
# 1 foot = 0.3048 meters
# Avg. Walking Speed = 3.1 MPH
# Print out all conversions rounded 3 as well as minutes to walk 
# 
# r is input of rods
# time(t) for walk in minutes = r * 5.0292 * 60 / 1909.34 / 3.1
# 
#############################################

r = input( "Input rods: " )

dist_rod = float( r )
dist_met = dist_rod * 5.0292
dist_fee = dist_met / 0.3048
dist_mil = dist_met / 1609.34
dist_fur = dist_rod / 40
t = dist_mil * 60 / 3.1

print( "You input", dist_rod, "rods." )
print( " " )
print( "Conversions" )
print( "Meters:", round( dist_met,3 ) )
print( "Feet: ", round( dist_fee, 3 ) ) #Extra Space
print( "Miles:", round( dist_mil,3 ) )
print( "Furlongs:", round( dist_fur,3 ) )
print( "Minutes to walk", dist_rod,"rods:", round( t,3 ) )
