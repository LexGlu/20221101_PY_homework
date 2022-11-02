def test_print():
    # Alexa Siri Bixby
    print('Alexa', 'Siri', 'Bixby')

    # Alexa ==> Siri ==> Bixby
    print('Alexa', 'Siri', 'Bixby', sep=' ==> ')

    # Alexa Siri Bixby!
    print('Alexa', 'Siri', 'Bixby', end='!\n')

    # Alexa and Siri and Bixby are virtual assistants.
    print('Alexa', 'Siri', 'Bixby', sep=' and ', end=' are virtual assistants.')


test_print()
