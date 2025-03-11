import pytest
import inspect
import importlib
from test.TestUtils import TestUtils
from urban_traffic_analysis_platform import (
    initialize_data,
    filter_by_congestion_level,
    filter_by_traffic_volume,
    filter_by_peak_hour,
    filter_by_incident_type,
    find_intersections_near_landmark,
    update_traffic_volume,
    update_congestion_level,
    add_incident_record,
    merge_intersection_data,
    calculate_congestion_distribution,
    calculate_total_traffic_volume,
    find_high_incident_areas,
    create_volume_brackets
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_variable_naming(test_obj):
    """Test that the required variable names and structure are used"""
    try:
        # Import the module
        module = importlib.import_module("urban_traffic_analysis_platform")

        # Check dictionary initialization
        init_source = inspect.getsource(module.initialize_data)
        assert "intersection_data = {" in init_source, "Initialize data must create intersection_data dictionary"
        assert "new_intersections = {" in init_source, "Initialize data must create new_intersections dictionary"
        
        # Check main function uses required data
        main_source = inspect.getsource(module.main)
        assert "intersection_data, new_intersections = initialize_data()" in main_source, "main() must initialize intersection data"
        
        # Check dictionary operation functions use correct parameter names
        assert "def filter_by_congestion_level(intersection_data, level)" in inspect.getsource(module), "filter_by_congestion_level() must use correct parameters"
        assert "def filter_by_traffic_volume(intersection_data, min_volume, max_volume)" in inspect.getsource(module), "filter_by_traffic_volume() must use correct parameters"
        assert "def merge_intersection_data(existing_intersections, new_intersections)" in inspect.getsource(module), "merge_intersection_data() must use correct parameters"
        
        # Verify predefined intersections in initialize_data
        intersection_data, _ = initialize_data()
        required_ids = ["I001", "I002", "I003", "I004", "I005"]
        assert all(id in intersection_data for id in required_ids), "Missing required intersection IDs"
        
        # Check specific intersection data
        assert intersection_data["I001"]["name"] == "Main & Broadway", "Incorrect name for I001"
        assert intersection_data["I004"]["congestion_level"] == "Critical", "Incorrect congestion level for I004"
        assert intersection_data["I005"]["traffic_volume"] == 600, "Incorrect traffic volume for I005"
        
        # Check new intersections
        _, new_intersections = initialize_data()
        required_new_ids = ["N001", "N002"]
        assert all(id in new_intersections for id in required_new_ids), "Missing required new intersection IDs"
        
        test_obj.yakshaAssert("test_variable_naming", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_variable_naming", False, "functional")
        pytest.fail(f"Variable naming test failed: {str(e)}")

def test_dictionary_operations(test_obj):
    """Test all dictionary operations"""
    try:
        # Test all filtering operations
        intersection_data, new_intersections = initialize_data()

        # Test filter_by_congestion_level
        filtered = filter_by_congestion_level(intersection_data, "High")
        assert len(filtered) == 1 and "I001" in filtered
        
        # Test filter_by_traffic_volume
        filtered = filter_by_traffic_volume(intersection_data, 1000, 2000)
        assert len(filtered) == 3 and "I001" in filtered and "I003" in filtered and "I004" in filtered
        
        # Modified peak hour test to use two separate filter operations
        filtered1 = filter_by_peak_hour(intersection_data, "07:00-09:00")
        filtered2 = filter_by_peak_hour(intersection_data, "08:00-09:00")
        assert "I001" in filtered1, "I001 should have peak hour 07:00-09:00"
        assert "I005" in filtered2, "I005 should have peak hour 08:00-09:00"
        
        # Test filter_by_incident_type
        filtered = filter_by_incident_type(intersection_data, "Accident")
        assert "I001" in filtered and "I003" in filtered
        
        # Test find_intersections_near_landmark
        filtered = find_intersections_near_landmark(intersection_data, "park")
        assert "I002" in filtered  # Central Park
        assert "I004" in filtered  # Industrial Park
        
        # Test update operations
        original_volume = intersection_data["I001"]["traffic_volume"]
        updated = update_traffic_volume(intersection_data, "I001", 1500)
        assert updated["I001"]["traffic_volume"] == 1500 and intersection_data["I001"]["traffic_volume"] == original_volume
        
        original_level = intersection_data["I002"]["congestion_level"]
        updated = update_congestion_level(intersection_data, "I002", "High")
        assert updated["I002"]["congestion_level"] == "High" and intersection_data["I002"]["congestion_level"] == original_level
        
        updated = add_incident_record(intersection_data, "I005", "Minor Accident")
        assert "Minor Accident" in updated["I005"]["incident_history"]
        assert not intersection_data["I005"]["incident_history"] or "Minor Accident" not in intersection_data["I005"]["incident_history"]
        
        # Test merge operation
        merged = merge_intersection_data(intersection_data, new_intersections)
        assert len(merged) == 7 and merged["N001"]["newly_added"] == True
        
        # Test statistics operations
        counts = calculate_congestion_distribution(intersection_data)
        assert counts["High"] == 1 and counts["Moderate"] == 1 and counts["Low"] == 1
        
        total = calculate_total_traffic_volume(intersection_data)
        expected_total = sum(intersection["traffic_volume"] for intersection in intersection_data.values())
        assert total == expected_total
        
        high_incidents = find_high_incident_areas(intersection_data, 1)
        assert "I001" in high_incidents and "I003" in high_incidents
        
        brackets = create_volume_brackets(intersection_data)
        assert "I005" in brackets["low"] and "I004" in brackets["high"]
        
        test_obj.yakshaAssert("test_dictionary_operations", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_dictionary_operations", False, "functional")
        pytest.fail(f"Dictionary operations test failed: {str(e)}")
        
def test_implementation_techniques(test_obj):
    """Test implementation of dictionary techniques"""
    try:
        # Check dictionary comprehension
        source = inspect.getsource(filter_by_congestion_level)
        assert "{" in source and "for" in source and "if" in source
        assert "in intersection_data.items()" in source or "items()" in source, "Dictionary comprehension must use .items()"
        
        # Check for dictionary comprehension in other functions
        volume_filter_source = inspect.getsource(filter_by_traffic_volume)
        assert "{" in volume_filter_source and "for" in volume_filter_source and "if" in volume_filter_source
        
        peak_filter_source = inspect.getsource(filter_by_peak_hour)
        assert "{" in peak_filter_source and "for" in peak_filter_source and "if" in peak_filter_source
        
        # Check dictionary methods
        source = inspect.getsource(calculate_congestion_distribution)
        assert ".values()" in source or ".items()" in source or ".keys()" in source
        
        # Check dictionary unpacking
        source1 = inspect.getsource(update_traffic_volume)
        source2 = inspect.getsource(merge_intersection_data)
        assert "**" in source1 and "**" in source2
        
        # Check dictionary unpacking for transformation
        assert "{**" in source1, "Dictionary unpacking must be used for transformation"
        
        # Check data immutability
        intersection_data, _ = initialize_data()
        intersection_id = "I001"
        original_volume = intersection_data[intersection_id]["traffic_volume"]
        updated = update_traffic_volume(intersection_data, intersection_id, original_volume + 1000)
        assert intersection_data[intersection_id]["traffic_volume"] == original_volume
        assert updated[intersection_id]["traffic_volume"] == original_volume + 1000
        
        # Check for proper copy() usage
        incident_source = inspect.getsource(add_incident_record)
        assert ".copy()" in incident_source, "Must use copy() to maintain immutability"
        
        # Check total volume calculation uses comprehension or generator
        total_source = inspect.getsource(calculate_total_traffic_volume)
        assert "sum(" in total_source and "for" in total_source
        
        # Check volume brackets implementation
        brackets_source = inspect.getsource(create_volume_brackets)
        assert "volume_brackets" in brackets_source and "for" in brackets_source and "if" in brackets_source
        
        test_obj.yakshaAssert("test_implementation_techniques", True, "functional")
    except Exception as e:
        test_obj.yakshaAssert("test_implementation_techniques", False, "functional")
        pytest.fail(f"Implementation techniques test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])