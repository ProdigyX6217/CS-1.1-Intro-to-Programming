class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.3, 0.8)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.3
    assert virus.mortality_rate == 0.8

    # virus = Virus("Bubonic Plague", 0.1, 0.6)
    # assert virus.name == "Bubonic Plague"
    # assert virus.repro_rate == 0.1
    # assert virus.mortality_rate == 0.6
