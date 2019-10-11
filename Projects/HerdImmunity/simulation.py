# Helped by David Evans/ Mariana Campbell
import random, sys
random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    ''' Main class that Simulates the Virus spread through a given population.. Expects init params passed as CMD line arguments when file is run.
        Percentage of Vac. Population, Population Size, and Amount of Init. Infected are Var(s) set when program is run.
    '''
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        ''' Logger object records all events during the simulation.
            Population represents all Persons in the population.
            The next_person_id is the next available id for all created Persons and should have a unique _id value.
            The vacc_percentage represents the total percentage of population vaccinated at the start of the simulation.
            Keep track of the number of people currently infected with the disease.
            Total Infected People is the total infected since simulation began, including the currently infected people who died.
            Keep track of the number of people that died from infection.

        All arguments will be passed as command-line arguments when the file is run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        '''

        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus.name, pop_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.population = self._create_population(initial_infected) # List of Person objects
        self.pop_size = pop_size # Int
        self.next_person_id = 0 # Int
        self.virus = virus # Virus object
        self.initial_infected = initial_infected # Int
        self.total_infected = 0 # Int
        self.current_infected = 0 # Int
        self.vacc_percentage = vacc_percentage # float between 0 and 1
        self.total_dead = 0 # Int
        self.newly_infected = []
        self.total_vaccinated = (pop_size * vacc_percentage)
        self.logger.write_metadata(pop_size, vacc_percentage, virus.name, virus.mortality_rate, virus.repro_rate)
        self.time_step_counter = 0

        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct parameters.
        # Store the array that this method will return in the self.population attribute.
        # TODO: Store each newly infected person's ID in newly_infected attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.

    def _create_population(self, initial_infected):
        '''This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the simulation
                will begin with.
            Returns:
                list: A list of Person objects.
        '''
        pop_list = []
        vacc_number = int(pop_size * vacc_percentage)

        for i in range(pop_size):
            if initial_infected > 0:
                pop_list.append(Person(i, False, virus))
                initial_infected -= 1
            elif vacc_number > 0:
                pop_list.append(Person(i, True))
                vacc_number -= 1
            else:
                pop_list.append(Person(i, False))

        return pop_list

        # TODO: Finish this method! This method should be called when the simulation
        # begins, to create the population that will be used. This method should return
        # an array filled with Person objects that matches the specifications of the
        # simulation (correct number of people in the population, correct percentage of
        # people vaccinated, correct number of initially infected people).
        # Use the attributes created in the init method to create a population that has
        # the correct intial vaccination percentage and initial infected.

    def _simulation_should_continue(self):
        ''' The simulation should only end if the entire population is dead
        or everyone is vaccinated.
            Returns:
                bool: True for simulation should continue, False if it should end.
        '''

        if self.pop_size == self.total_dead + self.total_vaccinated:
            return False
        else:
            return True


        # TODO: Complete this helper method.  Returns a Boolean.

    def run(self):
        ''' This method should run the simulation until all requirements for ending
        the simulation are met.
        '''

        should_continue = self._simulation_should_continue()
        while should_continue == True:
            print('start')
            self.time_step()
            print(1)
            self.logger.log_time_step(self.time_step_counter, self)
            print(2)
            self.time_step_counter += 1
            print(3)
            should_continue = self._simulation_should_continue()
            print(4)

        # else:

        # time_step_counter = 0
        # should_continue = None
        #
        # while should_continue
        #     self.time_step()

        print('The simulation has ended after {} turns.'.format(self.time_step_counter))

        # TODO: for every iteration of this loop, call self.time_step() to compute another
        # round of this simulation.
        # TODO: Finish this method.  To simplify the logic here, use the helper method
        # _simulation_should_continue() to tell us whether or not we should continue
        # the simulation and run at least 1 more time_step.
        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the end of each time step.
        # TODO: Set this variable using a helper


    def random_person(self, infected_person):
        # people_to_interact_with = list()
        # for person in self.population:
        #     if not person._id == infected_person._id:
        #         if person.is_alive == True:
        #             people_to_interact_with.append(person)

        # return people_to_interact_with

        # Omar Sagoo helped me with this recursive technique.
        '''return a random person from the population list, who is not dead and is not the (infected)person who is interacting.'''
        random_person = random.choice(self.population)
        if random_person.is_alive and random_person._id != infected_person._id:
            return random_person
        else:
            return self.random_person(infected_person)

    def time_step(self):
        ''' This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected person
                in the population
            2. If the person is dead, grab another random person from the population.
                Since we don't interact with dead people, this does not count as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
            '''
            # Sick person meets 100 (alive) random persons = 100 interactions = 1 time step
            # if person is dead = No interaction
            # else, count +1

        for person in self.population:
            print("ts 1")
            if person.infection and person.is_alive and not person.is_vaccinated:
                interactions = 0
                print("ts 2")
                while interactions <= 100:
                    random_person_interaction = self.random_person(person)
                    print('ts3')
                    self.interaction(person, random_person_interaction)
                    print('ts4')
                    interactions += 1
                print('ts5')
                did_survive = person.did_survive_infection()
                print('ts6')
                if did_survive:
                    self.total_vaccinated += 1
                    print("ts7")
                else:
                    self.total_dead += 1
                    print('ts8')
        self._infect_newly_infected()
        print("ats 2")
        self.logger.log_time_step(self.time_step_counter, self)
        print("ats3")



                # for random_person in self.random_list(person):
                #     self.interaction(person, random_person)


        # TODO: Finish this method.



    def interaction(self, person, random_person):
        '''This method should be called any time two living people are selected for an
        interaction. It assumes that only living people are passed in as parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        '''
        # Assert statements are included to make sure that only living people are passed in as params
        assert person.is_alive == True
        assert random_person.is_alive == True

        # if random_person.is_vaccinated:
        #     self.logger.log_interaction(person, random_person, False, True, False)
        # if random_person.infection:
        #     self.logger.log_interaction(person, random_person, True, False, False)
        # else:
        #     if random.random() < self.virus.repro_rate:
        #         self.newly_infected.append(random_person._id)
        #         self.total_infected += 1
        #         self.logger.log_interaction(person, random_person, True, False, True)
        #     else:
        #         self.logger.log_interaction(person, random_person, False, False, False)

        if random_person.is_vaccinated == False and random_person.infection == None and random_person._id not in self.newly_infected:
            random_person.infection = self.virus
            inf_chance = random.random()
            if inf_chance <= self.virus.repro_rate:
                self.newly_infected.append(random_person._id)
                self.logger.log_interaction(person, random_person, True, False, True)
                self.current_infected += 1
                self.total_infected += 1
        elif random_person.is_vaccinated == True:
            self.logger.log_interaction(person, random_person, False , True, False)
        elif random_person.infection != None:
            self.logger.log_interaction(person, random_person, True, False, False)


        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
            # random_person is vaccinated:
            #     nothing happens to random person.
            # random_person is already infected:
            #     nothing happens to random person.
            # random_person is healthy, but unvaccinated:
            #     generate a random number between 0 and 1.  If that number is smaller
            #     than repro_rate, random_person's ID should be appended to
            #     Simulation object's newly_infected array, so that their .infected
            #     attribute can be changed to True at the end of the time step.
        # TODO: Calls logger method during this method.
        # self.logger.log_interaction(person, random_person, random_person_sick='is alreadysick', did_infect=False)
        # self.logger.log_interaction(person, random_person_vacc='is vaccinated', did_infect=False)

    def _infect_newly_infected(self):
        ''' This method should iterate through the list of ._id stored in self.newly_infected
        and update each Person object with the disease. '''
        for person in self.population:
            if person._id in self.newly_infected:
                person.infection = self.virus

        self.newly_infected.clear()

        # TODO: Call this method at the end of every time step and infect each Person.
        # TODO: Once you have iterated through the entire list of self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.



if __name__ == "__main__":
    params = sys.argv[1:]
    name = str(params[2])
    repro_rate = float(params[4])
    mortality_rate = float(params[3])

    pop_size = int(params[0])
    vacc_percentage = float(params[1])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(name, repro_rate, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, virus, initial_infected)

    sim.run()
