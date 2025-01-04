# Location-Based Advertising Platform

## Overview  
The **Location-Based Advertising Platform** is an innovative solution designed to connect businesses with potential customers based on geographic location. By utilizing geofencing technology, businesses can define virtual boundaries for specific areas and associate targeted advertisements with them. When users enter these geofenced regions, they receive personalized offers or ads either automatically through GPS tracking or manually by providing their location.

## Features  
1. **Account Creation and Login**: Users can create an account or log in by entering their email and password. They can log in either as:
   - **Business Owners**: Owners who manage geofences and ads.
   - **Customers**: Shop owners who want to display their ads.  
2. **Add Geofence and Ad**: Allows business owners to:
   - Add geofence center by specifying latitude and longitude.
   - Define the radius of the geofence.
   - Provide ad details such as title and description.
   - Use buttons to save the geofence and ad or return to the dashboard.
3. **Business Dashboard**: Features buttons for:
   - Adding geofences and ads.
   - Viewing geofences and ads.
   - Viewing analytics.
   - Logging out.

## Dashboard Previews  
Below are snapshots of the platform's functionalities:  

1. **Account Creation/Login Tab**  
   - Users can log in as a business owner or customer by entering their email and password.  

   ![Account Creation/Login Tab](https://github.com/komal803/LOCATION-BASED-ADS-OFFER/blob/main/login_tab.jpg) <!-- Replace with your image path -->

2. **Add Geofence and Ad Tab**  
   - Users can define geofences by entering:
     - Latitude and longitude of the geofence center.
     - Radius for the geofence.
     - Ad title and description.  
   - Two buttons at the bottom allow saving the geofence and ad or returning to the dashboard.  

   ![Add Geofence and Ad Tab](assets/img/add-geofence.jpg) <!-- Replace with your image path -->

3. **Business Dashboard Tab**  
   - Business owners can access three primary functionalities:
     - **Add Geofence and Ad**.
     - **View Geofences and Ads**.
     - **View Analytics**.  
   - A "Logout" button is also available.  

   ![Business Dashboard Tab](assets/img/business-dashboard.jpg) <!-- Replace with your image path -->

## Analytics  
The platform provides insightful bar graphs for analytics:

1. **Geofence Usage Statistics**  
   - **X-axis**: Geofence IDs.  
   - **Y-axis**: Usage count.  

   ![Geofence Usage Statistics](assets/img/geofence-usage.jpg) <!-- Replace with your image path -->

2. **Ad Views**  
   - **X-axis**: Ad categories (e.g., Manhattan Fine Dining, Hoboken Coffee Special, Metropark Deals).  
   - **Y-axis**: Number of views.  

   ![Ad Views](assets/img/ad-views.jpg) <!-- Replace with your image path -->

## Technologies Used  
- **Programming Language**: Python  
- **Database**: SQLite  
- **Frameworks/Libraries**: Tkinter, Folium, Matplotlib, Geopy  
- **APIs**: Google Maps Geolocation API  

## Materials and Methods  
The platform is built on the following key technologies:  
- **Python** for core application logic and development.  
- **SQLite** for efficient and lightweight database management.  
- **Tkinter** for developing user-friendly graphical interfaces.  
- **Folium** for creating interactive maps and geofence visualizations.  
- **Matplotlib** for generating analytical graphs.  
- **Geopy** for handling geolocation data.  
- **Google Maps Geolocation API** for accurate location tracking and geofencing.

## Future Enhancements  
- **Advanced Analytics**: Incorporate heatmaps and real-time ad performance monitoring.  
- **Mobile App Support**: Develop a mobile app for improved accessibility and user engagement.  
- **AI Recommendations**: Implement AI for delivering personalized, targeted ads.  
- **Dynamic Geofencing**: Adapt geofences dynamically based on user density and events.


