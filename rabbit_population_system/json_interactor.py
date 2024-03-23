import random
failure_probability = 0.8 # Initial failure probability

def raise_random_exception_with_probability(json_func,record = None,massanger = None):
    global failure_probability
    while True:
        try:
            if random.random() < failure_probability:
                print('failure_probability', failure_probability)
                if failure_probability < 1.0:  # Cap the failure probability at 100%
                    failure_probability += 0.05  # Increase failure probability
                print('failure_probability after: ', failure_probability)
                # Raise a random exception
                random_exception = random.choice([
                    FileNotFoundError,
                    PermissionError,
                    IsADirectoryError,
                    FileExistsError,
                    NotADirectoryError,
                    IOError
                ])
                raise random_exception("Random exception raised")
            else:
                if record:
                    json_func(record,massanger)
                else:
                    return json_func()
                break
        except Exception as e:
            print('Exception occurred:', e)
            # Reset failure probability upon failure
            failure_probability = 0.5
            # Continue to the next iteration of the loop
            continue


