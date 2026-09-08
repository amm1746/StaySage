# downloads the raw AirBNB files for every city, runs once

import urllib.request

from staysage import config

def download_file(url, save_to):
    # downloads one file unless it already exists
    if save_to.exists():
        print("already have ", save_to.name)
        return True

    if "PASTE" in url:
        print("SKIPPED - no link filled in yet")
        return False

    print("Donwloading", save_to.name, "...")
    try:
        urllib.request.urlretrieve(url, save_to)
    except Exception as error:
        print("FAILED: ", error)
        return False

    size_mb = save_to.stat().st_size / 1_000_000
    print("Saved ", save_to.name, "-", round(size_mb, 1), "MB")
    return True

def main():
    succeeded = []
    failed = []

    for city_key, city in config.CITIES.items():
        print(city["name"])

        got_listings = download_file(
            city["listings_url"], config.listings_path(city_key)
        )
        got_calendar = download_file(
            city["calendar_url"], config.calendar_path(city_key)
        )

        if got_listings and got_calendar:
            succeeded.append(city_key)
        else:
            failed.append(city_key)

    print()
    print("Downloaded: ", len(succeeded), " cities")
    if failed:
        print("Failed: ", ", ".join(failed))

if __name__ == "__main__":
    main()