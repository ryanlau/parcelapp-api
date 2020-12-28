# parcelapp_api

This is an unofficial python API for interacting with the [Parcel app](https://parcelapp.net/). This API currently supports adding, removing, and listing parcels.

### Setup

Add [parcelapp_api.py](https://raw.githubusercontent.com/rynlu/parcelapp_api/main/parcelapp_api.py) to your package directory and import the Parcel class with the following line:

```python
from parcelapp_api import Parcel
```

### Initialization
```python
# request url arg can be left out if you only intend on adding and removing parcels
parcels = Parcel("TOKEN", "REQUEST URL")
```

### Usage
```python
print(parcels.add("DESCRIPTION", "TRACKING NUMBER", "CARRIER CODE"))
> ADDED

print(parcels.remove("TRACKING NUMBER", "CARRIER CODE"))
> SUCCESS

# returns list of all parcels and is able to display parcels in a rich-formatted table, request url arg can be left out if defined during initialization
print(parcels.fetch("REQUEST URL", table=True))
```

### Obtaining Token, Request URL, and Carrier Codes 
Your token can be found in your [web dashboard](https://web.parcelapp.net/) cookies:

![token_guide](https://cdn.discordapp.com/attachments/480736870540771329/790386685787504690/unknown.png)

Your request URL can be found through your Network tab of DevTools. Open the Network tab and then visit the [web dashboard](https://web.parcelapp.net/) on your browser. Look for a request with the name of `data.php?...` and click on it to get the Request URL. 

![request_url_guide](https://media.discordapp.net/attachments/480736870540771329/792793847712972840/unknown.png)

The carrier codes for USPS, UPS, and FedEx are `usps`, `ups`, and `fedex` respectively. Additional carrier codes can be found [here](https://ryanlau.dev/carriercodes).
