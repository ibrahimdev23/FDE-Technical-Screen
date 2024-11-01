
def sort(width, height, length, mass):

  # Calculate volume
  volume = width * height * length

  # Check if package is bulky
  is_bulky = (volume >= 1_000_000 or 
              width >= 150 or 
              height >= 150 or 
              length >= 150)

  # Check if package is heavy
  is_heavy = mass >= 20

  # if statements to determine stack based on criteria
  if is_bulky and is_heavy:
      return "REJECTED"
  elif is_bulky or is_heavy:
      return "SPECIAL"
  else:
      return "STANDARD"


# Test cases

#width = 150, is_bulky and mass > 20 should return REJECTED 
print(sort(150,50,80,90))

#volume >= 1_000_000, is_bulky should return SPECIAL
print(sort(100,100,100,15))

#mass = 22, is_heavy should return SPECIAL
print(sort(70,90,90,30))

#volume < 1_000_000, is_bulky and mass < 20 should return STANDARD
print(sort(40,30,20,10))

#Testing edge cases:
# Edge case where volume is exatly at the bulky threshold, returns SPECIAL 
print(sort(100, 100, 100, 10))
        
# Edge case where mass is exactly at the heavy hreshold, returns SPECIAL 
print(sort(50, 40, 30, 20))
        