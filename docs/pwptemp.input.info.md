# pwptemp.input.info(*about='all'*) #

Get information about the parameters involved.

> **Parameters:**
*  **about:** *string, default 'all'*
    - 'casings': parameters related to casings/riser
    - 'conditions': parameters related to simulation conditions
    - 'heatcoeff': parameters related to heat coefficients
    - 'densities': parameters related to densities
    - 'operational': parameters related to the operation
    - 'all': all the parameters

> **Returns:**

Print the information related with the parameters.

## Example ##

```
>>> pwptemp.wellpath.info(about='operational')
Use the ID of a parameter to change the default value (e.g. tdict['tin']=30 to change the fluid inlet temperature from the default value to 30° Celsius)
Notice that the information is provided as follows:
parameter ID: general description, units

PARAMETERS RELATED TO THE OPERATION
tin: fluid inlet temperature, °C
q: flow rate, m3/h
rpm: revolutions per minute
t: torque on the drill string, kN*m
tbit: torque on the bit, kN*m
wob: reight on bit, kN
rop: rate of penetration, m/h
an: area of the nozzles, m2
```

See the [pwptemp.input](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.md) documentation.
