from environs import Env 

env = Env()
env.read_env()

TOKEN = env.str("TASKBOT_TOKEN")
ETHSCAN_API_KEY = env.str("TASKJOBBOT_ETHSCAN_TOKEN")
ADMIN_ID = "enter admin id"