import tkinter as tk
from tkinter import messagebox
from models.user import User
from models.geofence import Geofence
from models.ad import Ad
from utils.geofence_logic import get_relevant_ads
from utils.db_connection import create_connection
import threading
import time
from random import uniform



class LocationBasedAdsApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Location-Based Ads & Offers")

        # Logged-in user ID
        self.logged_in_user_id = None

        self.create_login_screen()

    def create_login_screen(self):
        """
        Create the login screen for both business and personal users.
        """
        self.clear_window()
        tk.Label(self.root, text="Location-Based Ads", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Email:").pack()
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        tk.Label(self.root, text="Login as:").pack()
        self.user_type_var = tk.StringVar(value="business")
        tk.Radiobutton(self.root, text="Business", variable=self.user_type_var, value="business").pack()
        tk.Radiobutton(self.root, text="Personal", variable=self.user_type_var, value="personal").pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=10)

    def login(self):
        """
        Handle login for business and personal users.
        """
        email = self.email_entry.get()
        password = self.password_entry.get()
        user_type = self.user_type_var.get()

        user = User.login(email, password)
        if user and user[4] == user_type:  # user[4] is the user_type
            self.logged_in_user_id = user[0]  # user[0] is the user ID
            messagebox.showinfo("Success", f"Welcome, {user[1]}!")  # user[1] is the username

            if user_type == "business":
                self.create_business_dashboard()
            elif user_type == "personal":
                self.create_personal_user_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials or user type.")

    def create_business_dashboard(self):
        """
        Create the dashboard for business users to manage geofences and ads.
        """
        self.clear_window()
        tk.Label(self.root, text="Business Dashboard", font=("Arial", 16)).pack(pady=10)

        tk.Button(self.root, text="Add Geofence and Ad", command=self.add_geofence_and_ad).pack(pady=5)
        tk.Button(self.root, text="View Geofences and Ads", command=self.view_geofences_and_ads).pack(pady=5)

    def create_personal_user_dashboard(self):
        """
        Create the dashboard for personal users to view offers.
        """
        self.clear_window()
        tk.Label(self.root, text="Personal User Dashboard", font=("Arial", 16)).pack(pady=10)

        # Enter location manually
        tk.Label(self.root, text="Enter Your Current Location (latitude, longitude):").pack(pady=5)
        self.latitude_entry = tk.Entry(self.root)
        self.latitude_entry.pack(pady=5)
        self.longitude_entry = tk.Entry(self.root)
        self.longitude_entry.pack(pady=5)

        tk.Button(self.root, text="Check for Offers", command=self.check_for_offers).pack(pady=10)

        # Simulate user movement
        tk.Button(self.root, text="Simulate Movement", command=self.simulate_user_movement).pack(pady=5)

        self.offers_text = tk.Text(self.root, width=50, height=15)
        self.offers_text.pack(pady=5)

    def add_geofence_and_ad(self):
        """
        Allow business users to add geofences and ads.
        """
        self.clear_window()
        tk.Label(self.root, text="Add Geofence and Ad", font=("Arial", 16)).pack(pady=10)

        # Geofence Inputs
        tk.Label(self.root, text="Geofence Center (latitude, longitude):").pack(pady=5)
        self.geo_lat_entry = tk.Entry(self.root)
        self.geo_lat_entry.pack(pady=5)
        self.geo_lon_entry = tk.Entry(self.root)
        self.geo_lon_entry.pack(pady=5)

        tk.Label(self.root, text="Radius (km):").pack(pady=5)
        self.geo_radius_entry = tk.Entry(self.root)
        self.geo_radius_entry.pack(pady=5)

        # Ad Inputs
        tk.Label(self.root, text="Ad Title:").pack(pady=5)
        self.ad_title_entry = tk.Entry(self.root)
        self.ad_title_entry.pack(pady=5)

        tk.Label(self.root, text="Ad Description:").pack(pady=5)
        self.ad_description_entry = tk.Entry(self.root)
        self.ad_description_entry.pack(pady=5)

        tk.Button(self.root, text="Add", command=self.save_geofence_and_ad).pack(pady=10)
        tk.Button(self.root, text="Back to Dashboard", command=self.create_business_dashboard).pack(pady=5)

    def save_geofence_and_ad(self):
        """
        Save the geofence and associated ad to the database.
        """
        try:
            # Geofence Inputs
            latitude = float(self.geo_lat_entry.get())
            longitude = float(self.geo_lon_entry.get())
            radius_km = float(self.geo_radius_entry.get())

            # Ad Inputs
            ad_title = self.ad_title_entry.get()
            ad_description = self.ad_description_entry.get()

            # Save Geofence
            geofence = Geofence(self.logged_in_user_id, latitude, longitude, radius_km)
            geofence.save_to_db()

            # Fetch the ID of the newly created geofence
            conn = create_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT last_insert_rowid()")
            geofence_id = cursor.fetchone()[0]
            conn.close()

            # Save Ad
            ad = Ad(geofence_id, ad_title, ad_description)
            ad.save_to_db()

            messagebox.showinfo("Success", "Geofence and Ad added successfully!")
            self.create_business_dashboard()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid geofence and ad details.")

    def view_geofences_and_ads(self):
        """
        Display all geofences and ads created by the business user.
        """
        self.clear_window()
        tk.Label(self.root, text="Your Geofences and Ads", font=("Arial", 16)).pack(pady=10)

        # Fetch Geofences and Ads
        geofences = Geofence.get_all_geofences()
        conn = create_connection()
        cursor = conn.cursor()

        for geofence in geofences:
            if geofence[1] == self.logged_in_user_id:  # Only show geofences created by this user
                tk.Label(self.root, text=f"Geofence ID: {geofence[0]}").pack()
                tk.Label(self.root, text=f"Center: ({geofence[2]}, {geofence[3]})").pack()
                tk.Label(self.root, text=f"Radius: {geofence[4]} km").pack()

                # Fetch ads for this geofence
                ads = Ad.get_ads_by_geofence(geofence[0])
                for ad in ads:
                    tk.Label(self.root, text=f"    Ad Title: {ad[2]}").pack()
                    tk.Label(self.root, text=f"    Description: {ad[3]}").pack()
                tk.Label(self.root, text="").pack()  # Blank line for spacing

        tk.Button(self.root, text="Back to Dashboard", command=self.create_business_dashboard).pack(pady=10)

    def check_for_offers(self):
        """
        Check for relevant ads based on the user's location using geofencing logic.
        """
        try:
            # Get user input for current location
            user_lat = float(self.latitude_entry.get())
            user_lon = float(self.longitude_entry.get())
            user_location = (user_lat, user_lon)

            # Fetch relevant ads
            ads = get_relevant_ads(user_location)
            self.offers_text.delete("1.0", tk.END)  # Clear previous offers

            if ads:
                for ad in ads:
                    self.offers_text.insert(tk.END, f"Ad Title: {ad['title']}\nDescription: {ad['description']}\n\n")
            else:
                self.offers_text.insert(tk.END, "No offers available in your area.\n")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid latitude and longitude.")

    def clear_window(self):
        """
        Clear the current window content.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        """
        Start the main loop of the application.
        """
        self.root.mainloop()

    def simulate_user_movement(self):
        """
        Simulate a user moving through random locations.
        """
        tk.Label(self.root, text="Simulated Movement Active", fg="blue").pack(pady=5)

        def move():
            while True:
                # Randomly generate new user location
                user_lat = uniform(40.7000, 40.8000)  # Latitude range near NYC
                user_lon = uniform(-74.1000, -73.9000)  # Longitude range near NYC
                user_location = (user_lat, user_lon)

                # Fetch relevant ads
                ads = get_relevant_ads(user_location)
                self.offers_text.delete("1.0", tk.END)  # Clear previous offers

                if ads:
                    for ad in ads:
                        self.offers_text.insert(tk.END,
                                                f"Ad Title: {ad['title']}\nDescription: {ad['description']}\n\n")
                else:
                    self.offers_text.insert(tk.END, "No offers available in your area.\n")

                # Wait for 5 seconds before the next movement
                time.sleep(5)

        # Run movement simulation in a separate thread
        threading.Thread(target=move, daemon=True).start()

if __name__ == "__main__":
    app = LocationBasedAdsApp()
    app.run()
