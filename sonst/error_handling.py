try:
    do_something()
except BaseException as e:
    logger.error('Failed to do something: ' + str(e))
