from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
MESSAGE_LEN = env.int("MESSAGE_LEN")
VARIANT_LEN = env.int("VARIANT_LEN")
VARIANT_NUM = env.int("VARIANT_NUM")