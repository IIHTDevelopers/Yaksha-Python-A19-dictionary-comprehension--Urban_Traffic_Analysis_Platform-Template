"""
Urban Traffic Analysis Platform
This program demonstrates dictionary operations through an urban traffic analysis system.
"""

def initialize_data():
    """
    Initialize the intersection data with predefined intersections using dictionaries.
    
    Returns:
        tuple: A tuple containing (intersection_data, new_intersections) dictionaries
    """
    # Create the main intersection data dictionary
    intersection_data = {
        "I001": {
            "name": "Main & Broadway",
            "coordinates": (40.7128, -74.0060),
            "traffic_volume": 1200,
            "congestion_level": "High",
            "peak_hours": ["07:00-09:00", "16:00-18:00"],
            "nearby_landmarks": ["Central Station", "City Hall", "Shopping Mall"],
            "incident_history": ["Accident", "Signal Failure"]
        },
        "I002": {
            "name": "Park & 5th",
            "coordinates": (40.7580, -73.9855),
            "traffic_volume": 800,
            "congestion_level": "Moderate",
            "peak_hours": ["07:30-09:30", "17:00-19:00"],
            "nearby_landmarks": ["Central Park", "Museum", "Office Complex"],
            "incident_history": ["Road Work"]
        },
        "I003": {
            "name": "River & Market",
            "coordinates": (40.7020, -74.0160),
            "traffic_volume": 1500,
            "congestion_level": "Severe",
            "peak_hours": ["07:00-10:00", "15:30-19:30"],
            "nearby_landmarks": ["Financial District", "Ferry Terminal", "Restaurant Row"],
            "incident_history": ["Accident", "Flooding", "Traffic Light Outage"]
        },
        "I004": {
            "name": "Highway Junction 42",
            "coordinates": (40.7310, -73.9980),
            "traffic_volume": 2000,
            "congestion_level": "Critical",
            "peak_hours": ["06:30-10:30", "15:00-20:00"],
            "nearby_landmarks": ["Shopping Center", "Industrial Park", "Residential Area"],
            "incident_history": ["Multiple Accidents", "Construction"]
        },
        "I005": {
            "name": "University & College",
            "coordinates": (40.7480, -74.0010),
            "traffic_volume": 600,
            "congestion_level": "Low",
            "peak_hours": ["08:00-09:00", "14:00-16:00"],
            "nearby_landmarks": ["University Campus", "Student Housing", "Sports Arena"],
            "incident_history": []
        }
    }
    
    # Create new intersections to be added later
    new_intersections = {
        "N001": {
            "name": "Airport Access Road",
            "coordinates": (40.6413, -73.7781),
            "traffic_volume": 1800,
            "congestion_level": "Severe",
            "peak_hours": ["05:00-07:00", "19:00-21:00"],
            "nearby_landmarks": ["International Terminal", "Parking Garage", "Hotel Zone"],
            "incident_history": ["Accident", "Road Work"]
        },
        "N002": {
            "name": "Harbor & Waterfront",
            "coordinates": (40.7023, -74.0190),
            "traffic_volume": 750,
            "congestion_level": "Moderate",
            "peak_hours": ["08:00-10:00", "16:30-18:30"],
            "nearby_landmarks": ["Ferry Terminal", "Tourist Area", "Restaurant District"],
            "incident_history": ["Pedestrian Incident"]
        }
    }
    
    return intersection_data, new_intersections

def filter_by_congestion_level(intersection_data, level):
    """
    Filter intersections by congestion level using dictionary comprehension.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        level (str): Congestion level to filter by
    
    Returns:
        dict: Filtered intersection dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if level is None:
        raise ValueError("Congestion level cannot be None")
    
    return {iid: intersection for iid, intersection in intersection_data.items() 
            if intersection["congestion_level"] == level}

def filter_by_traffic_volume(intersection_data, min_volume, max_volume):
    """
    Filter intersections by traffic volume range using dictionary comprehension.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        min_volume (int): Minimum traffic volume
        max_volume (int): Maximum traffic volume
    
    Returns:
        dict: Filtered intersection dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if min_volume is None or max_volume is None:
        raise ValueError("Volume range cannot be None")
    if min_volume < 0:
        raise ValueError("Minimum volume cannot be negative")
    if min_volume > max_volume:
        raise ValueError("Minimum volume cannot be greater than maximum volume")
    
    return {iid: intersection for iid, intersection in intersection_data.items() 
            if min_volume <= intersection["traffic_volume"] <= max_volume}

