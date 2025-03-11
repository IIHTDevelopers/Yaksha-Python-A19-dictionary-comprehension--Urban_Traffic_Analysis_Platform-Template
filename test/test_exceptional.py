import pytest
from test.TestUtils import TestUtils
from urban_traffic_analysis_platform import *

@pytest.fixture
def test_obj():
    return TestUtils()

def test_input_validation(test_obj):
    """Consolidated test for input validation and error handling"""
    try:
        # Test with None inputs for critical functions
        functions_to_test = [
            (filter_by_congestion_level, [None, "High"]),
            (filter_by_congestion_level, [{"I001": {}}, None]),
            (filter_by_traffic_volume, [None, 100, 1000]),
            (filter_by_traffic_volume, [{"I001": {}}, None, 1000]),
            (filter_by_traffic_volume, [{"I001": {}}, 100, None]),
            (filter_by_peak_hour, [None, "07:00-09:00"]),
            (filter_by_peak_hour, [{"I001": {}}, None]),
            (filter_by_incident_type, [None, "Accident"]),
            (filter_by_incident_type, [{"I001": {}}, None]),
            (find_intersections_near_landmark, [None, "Park"]),
            (find_intersections_near_landmark, [{"I001": {}}, None]),
            (update_traffic_volume, [None, "I001", 1000]),
            (update_traffic_volume, [{"I001": {}}, None, 1000]),
            (update_traffic_volume, [{"I001": {}}, "I001", None]),
            (update_congestion_level, [None, "I001", "High"]),
            (update_congestion_level, [{"I001": {}}, None, "High"]),
            (update_congestion_level, [{"I001": {}}, "I001", None]),
            (add_incident_record, [None, "I001", "New Incident"]),
            (add_incident_record, [{"I001": {}}, None, "New Incident"]),
            (add_incident_record, [{"I001": {}}, "I001", None]),
            (merge_intersection_data, [None, {"N001": {}}]),
            (merge_intersection_data, [{"I001": {}}, None]),
            (calculate_congestion_distribution, [None]),
            (calculate_total_traffic_volume, [None]),
            (find_high_incident_areas, [None]),
            (create_volume_brackets, [None]),
            (get_formatted_intersection, ["I001", None])
        ]
        
        # Test all functions with None inputs
        for func, args in functions_to_test:
            with pytest.raises(ValueError):
                func(*args)
        
        # Test with invalid parameter values
        intersection_data = {
            "I001": {
                "name": "Test Intersection",
                "coordinates": (40.7128, -74.0060),
                "traffic_volume": 1000,
                "congestion_level": "High",
                "peak_hours": ["07:00-09:00"],
                "nearby_landmarks": ["Test Landmark"],
                "incident_history": ["Test Incident"]
            }
        }
        
        # Test negative min_volume
        with pytest.raises(ValueError):
            filter_by_traffic_volume(intersection_data, -100, 1000)
        
        # Test min_volume > max_volume
        with pytest.raises(ValueError):
            filter_by_traffic_volume(intersection_data, 2000, 1000)
        
        # Test negative traffic volume
        with pytest.raises(ValueError):
            update_traffic_volume(intersection_data, "I001", -10)
        
        # Test invalid intersection_id
        with pytest.raises(ValueError):
            update_traffic_volume(intersection_data, "INVALID", 1000)
        
        # Test invalid congestion level
        with pytest.raises(ValueError):
            update_congestion_level(intersection_data, "I001", "Not A Level")
        
        # Test empty incident
        with pytest.raises(ValueError):
            add_incident_record(intersection_data, "I001", "")
        
        # Test find_high_incident_areas with negative threshold
        with pytest.raises(ValueError):
            find_high_incident_areas(intersection_data, -1)
        
        test_obj.yakshaAssert("TestInputValidation", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestInputValidation", False, "exception")
        pytest.fail(f"Input validation test failed: {str(e)}")

def test_data_integrity(test_obj):
    """Test data integrity and immutability"""
    try:
        # Setup intersection data with specific conditions for testing
        intersection_data = {
            "I001": {
                "name": "Test Intersection",
                "coordinates": (40.7128, -74.0060),
                "traffic_volume": 1000,
                "congestion_level": "High",
                "peak_hours": ["07:00-09:00"],
                "nearby_landmarks": ["Test Landmark"],
                "incident_history": ["Test Incident"]
            }
        }
        
        # Test handling missing fields in intersection data
        invalid_intersection_data = {
            "I001": {
                "name": "Invalid Intersection"
                # Missing required fields
            }
        }
        
        # Should raise exception when accessing missing fields
        with pytest.raises(Exception):
            filter_by_congestion_level(invalid_intersection_data, "High")
        
        with pytest.raises(Exception):
            filter_by_traffic_volume(invalid_intersection_data, 0, 2000)
        
        # Test immutability - original intersection_data should not change
        original_volume = intersection_data["I001"]["traffic_volume"]
        updated_data = update_traffic_volume(intersection_data, "I001", 2000)
        assert intersection_data["I001"]["traffic_volume"] == original_volume, "Original intersection_data should not be modified"
        assert updated_data["I001"]["traffic_volume"] == 2000, "New intersection_data should have updated volume"
        
        original_level = intersection_data["I001"]["congestion_level"]
        updated_data = update_congestion_level(intersection_data, "I001", "Moderate")
        assert intersection_data["I001"]["congestion_level"] == original_level, "Original intersection_data should not be modified"
        assert updated_data["I001"]["congestion_level"] == "Moderate", "New intersection_data should have updated level"
        
        original_incidents = intersection_data["I001"]["incident_history"].copy()
        updated_data = add_incident_record(intersection_data, "I001", "New Incident")
        assert intersection_data["I001"]["incident_history"] == original_incidents, "Original intersection_data should not be modified"
        assert "New Incident" in updated_data["I001"]["incident_history"], "New intersection_data should have new incident"
        
        # Test adding duplicate incident (should not add)
        existing_incident = intersection_data["I001"]["incident_history"][0]
        updated_data = add_incident_record(intersection_data, "I001", existing_incident)
        assert len(updated_data["I001"]["incident_history"]) == len(intersection_data["I001"]["incident_history"]), "Duplicate incident should not be added"
        
        # Test with real intersection data
        test_data, new_data = initialize_data()
        original_test_data = test_data.copy()
        
        # Attempt modifications should create new lists/tuples
        filtered_data = filter_by_congestion_level(test_data, "High")
        assert test_data == original_test_data, "Original test_data should not be modified"
        
        sorted_data = filter_by_traffic_volume(test_data, 1000, 2000)
        assert test_data == original_test_data, "Original test_data should not be modified"
        
        # Test new intersections integration
        combined = merge_intersection_data(test_data, new_data)
        assert test_data == original_test_data, "Original test_data should not be modified"
        assert len(combined) == len(test_data) + len(new_data)
        
        # Test newly_added flag is set on merged intersections
        for iid in new_data:
            assert combined[iid].get("newly_added") == True, "Newly added intersections should have newly_added flag"
        
        test_obj.yakshaAssert("TestDataIntegrity", True, "exception")
    except Exception as e:
        test_obj.yakshaAssert("TestDataIntegrity", False, "exception")
        pytest.fail(f"Data integrity test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])