import json

import joblib

import send_results

MODEL_PATH = "model.joblib"
VALID_FEATURES = [
    "brk",
    "mmap",
    "readlink",
    "access",
    "openat",
    "newfstatat",
    "close",
    "read",
    "pread64",
    "arch_prctl",
    "set_tid_address",
    "set_robust_list",
    "rseq",
    "mprotect",
    "prlimit64",
    "munmap",
    "getrandom",
    "futex",
    "stat",
    "sysinfo",
    "lseek",
    "getdents64",
    "fcntl",
    "fstat",
    "ioctl",
    "rt_sigaction",
    "dup",
    "geteuid",
    "getuid",
    "getegid",
    "getgid",
    "write",
    "exit_group",
    "+++ exited with 2 +++",
    "label",
]


def transform_json_to_instance(json_data):
    # Sostituisci gli apici singoli con apici doppi
    json_data = json_data.replace("'", '"')
    # Converti la stringa JSON in un dizionario Python
    data_dict = json.loads(json_data)
    # Crea una lista vuota per l'istanza
    instance = []
    # Per ogni attributo nell'ordine definito sopra, aggiungi il valore corrispondente alla lista
    for attribute in VALID_FEATURES:
        if attribute in data_dict:
            instance.append(data_dict[attribute])
        else:
            instance.append(0)  # Aggiungi 0 se l'attributo non è presente
    # Restituisci l'istanza come lista
    return instance


def predict_instance(model_path, instance):
    model = joblib.load(model_path)
    prediction = model.predict([instance])
    print("PREDICTION: " + str(prediction[0]))
    return prediction[0]


def receive_data(data):
    print("Received: " + str(data) + "\n")
    data = data.split(">, ")[1].split(")")[0]
    print(data)
    instance = transform_json_to_instance(data)
    prediction = predict_instance(MODEL_PATH, instance)
    if prediction == 1:
        result = "System Violation"
        send_results.send_data(data, result)
    elif prediction == 0:
        result = "Correct Invocation"
        send_results.send_data(data, result)