def filter_by_peak_hour(intersection_data, time_period):
    """
    Filter intersections by peak hour using dictionary comprehension.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        time_period (str): Time period to filter by (e.g., "07:00-09:00")
    
    Returns:
        dict: Filtered intersection dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if time_period is None:
        raise ValueError("Time period cannot be None")
    
    return {iid: intersection for iid, intersection in intersection_data.items() 
            if time_period in intersection["peak_hours"]}

def filter_by_incident_type(intersection_data, incident_type):
    """
    Filter intersections by incident type using dictionary comprehension.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        incident_type (str): Incident type to filter by
    
    Returns:
        dict: Filtered intersection dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if incident_type is None:
        raise ValueError("Incident type cannot be None")
    
    return {iid: intersection for iid, intersection in intersection_data.items() 
            if any(incident_type in incident for incident in intersection["incident_history"])}

def find_intersections_near_landmark(intersection_data, landmark):
    """
    Find intersections near a specific landmark.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        landmark (str): Landmark to search for
    
    Returns:
        dict: Filtered intersection dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if landmark is None:
        raise ValueError("Landmark cannot be None")
    
    return {iid: intersection for iid, intersection in intersection_data.items() 
            if any(landmark.lower() in l.lower() for l in intersection["nearby_landmarks"])}

def update_traffic_volume(intersection_data, intersection_id, new_volume):
    """
    Update an intersection's traffic volume.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        intersection_id (str): Intersection ID to update
        new_volume (int): New traffic volume
    
    Returns:
        dict: Updated intersection data dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if intersection_id is None:
        raise ValueError("Intersection ID cannot be None")
    if new_volume is None or new_volume < 0:
        raise ValueError("New volume cannot be None or negative")
    
    if intersection_id not in intersection_data:
        raise ValueError(f"Intersection ID {intersection_id} not found")
    
    # Create a new dictionary with the updated traffic volume
    updated_intersection_data = intersection_data.copy()
    updated_intersection_data[intersection_id] = {**updated_intersection_data[intersection_id], "traffic_volume": new_volume}
    
    return updated_intersection_data

def update_congestion_level(intersection_data, intersection_id, new_level):
    """
    Update an intersection's congestion level.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        intersection_id (str): Intersection ID to update
        new_level (str): New congestion level
    
    Returns:
        dict: Updated intersection data dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if intersection_id is None:
        raise ValueError("Intersection ID cannot be None")
    if new_level is None:
        raise ValueError("New congestion level cannot be None")
    
    valid_levels = ["Low", "Moderate", "High", "Severe", "Critical"]
    if new_level not in valid_levels:
        raise ValueError(f"Invalid congestion level. Must be one of {valid_levels}")
    
    if intersection_id not in intersection_data:
        raise ValueError(f"Intersection ID {intersection_id} not found")
    
    # Create a new dictionary with the updated congestion level
    updated_intersection_data = intersection_data.copy()
    updated_intersection_data[intersection_id] = {**updated_intersection_data[intersection_id], "congestion_level": new_level}
    
    return updated_intersection_data

def add_incident_record(intersection_data, intersection_id, incident):
    """
    Add an incident to an intersection's history.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        intersection_id (str): Intersection ID to update
        incident (str): New incident to add
    
    Returns:
        dict: Updated intersection data dictionary
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if intersection_id is None:
        raise ValueError("Intersection ID cannot be None")
    if incident is None or incident == "":
        raise ValueError("Incident cannot be None or empty")
    
    if intersection_id not in intersection_data:
        raise ValueError(f"Intersection ID {intersection_id} not found")
    
    # Create a new dictionary with the updated incident history
    updated_intersection_data = intersection_data.copy()
    if incident not in updated_intersection_data[intersection_id]["incident_history"]:
        updated_incidents = updated_intersection_data[intersection_id]["incident_history"].copy()
        updated_incidents.append(incident)
        updated_intersection_data[intersection_id] = {**updated_intersection_data[intersection_id], "incident_history": updated_incidents}
    
    return updated_intersection_data

def merge_intersection_data(existing_intersections, new_intersections):
    """
    Merge two intersection data dictionaries with transformation.
    
    Args:
        existing_intersections (dict): The existing intersection data dictionary
        new_intersections (dict): New intersections to add
    
    Returns:
        dict: Merged intersection data dictionary
    """
    if existing_intersections is None or new_intersections is None:
        raise ValueError("Intersection data dictionaries cannot be None")
    
    # Create a copy of the existing intersection data
    merged_intersection_data = existing_intersections.copy()
    
    # Add new intersections with a "newly_added" flag
    for iid, intersection in new_intersections.items():
        merged_intersection_data[iid] = {**intersection, "newly_added": True}
    
    return merged_intersection_data

