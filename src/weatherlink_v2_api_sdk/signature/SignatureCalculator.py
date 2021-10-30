import collections
import hashlib
import hmac

class SignatureCalculator:

    def calculate_stations_signature(self, api_key, api_secret, api_request_timestamp, station_ids = []):
        parameters_to_hash = {
            "api-key": api_key,
            "t": api_request_timestamp
        }
        return calculate_signature(api_secret, parameters_to_hash)

    def calculate_signature(api_secret, parameters_to_hash):

        return ""