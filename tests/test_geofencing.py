from models.geofence import Geofence
from models.ad import Ad

def test_geofence_creation():
    """
    Testing the creation of a geofence and saving to the database.
    """
    geofence = Geofence(1, 40.7128, -74.0060, 5.0)  # Business ID: 1, Lat/Long: NYC, Radius: 5km
    geofence.save_to_db()
    print("Geofence created successfully!")

def test_ad_creation():
    """
    Testing the creation of an ad and saving to the database.
    """
    ad = Ad(1, "50% Off!", "Get 50% off all items this weekend.")  # Geofence ID: 1
    ad.save_to_db()
    print("Ad created successfully!")

def test_fetch_geofences_and_ads():
    """
    Testing fetching geofences and ads from the database.
    """
    geofences = Geofence.get_all_geofences()
    print("All Geofences:", geofences)

    ads = Ad.get_ads_by_geofence(1)  # Assuming Geofence ID: 1
    print("Ads for Geofence 1:", ads)

if __name__ == "__main__":
    test_geofence_creation()
    test_ad_creation()
    test_fetch_geofences_and_ads()