def calculate_congestion_distribution(intersection_data):
    """
    Calculate the number of intersections at each congestion level.
    
    Args:
        intersection_data (dict): The intersection data dictionary
    
    Returns:
        dict: Dictionary with congestion levels as keys and counts as values
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    
    congestion_counts = {}
    for intersection in intersection_data.values():
        level = intersection["congestion_level"]
        if level in congestion_counts:
            congestion_counts[level] += 1
        else:
            congestion_counts[level] = 1
    
    return congestion_counts

def calculate_total_traffic_volume(intersection_data):
    """
    Calculate the total traffic volume across all intersections.
    
    Args:
        intersection_data (dict): The intersection data dictionary
    
    Returns:
        int: Total traffic volume
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    
    return sum(intersection["traffic_volume"] for intersection in intersection_data.values())

def find_high_incident_areas(intersection_data, threshold=1):
    """
    Find intersections with incidents above a threshold.
    
    Args:
        intersection_data (dict): The intersection data dictionary
        threshold (int): Minimum number of incidents
    
    Returns:
        dict: Dictionary of high incident intersections
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    if threshold < 0:
        raise ValueError("Threshold cannot be negative")
    
    return {iid: intersection for iid, intersection in intersection_data.items() 
            if len(intersection["incident_history"]) > threshold}

def create_volume_brackets(intersection_data):
    """
    Group intersections into traffic volume brackets.
    
    Args:
        intersection_data (dict): The intersection data dictionary
    
    Returns:
        dict: Dictionary with volume brackets as keys and lists of intersection IDs as values
    """
    if intersection_data is None:
        raise ValueError("Intersection data cannot be None")
    
    volume_brackets = {
        "low": [],       # 0-750
        "medium": [],    # 751-1500
        "high": [],      # 1501-2000
        "very_high": []  # 2001+
    }
    
    for iid, intersection in intersection_data.items():
        volume = intersection["traffic_volume"]
        if volume <= 750:
            volume_brackets["low"].append(iid)
        elif volume <= 1500:
            volume_brackets["medium"].append(iid)
        elif volume <= 2000:
            volume_brackets["high"].append(iid)
        else:  # volume > 2000
            volume_brackets["very_high"].append(iid)
    
    return volume_brackets


def get_formatted_intersection(iid, intersection):
    """
    Format an intersection for display.
    
    Args:
        iid (str): Intersection ID
        intersection (dict): Intersection data
    
    Returns:
        str: Formatted intersection string
    """
    if intersection is None:
        raise ValueError("Intersection data cannot be None")
    
    # Format traffic volume with thousands separator
    formatted_volume = f"{intersection['traffic_volume']:,}"
    
    # Format landmarks and incidents as comma-separated strings
    landmarks = ", ".join(intersection["nearby_landmarks"])
    incidents = ", ".join(intersection["incident_history"]) if intersection["incident_history"] else "None"
    peak_hours = ", ".join(intersection["peak_hours"])
    
    # Format the newly added flag if present
    newly_added = " [NEW]" if intersection.get("newly_added", False) else ""
    
    # Return formatted string
    return (
        f"{iid} | {intersection['name']}{newly_added} | Coordinates: {intersection['coordinates']} | "
        f"Traffic Volume: {formatted_volume} vph | Congestion: {intersection['congestion_level']} | "
        f"Peak Hours: {peak_hours} | Landmarks: {landmarks} | Incidents: {incidents}"
    )

def display_data(data, data_type):
    """
    Display formatted data based on data type.
    
    Args:
        data: Data to display (dict, tuple, etc.)
        data_type (str): Type of data being displayed
    """
    if data is None:
        print("No data to display.")
        return
    
    if data_type == "intersections" or data_type == "filtered":
        header = "\nCurrent Intersection Data:" if data_type == "intersections" else "\nFiltered Results:"
        print(header)
        
        if not data:
            print("No intersections to display.")
            return
        
        for iid, intersection in data.items():
            print(get_formatted_intersection(iid, intersection))
    
    elif data_type == "congestion_distribution":
        print("\nCongestion Level Distribution:")
        for level, count in data.items():
            print(f"{level}: {count} intersections")
    
    elif data_type == "volume_brackets":
        print("\nTraffic Volume Brackets:")
        for bracket, intersection_ids in data.items():
            print(f"{bracket}: {len(intersection_ids)} intersections")
            if intersection_ids:
                print(f"  Intersection IDs: {', '.join(intersection_ids)}")
    
    elif data_type == "high_incidents":
        print("\nHigh Incident Areas:")
        if not data:
            print("No high incident areas found.")
            return
        
        for iid, intersection in data.items():
            print(get_formatted_intersection(iid, intersection))
    
    elif data_type == "total_volume":
        print(f"\nTotal Traffic Volume Across All Intersections: {data:,} vehicles per hour")
    
    else:
        print(f"\n{data_type}:")
        print(data)

def main():
    """Main program function."""
    intersection_data, new_intersections = initialize_data()
    
    while True:
        # Show basic info about the data
        congestion_levels = set(intersection["congestion_level"] for intersection in intersection_data.values())
        
        print(f"\n===== URBAN TRAFFIC ANALYSIS PLATFORM =====")
        print(f"Total Intersections: {len(intersection_data)}")
        print(f"Congestion Levels: {', '.join(sorted(congestion_levels))}")
        
        print("\nMain Menu:")
        print("1. View Intersection Data")
        print("2. Filter Intersections")
        print("3. Update Intersection Data")
        print("4. Add New Intersections")
        print("5. View Traffic Statistics")
        print("0. Exit")
        
        choice = input("Enter your choice (0-5): ")
        
        if choice == "0":
            print("Thank you for using the Urban Traffic Analysis Platform!")
            break
        
        elif choice == "1":
            display_data(intersection_data, "intersections")
        
        elif choice == "2":
            print("\nFilter Options:")
            print("1. Filter by Congestion Level")
            print("2. Filter by Traffic Volume Range")
            print("3. Filter by Peak Hour")
            print("4. Filter by Incident Type")
            print("5. Find Intersections Near Landmark")
            filter_choice = input("Select filter option (1-5): ")
            
            if filter_choice == "1":
                level = input("Enter congestion level to filter by (Low, Moderate, High, Severe, Critical): ")
                filtered = filter_by_congestion_level(intersection_data, level)
                display_data(filtered, "filtered")
            
            elif filter_choice == "2":
                try:
                    min_volume = int(input("Enter minimum traffic volume: "))
                    max_volume = int(input("Enter maximum traffic volume: "))
                    filtered = filter_by_traffic_volume(intersection_data, min_volume, max_volume)
                    display_data(filtered, "filtered")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif filter_choice == "3":
                time_period = input("Enter peak hour to filter by (e.g., '07:00-09:00'): ")
                filtered = filter_by_peak_hour(intersection_data, time_period)
                display_data(filtered, "filtered")
            
            elif filter_choice == "4":
                incident_type = input("Enter incident type to filter by (e.g., 'Accident'): ")
                filtered = filter_by_incident_type(intersection_data, incident_type)
                display_data(filtered, "filtered")
            
            elif filter_choice == "5":
                landmark = input("Enter landmark to search for: ")
                filtered = find_intersections_near_landmark(intersection_data, landmark)
                display_data(filtered, "filtered")
            
            else:
                print("Invalid choice.")
        
        elif choice == "3":
            print("\nUpdate Options:")
            print("1. Update Traffic Volume")
            print("2. Update Congestion Level")
            print("3. Add Incident Record")
            update_choice = input("Select update option (1-3): ")
            
            if update_choice == "1":
                try:
                    iid = input("Enter intersection ID to update: ")
                    new_volume = int(input("Enter new traffic volume: "))
                    intersection_data = update_traffic_volume(intersection_data, iid, new_volume)
                    print(f"Traffic volume updated for intersection {iid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif update_choice == "2":
                try:
                    iid = input("Enter intersection ID to update: ")
                    print("Valid levels: Low, Moderate, High, Severe, Critical")
                    new_level = input("Enter new congestion level: ")
                    intersection_data = update_congestion_level(intersection_data, iid, new_level)
                    print(f"Congestion level updated for intersection {iid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif update_choice == "3":
                try:
                    iid = input("Enter intersection ID to update: ")
                    incident = input("Enter incident to add: ")
                    intersection_data = add_incident_record(intersection_data, iid, incident)
                    print(f"Incident added to intersection {iid}.")
                except ValueError as e:
                    print(f"Error: {e}")
            
            else:
                print("Invalid choice.")
        
        elif choice == "4":
            try:
                print("\nAdding new intersections to the database...")
                intersection_data = merge_intersection_data(intersection_data, new_intersections)
                print(f"{len(new_intersections)} new intersections added to database.")
                # Clear new_intersections after adding
                new_intersections = {}
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == "5":
            print("\nStatistics Options:")
            print("1. Congestion Level Distribution")
            print("2. Total Traffic Volume")
            print("3. High Incident Areas")
            print("4. Traffic Volume Brackets")
            stats_choice = input("Select statistics option (1-4): ")
            
            if stats_choice == "1":
                congestion_distribution = calculate_congestion_distribution(intersection_data)
                display_data(congestion_distribution, "congestion_distribution")
            
            elif stats_choice == "2":
                total_volume = calculate_total_traffic_volume(intersection_data)
                display_data(total_volume, "total_volume")
            
            elif stats_choice == "3":
                try:
                    threshold = int(input("Enter incident threshold (default 1): ") or "1")
                    high_incidents = find_high_incident_areas(intersection_data, threshold)
                    display_data(high_incidents, "high_incidents")
                except ValueError as e:
                    print(f"Error: {e}")
            
            elif stats_choice == "4":
                volume_brackets = create_volume_brackets(intersection_data)
                display_data(volume_brackets, "volume_brackets")
            
            else:
                print("Invalid choice.")
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()