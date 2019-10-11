# Helped by Zurich Olrich/ Naomi Alderrmann
class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        # TODO:  Finish this initialization method. The file_name passed should be the
        # full file name of the file that the logs will be written to.
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num):
        '''
        Simulation Class should use this method immediately to log the specific params of the simulation as the first line of the file.
        '''
        # first_line = f"Population: {pop_size}, Vaccination Percentage: {vacc_percentage}, Virus: {virus_name},Death Rate: {mortality_rate}, Reproductive Rate: {basic_repro_num}\n"
        # logger = open(self.file_name, mode='w+')
        # logger.write(first_line)
        # logger.close()

        log_file = open(self.file_name, 'w+')
        log_file.write("_____________Metadata_File_______________\n")
        log_file.write(f"{pop_size}\t {vacc_percentage}\t {virus_name}\t {mortality_rate}\t \n")
        log_file.write("______________given_stats________________\n")
        log_file.write(f"""\n
                Population Size: {pop_size},
        vaccination Percentage: {vacc_percentage*100}%,
                Name of the virus: {virus_name},
        Mortality rate of virus: {mortality_rate*100}%,
basic reproduction rate of virus: {basic_repro_num*100}%
                    \n""")
        log_file.write("_____________________________________________\n")
        log_file.close()


        # TODO: Finish this method. This line of metadata should be tab-delimited
        # it should create the text file that we will store all logs in.
        # TIP: Use 'w' mode when you open the file. For all other methods, use
        # the 'a' mode to append a new log to the end, since 'w' overwrites the file.
        # NOTE: Make sure to end every line with a '\n' character to ensure that each
        # event logged ends up on a separate line!

    def log_interaction(self, person, random_person, random_person_inf=None, random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"
        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''
        # if did_infect:
        #     interaction = f"{person._id} infects {random_person._id} \n"
        # else:
        #     interaction = f"{person._id} didn't infect {random_person._id} because {random_person_vacc or random_person_sick} \n"
        # logger = open(self.file_name, mode='a')
        # logger.write("\n")
        # logger.close()

        log_file = open(self.file_name, 'a+') 
        if did_infect == False and random_person_vacc == False and random_person_inf == False:
            log_file.write(f"{person._id} does not infect {random_person._id} becasue the chances of getting sick were too low. \n")
        elif random_person_inf == True and did_infect == False and random_person_vacc == False:
            log_file.write(f"{person._id} does not infect {random_person._id} because they were already sick. \n")
        elif did_infect == True and random_person_vacc == True:
            log_file.write(f"{random_person._id} does not gets infected by {person._id} because they were vaccinated.\n")
        elif did_infect == True:
            log_file.write(f"{person._id} infects {random_person._id} because they werent vaccinated\n")
        log_file.close()

        # TODO: Finish this method. Think about how the booleans passed (or not passed)
        # represent all the possible edge cases. Use the values passed along with each person,
        # along with whether they are sick or vaccinated when they interact to determine
        # exactly what happened in the interaction and create a String, and write to your logfile.


    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every call of a Person object's .resolve_infection() method.
            The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''
        # if did_die_from_infection:
        #     log_infection_survival = f"{person.ID} died from infection.\n"
        # else:
        #     log_infection_survival = f"{person.ID} survived infection.\n"
        # logger = open(file='log.txt', mode = 'a', newline = log_infection_survival)
        # logger.close()

        log_file = open(self.file_name, 'a+')
        if did_die_from_infection == False:
            log_file.write(f"{person._id} died from the infection. \n")
        else:
            log_file.write(f"{person._id} survived the infection\n")


        # TODO: Finish this method. If the person survives, did_die_from_infection should be False.
        # Otherwise, did_die_from_infection should be True.
        # Append the results of the infection to the logfile.


    def log_time_step(self, time_step_number, sim_data):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        with open(self.file_name, 'a') as log_file:
            log_file.write(f"\n)Time step {time_step_number} ended..\n{sim_data.total_infected} people were infected\n{sim_data.total_dead} people died\n{sim_data.total_infected} total infected\n{sim_data.total_dead} total dead\n{time_step_number+1} beginning..")
        # TODO: Finish this method. This method should log when a time step ends, and a new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
