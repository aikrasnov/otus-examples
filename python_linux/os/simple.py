import os
import copy
import time

env_copy = copy.deepcopy(os.environ)
env_copy.pop("GOQA_TESTRAIL_LOGIN", None)
env_copy.pop("GOQA_TESTRAIL_PASSWORD", None)

print(env_copy)

time.sleep(30)
print("\n\n\n\n####\n\n\n\n")

print(os.path.join("foo", "bar", "otus"))
print(os.path.join("foo/", "bar/", "otus/"))
