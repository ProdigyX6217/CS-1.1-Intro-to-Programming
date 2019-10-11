

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

    virus1 = Virus("Polio", 0.6, 0.2)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.6
    assert virus.mortality_rate == 0.2

def test_zero_values():
    virus = Virus("Shingles", 0.7, 1.0)
    assert virus.name != ""
    assert virus.repro_rate > 0.0
    assert virus.mortality_rate > 0.0
