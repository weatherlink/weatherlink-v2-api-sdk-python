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
        return self.calculate_signature(api_secret, parameters_to_hash)

    def calculate_signature(self, api_secret, parameters_to_hash):
        string_to_hash = ""
        for parameter_name in sorted(parameters_to_hash.keys()):
            string_to_hash = string_to_hash + parameter_name + str(parameters_to_hash[parameter_name])
        api_signature = hmac.new(api_secret.encode("UTF-8"), string_to_hash.encode("UTF-8"), hashlib.sha256).hexdigest()
        return api_signature
