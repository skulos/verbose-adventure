""" Insert """
from engine_logging import logger
from simulator.simulate_main import simulate_main


logger.info("Starting Engine...")
simulate_main()
logger.info("Exiting Engine...")