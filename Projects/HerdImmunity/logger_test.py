# Helped by Audi Blades
from logger import Logger
from person import Person
from virus import Virus
import unittest
import os


class LoggerTestCoverage(unittest.TestCase):

    # def test__init__(self,):
    #     self.logger = Logger("file_name.txt")
    #     self.assertEqual(logger.file_name, "file_name.txt")
    #     os.remove("file_name.txt")

    # def test_write_metadata(self):
    #     logger = Logger("file_name.txt")
    #     logger.write_metadata(1000, 0.3, "Hello" , 0.7, 0.35)
    #     open (logger.file_name)
    #     self.assertEqual()

    def test_log_interaction(self):
        virus = Virus("Dysentery", 0.7, 0.2)
        person = Person(1, False, virus)
        random_person =Person(17, False)

        # if did_infect:
        #     interaction = f"{person.ID} infects {random_person.ID} \n"
        # else:
        #     interaction = f"{person.ID} didn't infect {random_person.ID} because {random_person_vacc or random_person_sick} \n"

        logger = Logger("file_name.txt")
        self.assertEqual(logger.log_interaction(person,random_person, did_infect=True), "1 infects 17 ")
        os.remove("file_name.txt")

    #
    # def test_log_infection_survival():
    #     logger = Logger()
    #     self.assertEqual()
    #
    # def test_log_time_step():
    #     logger = Logger()
    #     self.assertEqual()
