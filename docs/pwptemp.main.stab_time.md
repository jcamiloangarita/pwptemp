# pwptemp.main.stab_time(*well*) #

Calculate the stabilization time of the temperature profile.

> **Parameters:**
* **well: class** - NewWell instance from [pwptemp.input.set_well.md](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.input.set_well.md).

> **Returns:**

a **StabTime** instance with the following features:
* **.finaltime: int** - Stabilization time (when T average remains constant).
* **.tbot: list** - Temperatures at bottom values (every hour).
* **.tout: list** - Outlet temperatures (every hour).
* **.tfm: list** - Formation temperature.

## Example ##

```
>>> stabilization = pwptemp.main.stab_time(well)
>>> type(stabilization.finaltime)
<class 'int'>
>>> type(stabilization.tbot)
<class 'list'>
>>> type(stabilization.tout)
<class 'list'>
>>> type(stabilization.tfm)
<class 'list'>
```

See the [pwptemp.main](https://github.com/pro-well-plan/pwptemp/blob/master/docs/pwptemp.main.md) documentation.
