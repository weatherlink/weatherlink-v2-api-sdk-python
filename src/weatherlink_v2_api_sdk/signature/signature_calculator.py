import hashlib
import hmac

class SignatureCalculator:
    """A collection of API Signature calculation functions.

        Typical usage example:

        ```
        sc = SignatureCalculator()
        api_signature = sc.calculate_stations_signature(api_key, api_secret, timestamp)
        ```
    """

    def calculate_stations_signature(self, api_key: str, api_secret: str, api_request_timestamp: int, station_ids: list[int] = []) -> str:
        """Computes the API Signature for an API call to /stations given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made
            station_ids: integer list of up to 100 station ID numbers

        Returns:
            The API Signature string
        """
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(station_ids) > 0:
            parameters_to_hash["station-ids"] = ",".join(map(str, station_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_nodes_signature(self, api_key: str, api_secret: str, api_request_timestamp: int, node_ids: list[int] = []) -> str:
        """Computes the API Signature for an API call to /nodes given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made
            node_ids: integer list of up to 100 node ID numbers

        Returns:
            The API Signature string
        """
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(node_ids) > 0:
            parameters_to_hash["node-ids"] = ",".join(map(str, node_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_sensors_signature(self, api_key: str, api_secret: str, api_request_timestamp: int, sensor_ids: list[int] = []) -> str:
        """Computes the API Signature for an API call to /sensors given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made
            sensor_ids: integer list of up to 100 sensor ID numbers

        Returns:
            The API Signature string
        """
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(sensor_ids) > 0:
            parameters_to_hash["sensor-ids"] = ",".join(map(str, sensor_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_sensor_activity_signature(self, api_key: str, api_secret: str, api_request_timestamp: int, sensor_ids: list[int] = []) -> str:
        """Computes the API Signature for an API call to /sensor-activity given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made
            sensor_ids: integer list of up to 100 sensor ID numbers

        Returns:
            The API Signature string
        """
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        if len(sensor_ids) > 0:
            parameters_to_hash["sensor-ids"] = ",".join(map(str, sensor_ids))
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_sensor_catalog_signature(self, api_key: str, api_secret: str, api_request_timestamp: int) -> str:
        """Computes the API Signature for an API call to /sensor-catalog given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made

        Returns:
            The API Signature string
        """
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_current_signature(self, api_key: str, api_secret: str, api_request_timestamp: int, station_id: int) -> str:
        """Computes the API Signature for an API call to /current given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made
            station_id: the station ID

        Returns:
            The API Signature string
        """
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp,
            "station-id": station_id
        }
        return self.__calculate_signature(api_secret, parameters_to_hash)

    def calculate_historic_signature(self, api_key: str, api_secret: str, api_request_timestamp: int, station_id: int, start_timestamp: int, end_timestamp: int) -> str:
        """Computes the API Signature for an API call to /historic given the specific parameters.

        Args:
            api_key: the API Key
            api_secret: the API Secret
            api_request_timestamp: the Unix timestamp for when the API request is being made
            station_id: the station ID
            start_timestamp: the Unix timestamp marking the beginning of the time window for the data requested
            end_timestamp: the Unix timestamp marking the end of the time window for the data requested

        Returns:
            The API Signature string
        """
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