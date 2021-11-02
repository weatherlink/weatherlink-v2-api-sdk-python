import hashlib
import hmac

class SignatureCalculator:

    def calculate_stations_signature(self, api_key, api_secret, api_request_timestamp, station_ids = []):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(station_ids) > 0:
            parameters_to_hash["station-ids"] = ",".join(map(str, station_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_nodes_signature(self, api_key, api_secret, api_request_timestamp, node_ids = []):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(node_ids) > 0:
            parameters_to_hash["node-ids"] = ",".join(map(str, node_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_sensors_signature(self, api_key, api_secret, api_request_timestamp, sensor_ids = []):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(sensor_ids) > 0:
            parameters_to_hash["sensor-ids"] = ",".join(map(str, sensor_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_sensor_activity_signature(self, api_key, api_secret, api_request_timestamp, sensor_ids = []):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(sensor_ids) > 0:
            parameters_to_hash["sensor-ids"] = ",".join(map(str, sensor_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_sensor_catalog_signature(self, api_key, api_secret, api_request_timestamp):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_current_signature(self, api_key, api_secret, api_request_timestamp, station_id):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp,
            "station-id": station_id
        }
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_historic_signature(self, api_key, api_secret, api_request_timestamp, station_id, start_timestamp, end_timestamp):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp,
            "station-id": station_id,
            "start-timestamp": start_timestamp,
            "end-timestamp": end_timestamp
        }
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def __calculate_signature(self, api_secret, parameters_to_hash):
        string_to_hash = ""
        for parameter_name in sorted(parameters_to_hash.keys()):
            string_to_hash = string_to_hash + parameter_name + str(parameters_to_hash[parameter_name])
        api_signature = hmac.new(api_secret.encode("UTF-8"), string_to_hash.encode("UTF-8"), hashlib.sha256).hexdigest()
        return api_signature