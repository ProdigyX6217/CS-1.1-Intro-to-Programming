import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when file is run.
    Simulates the spread of a virus through a given population.  The percentage of the
    population that are vaccinated, the size of the population, and the amount of initially
    infected people in a population are all variables that can be set when the program is run.
    '''
    def __init__(self, population_size, v_percentage, v, initial_infected=1):
        ''' Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of population
        vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected with the disease.
        The total infected people is the running total that have been infected since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have died as a result
        of the infection.
        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''

        self.next_person_id = 0
        self.virus = v
        self.pop_size = population_size
        self.initial_infected = initial_infected
        self.total_infected = initial_infected
        self.current_infected = initial_infected
        self.vacc_percentage = v_percentage
        self.total_dead = 0
        self.file_name = f"{self.virus.name}_simulation_pop_{self.pop_size}_vp_{self.vacc_percentage}_infected_{self.initial_infected}.txt"
        self.newly_infected = []
        self.newly_dead = []
        self.population = self._create_population(self.initial_infected)


        self.logger = Logger(self.file_name)
        self.logger.write_metadata(self.pop_size,self.vacc_percentage,self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        '''
        self.population = []
        vac_pop = int(self.pop_size * self.vacc_percentage)
        for i in range(vac_pop):
            self.population.append(Person(self.next_person_id, True))
            self.next_person_id += 1

        for i in range(self.initial_infected):
            self.population.append(Person(self.next_person_id, False, self.virus))
            self.next_person_id += 1

        for person in range(self.pop_size - vac_pop - initial_infected):
            self.population.append(Person(self.next_person_id, False))
            self.next_person_id += 1

        return self.population

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should end.
        '''
        vac_pop = 0
        self.total_dead = 0
        infected_num = 0
        for person in self.population:
            if person.is_alive and person.is_vaccinated:
                vac_pop += 1

            if person.is_alive == False:
                self.total_dead += 1

            if person.infection is not None:
                infected_num += 1


        if self.total_dead == self.pop_size or infected_num == 0:
            return False

        if vac_pop == self.pop_size - self.total_dead:
            return False
        return True
    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''
        time_step_counter = 0

        while self._simulation_should_continue():

            self.time_step()

            self.logger.log_time_step(time_step_counter, len(self.newly_infected), len(self.newly_dead),self.total_infected, self.total_dead)

            self._infect_newly_infected()

            time_step_counter += 1

        print(f"The simulation has ended after {time_step_counter} turns.")

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.
        This includes:
            1. 100 total interactions with a random person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''

        for person in self.population:

            if person.is_alive and person.infection:

                interactions = 0
                while(interactions < 100):

                    rand_person = self.population[random.randrange(0, self.pop_size)]


                    if rand_person.is_alive:
                        interactions +=1
                        self.interaction(person, rand_person)


        for person in self.population:
            if person.is_alive and person.infection:

                if person.did_survive_infection():
                    self.logger.log_infection_survival(person, False)

                else:
                    self.logger.log_infection_survival(person, True)
                    self.current_infected -= 1
                    self.total_dead += 1
                    self.newly_dead.append(person._id)

    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        assert person.is_alive == True
        assert random_person.is_alive == True
        r_person_sick = False
        if random_person.infection is None:
            r_person_sick = False
        else:
            r_person_sick = True
        if random.random() < self.virus.repro_rate:
            self.logger.log_interaction(person, random_person, r_person_sick, random_person.is_vaccinated, did_infect=True)

            if random_person.is_vaccinated is False and r_person_sick is False:
                self.newly_infected.append(random_person._id)
        else:
            self.logger.log_interaction(person, random_person, r_person_sick ,random_person.is_vaccinated, did_infect=False)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''

        for person_id in self.newly_infected:
            self.population[person_id].infection = self.virus
            self.current_infected += 1
        self.newly_infected = []
        self.newly_dead = []

if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[2])
    repro_num = float(params[4])
    mortality_rate = float(params[3])

    pop_size = int(params[0])
    vacc_percentage = float(params[1])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus,initial_infected)
    sim.run()
