import unittest
from parameterized import parameterized

from weatherlink_v2_api_sdk.signature.signature_calculator import SignatureCalculator

class TestSignatureCalculator(unittest.TestCase):

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, "6fc5636eeccc766216d14887530b2a4adb7896d289dd710a59db40eacf76069d")
    ])
    def test_calculate_stations_signature_without_station_ids(self, api_key, api_secret, api_request_timestamp, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_stations_signature(api_key, api_secret, api_request_timestamp)
        self.assertEqual(expected_api_signature, api_signature)

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, [1234, 6789], "68b3f48d5660926e09b093a6ddb0d98f07dc06215daacbb4e9566339625c6f7d")
    ])
    def test_calculate_stations_signature_with_station_ids(self, api_key, api_secret, api_request_timestamp, station_ids, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_stations_signature(api_key, api_secret, api_request_timestamp, station_ids)
        self.assertEqual(expected_api_signature, api_signature)

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, "6fc5636eeccc766216d14887530b2a4adb7896d289dd710a59db40eacf76069d")
    ])
    def test_calculate_nodes_signature_without_node_ids(self, api_key, api_secret, api_request_timestamp, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_nodes_signature(api_key, api_secret, api_request_timestamp)
        self.assertEqual(expected_api_signature, api_signature)

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, [1234, 6789], "62517e3e306a3f39734fbdb141918edc2f32afc32295035f755984c1cf8cdabf")
    ])
    def test_calculate_nodes_signature_with_node_ids(self, api_key, api_secret, api_request_timestamp, node_ids, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_nodes_signature(api_key, api_secret, api_request_timestamp, node_ids)
        self.assertEqual(expected_api_signature, api_signature)

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, "6fc5636eeccc766216d14887530b2a4adb7896d289dd710a59db40eacf76069d")
    ])
    def test_calculate_sensors_signature_without_sensor_ids(self, api_key, api_secret, api_request_timestamp, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_sensors_signature(api_key, api_secret, api_request_timestamp)
        self.assertEqual(expected_api_signature, api_signature)

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, [1234, 6789], "4f66b360a2308e6022b9ed2ce603a4c048cf42a18b43461a42ac80e7b666d10d")
    ])
    def test_calculate_sensors_signature_with_sensor_ids(self, api_key, api_secret, api_request_timestamp, sensor_ids, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_sensors_signature(api_key, api_secret, api_request_timestamp, sensor_ids)
        self.assertEqual(expected_api_signature, api_signature)

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, "6fc5636eeccc766216d14887530b2a4adb7896d289dd710a59db40eacf76069d")
    ])
    def test_calculate_sensor_activity_signature_without_sensor_ids(self, api_key, api_secret, api_request_timestamp, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_sensor_activity_signature(api_key, api_secret, api_request_timestamp)
        self.assertEqual(expected_api_signature, api_signature)

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, [1234, 6789], "4f66b360a2308e6022b9ed2ce603a4c048cf42a18b43461a42ac80e7b666d10d")
    ])
    def test_calculate_sensor_activity_signature_with_sensor_ids(self, api_key, api_secret, api_request_timestamp, sensor_ids, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_sensor_activity_signature(api_key, api_secret, api_request_timestamp, sensor_ids)
        self.assertEqual(expected_api_signature, api_signature)

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, "6fc5636eeccc766216d14887530b2a4adb7896d289dd710a59db40eacf76069d")
    ])
    def test_calculate_sensor_catalog_signature(self, api_key, api_secret, api_request_timestamp, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_sensor_catalog_signature(api_key, api_secret, api_request_timestamp)
        self.assertEqual(expected_api_signature, api_signature)

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, 1234, "9a9d74b35761646ebf59856d18cf91c620ea263c67a910a39672d32edadda8c5")
    ])
    def test_calculate_current_signature(self, api_key, api_secret, api_request_timestamp, station_id, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_current_signature(api_key, api_secret, api_request_timestamp, station_id)
        self.assertEqual(expected_api_signature, api_signature)

    ##################################################

    @parameterized.expand([
        ("3l4raa5xl6xcgfkh5r5tdgnvbbb0d0zp", "ooxqc6n6cs4n74zyn6djgsz470bxsho1", 1633115254, 1234, 1633071600, 1633158000, "ddfd79473fa8aa7ff918147c4016faa86c18c3a54a9c2bbb632e92bcb09335b1")
    ])
    def test_calculate_historic_signature(self, api_key, api_secret, api_request_timestamp, station_id, start_timestamp, end_timestamp, expected_api_signature):
        signature_calculator = SignatureCalculator()
        api_signature = signature_calculator.calculate_historic_signature(api_key, api_secret, api_request_timestamp, station_id, start_timestamp, end_timestamp)
        self.assertEqual(expected_api_signature, api_signature)

