"""
aioschedule - если python 3.11+ то открываешь библиотеку и на 107 строчке меняешь это

jobs = [job.run() for job in self.jobs if job.should_run]

на вот это

jobs = [asyncio.create_task(job.run()) for job in self.jobs if job.should_run]


https://progr.interplanety.org/en/removing-the-passing-coroutines-is-forbidden-use-tasks-explicitly-error-when-using-aioschedule-in-python-3-11/
"""


# import sqlite3
#
# conn = sqlite3.connect('reg_base.sqlite')
# cursor = conn.cursor()
#
# cursor.execute("ALTER TABLE users DROP COLUMN pidor")
# cursor.execute("ALTER TABLE users DROP COLUMN run")
# cursor.execute("ALTER TABLE users DROP COLUMN artpub")
#
# conn.commit()
# conn.close()


