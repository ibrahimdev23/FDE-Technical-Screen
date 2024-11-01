
Sort packages into appropriate stacks based on volume and mass.
    
Input:
width (float): Package width in centimeters
height (float): Package height in centimeters
length (float): Package length in centimeters
mass (float): Package mass in kilograms
    
Output:
Returns str: Stack name ('STANDARD', 'SPECIAL', or 'REJECTED')

The function works in the following steps:
- Calculate volume
- Determine if the package is bulky or heavy 
- Determine the return category based on heaviness and bulkiness of packages.

