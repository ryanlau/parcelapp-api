import json

import requests
from rich.console import Console
from rich.table import Table


class Parcel:
    def __init__(self, token, request_url=None):
        self.token = token
        self.request_url = request_url
        self.headers = {
            "cookie": f"token={self.token}; language=en",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Safari/537.36",
            "content-type": "application/x-www-form-urlencoded",
        }

    def add(self, description, tracking_number, courier):
        data = f"name={description}&number={tracking_number}&courier={courier}&postcode=&lang=en"

        r = requests.post(
            "https://web.parcelapp.net/add-ajax.php", headers=self.headers, data=data
        )

        return r.text

    def remove(self, tracking_number, courier):
        data = f"number={tracking_number}&type={courier}"

        r = requests.post(
            "https://web.parcelapp.net/delete-ajax.php", headers=self.headers, data=data
        )

        return r.text

    def fetch(self, request_url=None, table=False):
        if request_url is None:
            request_url = self.request_url

        parcels = requests.get(request_url, headers=self.headers)

        parcels = json.loads(parcels.text.split("(", 1)[1][:-1])

        parcels = parcels[0]

        if table is True:
            table = Table(title="Parcels")
            table.add_column("ID")
            table.add_column("Estimated Delivery Date")
            table.add_column("Parcel Name")
            table.add_column("Tracking Number")
            table.add_column("Status")

            i = 1

            for parcel in parcels:
                if parcel[5] == "":
                    if "delivered" in parcel[4][0][0].lower():
                        parcel[5] = "Delivered"
                    else:
                        parcel[5] = "No estimated date"
                else:
                    parcel[5] = parcel[5].split(" ")[0]

                table.add_row(str(i), parcel[5], parcel[1], parcel[0], parcel[4][0][0])
                i += 1
            console = Console()
            console.print(table)

        return parcels
