import pytest
from test.TestUtils import TestUtils
from urban_traffic_analysis_platform import (
    initialize_data,
    filter_by_congestion_level,
    filter_by_traffic_volume,
    filter_by_peak_hour,
    filter_by_incident_type,
    update_traffic_volume,
    update_congestion_level,
    merge_intersection_data,
    create_volume_brackets
)

@pytest.fixture
def test_obj():
    return TestUtils()

def test_boundary_scenarios(test_obj):
    """Consolidated test for boundary scenarios"""
    try:
        # Test with empty intersection data
        empty_intersection_data = {}
        
        # Test filter functions with empty intersection data
        filtered = filter_by_congestion_level(empty_intersection_data, "High")
        assert filtered == {}, "Filtering empty intersection data should return empty dict"
        
        filtered = filter_by_traffic_volume(empty_intersection_data, 0, 2000)
        assert filtered == {}, "Filtering empty intersection data by volume should return empty dict"
        
        filtered = filter_by_peak_hour(empty_intersection_data, "07:00-09:00")
        assert filtered == {}, "Filtering empty intersection data by peak hour should return empty dict"
        
        filtered = filter_by_incident_type(empty_intersection_data, "Accident")
        assert filtered == {}, "Filtering empty intersection data by incident should return empty dict"
        
        # Test merge with empty intersection data
        _, new_intersections = initialize_data()
        merged = merge_intersection_data(empty_intersection_data, new_intersections)
        assert len(merged) == len(new_intersections), "Merging empty intersection data should only include new intersections"
        
        # Test with real intersection data
        intersection_data, _ = initialize_data()
        
        # Test traffic volume at exactly boundary values
        # Volume bracket boundaries are: 0-750, 751-1500, 1501-2000, 2001+
        test_intersection_data = {
            "T001": {"name": "Test Intersection 1", "traffic_volume": 0},
            "T002": {"name": "Test Intersection 2", "traffic_volume": 750},
            "T003": {"name": "Test Intersection 3", "traffic_volume": 751},
            "T004": {"name": "Test Intersection 4", "traffic_volume": 1500},
            "T005": {"name": "Test Intersection 5", "traffic_volume": 1501},
            "T006": {"name": "Test Intersection 6", "traffic_volume": 2000},
            "T007": {"name": "Test Intersection 7", "traffic_volume": 2001}
        }
        
        brackets = create_volume_brackets(test_intersection_data)
        assert "T001" in brackets["low"] and "T002" in brackets["low"], "Intersections with 0 and 750 volume should be low"
        assert "T003" in brackets["medium"] and "T004" in brackets["medium"], "Intersections with 751 and 1500 volume should be medium"
        assert "T005" in brackets["high"] and "T006" in brackets["high"], "Intersections with 1501 and 2000 volume should be high"
        assert "T007" in brackets["very_high"], "Intersections with 2001+ volume should be very_high"
        
        # Test update_traffic_volume with edge cases
        iid = "I001"
        updated = update_traffic_volume(intersection_data, iid, 0)
        assert updated[iid]["traffic_volume"] == 0, "Should allow setting traffic volume to exactly zero"
        
        # Test valid congestion level values
        levels = ["Low", "Moderate", "High", "Severe", "Critical"]
        for level in levels:
            updated = update_congestion_level(intersection_data, "I001", level)
            assert updated["I001"]["congestion_level"] == level, f"Should accept valid level: {level}"
        
        test_obj.yakshaAssert("TestBoundaryScenarios", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestBoundaryScenarios", False, "boundary")
        pytest.fail(f"Boundary scenarios test failed: {str(e)}")

def test_edge_case_filtering(test_obj):
    """Test filtering with edge case inputs"""
    try:
        intersection_data, _ = initialize_data()
        
        # Test merging empty dictionaries
        empty_dict = {}
        merged = merge_intersection_data(intersection_data, empty_dict)
        assert merged == intersection_data, "Merging empty dict into intersection_data should not change intersection_data"
        
        merged = merge_intersection_data(empty_dict, empty_dict)
        assert merged == {}, "Merging empty dicts should result in empty dict"
        
        # Test volume with exact range boundaries
        min_vol = intersection_data["I005"]["traffic_volume"]  # University & College with 600
        max_vol = intersection_data["I003"]["traffic_volume"]  # River & Market with 1500
        
        # Test with exact min/max values
        filtered = filter_by_traffic_volume(intersection_data, min_vol, max_vol)
        assert "I003" in filtered and "I005" in filtered, "Exact min/max volume values should be included"
        
        # Test with no match range
        filtered = filter_by_traffic_volume(intersection_data, 2100, 2500)
        assert len(filtered) == 0, "Should return empty dict for volume range with no matches"
        
        # Test filtering on unique values
        filtered = filter_by_congestion_level(intersection_data, "Critical")
        assert len(filtered) == 1 and "I004" in filtered, "Only one intersection has Critical congestion"
        
        # Test for unique peak hour
        filtered = filter_by_peak_hour(intersection_data, "08:00-09:00")
        assert "I005" in filtered, "University & College has peak hour 08:00-09:00"
        
        # Test filter with non-existent values
        filtered = filter_by_congestion_level(intersection_data, "Extreme")
        assert filtered == {}, "Filtering by non-existent level should return empty dict"
        
        filtered = filter_by_peak_hour(intersection_data, "12:00-13:00")
        assert filtered == {}, "Filtering by non-existent peak hour should return empty dict"
        
        filtered = filter_by_incident_type(intersection_data, "Earthquake")
        assert filtered == {}, "Filtering by non-existent incident should return empty dict"
        
        test_obj.yakshaAssert("TestEdgeCaseFiltering", True, "boundary")
    except Exception as e:
        test_obj.yakshaAssert("TestEdgeCaseFiltering", False, "boundary")
        pytest.fail(f"Edge case filtering test failed: {str(e)}")

if __name__ == '__main__':
    pytest.main(['-v'])