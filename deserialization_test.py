import pickle

def vulnerable_deserialize(data):
    # Vulnerable to Insecure Deserialization
    obj = pickle.loads(data)
    return obj
